# -*- coding: utf-8 -*-

from odoo import fields, models
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    cali_1 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_cali_1 = fields.Text()
    p_cali_1 = fields.Integer(
        default=0
    )
    g_cali_1 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    cali_2 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    t_cali_2_1 = fields.Boolean(default=False)
    t_cali_2_2 = fields.Boolean(default=False)
    t_cali_2_3 = fields.Boolean(default=False)
    obs_cali_2 = fields.Text()
    p_cali_2 = fields.Integer(
        default=0
    )
    g_cali_2 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    cali_3 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_cali_3 = fields.Text()
    p_cali_3 = fields.Integer(
        default=0
    )
    g_cali_3 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    cali_4 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_cali_4 = fields.Text()
    p_cali_4 = fields.Integer(
        default=0
    )
    g_cali_4 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    cali_5 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_cali_5 = fields.Text()
    p_cali_5 = fields.Integer(
        default=0
    )
    g_cali_5 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    cali_6 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_cali_6 = fields.Text()
    p_cali_6 = fields.Integer(
        default=0
    )
    g_cali_6 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    cali_7 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_cali_7 = fields.Text()
    p_cali_7 = fields.Integer(
        default=0
    )
    g_cali_7 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    cali_8 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_cali_8 = fields.Text()
    p_cali_8 = fields.Integer(
        default=0
    )
    g_cali_8 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
