# -*- coding: utf-8 -*-

from odoo import fields, models, api
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    t_infra_instal_1 = fields.Selection(
        selection=constants.SELECTION_PISO,
    )
    esp_infra_instal_1 = fields.Float()
    obs_infra_instal_1 = fields.Text()
    p_infra_instal_1 = fields.Integer()
    g_infra_instal_1 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_infra_instal_2_1 = fields.Boolean(default=False)
    t_infra_instal_2_2 = fields.Boolean(default=False)
    t_infra_instal_2_3 = fields.Boolean(default=False)
    t_infra_instal_2_4 = fields.Boolean(default=False)
    obs_infra_instal_2 = fields.Text()
    p_infra_instal_2 = fields.Integer(
        default=0
    )
    g_infra_instal_2 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    esp_infra_instal_3 = fields.Text()
    obs_infra_instal_3 = fields.Text()
    p_infra_instal_3 = fields.Integer(
        default=0
    )
    g_infra_instal_3 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    esp_infra_instal_4 = fields.Text()
    obs_infra_instal_4 = fields.Text()
    p_infra_instal_4 = fields.Integer(
        default=0
    )
    g_infra_instal_4 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    infra_instal_5 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_5 = fields.Text()
    p_infra_instal_5 = fields.Integer()
    g_infra_instal_5 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_6 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_6 = fields.Text()
    p_infra_instal_6 = fields.Integer()
    g_infra_instal_6 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_7 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_7 = fields.Text()
    p_infra_instal_7 = fields.Integer()
    g_infra_instal_7 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_8 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_8 = fields.Text()
    p_infra_instal_8 = fields.Integer()
    g_infra_instal_8 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_9 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_9 = fields.Text()
    p_infra_instal_9 = fields.Integer()
    g_infra_instal_9 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_10 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_10 = fields.Text()
    p_infra_instal_10 = fields.Integer(
        default=0
    )
    g_infra_instal_10 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    infra_instal_11 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_11 = fields.Text()
    p_infra_instal_11 = fields.Integer()
    g_infra_instal_11 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_12 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_12 = fields.Text()
    p_infra_instal_12 = fields.Integer()
    g_infra_instal_12 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_13 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_13 = fields.Text()
    p_infra_instal_13 = fields.Integer()
    g_infra_instal_13 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_14 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_14 = fields.Text()
    p_infra_instal_14 = fields.Integer()
    g_infra_instal_14 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_15 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_15 = fields.Text()
    p_infra_instal_15 = fields.Integer()
    g_infra_instal_15 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_16 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_16 = fields.Text()
    p_infra_instal_16 = fields.Integer()
    g_infra_instal_16 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_17 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_17 = fields.Text()
    p_infra_instal_17 = fields.Integer()
    g_infra_instal_17 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_18 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_18 = fields.Text()
    p_infra_instal_18 = fields.Integer()
    g_infra_instal_18 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_19 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_19 = fields.Text()
    p_infra_instal_19 = fields.Integer()
    g_infra_instal_19 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_20 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_20 = fields.Text()
    p_infra_instal_20 = fields.Integer()
    g_infra_instal_20 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_21 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    t_infra_instal_21 = fields.Selection(
        selection=constants.SELECTION_INFRA_INSTAL,
    )
    obs_infra_instal_21 = fields.Text()
    p_infra_instal_21 = fields.Integer()
    g_infra_instal_21 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_22 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_22 = fields.Text()
    p_infra_instal_22 = fields.Integer()
    g_infra_instal_22 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_23 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    t_infra_instal_23 = fields.Selection(
        selection=constants.SELECTION_INFRA_INSTAL,
    )
    obs_infra_instal_23 = fields.Text()
    p_infra_instal_23 = fields.Integer()
    g_infra_instal_23 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    infra_instal_24 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_24 = fields.Text()
    p_infra_instal_24 = fields.Integer(
        default=0
    )
    g_infra_instal_24 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    infra_instal_25 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_25 = fields.Text()
    p_infra_instal_25 = fields.Integer(
        default=0
    )
    g_infra_instal_25 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    infra_instal_26 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_26 = fields.Text()
    p_infra_instal_26 = fields.Integer()
    g_infra_instal_26 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )

    infra_instal_27 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_27 = fields.Text()
    p_infra_instal_27 = fields.Integer(default=0)
    g_infra_instal_27 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    infra_instal_28 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_infra_instal_28 = fields.Text()
    p_infra_instal_28 = fields.Integer(default=0)
    g_infra_instal_28 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )

    @api.onchange('t_infra_instal_1')
    def _onchange_t_infra_instal_1(self):
        if self.t_infra_instal_1 == constants.PRIMER_PISO:
            self.p_infra_instal_1 = 5
            self.g_infra_instal_1 = constants.NULO
        elif self.t_infra_instal_1 == constants.SEGUNDO_PISO or self.t_infra_instal_1 == constants.SOTANO:
            self.p_infra_instal_1 = 2
            self.g_infra_instal_1 = constants.LEVE
        else:
            self.p_infra_instal_1 = 1
            self.g_infra_instal_1 = constants.MODERADO

    @api.onchange('infra_instal_5')
    def _onchange_infra_instal_5(self):
        if self.infra_instal_5 == constants.SI:
            self.p_infra_instal_5 = 5
            self.g_infra_instal_5 = constants.NULO
        else:
            self.p_infra_instal_5 = 0
            self.g_infra_instal_5 = constants.MODERADO

    @api.onchange('infra_instal_6')
    def _onchange_infra_instal_6(self):
        if self.infra_instal_6 == constants.SI:
            self.p_infra_instal_6 = 5
            self.g_infra_instal_6 = constants.NULO
        else:
            self.p_infra_instal_6 = 0
            self.g_infra_instal_6 = constants.MODERADO

    @api.onchange('infra_instal_7')
    def _onchange_infra_instal_7(self):
        if self.infra_instal_7 == constants.SI:
            self.p_infra_instal_7 = 5
            self.g_infra_instal_7 = constants.NULO
        else:
            self.p_infra_instal_7 = 0
            self.g_infra_instal_7 = constants.MODERADO

    @api.onchange('infra_instal_8')
    def _onchange_infra_instal_8(self):
        if self.infra_instal_8 == constants.SI:
            self.p_infra_instal_8 = 5
            self.g_infra_instal_8 = constants.NULO
        else:
            self.p_infra_instal_8 = 0
            self.g_infra_instal_8 = constants.MODERADO

    @api.onchange('infra_instal_9')
    def _onchange_infra_instal_9(self):
        if self.infra_instal_9 == constants.SI:
            self.p_infra_instal_9 = 5
            self.g_infra_instal_9 = constants.NULO
        else:
            self.p_infra_instal_9 = 0
            self.g_infra_instal_9 = constants.MODERADO

    @api.onchange('infra_instal_11')
    def _onchange_infra_instal_11(self):
        if self.infra_instal_11 == constants.SI:
            self.p_infra_instal_11 = 5
            self.g_infra_instal_11 = constants.NULO
        else:
            self.p_infra_instal_11 = 0
            self.g_infra_instal_11 = constants.MODERADO

    @api.onchange('infra_instal_12')
    def _onchange_infra_instal_12(self):
        if self.infra_instal_12 == constants.SI:
            self.p_infra_instal_12 = 5
            self.g_infra_instal_12 = constants.NULO
        else:
            self.p_infra_instal_12 = 0
            self.g_infra_instal_12 = constants.MODERADO

    @api.onchange('infra_instal_13')
    def _onchange_infra_instal_13(self):
        if self.infra_instal_13 == constants.SI:
            self.p_infra_instal_13 = 5
            self.g_infra_instal_13 = constants.NULO
        else:
            self.p_infra_instal_13 = 0
            self.g_infra_instal_13 = constants.MODERADO

    @api.onchange('infra_instal_14')
    def _onchange_infra_instal_14(self):
        if self.infra_instal_14 == constants.SI:
            self.p_infra_instal_14 = 5
            self.g_infra_instal_14 = constants.NULO
        else:
            self.p_infra_instal_14 = 0
            self.g_infra_instal_14 = constants.MODERADO

    @api.onchange('infra_instal_15')
    def _onchange_infra_instal_15(self):
        if self.infra_instal_15 == constants.SI:
            self.p_infra_instal_15 = 5
            self.g_infra_instal_15 = constants.NULO
        else:
            self.p_infra_instal_15 = 0
            self.g_infra_instal_15 = constants.MODERADO

    @api.onchange('infra_instal_16')
    def _onchange_infra_instal_16(self):
        if self.infra_instal_16 == constants.SI:
            self.p_infra_instal_16 = 5
            self.g_infra_instal_16 = constants.NULO
        else:
            self.p_infra_instal_16 = 0
            self.g_infra_instal_16 = constants.MODERADO

    @api.onchange('infra_instal_17')
    def _onchange_infra_instal_17(self):
        if self.infra_instal_17 == constants.SI:
            self.p_infra_instal_17 = 5
            self.g_infra_instal_17 = constants.NULO
        else:
            self.p_infra_instal_17 = 0
            self.g_infra_instal_17 = constants.MODERADO

    @api.onchange('infra_instal_18')
    def _onchange_infra_instal_18(self):
        if self.infra_instal_18 == constants.SI:
            self.p_infra_instal_18 = 5
            self.g_infra_instal_18 = constants.NULO
        else:
            self.p_infra_instal_18 = 0
            self.g_infra_instal_18 = constants.MODERADO

    @api.onchange('infra_instal_19')
    def _onchange_infra_instal_19(self):
        if self.infra_instal_19 == constants.SI:
            self.p_infra_instal_19 = 5
            self.g_infra_instal_19 = constants.NULO
        else:
            self.p_infra_instal_19 = 0
            self.g_infra_instal_19 = constants.MODERADO

    @api.onchange('infra_instal_20')
    def _onchange_infra_instal_20(self):
        if self.infra_instal_20 == constants.SI:
            self.p_infra_instal_20 = 5
            self.g_infra_instal_20 = constants.NULO
        else:
            self.p_infra_instal_20 = 0
            self.g_infra_instal_20 = constants.MODERADO

    @api.onchange('infra_instal_21')
    def _onchange_infra_instal_21(self):
        if self.infra_instal_21 == constants.SI:
            self.p_infra_instal_21 = 5
            self.g_infra_instal_21 = constants.NULO
        else:
            self.p_infra_instal_21 = 0
            self.g_infra_instal_21 = constants.MODERADO

    @api.onchange('infra_instal_22')
    def _onchange_infra_instal_22(self):
        if self.infra_instal_22 == constants.SI:
            self.p_infra_instal_22 = 5
            self.g_infra_instal_22 = constants.NULO
        else:
            self.p_infra_instal_22 = 0
            self.g_infra_instal_22 = constants.MODERADO

    @api.onchange('infra_instal_23')
    def _onchange_infra_instal_23(self):
        if self.infra_instal_23 == constants.SI:
            self.p_infra_instal_23 = 5
            self.g_infra_instal_23 = constants.NULO
        else:
            self.p_infra_instal_23 = 0
            self.g_infra_instal_23 = constants.MODERADO

    @api.onchange('infra_instal_26')
    def _onchange_infra_instal_26(self):
        if self.infra_instal_26 == constants.SI:
            self.p_infra_instal_26 = 5
            self.g_infra_instal_26 = constants.NULO
        else:
            self.p_infra_instal_26 = 0
            self.g_infra_instal_26 = constants.MODERADO
