# -*- coding: utf-8 -*-

from odoo import fields, models

from ..models import constants, fichas_stock

MN_Configuracion = '.'.join([constants.MODULO, 'configuracion'])


class Configuracion(models.Model):
    _inherit = 'mail.thread'
    _name = MN_Configuracion
    _description = 'Configuración Stock Hemocomponentes'
    _rec_name = 'periodicidad'

    periodicidad = fields.Selection(
        constants.SELECTION_PERIODICIDAD,
        string='Periodicidad',
        track_visibility='onchange'
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: fichas_stock._get_company(self),
        track_visibility='onchange'
    )

    _sql_constraints = [
        ('company_id', 'unique(company_id)',
         'La periodicidad debe ser única!'),
    ]
