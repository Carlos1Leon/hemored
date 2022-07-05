# -*- coding: utf-8 -*-

from odoo import fields, models, api
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    rg_1 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_1 = fields.Text()
    p_rg_1 = fields.Integer()
    g_rg_1 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_2 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_2 = fields.Text()
    p_rg_2 = fields.Integer()
    g_rg_2 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_rg_3 = fields.Selection(
        selection=constants.SELECTION_SERVICIO_DEPARTAMENTO,
    )
    obs_rg_3 = fields.Text()
    p_rg_3 = fields.Integer()
    g_rg_3 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    rg_4 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_4 = fields.Text()
    p_rg_4 = fields.Integer()
    g_rg_4 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_5 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_5 = fields.Text()
    p_rg_5 = fields.Integer()
    g_rg_5 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_6 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_6 = fields.Text()
    p_rg_6 = fields.Integer()
    g_rg_6 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_8 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_8 = fields.Text()
    p_rg_8 = fields.Integer()
    g_rg_8 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_9 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_9 = fields.Text()
    p_rg_9 = fields.Integer()
    g_rg_9 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_10 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_10 = fields.Text()
    p_rg_10 = fields.Integer()
    g_rg_10 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_11 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_11 = fields.Text()
    p_rg_11 = fields.Integer()
    g_rg_11 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_12 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_12 = fields.Text()
    p_rg_12 = fields.Integer()
    g_rg_12 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_13 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_13 = fields.Text()
    p_rg_13 = fields.Integer()
    g_rg_13 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_14 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_14 = fields.Text()
    p_rg_14 = fields.Integer()
    g_rg_14 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_15 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_15 = fields.Text()
    p_rg_15 = fields.Integer()
    g_rg_15 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_16 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_16 = fields.Text()
    p_rg_16 = fields.Integer()
    g_rg_16 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    obs_rg_17 = fields.Text()
    esp_rg_17 = fields.Text()
    p_rg_17 = fields.Integer()
    g_rg_17 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_18 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_18 = fields.Text()
    p_rg_18 = fields.Integer()
    g_rg_18 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_19 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_19 = fields.Text()
    p_rg_19 = fields.Integer()
    g_rg_19 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_rg_20 = fields.Selection(
        selection=constants.SELECTION_TIPO_CONDICION,
    )
    obs_rg_20 = fields.Text()
    esp_rg_20 = fields.Text()
    p_rg_20 = fields.Integer()
    g_rg_20 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_21 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_21 = fields.Text()
    p_rg_21 = fields.Integer()
    g_rg_21 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_rg_22 = fields.Selection(
        selection=constants.SELECTION_CANT_CONVENIO,
    )
    obs_rg_22 = fields.Text()
    p_rg_22 = fields.Integer(
        default=0
    )
    g_rg_22 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    rg_23 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_23 = fields.Text()
    p_rg_23 = fields.Integer()
    g_rg_23 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_24 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_24 = fields.Text()
    p_rg_24 = fields.Integer()
    g_rg_24 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_25 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_25 = fields.Text()
    p_rg_25 = fields.Integer()
    g_rg_25 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_26 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_26 = fields.Text()
    p_rg_26 = fields.Integer()
    g_rg_26 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_28 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_28 = fields.Text()
    p_rg_28 = fields.Integer()
    g_rg_28 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_29 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_29 = fields.Text()
    p_rg_29 = fields.Integer()
    g_rg_29 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    rg_30 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rg_30 = fields.Text()
    p_rg_30 = fields.Integer()
    g_rg_30 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )

    @api.onchange('rg_1')
    def _onchange_rg_1(self):
        if self.rg_1 == constants.SI:
            self.p_rg_1 = 5
            self.g_rg_1 = constants.NULO
        elif self.rg_1 == constants.NO:
            self.p_rg_1 = 0
            self.g_rg_1 = constants.LEVE
        else:
            self.p_rg_1 = 0
            self.g_rg_1 = False

    @api.onchange('rg_2')
    def _onchange_rg_2(self):
        if self.rg_2 == constants.SI:
            self.p_rg_2 = 5
            self.g_rg_2 = constants.NULO
        elif self.rg_2 == constants.NO:
            self.p_rg_2 = 0
            self.g_rg_2 = constants.LEVE
        else:
            self.p_rg_2 = 0
            self.g_rg_2 = False

    @api.onchange('t_rg_3')
    def _onchange_t_rg_3(self):
        if self.t_rg_3 == constants.SERVICIO:
            self.p_rg_3 = 0
        elif self.t_rg_3 == constants.DEPARTAMENTO:
            self.p_rg_3 = 2
        elif self.t_rg_3 == constants.AREA:
            self.p_rg_3 = 3
        else:
            self.p_rg_3 = 0
            self.g_rg_3 = False

    @api.onchange('rg_4')
    def _onchange_rg_4(self):
        if self.rg_4 == constants.SI:
            self.p_rg_4 = 4
            self.g_rg_4 = constants.NULO
        elif self.rg_4 == constants.NO:
            self.p_rg_4 = 0
            self.g_rg_4 = constants.LEVE
        else:
            self.p_rg_4 = 0
            self.g_rg_4 = False

    @api.onchange('rg_5')
    def _onchange_rg_5(self):
        if self.rg_5 == constants.SI:
            self.p_rg_5 = 4
            self.g_rg_5 = constants.NULO
        elif self.rg_5 == constants.NO:
            self.p_rg_5 = 0
            self.g_rg_5 = constants.LEVE
        else:
            self.p_rg_5 = 0
            self.g_rg_5 = False

    @api.onchange('rg_6')
    def _onchange_rg_6(self):
        if self.rg_6 == constants.SI:
            self.p_rg_6 = 4
            self.g_rg_6 = constants.NULO
        elif self.rg_6 == constants.NO:
            self.p_rg_6 = 0
            self.g_rg_6 = constants.LEVE
        else:
            self.p_rg_6 = 0
            self.g_rg_6 = False

    @api.onchange('rg_8')
    def _onchange_rg_8(self):
        if self.rg_8 == constants.SI:
            self.p_rg_8 = 5
            self.g_rg_8 = constants.NULO
        elif self.rg_8 == constants.NO:
            self.p_rg_8 = 0
            self.g_rg_8 = constants.LEVE
        else:
            self.p_rg_8 = 0
            self.g_rg_8 = False

    @api.onchange('rg_9')
    def _onchange_rg_9(self):
        if self.rg_9 == constants.SI:
            self.p_rg_9 = 5
            self.g_rg_9 = constants.NULO
        elif self.rg_9 == constants.NO:
            self.p_rg_9 = 0
            self.g_rg_9 = constants.LEVE
        else:
            self.p_rg_9 = 0
            self.g_rg_9 = False

    @api.onchange('rg_10')
    def _onchange_rg_10(self):
        if self.rg_10 == constants.SI:
            self.p_rg_10 = 5
            self.g_rg_10 = constants.NULO
        elif self.rg_10 == constants.NO:
            self.p_rg_10 = 0
            self.g_rg_10 = constants.LEVE
        else:
            self.p_rg_10 = 0
            self.g_rg_10 = False

    @api.onchange('rg_11')
    def _onchange_rg_11(self):
        if self.rg_11 == constants.SI:
            self.p_rg_11 = 5
            self.g_rg_11 = constants.NULO
        elif self.rg_11 == constants.NO:
            self.p_rg_11 = 0
            self.g_rg_11 = constants.LEVE
        else:
            self.p_rg_11 = 0
            self.g_rg_11 = False

    @api.onchange('rg_12')
    def _onchange_rg_12(self):
        if self.rg_12 == constants.SI:
            self.p_rg_12 = 5
            self.g_rg_12 = constants.NULO
        elif self.rg_12 == constants.NO:
            self.p_rg_12 = 0
            self.g_rg_12 = constants.LEVE
        else:
            self.p_rg_12 = 0
            self.g_rg_12 = False

    @api.onchange('rg_13')
    def _onchange_rg_13(self):
        if self.rg_13 == constants.SI:
            self.p_rg_13 = 5
            self.g_rg_13 = constants.NULO
        elif self.rg_13 == constants.NO:
            self.p_rg_13 = 0
            self.g_rg_13 = constants.LEVE
        else:
            self.p_rg_13 = 0
            self.g_rg_13 = False

    @api.onchange('rg_14')
    def _onchange_rg_14(self):
        if self.rg_14 == constants.SI:
            self.p_rg_14 = 4
            self.g_rg_14 = constants.NULO
        elif self.rg_14 == constants.NO:
            self.p_rg_14 = 0
            self.g_rg_14 = constants.MODERADO
        else:
            self.p_rg_14 = 0
            self.g_rg_14 = False

    @api.onchange('rg_15')
    def _onchange_rg_15(self):
        if self.rg_15 == constants.SI:
            self.p_rg_15 = 5
            self.g_rg_15 = constants.NULO
        elif self.rg_15 == constants.NO:
            self.p_rg_15 = 0
            self.g_rg_15 = constants.LEVE
        else:
            self.p_rg_15 = 0
            self.g_rg_15 = False

    @api.onchange('rg_16')
    def _onchange_rg_16(self):
        if self.rg_16 == constants.SI:
            self.p_rg_16 = 4
            self.g_rg_16 = constants.NULO
        elif self.rg_16 == constants.NO:
            self.p_rg_16 = 0
            self.g_rg_16 = constants.LEVE
        else:
            self.p_rg_16 = 0
            self.g_rg_16 = False

    @api.onchange('rg_18')
    def _onchange_rg_18(self):
        if self.rg_18 == constants.SI:
            self.p_rg_18 = 4
            self.g_rg_18 = constants.NULO
        elif self.rg_18 == constants.NO:
            self.p_rg_18 = 0
            self.g_rg_18 = constants.LEVE
        else:
            self.p_rg_18 = 0
            self.g_rg_18 = False

    @api.onchange('rg_19')
    def _onchange_rg_19(self):
        if self.rg_19 == constants.SI:
            self.p_rg_19 = 5
            self.g_rg_19 = constants.NULO
        elif self.rg_19 == constants.NO:
            self.p_rg_19 = 0
            self.g_rg_19 = constants.GRAVE
        else:
            self.p_rg_19 = 0
            self.g_rg_19 = False

    @api.onchange('t_rg_20')
    def _onchange_t_rg_20(self):
        if self.t_rg_20 == constants.NOMBRADO:
            self.p_rg_20 = 4
            self.g_rg_20 = constants.NULO
        elif self.t_rg_20 == constants.CAS:
            self.p_rg_20 = 4
            self.g_rg_20 = constants.NULO
        elif self.t_rg_20 == constants.TERCERO:
            self.p_rg_20 = 4
            self.g_rg_20 = constants.LEVE
        else:
            self.p_rg_20 = 0
            self.g_rg_20 = False

    @api.onchange('rg_21')
    def _onchange_rg_21(self):
        if self.rg_21 == constants.SI:
            self.p_rg_21 = 3
            self.g_rg_21 = constants.NULO
        elif self.rg_21 == constants.NO:
            self.p_rg_21 = 0
            self.g_rg_21 = constants.NULO
        else:
            self.p_rg_21 = 0
            self.g_rg_21 = False

    @api.onchange('rg_23')
    def _onchange_rg_23(self):
        if self.rg_23 == constants.SI:
            self.p_rg_23 = 4
            self.g_rg_23 = constants.NULO
        elif self.rg_23 == constants.NO:
            self.p_rg_23 = 0
            self.g_rg_23 = constants.NULO
        else:
            self.p_rg_23 = 0
            self.g_rg_23 = False

    @api.onchange('rg_24')
    def _onchange_rg_24(self):
        if self.rg_24 == constants.SI:
            self.p_rg_24 = 4
            self.g_rg_24 = constants.NULO
        elif self.rg_24 == constants.NO:
            self.p_rg_24 = 0
            self.g_rg_24 = constants.MODERADO
        else:
            self.p_rg_24 = 0
            self.g_rg_24 = False

    @api.onchange('rg_25')
    def _onchange_rg_25(self):
        if self.rg_25 == constants.SI:
            self.p_rg_25 = 5
            self.g_rg_25 = constants.NULO
        elif self.rg_25 == constants.NO:
            self.p_rg_25 = 0
            self.g_rg_25 = constants.GRAVE
        else:
            self.p_rg_25 = 0
            self.g_rg_25 = False

    @api.onchange('rg_26')
    def _onchange_rg_26(self):
        if self.rg_26 == constants.SI:
            self.p_rg_26 = 4
            self.g_rg_26 = constants.NULO
        elif self.rg_26 == constants.NO:
            self.p_rg_26 = 0
            self.g_rg_26 = constants.MODERADO
        else:
            self.p_rg_26 = 0
            self.g_rg_26 = False

    @api.onchange('rg_28')
    def _onchange_rg_28(self):
        if self.rg_28 == constants.SI:
            self.p_rg_28 = 5
            self.g_rg_28 = constants.NULO
        elif self.rg_28 == constants.NO:
            self.p_rg_28 = 0
            self.g_rg_28 = constants.GRAVE
        else:
            self.p_rg_28 = 0
            self.g_rg_28 = False

    @api.onchange('rg_29')
    def _onchange_rg_29(self):
        if self.rg_29 == constants.SI:
            self.p_rg_29 = 5
            self.g_rg_29 = constants.NULO
        elif self.rg_29 == constants.NO:
            self.p_rg_29 = 0
            self.g_rg_29 = constants.GRAVE
        else:
            self.p_rg_29 = 0
            self.g_rg_29 = False

    @api.onchange('rg_30')
    def _onchange_rg_30(self):
        if self.rg_30 == constants.SI:
            self.p_rg_30 = 5
            self.g_rg_30 = constants.NULO
        elif self.rg_30 == constants.NO:
            self.p_rg_30 = 0
            self.g_rg_30 = constants.GRAVE
        else:
            self.p_rg_30 = 0
            self.g_rg_30 = False
