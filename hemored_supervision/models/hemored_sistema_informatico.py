# -*- coding: utf-8 -*-

from odoo import fields, models
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    sis_inform_1 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_sis_inform_1 = fields.Text()
    p_sis_inform_1 = fields.Integer(
        default=0
    )
    g_sis_inform_1 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    esp_sis_inform_2 = fields.Text()
    obs_sis_inform_2 = fields.Text()
    p_sis_inform_2 = fields.Integer(
        default=0
    )
    g_sis_inform_2 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    esp_sis_inform_3 = fields.Text()
    obs_sis_inform_3 = fields.Text()
    p_sis_inform_3 = fields.Integer(
        default=0
    )
    g_sis_inform_3 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    t_sis_inform_4 = fields.Selection(
        selection=constants.SELECTION_SGI,
    )
    obs_sis_inform_4 = fields.Text()
    p_sis_inform_4 = fields.Integer(
        default=0
    )
    g_sis_inform_4 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    sis_inform_5 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_sis_inform_5 = fields.Text()
    p_sis_inform_5 = fields.Integer(
        default=0
    )
    g_sis_inform_5 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
