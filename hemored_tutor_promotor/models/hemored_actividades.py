# -*- coding: utf-8 -*-

from odoo import fields, models, api

from ..models import constants, res_users


class RegistroActividad(models.Model):
    _inherit = 'mail.thread'
    _name = 'hemored.registro.actividad'
    _description = 'Registro de actividades'
    _rec_name = 'name'

    name = fields.Char(
        string='Nombre de la actividad'
    )
    fecha_actividad = fields.Date(
        string='Fecha de la actividad'
    )
    descripcion = fields.Char(
        string='Descripción de la actividad'
    )
    lugar_actividad = fields.Char(
        string='Lugar de la actividad'
    )
    departamento_id = fields.Many2one(
        comodel_name='res.country.state',
        string='Departamento',
        domain=[('country_id.code', '=', constants.PE), ('state_id', '=', False), ('province_id', '=', False)]
    )
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
    enlace = fields.Char(
        string='Enlace'
    )
    uso_promotor = fields.Boolean(
        string='Uso promotores'
    )
    promotor_ids = fields.Many2many(
        'hemored.registro.promotor'
    )
    tipo_actividad = fields.Selection(
        string='Tipo de actividad',
        selection=constants.SELECTION_TIPO_ACTIVIDAD,
    )
    cantidad_colectado = fields.Char(
        string='Cantidad Colectada'
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS',
    )
    especificar = fields.Char(
        string='Especificar'
    )
    state = fields.Selection(
        string='Estado',
        selection=constants.SELECTION_ESTADO,
        default=constants.BORRADOR
    )
    tutor_id = _id = fields.Many2one(
        comodel_name='hemored.registro.tutor',
        string='Tutor en cargado',
        default=lambda self: res_users._default_tutor(self),
    )
    usuario_tutor_id = fields.Many2one(
        comodel_name='res.users',
        string='Usuario tutor',
        related='tutor_id.usuario_id',
        store=True
    )
    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='DIRIS/DIRESA/GERESA',
        track_visibility='onchange'
    )

    @api.onchange('diresa_id')
    def _onchange_diresa_id(self):
        self.departamento_id = False

    @api.onchange('departamento_id')
    def _onchange_departamento_id(self):
        self.provincia_id = False
        self.distrito_id = False

    @api.onchange('tipo_actividad')
    def _onchange_tipo_actividad(self):
        if self.tipo_actividad and self.tipo_actividad != constants.CAMPAHA:
            self.cantidad_colectado = False
            self.banco_id = False
        elif self.tipo_actividad and self.tipo_actividad != constants.OTRO:
            self.especificar = False

    @api.onchange('diresa_id')
    def onchange_diresa_id(self):
        domain = {}
        if self.diresa_id:
            domain = {'departamento_id': '''[('id', 'in', %s)]''' % (str(self.diresa_id.departamento_ids.ids))} # noqa
        else:
            domain = {'departamento_id': '''[('id', 'in', %s)]''' % []} # noqa
        return {'domain': domain}
