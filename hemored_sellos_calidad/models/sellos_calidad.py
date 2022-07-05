# -*- coding: utf-8 -*-

from odoo import api, fields, models
from ..models import constants


class SellosCalidadRegistro(models.Model):
    _name = 'hemored.sellos.calidad.registro'
    _inherit = 'mail.thread'
    _description = 'Lista de Sellos de Calidad'

    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='Diresa',
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS'
    )
    serie = fields.Char(
        string='Serie'
    )
    num_serie = fields.Char(
        string='Número de inicio'
    )
    series_id = fields.Many2one(
        comodel_name='hemored.serie.line',
        string='series'
    )
    componente = fields.Selection(
        string='Componente',
        selection=constants.SELECTION_COMPONENTES_SELLOS,
    )
    estado_registro = fields.Selection(
        string='Estado',
        selection=constants.SELECTION_STATE_REGISTRO,
    )
    num_unidad = fields.Char(
        string='Número de unidad'
    )
    grupo_sanguineo = fields.Selection(
        string='Grupo sanguineo',
        selection=constants.SELECTION_GRUPOSANGUINEO,
    )
    acta = fields.Boolean(
        string='Con acta',
        default=False
    )

    @api.multi
    def name_get(self):
        return [(obj.id, u'{} - {} - {}'.format(
            obj.serie, obj.num_serie, obj.componente)
        ) for obj in self]
