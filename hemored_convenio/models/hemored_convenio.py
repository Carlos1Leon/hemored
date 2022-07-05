# -*- coding: utf-8 -*-
from lxml import etree

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError

from ..models import constants


class Convenio(models.Model):
    _inherit = 'mail.thread'
    _name = 'hemored_convenio.convenio'
    _description = 'Convenios'

    name = fields.Char(
        string='EESS con quien subscribe convenio',
        required=True
    )
    name_eess = fields.Char(
        string='Nombre de EESS',
        store=True
    )
    description = fields.Text(
        string='Observación'
    )
    fecha_actual = fields.Date(
        string='Fecha de inicio'
    )
    numero_expediente = fields.Char(
        string='N° de expediente'
    )
    fecha = fields.Date(
        string='Fecha de vencimiento'
    )
    estado = fields.Selection(
        constants.SELECTION_ESTADO_CONVENIO,
        string='Estado'
    )
    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='Diresa',
        default=lambda self: self.env.user.diresa_id,
        readonly=True
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS',
        default=lambda self: self.env.user.banco_id
    )
    archivo = fields.Binary(
        string='Archivo',
        attachment=True
    )
    archivo_nombre = fields.Char(
        string='Nombre archivo'
    )
    convenio_id = fields.Many2one(
        comodel_name='hemored_convenio.convenio',
        string='Convenio previo'
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(Convenio, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        es_coordinador_establecimiento = self.env.user.has_group('hemored.group_coordinador_establecimiento_hemored')
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            modifiers = '{"readonly": true}'
            if es_coordinador_establecimiento:
                for node in doc.xpath("//field[@name='banco_id']"):
                    node.set('modifiers', modifiers)
            res['arch'] = etree.tostring(doc)
        return res

    @api.model
    def create(self, vals):
        es_coordinador_establecimiento = self.env.user.has_group('hemored.group_coordinador_establecimiento_hemored')
        if es_coordinador_establecimiento:
            domain_busqueda_vigente = [('name', '=', vals.get('name')), ('banco_id', '=', self.env.user.banco_id.id), ('estado', '=', constants.VIGENTE)]
            domain_busqueda_previo = [('name', '=', vals.get('name')), ('banco_id', '=', self.env.user.banco_id.id), ('estado', 'in', (constants.POR_VENCER, constants.VENCIDO))]
        else:
            domain_busqueda_vigente = [('name', '=', vals.get('name')), ('banco_id', '=', vals.get('banco_id')), ('estado', '=', constants.VIGENTE)]
            domain_busqueda_previo = [('name', '=', vals.get('name')), ('banco_id', '=', vals.get('banco_id')), ('estado', 'in', (constants.POR_VENCER, constants.VENCIDO))]
        convenio_previo = self.env['hemored_convenio.convenio'].search(domain_busqueda_vigente, limit=1)
        convenio_previo_funcional = self.env['hemored_convenio.convenio'].search(domain_busqueda_previo, limit=1)
        if convenio_previo:
            if convenio_previo.estado == constants.VIGENTE:
                raise ValidationError('Ya existe un convenio vigente con esta entidad')
        if convenio_previo_funcional:
            fecha_actual = fields.Date.from_string(vals.get('fecha_actual'))
            fecha_fin = fields.Date.from_string(vals.get('fecha'))
            if convenio_previo_funcional.fecha_actual > fecha_actual:
                raise ValidationError('El convenio previo tiene una fecha de inicio mayor a la fecha de inicio actual')
            if convenio_previo_funcional.fecha > fecha_fin:
                raise ValidationError('El convenio previo tiene una fecha de finalización mayor a la fecha de finalización actual')
        vals.update(dict(estado=constants.VIGENTE))
        res = super(Convenio, self).create(vals)
        convenio = self.env['hemored_convenio.convenio'].sudo().search([('name', '=', res.name), ('banco_id', '=', res.banco_id.id), ('estado', 'in', (constants.POR_VENCER, constants.VENCIDO))], limit=1)
        if convenio.banco_id:
            convenio.estado = constants.RENOVADO
            res.convenio_id = convenio.id
        return res

    @api.one
    def action_done(self):
        self.estado = constants.CESADO

    @api.one
    @api.constrains('fecha_actual', 'fecha')
    def _check_fecha(self):
        if self.fecha_actual and self.fecha and self.fecha_actual > self.fecha:
            raise ValidationError('Fecha de vencimiento debe ser mayor a la fecha de inicio')

    @api.model
    def _verificar_fecha(self):
        for obj in self.env['hemored_convenio.convenio'].search([]):
            obj.action_vencimiento()
        return True

    @api.one
    def action_vencimiento(self):
        fecha_hoy = fields.Date.today()
        fecha_por_vencer = fields.Date.from_string(self.fecha) - relativedelta(months=6)
        if self.estado == constants.VIGENTE or self.estado == constants.POR_VENCER:
            if self.fecha <= fecha_hoy:
                self.estado = constants.VENCIDO
            elif fecha_hoy >= fecha_por_vencer:
                self.estado = constants.POR_VENCER

    @api.onchange('name')
    def _onchange_name_eess(self):
        banco_id = self.env['hemored.banco_sangre'].sudo().search([('codigo_eess', '=', self.name)], limit=1)
        if self.banco_id:
            if not banco_id and self.name:
                return {
                    'warning': {'message': u'El código RENIPRESS no existe', },
                    'value': {'name': False},
                }
            else:
                if banco_id.codigo_eess == self.env.user.banco_id.codigo_eess:
                    return {
                        'warning': {'message': u'El código RENIPRESS es el mismo de su establecimiento', },
                        'value': {'name': False},
                    }
                else:
                    if banco_id.tipo_banco == self.env.user.banco_id.tipo_banco:
                        return {
                            'warning': {'message': u'No se pueden realizar convenios con CHBS del mismo tipo', },
                            'value': {'name': False},
                        }
                    else:
                        self.name_eess = banco_id.name

    @api.one
    @api.constrains('name')
    def _check_name(self):
        banco_id = self.env['hemored.banco_sangre'].sudo().search([('codigo_eess', '=', self.name)], limit=1)
        if not banco_id or not self.name:
            raise ValidationError('El código RENIPRESS no existe')
        else:
            if banco_id.codigo_eess == self.banco_id.codigo_eess:
                raise ValidationError('El código RENIPRESS es el mismo de su establecimiento')
            else:
                if banco_id.tipo_banco == self.banco_id.tipo_banco:
                    raise ValidationError('No se pueden realizar convenios con CHBS del mismo tipo')

    @api.one
    @api.constrains('archivo_nombre')
    def _check_file(self):
        if not self.archivo_nombre.endswith('.pdf'):
            raise ValidationError('Tipo de archivo NO válido, debe ser PDF')
