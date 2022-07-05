# -*- coding: utf-8 -*-

from odoo import fields, models, api
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    rh_1 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_rh_1 = fields.Text()
    obs_rh_1 = fields.Text()
    p_rh_1 = fields.Integer()
    g_rh_1 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rh_2 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_rh_2 = fields.Text()
    obs_rh_2 = fields.Text()
    p_rh_2 = fields.Integer()
    g_rh_2 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rh_3 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_rh_3 = fields.Text()
    obs_rh_3 = fields.Text()
    p_rh_3 = fields.Integer()
    g_rh_3 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rh_4 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_rh_4 = fields.Text()
    obs_rh_4 = fields.Text()
    p_rh_4 = fields.Integer()
    g_rh_4 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rh_5 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_rh_5 = fields.Text()
    obs_rh_5 = fields.Text()
    p_rh_5 = fields.Integer()
    g_rh_5 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rh_6 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_rh_6 = fields.Text()
    obs_rh_6 = fields.Text()
    p_rh_6 = fields.Integer()
    g_rh_6 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rh_7 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_rh_7 = fields.Text()
    obs_rh_7 = fields.Text()
    p_rh_7 = fields.Integer()
    g_rh_7 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rh_8 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_rh_8 = fields.Text()
    obs_rh_8 = fields.Text()
    p_rh_8 = fields.Integer()
    g_rh_8 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rh_9 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_rh_9 = fields.Text()
    obs_rh_9 = fields.Text()
    p_rh_9 = fields.Integer()
    g_rh_9 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rh_10 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rh_10 = fields.Text()
    p_rh_10 = fields.Integer()
    g_rh_10 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )

    @api.onchange('rh_1')
    def _onchange_rh_1(self):
        if self.rh_1 == constants.SI:
            self.p_rh_1 = 5
            self.g_rh_1 = constants.NULO
        elif self.rh_1 == constants.NO:
            self.p_rh_1 = 0
            self.g_rh_1 = constants.GRAVE
        else:
            self.p_rh_1 = 0
            self.g_rh_1 = False

    @api.onchange('rh_2')
    def _onchange_rh_2(self):
        if self.rh_2 == constants.SI:
            self.p_rh_2 = 4
            self.g_rh_2 = constants.NULO
        elif self.rh_2 == constants.NO:
            self.p_rh_2 = 0
            self.g_rh_2 = constants.NULO
        else:
            self.p_rh_2 = 0
            self.g_rh_2 = False

    @api.onchange('rh_3')
    def _onchange_rh_3(self):
        if self.rh_3 == constants.SI:
            self.p_rh_3 = 5
            self.g_rh_3 = constants.NULO
        elif self.rh_3 == constants.NO:
            self.p_rh_3 = 0
            self.g_rh_3 = constants.GRAVE
        else:
            self.p_rh_3 = 0
            self.g_rh_3 = False

    @api.onchange('rh_4')
    def _onchange_rh_4(self):
        if self.rh_4 == constants.SI:
            self.p_rh_4 = 4
            self.g_rh_4 = constants.NULO
        elif self.rh_4 == constants.NO:
            self.p_rh_4 = 0
            self.g_rh_4 = constants.LEVE
        else:
            self.p_rh_4 = 0
            self.g_rh_4 = False

    @api.onchange('rh_5')
    def _onchange_rh_5(self):
        if self.rh_5 == constants.SI:
            self.p_rh_5 = 4
            self.g_rh_5 = constants.NULO
        elif self.rh_5 == constants.NO:
            self.p_rh_5 = 0
            self.g_rh_5 = constants.GRAVE
        else:
            self.p_rh_5 = 0
            self.g_rh_5 = False

    @api.onchange('rh_6')
    def _onchange_rh_6(self):
        if self.rh_6 == constants.SI:
            self.p_rh_6 = 2
            self.g_rh_6 = constants.NULO
        elif self.rh_6 == constants.NO:
            self.p_rh_6 = 0
            self.g_rh_6 = constants.NULO
        else:
            self.p_rh_6 = 0
            self.g_rh_6 = False

    @api.onchange('rh_7')
    def _onchange_rh_7(self):
        if self.rh_7 == constants.SI:
            self.p_rh_7 = 1
            self.g_rh_7 = constants.NULO
        elif self.rh_7 == constants.NO:
            self.p_rh_7 = 0
            self.g_rh_7 = constants.NULO
        else:
            self.p_rh_7 = 0
            self.g_rh_7 = False

    @api.onchange('rh_8')
    def _onchange_rh_8(self):
        if self.rh_8 == constants.SI:
            self.p_rh_8 = 3
            self.g_rh_8 = constants.NULO
        elif self.rh_8 == constants.NO:
            self.p_rh_8 = 0
            self.g_rh_8 = constants.NULO
        else:
            self.p_rh_8 = 0
            self.g_rh_8 = False

    @api.onchange('rh_9')
    def _onchange_rh_9(self):
        if self.rh_9 == constants.SI:
            self.p_rh_9 = 3
            self.g_rh_9 = constants.NULO
        elif self.rh_9 == constants.NO:
            self.p_rh_9 = 0
            self.g_rh_9 = constants.LEVE
        else:
            self.p_rh_9 = 0
            self.g_rh_9 = False

    @api.onchange('rh_10')
    def _onchange_rh_10(self):
        if self.rh_10 == constants.SI:
            self.p_rh_10 = 5
            self.g_rh_10 = constants.NULO
        elif self.rh_10 == constants.NO:
            self.p_rh_10 = 0
            self.g_rh_10 = constants.GRAVE
        else:
            self.p_rh_10 = 0
            self.g_rh_10 = False
