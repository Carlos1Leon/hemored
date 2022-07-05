# -*- coding: utf-8 -*-

from odoo import fields, models, api
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    clasf_bio_2 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_clasf_bio_2 = fields.Text()
    p_clasf_bio_2 = fields.Integer()
    g_clasf_bio_2 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    clasf_bio_3 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_clasf_bio_3 = fields.Text()
    p_clasf_bio_3 = fields.Integer()
    g_clasf_bio_3 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    esp_clasf_bio_4 = fields.Text()
    obs_clasf_bio_4 = fields.Text()
    p_clasf_bio_4 = fields.Integer(
        default=0
    )
    g_clasf_bio_4 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    t_clasf_bio_5 = fields.Selection(
        selection=constants.SELECTION_PROFESION,
    )
    obs_clasf_bio_5 = fields.Text()
    p_clasf_bio_5 = fields.Integer(
        default=0
    )
    g_clasf_bio_5 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    clasf_bio_6 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_clasf_bio_6 = fields.Text()
    p_clasf_bio_6 = fields.Integer()
    g_clasf_bio_6 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    clasf_bio_7 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_clasf_bio_7 = fields.Text()
    p_clasf_bio_7 = fields.Integer()
    g_clasf_bio_7 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    clasf_bio_8 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_clasf_bio_8 = fields.Text()
    p_clasf_bio_8 = fields.Integer()
    g_clasf_bio_8 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_clasf_bio_9 = fields.Selection(
        selection=constants.SELECTION_RANGO_EDAD,
    )
    obs_clasf_bio_9 = fields.Text()
    p_clasf_bio_9 = fields.Integer()
    g_clasf_bio_9 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    clasf_bio_14 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_clasf_bio_14 = fields.Text()
    p_clasf_bio_14 = fields.Integer()
    g_clasf_bio_14 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    clasf_bio_15 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_clasf_bio_15 = fields.Text()
    p_clasf_bio_15 = fields.Integer()
    g_clasf_bio_15 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    esp_clasf_bio_16 = fields.Text()
    obs_clasf_bio_16 = fields.Text()
    p_clasf_bio_16 = fields.Integer(
        default=0
    )
    g_clasf_bio_16 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    clasf_bio_18 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_clasf_bio_18 = fields.Text()
    p_clasf_bio_18 = fields.Integer()
    g_clasf_bio_18 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    clasf_bio_19 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_clasf_bio_19 = fields.Text()
    p_clasf_bio_19 = fields.Integer()
    g_clasf_bio_19 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )

    @api.onchange('clasf_bio_1')
    def _onchange_clasf_bio_1(self):
        if self.clasf_bio_1 == constants.SI:
            self.p_clasf_bio_1 = 5
            self.g_clasf_bio_1 = constants.NULO
        else:
            self.p_clasf_bio_1 = 0
            self.g_clasf_bio_1 = constants.GRAVE

    @api.onchange('clasf_bio_2')
    def _onchange_clasf_bio_2(self):
        if self.clasf_bio_2 == constants.SI:
            self.p_clasf_bio_2 = 5
            self.g_clasf_bio_2 = constants.NULO
        else:
            self.p_clasf_bio_2 = 0
            self.g_clasf_bio_2 = constants.GRAVE

    @api.onchange('clasf_bio_3')
    def _onchange_clasf_bio_3(self):
        if self.clasf_bio_3 == constants.SI:
            self.p_clasf_bio_3 = 5
            self.g_clasf_bio_3 = constants.NULO
        else:
            self.p_clasf_bio_3 = 0
            self.g_clasf_bio_3 = constants.GRAVE

    @api.onchange('clasf_bio_6')
    def _onchange_clasf_bio_6(self):
        if self.clasf_bio_6 == constants.SI:
            self.p_clasf_bio_6 = 5
            self.g_clasf_bio_6 = constants.NULO
        else:
            self.p_clasf_bio_6 = 0
            self.g_clasf_bio_6 = constants.GRAVE

    @api.onchange('clasf_bio_7')
    def _onchange_clasf_bio_7(self):
        if self.clasf_bio_7 == constants.SI:
            self.p_clasf_bio_7 = 5
            self.g_clasf_bio_7 = constants.NULO
        else:
            self.p_clasf_bio_7 = 0
            self.g_clasf_bio_7 = constants.GRAVE

    @api.onchange('clasf_bio_8')
    def _onchange_clasf_bio_8(self):
        if self.clasf_bio_8 == constants.SI:
            self.p_clasf_bio_8 = 5
            self.g_clasf_bio_8 = constants.NULO
        else:
            self.p_clasf_bio_8 = 0
            self.g_clasf_bio_8 = constants.GRAVE

    @api.onchange('t_clasf_bio_9')
    def _onchange_t_clasf_bio_9(self):
        if self.t_clasf_bio_9 == constants.MENOR_UN_ANO:
            self.p_clasf_bio_9 = 3
            self.g_clasf_bio_9 = constants.GRAVE
        elif self.t_clasf_bio_9 == constants.DE_UNO_A_DOS or self.t_clasf_bio_9 == constants.DE_DOS_A_TRES:
            self.p_clasf_bio_9 = 3
            self.g_clasf_bio_9 = constants.MODERADO
        elif self.t_clasf_bio_9 == constants.DE_TRES_A_CUATRO or self.t_clasf_bio_9 == constants.DE_CINCO_A_MAS:
            self.p_clasf_bio_9 = 3
            self.g_clasf_bio_9 = constants.NULO
        else:
            self.p_clasf_bio_9 = 0
            self.g_clasf_bio_9 = constants.GRAVE

    @api.onchange('clasf_bio_14')
    def _onchange_clasf_bio_14(self):
        if self.clasf_bio_14 == constants.SI:
            self.p_clasf_bio_14 = 5
            self.g_clasf_bio_14 = constants.NULO
        else:
            self.p_clasf_bio_14 = 0
            self.g_clasf_bio_14 = constants.GRAVE

    @api.onchange('clasf_bio_15')
    def _onchange_clasf_bio_15(self):
        if self.clasf_bio_15 == constants.SI:
            self.p_clasf_bio_15 = 5
            self.g_clasf_bio_15 = constants.NULO
        else:
            self.p_clasf_bio_15 = 0
            self.g_clasf_bio_15 = constants.GRAVE

    @api.onchange('clasf_bio_18')
    def _onchange_clasf_bio_18(self):
        if self.clasf_bio_18 == constants.SI:
            self.p_clasf_bio_18 = 5
            self.g_clasf_bio_18 = constants.NULO
        else:
            self.p_clasf_bio_18 = 0
            self.g_clasf_bio_18 = constants.GRAVE

    @api.onchange('clasf_bio_19')
    def _onchange_clasf_bio_19(self):
        if self.clasf_bio_19 == constants.SI:
            self.p_clasf_bio_19 = 5
            self.g_clasf_bio_19 = constants.NULO
        else:
            self.p_clasf_bio_19 = 0
            self.g_clasf_bio_19 = constants.GRAVE
