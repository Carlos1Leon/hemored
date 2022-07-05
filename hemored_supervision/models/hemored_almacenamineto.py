# -*- coding: utf-8 -*-

from odoo import fields, models, api
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    obs_alm_1 = fields.Text()
    esp_alm_1 = fields.Text()
    p_alm_1 = fields.Integer(
        default=0
    )
    g_alm_1 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    obs_alm_2 = fields.Text()
    esp_alm_2 = fields.Text()
    p_alm_2 = fields.Integer(
        default=0
    )
    g_alm_2 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    obs_alm_3 = fields.Text()
    esp_alm_3 = fields.Text()
    p_alm_3 = fields.Integer(
        default=0
    )
    g_alm_3 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    obs_alm_4 = fields.Text()
    esp_alm_4 = fields.Text()
    p_alm_4 = fields.Integer(
        default=0
    )
    g_alm_4 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    obs_alm_5 = fields.Text()
    esp_alm_5 = fields.Text()
    p_alm_5 = fields.Integer(
        default=0
    )
    g_alm_5 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    alm_6 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_alm_6 = fields.Text()
    p_alm_6 = fields.Integer()
    g_alm_6 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    alm_7 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_alm_7 = fields.Text()
    p_alm_7 = fields.Integer()
    g_alm_7 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    alm_8 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_alm_8 = fields.Text()
    p_alm_8 = fields.Integer()
    g_alm_8 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    esp_alm_9 = fields.Text()
    obs_alm_9 = fields.Text()
    p_alm_9 = fields.Integer(
        default=0
    )
    g_alm_9 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    esp_alm_10 = fields.Text()
    obs_alm_10 = fields.Text()
    p_alm_10 = fields.Integer(
        default=0
    )
    g_alm_10 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    esp_alm_11 = fields.Text()
    obs_alm_11 = fields.Text()
    p_alm_11 = fields.Integer(
        default=0
    )
    g_alm_11 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    esp_alm_12 = fields.Text()
    obs_alm_12 = fields.Text()
    p_alm_12 = fields.Integer(
        default=0
    )
    g_alm_12 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    esp_alm_13 = fields.Text()
    obs_alm_13 = fields.Text()
    p_alm_13 = fields.Integer(
        default=0
    )
    g_alm_13 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    esp_alm_14 = fields.Text()
    obs_alm_14 = fields.Text()
    p_alm_14 = fields.Integer(
        default=0
    )
    g_alm_14 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )

    @api.onchange('alm_6')
    def _onchange_alm_6(self):
        if self.alm_6 == constants.SI:
            self.p_alm_6 = 5
            self.g_alm_6 = constants.NULO
        elif self.alm_6 == constants.NO:
            self.p_alm_6 = 0
            self.g_alm_6 = constants.GRAVE
        else:
            self.p_alm_6 = 0
            self.g_alm_6 = False

    @api.onchange('alm_7')
    def _onchange_alm_7(self):
        if self.alm_7 == constants.SI:
            self.p_alm_7 = 4
            self.g_alm_7 = constants.NULO
        elif self.alm_7 == constants.NO:
            self.p_alm_7 = 0
            self.g_alm_7 = constants.MODERADO
        else:
            self.p_alm_7 = 0
            self.g_alm_7 = False

    @api.onchange('alm_8')
    def _onchange_alm_8(self):
        if self.alm_8 == constants.SI:
            self.p_alm_8 = 5
            self.g_alm_8 = constants.NULO
        elif self.alm_8 == constants.NO:
            self.p_alm_8 = 0
            self.g_alm_8 = constants.GRAVE
        else:
            self.p_alm_8 = 0
            self.g_alm_8 = False
