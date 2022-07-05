# -*- coding: utf-8 -*-

from odoo import fields, models, api
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    equip_1 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_1 = fields.Text()
    p_equip_1 = fields.Integer()
    g_equip_1 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    equip_2 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_2 = fields.Text()
    p_equip_2 = fields.Integer()
    g_equip_2 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    equip_3 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_3 = fields.Text()
    p_equip_3 = fields.Integer()
    g_equip_3 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    equip_4 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_4 = fields.Text()
    p_equip_4 = fields.Integer()
    g_equip_4 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    equip_5 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_5 = fields.Text()
    p_equip_5 = fields.Integer()
    g_equip_5 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    equip_6 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_6 = fields.Text()
    p_equip_6 = fields.Integer()
    g_equip_6 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    equip_7 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_7 = fields.Text()
    p_equip_7 = fields.Integer()
    g_equip_7 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    equip_8 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_8 = fields.Text()
    p_equip_8 = fields.Integer()
    g_equip_8 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    equip_9 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_9 = fields.Text()
    p_equip_9 = fields.Integer()
    g_equip_9 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    equip_10 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_10 = fields.Text()
    p_equip_10 = fields.Integer()
    g_equip_10 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    equip_11 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_equip_11 = fields.Text()
    p_equip_11 = fields.Integer()
    g_equip_11 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )

    @api.onchange('equip_1')
    def _onchange_equip_1(self):
        if self.equip_1 == constants.SI:
            self.p_equip_1 = 5
            self.g_equip_1 = constants.NULO
        else:
            self.p_equip_1 = 0
            self.g_equip_1 = constants.GRAVE

    @api.onchange('equip_2')
    def _onchange_equip_2(self):
        if self.equip_2 == constants.SI:
            self.p_equip_2 = 5
            self.g_equip_2 = constants.NULO
        else:
            self.p_equip_2 = 0
            self.g_equip_2 = constants.GRAVE

    @api.onchange('equip_3')
    def _onchange_equip_3(self):
        if self.equip_3 == constants.SI:
            self.p_equip_3 = 4
            self.g_equip_3 = constants.NULO
        else:
            self.p_equip_3 = 0
            self.g_equip_3 = constants.MODERADO

    @api.onchange('equip_4')
    def _onchange_equip_4(self):
        if self.equip_4 == constants.SI:
            self.p_equip_4 = 3
            self.g_equip_4 = constants.NULO
        else:
            self.p_equip_4 = 0
            self.g_equip_4 = constants.MODERADO

    @api.onchange('equip_5')
    def _onchange_equip_5(self):
        if self.equip_5 == constants.SI:
            self.p_equip_5 = 5
            self.g_equip_5 = constants.NULO
        else:
            self.p_equip_5 = 0
            self.g_equip_5 = constants.GRAVE

    @api.onchange('equip_6')
    def _onchange_equip_6(self):
        if self.equip_6 == constants.SI:
            self.p_equip_6 = 5
            self.g_equip_6 = constants.NULO
        else:
            self.p_equip_6 = 0
            self.g_equip_6 = constants.GRAVE

    @api.onchange('equip_7')
    def _onchange_equip_7(self):
        if self.equip_7 == constants.SI:
            self.p_equip_7 = 4
            self.g_equip_7 = constants.NULO
        else:
            self.p_equip_7 = 0
            self.g_equip_7 = constants.MODERADO

    @api.onchange('equip_8')
    def _onchange_equip_8(self):
        if self.equip_8 == constants.SI:
            self.p_equip_8 = 5
            self.g_equip_8 = constants.NULO
        else:
            self.p_equip_8 = 0
            self.g_equip_8 = constants.GRAVE

    @api.onchange('equip_9')
    def _onchange_equip_9(self):
        if self.equip_9 == constants.SI:
            self.p_equip_9 = 5
            self.g_equip_9 = constants.NULO
        else:
            self.p_equip_9 = 0
            self.g_equip_9 = constants.GRAVE

    @api.onchange('equip_10')
    def _onchange_equip_10(self):
        if self.equip_10 == constants.SI:
            self.p_equip_10 = 5
            self.g_equip_10 = constants.NULO
        else:
            self.p_equip_10 = 0
            self.g_equip_10 = constants.MODERADO

    @api.onchange('equip_11')
    def _onchange_equip_11(self):
        if self.equip_11 == constants.SI:
            self.p_equip_11 = 5
            self.g_equip_11 = constants.NULO
        else:
            self.p_equip_11 = 0
            self.g_equip_11 = constants.GRAVE
