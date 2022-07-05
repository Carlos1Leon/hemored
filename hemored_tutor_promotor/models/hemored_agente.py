# -*- coding: utf-8 -*-

import re

from odoo import fields, models, api
from odoo.exceptions import ValidationError

from ..models import constants


class HemoredAgente(models.Model):
    _name = 'hemored.agente'
    _description = 'Registro de Tutores y/o Promotores'
    _rec_name = 'name'

    dni = fields.Char(
        string='DNI'
    )
    name = fields.Char(
        string='Nombre'
    )
    fecha_nacimiento = fields.Date(
        string='Fecha de nacimiento'
    )
    edad = fields.Char(
        string='Edad'
    )
    sexo = fields.Char(
        string='Sexo'
    )
    departamento_name = fields.Char(
        string='Departamento de nacimiento'
    )
    provincia_name = fields.Char(
        string='Provincia de nacimiento'
    )
    distrito_name = fields.Char(
        string='Distrito de nacimiento'
    )
    departamento_id = fields.Many2one(
        comodel_name='res.country.state',
        string='Departamento',
        domain=[('country_id.code', '=', constants.PE), ('state_id', '=', False), ('province_id', '=', False)])
    provincia_id = fields.Many2one(
        comodel_name='res.country.state',
        string='Provincia',
        domain="[('state_id.state_id', '=', False), ('state_id.province_id', '=', False),"
               " ('state_id', '=', departamento_id), ('province_id', '=', False)]"
    )
    distrito_id = fields.Many2one(
        comodel_name='res.country.state',
        string='Distrito',
        domain="[('state_id.province_id', '=', False),"
               " ('state_id', '=', departamento_id), ('province_id', '=', provincia_id)]"
    )
    ocupacion = fields.Char(
        string='Ocupación'
    )
    correo = fields.Char(
        string='Correo electronico'
    )
    telefono = fields.Char(
        string='Telefono',
        size=9,
    )
    lugar_de_trabajo = fields.Char(
        string='Lugar de trabajo'
    )
    usuario_id = fields.Many2one(
        comodel_name='res.users',
        string='Usuario tutor ó promotor',
    )
    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='DIRIS/DIRESA/GERESA',
        track_visibility='onchange'
    )

    @api.multi
    def write(self, vals):
        res = super(HemoredAgente, self).write(vals)
        if 'departamento_id' in vals:
            for obj in self:
                obj.action_change_diresa()
        return res

    @api.onchange('departamento_id')
    def _onchange_departamento_id(self):
        self.provincia_id = False
        self.distrito_id = False

    @api.one
    def action_change_diresa(self):
        domain_departamento = [('code', '=', self.departamento_id.code)]
        departamento_id = self.env['res.country.state'].search(domain_departamento, limit=1)
        if departamento_id and departamento_id.diresa_ids:
            diresa_id = departamento_id.diresa_ids
        vals = {
            'diresa_id': diresa_id.id,
        }
        self.sudo().write(vals)

    @api.one
    @api.constrains('telefono')
    def _check_telefono(self):
        if self.telefono and (len(self.telefono) < 9 or not self.telefono.isdigit()):
            raise ValidationError('Teléfono no válido')

    @api.one
    @api.constrains('email')
    def _check_email(self):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', self.email):
            raise ValidationError('E-mail no válido')

    @api.onchange('dni')
    def _onchange_dni(self):
        if self.dni:
            if len(self.dni) != 8 or not self.dni.isdigit():
                return {
                    'warning': {
                        'title': 'Error en el DNI',
                        'message': 'El DNI debe tener 8 números',
                    },
                }

            values = {}
            data = self.env['consultadatos.mpi'].ver(self.dni, '01')
            if 'error' in data:
                raise ValidationError(data['error'])

            if not data.get('es_persona_viva'):
                raise ValidationError('Persona fallecida')

            domain_departamento = [('code', '=', data.get('get_departamento_domicilio_ubigeo_inei')), ('country_id.code', '=', constants.PE)]
            departamento_id = self.env['res.country.state'].search(domain_departamento, limit=1)
            domain_provincia = [('code', '=', data.get('get_provincia_domicilio_ubigeo_inei')), ('state_id', '=', departamento_id.id), ('country_id.code', '=', constants.PE)]
            provincia_id = self.env['res.country.state'].search(domain_provincia, limit=1)
            domain_distrito = [('code', '=', data.get('get_distrito_domicilio_ubigeo_inei')), ('state_id', '=', departamento_id.id), ('province_id', '=', provincia_id.id), ('country_id.code', '=', constants.PE)]
            distrito_id = self.env['res.country.state'].search(domain_distrito, limit=1)
            if departamento_id and departamento_id.diresa_ids:
                if len(departamento_id.diresa_ids) == 1:
                    diresa_id = departamento_id.diresa_ids
                else:
                    diresa_id = departamento_id.diresa_ids.filtered(lambda l: l.codigo_diresa == '36')
            else:
                diresa_id = False
            values = {
                'name': '%s %s %s' % (
                    data.get('nombres', ''),
                    data.get('apellido_paterno', ''),
                    data.get('apellido_materno', '')
                ),
                'fecha_nacimiento': data.get('fecha_nacimiento', False),
                'edad': data.get('edad_anios', False),
                'sexo': 'Masculino' if data.get('sexo', False) == '1' else 'Femenino',
                'departamento_name': data.get('nacimiento_departamento', False),
                'provincia_name': data.get('nacimiento_provincia', False),
                'distrito_name': data.get('nacimiento_distrito', False),
                'diresa_id': diresa_id,
                'departamento_id': departamento_id,
                'provincia_id': provincia_id,
                'distrito_id': distrito_id,
            }
            return {'value': values}
