# -*- coding: utf-8 -*-

from odoo import fields, models, api
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    bio_s_2 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_bio_s_2 = fields.Text()
    p_bio_s_2 = fields.Integer()
    g_bio_s_2 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    bio_s_3 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_bio_s_3 = fields.Text()
    p_bio_s_3 = fields.Integer(
        default=0
    )
    g_bio_s_3 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    bio_s_4 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_bio_s_4 = fields.Text()
    p_bio_s_4 = fields.Integer(
        default=0
    )
    g_bio_s_4 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    bio_s_5 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_bio_s_5 = fields.Text()
    p_bio_s_5 = fields.Integer()
    g_bio_s_5 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )

    @api.onchange('bio_s_2')
    def _onchange_bio_s_2(self):
        if self.bio_s_2 == constants.SI:
            self.p_bio_s_2 = 5
            self.g_bio_s_2 = constants.NULO
        else:
            self.p_bio_s_2 = 0
            self.g_bio_s_2 = constants.GRAVE

    @api.onchange('bio_s_5')
    def _onchange_bio_s_5(self):
        if self.bio_s_5 == constants.SI:
            self.p_bio_s_5 = 5
            self.g_bio_s_5 = constants.NULO
        else:
            self.p_bio_s_5 = 0
            self.g_bio_s_5 = constants.GRAVE
