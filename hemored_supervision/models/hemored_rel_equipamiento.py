# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    rel_equip_cant_c_1 = fields.Integer()
    rel_equip_cant_c_b_1 = fields.Integer()
    rel_equip_cant_c_r_1 = fields.Integer()
    rel_equip_cant_c_m_1 = fields.Integer()
    rel_c_equip_1 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_1 = fields.Integer()
    rel_equip_cant_p_b_1 = fields.Integer()
    rel_equip_cant_p_r_1 = fields.Integer()
    rel_equip_cant_p_m_1 = fields.Integer()
    rel_p_equip_1 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_1 = fields.Text()
    rel_equip_cant_c_2 = fields.Integer()
    rel_equip_cant_c_b_2 = fields.Integer()
    rel_equip_cant_c_r_2 = fields.Integer()
    rel_equip_cant_c_m_2 = fields.Integer()
    rel_c_equip_2 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_2 = fields.Integer()
    rel_equip_cant_p_b_2 = fields.Integer()
    rel_equip_cant_p_r_2 = fields.Integer()
    rel_equip_cant_p_m_2 = fields.Integer()
    rel_p_equip_2 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_2 = fields.Text()
    rel_equip_cant_c_3 = fields.Integer()
    rel_equip_cant_c_b_3 = fields.Integer()
    rel_equip_cant_c_r_3 = fields.Integer()
    rel_equip_cant_c_m_3 = fields.Integer()
    rel_c_equip_3 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_3 = fields.Integer()
    rel_equip_cant_p_b_3 = fields.Integer()
    rel_equip_cant_p_r_3 = fields.Integer()
    rel_equip_cant_p_m_3 = fields.Integer()
    rel_p_equip_3 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_3 = fields.Text()
    rel_equip_cant_c_4 = fields.Integer()
    rel_equip_cant_c_b_4 = fields.Integer()
    rel_equip_cant_c_r_4 = fields.Integer()
    rel_equip_cant_c_m_4 = fields.Integer()
    rel_c_equip_4 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_4 = fields.Integer()
    rel_equip_cant_p_b_4 = fields.Integer()
    rel_equip_cant_p_r_4 = fields.Integer()
    rel_equip_cant_p_m_4 = fields.Integer()
    rel_p_equip_4 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_4 = fields.Text()
    rel_equip_cant_c_5 = fields.Integer()
    rel_equip_cant_c_b_5 = fields.Integer()
    rel_equip_cant_c_r_5 = fields.Integer()
    rel_equip_cant_c_m_5 = fields.Integer()
    rel_c_equip_5 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_5 = fields.Integer()
    rel_equip_cant_p_b_5 = fields.Integer()
    rel_equip_cant_p_r_5 = fields.Integer()
    rel_equip_cant_p_m_5 = fields.Integer()
    rel_p_equip_5 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_5 = fields.Text()
    rel_equip_cant_c_6 = fields.Integer()
    rel_equip_cant_c_b_6 = fields.Integer()
    rel_equip_cant_c_r_6 = fields.Integer()
    rel_equip_cant_c_m_6 = fields.Integer()
    rel_c_equip_6 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_6 = fields.Integer()
    rel_equip_cant_p_b_6 = fields.Integer()
    rel_equip_cant_p_r_6 = fields.Integer()
    rel_equip_cant_p_m_6 = fields.Integer()
    rel_p_equip_6 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_6 = fields.Text()
    rel_equip_cant_c_7 = fields.Integer()
    rel_equip_cant_c_b_7 = fields.Integer()
    rel_equip_cant_c_r_7 = fields.Integer()
    rel_equip_cant_c_m_7 = fields.Integer()
    rel_c_equip_7 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_7 = fields.Integer()
    rel_equip_cant_p_b_7 = fields.Integer()
    rel_equip_cant_p_r_7 = fields.Integer()
    rel_equip_cant_p_m_7 = fields.Integer()
    rel_p_equip_7 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_7 = fields.Text()
    rel_equip_cant_c_8 = fields.Integer()
    rel_equip_cant_c_b_8 = fields.Integer()
    rel_equip_cant_c_r_8 = fields.Integer()
    rel_equip_cant_c_m_8 = fields.Integer()
    rel_c_equip_8 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_8 = fields.Integer()
    rel_equip_cant_p_b_8 = fields.Integer()
    rel_equip_cant_p_r_8 = fields.Integer()
    rel_equip_cant_p_m_8 = fields.Integer()
    rel_p_equip_8 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_8 = fields.Text()
    rel_equip_cant_c_9 = fields.Integer()
    rel_equip_cant_c_b_9 = fields.Integer()
    rel_equip_cant_c_r_9 = fields.Integer()
    rel_equip_cant_c_m_9 = fields.Integer()
    rel_c_equip_9 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_9 = fields.Integer()
    rel_equip_cant_p_b_9 = fields.Integer()
    rel_equip_cant_p_r_9 = fields.Integer()
    rel_equip_cant_p_m_9 = fields.Integer()
    rel_p_equip_9 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_9 = fields.Text()
    rel_equip_cant_c_10 = fields.Integer()
    rel_equip_cant_c_b_10 = fields.Integer()
    rel_equip_cant_c_r_10 = fields.Integer()
    rel_equip_cant_c_m_10 = fields.Integer()
    rel_c_equip_10 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_10 = fields.Integer()
    rel_equip_cant_p_b_10 = fields.Integer()
    rel_equip_cant_p_r_10 = fields.Integer()
    rel_equip_cant_p_m_10 = fields.Integer()
    rel_p_equip_10 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_10 = fields.Text()
    rel_equip_cant_c_11 = fields.Integer()
    rel_equip_cant_c_b_11 = fields.Integer()
    rel_equip_cant_c_r_11 = fields.Integer()
    rel_equip_cant_c_m_11 = fields.Integer()
    rel_c_equip_11 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_11 = fields.Integer()
    rel_equip_cant_p_b_11 = fields.Integer()
    rel_equip_cant_p_r_11 = fields.Integer()
    rel_equip_cant_p_m_11 = fields.Integer()
    rel_p_equip_11 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_11 = fields.Text()
    rel_equip_cant_c_12 = fields.Integer()
    rel_equip_cant_c_b_12 = fields.Integer()
    rel_equip_cant_c_r_12 = fields.Integer()
    rel_equip_cant_c_m_12 = fields.Integer()
    rel_c_equip_12 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_12 = fields.Integer()
    rel_equip_cant_p_b_12 = fields.Integer()
    rel_equip_cant_p_r_12 = fields.Integer()
    rel_equip_cant_p_m_12 = fields.Integer()
    rel_p_equip_12 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_12 = fields.Text()
    rel_equip_cant_c_13 = fields.Integer()
    rel_equip_cant_c_b_13 = fields.Integer()
    rel_equip_cant_c_r_13 = fields.Integer()
    rel_equip_cant_c_m_13 = fields.Integer()
    rel_c_equip_13 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_13 = fields.Integer()
    rel_equip_cant_p_b_13 = fields.Integer()
    rel_equip_cant_p_r_13 = fields.Integer()
    rel_equip_cant_p_m_13 = fields.Integer()
    rel_p_equip_13 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_13 = fields.Text()
    rel_equip_cant_c_14 = fields.Integer()
    rel_equip_cant_c_b_14 = fields.Integer()
    rel_equip_cant_c_r_14 = fields.Integer()
    rel_equip_cant_c_m_14 = fields.Integer()
    rel_c_equip_14 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_14 = fields.Integer()
    rel_equip_cant_p_b_14 = fields.Integer()
    rel_equip_cant_p_r_14 = fields.Integer()
    rel_equip_cant_p_m_14 = fields.Integer()
    rel_p_equip_14 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_14 = fields.Text()
    rel_equip_cant_c_15 = fields.Integer()
    rel_equip_cant_c_b_15 = fields.Integer()
    rel_equip_cant_c_r_15 = fields.Integer()
    rel_equip_cant_c_m_15 = fields.Integer()
    rel_c_equip_15 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_15 = fields.Integer()
    rel_equip_cant_p_b_15 = fields.Integer()
    rel_equip_cant_p_r_15 = fields.Integer()
    rel_equip_cant_p_m_15 = fields.Integer()
    rel_p_equip_15 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_15 = fields.Text()
    rel_equip_cant_c_16 = fields.Integer()
    rel_equip_cant_c_b_16 = fields.Integer()
    rel_equip_cant_c_r_16 = fields.Integer()
    rel_equip_cant_c_m_16 = fields.Integer()
    rel_c_equip_16 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_16 = fields.Integer()
    rel_equip_cant_p_b_16 = fields.Integer()
    rel_equip_cant_p_r_16 = fields.Integer()
    rel_equip_cant_p_m_16 = fields.Integer()
    rel_p_equip_16 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_16 = fields.Text()
    rel_equip_cant_c_17 = fields.Integer()
    rel_equip_cant_c_b_17 = fields.Integer()
    rel_equip_cant_c_r_17 = fields.Integer()
    rel_equip_cant_c_m_17 = fields.Integer()
    rel_c_equip_17 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_17 = fields.Integer()
    rel_equip_cant_p_b_17 = fields.Integer()
    rel_equip_cant_p_r_17 = fields.Integer()
    rel_equip_cant_p_m_17 = fields.Integer()
    rel_p_equip_17 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_17 = fields.Text()
    rel_equip_cant_c_18 = fields.Integer()
    rel_equip_cant_c_b_18 = fields.Integer()
    rel_equip_cant_c_r_18 = fields.Integer()
    rel_equip_cant_c_m_18 = fields.Integer()
    rel_c_equip_18 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_18 = fields.Integer()
    rel_equip_cant_p_b_18 = fields.Integer()
    rel_equip_cant_p_r_18 = fields.Integer()
    rel_equip_cant_p_m_18 = fields.Integer()
    rel_p_equip_18 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_18 = fields.Text()
    rel_equip_cant_c_19 = fields.Integer()
    rel_equip_cant_c_b_19 = fields.Integer()
    rel_equip_cant_c_r_19 = fields.Integer()
    rel_equip_cant_c_m_19 = fields.Integer()
    rel_c_equip_19 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_19 = fields.Integer()
    rel_equip_cant_p_b_19 = fields.Integer()
    rel_equip_cant_p_r_19 = fields.Integer()
    rel_equip_cant_p_m_19 = fields.Integer()
    rel_p_equip_19 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_19 = fields.Text()
    rel_equip_cant_c_20 = fields.Integer()
    rel_equip_cant_c_b_20 = fields.Integer()
    rel_equip_cant_c_r_20 = fields.Integer()
    rel_equip_cant_c_m_20 = fields.Integer()
    rel_c_equip_20 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_20 = fields.Integer()
    rel_equip_cant_p_b_20 = fields.Integer()
    rel_equip_cant_p_r_20 = fields.Integer()
    rel_equip_cant_p_m_20 = fields.Integer()
    rel_p_equip_20 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_20 = fields.Text()
    rel_equip_cant_c_21 = fields.Integer()
    rel_equip_cant_c_b_21 = fields.Integer()
    rel_equip_cant_c_r_21 = fields.Integer()
    rel_equip_cant_c_m_21 = fields.Integer()
    rel_c_equip_21 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_21 = fields.Integer()
    rel_equip_cant_p_b_21 = fields.Integer()
    rel_equip_cant_p_r_21 = fields.Integer()
    rel_equip_cant_p_m_21 = fields.Integer()
    rel_p_equip_21 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_21 = fields.Text()
    rel_equip_cant_c_22 = fields.Integer()
    rel_equip_cant_c_b_22 = fields.Integer()
    rel_equip_cant_c_r_22 = fields.Integer()
    rel_equip_cant_c_m_22 = fields.Integer()
    rel_c_equip_22 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_22 = fields.Integer()
    rel_equip_cant_p_b_22 = fields.Integer()
    rel_equip_cant_p_r_22 = fields.Integer()
    rel_equip_cant_p_m_22 = fields.Integer()
    rel_p_equip_22 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_22 = fields.Text()
    rel_equip_cant_c_23 = fields.Integer()
    rel_equip_cant_c_b_23 = fields.Integer()
    rel_equip_cant_c_r_23 = fields.Integer()
    rel_equip_cant_c_m_23 = fields.Integer()
    rel_c_equip_23 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_23 = fields.Integer()
    rel_equip_cant_p_b_23 = fields.Integer()
    rel_equip_cant_p_r_23 = fields.Integer()
    rel_equip_cant_p_m_23 = fields.Integer()
    rel_p_equip_23 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_23 = fields.Text()
    rel_equip_cant_c_24 = fields.Integer()
    rel_equip_cant_c_b_24 = fields.Integer()
    rel_equip_cant_c_r_24 = fields.Integer()
    rel_equip_cant_c_m_24 = fields.Integer()
    rel_c_equip_24 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_24 = fields.Integer()
    rel_equip_cant_p_b_24 = fields.Integer()
    rel_equip_cant_p_r_24 = fields.Integer()
    rel_equip_cant_p_m_24 = fields.Integer()
    rel_p_equip_24 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_24 = fields.Text()
    rel_equip_cant_c_25 = fields.Integer()
    rel_equip_cant_c_b_25 = fields.Integer()
    rel_equip_cant_c_r_25 = fields.Integer()
    rel_equip_cant_c_m_25 = fields.Integer()
    rel_c_equip_25 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_25 = fields.Integer()
    rel_equip_cant_p_b_25 = fields.Integer()
    rel_equip_cant_p_r_25 = fields.Integer()
    rel_equip_cant_p_m_25 = fields.Integer()
    rel_p_equip_25 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_25 = fields.Text()
    rel_equip_cant_c_26 = fields.Integer()
    rel_equip_cant_c_b_26 = fields.Integer()
    rel_equip_cant_c_r_26 = fields.Integer()
    rel_equip_cant_c_m_26 = fields.Integer()
    rel_c_equip_26 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_26 = fields.Integer()
    rel_equip_cant_p_b_26 = fields.Integer()
    rel_equip_cant_p_r_26 = fields.Integer()
    rel_equip_cant_p_m_26 = fields.Integer()
    rel_p_equip_26 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_26 = fields.Text()
    rel_equip_cant_c_27 = fields.Integer()
    rel_equip_cant_c_b_27 = fields.Integer()
    rel_equip_cant_c_r_27 = fields.Integer()
    rel_equip_cant_c_m_27 = fields.Integer()
    rel_c_equip_27 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_27 = fields.Integer()
    rel_equip_cant_p_b_27 = fields.Integer()
    rel_equip_cant_p_r_27 = fields.Integer()
    rel_equip_cant_p_m_27 = fields.Integer()
    rel_p_equip_27 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_27 = fields.Text()
    rel_equip_cant_c_28 = fields.Integer()
    rel_equip_cant_c_b_28 = fields.Integer()
    rel_equip_cant_c_r_28 = fields.Integer()
    rel_equip_cant_c_m_28 = fields.Integer()
    rel_c_equip_28 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_28 = fields.Integer()
    rel_equip_cant_p_b_28 = fields.Integer()
    rel_equip_cant_p_r_28 = fields.Integer()
    rel_equip_cant_p_m_28 = fields.Integer()
    rel_p_equip_28 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_28 = fields.Text()
    rel_equip_cant_c_29 = fields.Integer()
    rel_equip_cant_c_b_29 = fields.Integer()
    rel_equip_cant_c_r_29 = fields.Integer()
    rel_equip_cant_c_m_29 = fields.Integer()
    rel_c_equip_29 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_29 = fields.Integer()
    rel_equip_cant_p_b_29 = fields.Integer()
    rel_equip_cant_p_r_29 = fields.Integer()
    rel_equip_cant_p_m_29 = fields.Integer()
    rel_p_equip_29 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_29 = fields.Text()
    rel_equip_cant_c_30 = fields.Integer()
    rel_equip_cant_c_b_30 = fields.Integer()
    rel_equip_cant_c_r_30 = fields.Integer()
    rel_equip_cant_c_m_30 = fields.Integer()
    rel_c_equip_30 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_30 = fields.Integer()
    rel_equip_cant_p_b_30 = fields.Integer()
    rel_equip_cant_p_r_30 = fields.Integer()
    rel_equip_cant_p_m_30 = fields.Integer()
    rel_p_equip_30 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_30 = fields.Text()

    rel_equip_cant_c_31 = fields.Integer()
    rel_equip_cant_c_b_31 = fields.Integer()
    rel_equip_cant_c_r_31 = fields.Integer()
    rel_equip_cant_c_m_31 = fields.Integer()
    rel_c_equip_31 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_31 = fields.Integer()
    rel_equip_cant_p_b_31 = fields.Integer()
    rel_equip_cant_p_r_31 = fields.Integer()
    rel_equip_cant_p_m_31 = fields.Integer()
    rel_p_equip_31 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_31 = fields.Text()

    rel_equip_cant_c_32 = fields.Integer()
    rel_equip_cant_c_b_32 = fields.Integer()
    rel_equip_cant_c_r_32 = fields.Integer()
    rel_equip_cant_c_m_32 = fields.Integer()
    rel_c_equip_32 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_32 = fields.Integer()
    rel_equip_cant_p_b_32 = fields.Integer()
    rel_equip_cant_p_r_32 = fields.Integer()
    rel_equip_cant_p_m_32 = fields.Integer()
    rel_p_equip_32 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_32 = fields.Text()

    rel_equip_cant_c_33 = fields.Integer()
    rel_equip_cant_c_b_33 = fields.Integer()
    rel_equip_cant_c_r_33 = fields.Integer()
    rel_equip_cant_c_m_33 = fields.Integer()
    rel_c_equip_33 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_33 = fields.Integer()
    rel_equip_cant_p_b_33 = fields.Integer()
    rel_equip_cant_p_r_33 = fields.Integer()
    rel_equip_cant_p_m_33 = fields.Integer()
    rel_p_equip_33 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_33 = fields.Text()

    rel_equip_cant_c_34 = fields.Integer()
    rel_equip_cant_c_b_34 = fields.Integer()
    rel_equip_cant_c_r_34 = fields.Integer()
    rel_equip_cant_c_m_34 = fields.Integer()
    rel_c_equip_34 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    rel_equip_cant_p_34 = fields.Integer()
    rel_equip_cant_p_b_34 = fields.Integer()
    rel_equip_cant_p_r_34 = fields.Integer()
    rel_equip_cant_p_m_34 = fields.Integer()
    rel_p_equip_34 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_rel_equip_34 = fields.Text()

    @api.one
    @api.constrains('rel_equip_cant_c_1', 'rel_equip_cant_c_b_1', 'rel_equip_cant_c_r_1', 'rel_equip_cant_c_m_1')
    def _check_verificacion_totales_c_1(self):
        if self.rel_equip_cant_c_1 != (self.rel_equip_cant_c_b_1 + self.rel_equip_cant_c_r_1 + self.rel_equip_cant_c_m_1):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 1 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_1', 'rel_equip_cant_p_b_1', 'rel_equip_cant_p_r_1', 'rel_equip_cant_p_m_1')
    def _check_verificacion_totales_p_1(self):
        if self.rel_equip_cant_p_1 != (self.rel_equip_cant_p_b_1 + self.rel_equip_cant_p_r_1 + self.rel_equip_cant_p_m_1):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 1 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_2', 'rel_equip_cant_c_b_2', 'rel_equip_cant_c_r_2', 'rel_equip_cant_c_m_2')
    def _check_verificacion_totales_c_2(self):
        if self.rel_equip_cant_c_2 != (self.rel_equip_cant_c_b_2 + self.rel_equip_cant_c_r_2 + self.rel_equip_cant_c_m_2):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 2 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_2', 'rel_equip_cant_p_b_2', 'rel_equip_cant_p_r_2', 'rel_equip_cant_p_m_2')
    def _check_verificacion_totales_p_2(self):
        if self.rel_equip_cant_p_2 != (self.rel_equip_cant_p_b_2 + self.rel_equip_cant_p_r_2 + self.rel_equip_cant_p_m_2):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 2 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_3', 'rel_equip_cant_c_b_3', 'rel_equip_cant_c_r_3', 'rel_equip_cant_c_m_3')
    def _check_verificacion_totales_c_3(self):
        if self.rel_equip_cant_c_3 != (self.rel_equip_cant_c_b_3 + self.rel_equip_cant_c_r_3 + self.rel_equip_cant_c_m_3):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 3 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_3', 'rel_equip_cant_p_b_3', 'rel_equip_cant_p_r_3', 'rel_equip_cant_p_m_3')
    def _check_verificacion_totales_p_3(self):
        if self.rel_equip_cant_p_3 != (self.rel_equip_cant_p_b_3 + self.rel_equip_cant_p_r_3 + self.rel_equip_cant_p_m_3):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 3 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_4', 'rel_equip_cant_c_b_4', 'rel_equip_cant_c_r_4', 'rel_equip_cant_c_m_4')
    def _check_verificacion_totales_c_4(self):
        if self.rel_equip_cant_c_4 != (self.rel_equip_cant_c_b_4 + self.rel_equip_cant_c_r_4 + self.rel_equip_cant_c_m_4):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 4 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_4', 'rel_equip_cant_p_b_4', 'rel_equip_cant_p_r_4', 'rel_equip_cant_p_m_4')
    def _check_verificacion_totales_p_4(self):
        if self.rel_equip_cant_p_4 != (self.rel_equip_cant_p_b_4 + self.rel_equip_cant_p_r_4 + self.rel_equip_cant_p_m_4):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 4 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_5', 'rel_equip_cant_c_b_5', 'rel_equip_cant_c_r_5', 'rel_equip_cant_c_m_5')
    def _check_verificacion_totales_c_5(self):
        if self.rel_equip_cant_c_5 != (self.rel_equip_cant_c_b_5 + self.rel_equip_cant_c_r_5 + self.rel_equip_cant_c_m_5):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 5 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_5', 'rel_equip_cant_p_b_5', 'rel_equip_cant_p_r_5', 'rel_equip_cant_p_m_5')
    def _check_verificacion_totales_p_5(self):
        if self.rel_equip_cant_p_5 != (self.rel_equip_cant_p_b_5 + self.rel_equip_cant_p_r_5 + self.rel_equip_cant_p_m_5):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 5 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_6', 'rel_equip_cant_c_b_6', 'rel_equip_cant_c_r_6', 'rel_equip_cant_c_m_6')
    def _check_verificacion_totales_c_6(self):
        if self.rel_equip_cant_c_6 != (self.rel_equip_cant_c_b_6 + self.rel_equip_cant_c_r_6 + self.rel_equip_cant_c_m_6):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 6 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_6', 'rel_equip_cant_p_b_6', 'rel_equip_cant_p_r_6', 'rel_equip_cant_p_m_6')
    def _check_verificacion_totales_p_6(self):
        if self.rel_equip_cant_p_6 != (self.rel_equip_cant_p_b_6 + self.rel_equip_cant_p_r_6 + self.rel_equip_cant_p_m_6):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 6 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_7', 'rel_equip_cant_c_b_7', 'rel_equip_cant_c_r_7', 'rel_equip_cant_c_m_7')
    def _check_verificacion_totales_c_7(self):
        if self.rel_equip_cant_c_7 != (self.rel_equip_cant_c_b_7 + self.rel_equip_cant_c_r_7 + self.rel_equip_cant_c_m_7):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 7 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_7', 'rel_equip_cant_p_b_7', 'rel_equip_cant_p_r_7', 'rel_equip_cant_p_m_7')
    def _check_verificacion_totales_p_7(self):
        if self.rel_equip_cant_p_7 != (self.rel_equip_cant_p_b_7 + self.rel_equip_cant_p_r_7 + self.rel_equip_cant_p_m_7):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 7 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_8', 'rel_equip_cant_c_b_8', 'rel_equip_cant_c_r_8', 'rel_equip_cant_c_m_8')
    def _check_verificacion_totales_c_8(self):
        if self.rel_equip_cant_c_8 != (self.rel_equip_cant_c_b_8 + self.rel_equip_cant_c_r_8 + self.rel_equip_cant_c_m_8):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 8 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_8', 'rel_equip_cant_p_b_8', 'rel_equip_cant_p_r_8', 'rel_equip_cant_p_m_8')
    def _check_verificacion_totales_p_8(self):
        if self.rel_equip_cant_p_8 != (self.rel_equip_cant_p_b_8 + self.rel_equip_cant_p_r_8 + self.rel_equip_cant_p_m_8):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 8 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_9', 'rel_equip_cant_c_b_9', 'rel_equip_cant_c_r_9', 'rel_equip_cant_c_m_9')
    def _check_verificacion_totales_c_9(self):
        if self.rel_equip_cant_c_9 != (self.rel_equip_cant_c_b_9 + self.rel_equip_cant_c_r_9 + self.rel_equip_cant_c_m_9):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 9 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_9', 'rel_equip_cant_p_b_9', 'rel_equip_cant_p_r_9', 'rel_equip_cant_p_m_9')
    def _check_verificacion_totales_p_9(self):
        if self.rel_equip_cant_p_9 != (self.rel_equip_cant_p_b_9 + self.rel_equip_cant_p_r_9 + self.rel_equip_cant_p_m_9):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 9 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_10', 'rel_equip_cant_c_b_10', 'rel_equip_cant_c_r_10', 'rel_equip_cant_c_m_10')
    def _check_verificacion_totales_c_10(self):
        if self.rel_equip_cant_c_10 != (self.rel_equip_cant_c_b_10 + self.rel_equip_cant_c_r_10 + self.rel_equip_cant_c_m_10):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 10 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_10', 'rel_equip_cant_p_b_10', 'rel_equip_cant_p_r_10', 'rel_equip_cant_p_m_10')
    def _check_verificacion_totales_p_10(self):
        if self.rel_equip_cant_p_10 != (self.rel_equip_cant_p_b_10 + self.rel_equip_cant_p_r_10 + self.rel_equip_cant_p_m_10):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 10 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_11', 'rel_equip_cant_c_b_11', 'rel_equip_cant_c_r_11', 'rel_equip_cant_c_m_11')
    def _check_verificacion_totales_c_11(self):
        if self.rel_equip_cant_c_11 != (self.rel_equip_cant_c_b_11 + self.rel_equip_cant_c_r_11 + self.rel_equip_cant_c_m_11):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 11 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_11', 'rel_equip_cant_p_b_11', 'rel_equip_cant_p_r_11', 'rel_equip_cant_p_m_11')
    def _check_verificacion_totales_p_11(self):
        if self.rel_equip_cant_p_11 != (self.rel_equip_cant_p_b_11 + self.rel_equip_cant_p_r_11 + self.rel_equip_cant_p_m_11):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 11 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_12', 'rel_equip_cant_c_b_12', 'rel_equip_cant_c_r_12', 'rel_equip_cant_c_m_12')
    def _check_verificacion_totales_c_12(self):
        if self.rel_equip_cant_c_12 != (self.rel_equip_cant_c_b_12 + self.rel_equip_cant_c_r_12 + self.rel_equip_cant_c_m_12):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 12 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_12', 'rel_equip_cant_p_b_12', 'rel_equip_cant_p_r_12', 'rel_equip_cant_p_m_12')
    def _check_verificacion_totales_p_12(self):
        if self.rel_equip_cant_p_12 != (self.rel_equip_cant_p_b_12 + self.rel_equip_cant_p_r_12 + self.rel_equip_cant_p_m_12):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 12 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_13', 'rel_equip_cant_c_b_13', 'rel_equip_cant_c_r_13', 'rel_equip_cant_c_m_13')
    def _check_verificacion_totales_c_13(self):
        if self.rel_equip_cant_c_13 != (self.rel_equip_cant_c_b_13 + self.rel_equip_cant_c_r_13 + self.rel_equip_cant_c_m_13):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 13 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_13', 'rel_equip_cant_p_b_13', 'rel_equip_cant_p_r_13', 'rel_equip_cant_p_m_13')
    def _check_verificacion_totales_p_13(self):
        if self.rel_equip_cant_p_13 != (self.rel_equip_cant_p_b_13 + self.rel_equip_cant_p_r_13 + self.rel_equip_cant_p_m_13):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 13 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_14', 'rel_equip_cant_c_b_14', 'rel_equip_cant_c_r_14', 'rel_equip_cant_c_m_14')
    def _check_verificacion_totales_c_14(self):
        if self.rel_equip_cant_c_14 != (self.rel_equip_cant_c_b_14 + self.rel_equip_cant_c_r_14 + self.rel_equip_cant_c_m_14):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 14 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_14', 'rel_equip_cant_p_b_14', 'rel_equip_cant_p_r_14', 'rel_equip_cant_p_m_14')
    def _check_verificacion_totales_p_14(self):
        if self.rel_equip_cant_p_14 != (self.rel_equip_cant_p_b_14 + self.rel_equip_cant_p_r_14 + self.rel_equip_cant_p_m_14):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 14 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_15', 'rel_equip_cant_c_b_15', 'rel_equip_cant_c_r_15', 'rel_equip_cant_c_m_15')
    def _check_verificacion_totales_c_15(self):
        if self.rel_equip_cant_c_15 != (self.rel_equip_cant_c_b_15 + self.rel_equip_cant_c_r_15 + self.rel_equip_cant_c_m_15):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 15 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_15', 'rel_equip_cant_p_b_15', 'rel_equip_cant_p_r_15', 'rel_equip_cant_p_m_15')
    def _check_verificacion_totales_p_15(self):
        if self.rel_equip_cant_p_15 != (self.rel_equip_cant_p_b_15 + self.rel_equip_cant_p_r_15 + self.rel_equip_cant_p_m_15):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 15 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_16', 'rel_equip_cant_c_b_16', 'rel_equip_cant_c_r_16', 'rel_equip_cant_c_m_16')
    def _check_verificacion_totales_c_16(self):
        if self.rel_equip_cant_c_16 != (self.rel_equip_cant_c_b_16 + self.rel_equip_cant_c_r_16 + self.rel_equip_cant_c_m_16):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 16 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_16', 'rel_equip_cant_p_b_16', 'rel_equip_cant_p_r_16', 'rel_equip_cant_p_m_16')
    def _check_verificacion_totales_p_16(self):
        if self.rel_equip_cant_p_16 != (self.rel_equip_cant_p_b_16 + self.rel_equip_cant_p_r_16 + self.rel_equip_cant_p_m_16):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 16 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_17', 'rel_equip_cant_c_b_17', 'rel_equip_cant_c_r_17', 'rel_equip_cant_c_m_17')
    def _check_verificacion_totales_c_17(self):
        if self.rel_equip_cant_c_17 != (self.rel_equip_cant_c_b_17 + self.rel_equip_cant_c_r_17 + self.rel_equip_cant_c_m_17):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 17 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_17', 'rel_equip_cant_p_b_17', 'rel_equip_cant_p_r_17', 'rel_equip_cant_p_m_17')
    def _check_verificacion_totales_p_17(self):
        if self.rel_equip_cant_p_17 != (self.rel_equip_cant_p_b_17 + self.rel_equip_cant_p_r_17 + self.rel_equip_cant_p_m_17):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 17 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_18', 'rel_equip_cant_c_b_18', 'rel_equip_cant_c_r_18', 'rel_equip_cant_c_m_18')
    def _check_verificacion_totales_c_18(self):
        if self.rel_equip_cant_c_18 != (self.rel_equip_cant_c_b_18 + self.rel_equip_cant_c_r_18 + self.rel_equip_cant_c_m_18):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 18 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_18', 'rel_equip_cant_p_b_18', 'rel_equip_cant_p_r_18', 'rel_equip_cant_p_m_18')
    def _check_verificacion_totales_p_18(self):
        if self.rel_equip_cant_p_18 != (self.rel_equip_cant_p_b_18 + self.rel_equip_cant_p_r_18 + self.rel_equip_cant_p_m_18):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 18 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_19', 'rel_equip_cant_c_b_19', 'rel_equip_cant_c_r_19', 'rel_equip_cant_c_m_19')
    def _check_verificacion_totales_c_19(self):
        if self.rel_equip_cant_c_19 != (self.rel_equip_cant_c_b_19 + self.rel_equip_cant_c_r_19 + self.rel_equip_cant_c_m_19):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 19 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_19', 'rel_equip_cant_p_b_19', 'rel_equip_cant_p_r_19', 'rel_equip_cant_p_m_19')
    def _check_verificacion_totales_p_19(self):
        if self.rel_equip_cant_p_19 != (self.rel_equip_cant_p_b_19 + self.rel_equip_cant_p_r_19 + self.rel_equip_cant_p_m_19):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 19 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_20', 'rel_equip_cant_c_b_20', 'rel_equip_cant_c_r_20', 'rel_equip_cant_c_m_20')
    def _check_verificacion_totales_c_20(self):
        if self.rel_equip_cant_c_20 != (self.rel_equip_cant_c_b_20 + self.rel_equip_cant_c_r_20 + self.rel_equip_cant_c_m_20):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 20 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_20', 'rel_equip_cant_p_b_20', 'rel_equip_cant_p_r_20', 'rel_equip_cant_p_m_20')
    def _check_verificacion_totales_p_20(self):
        if self.rel_equip_cant_p_20 != (self.rel_equip_cant_p_b_20 + self.rel_equip_cant_p_r_20 + self.rel_equip_cant_p_m_20):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 20 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_21', 'rel_equip_cant_c_b_21', 'rel_equip_cant_c_r_21', 'rel_equip_cant_c_m_21')
    def _check_verificacion_totales_c_21(self):
        if self.rel_equip_cant_c_21 != (self.rel_equip_cant_c_b_21 + self.rel_equip_cant_c_r_21 + self.rel_equip_cant_c_m_21):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 21 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_21', 'rel_equip_cant_p_b_21', 'rel_equip_cant_p_r_21', 'rel_equip_cant_p_m_21')
    def _check_verificacion_totales_p_21(self):
        if self.rel_equip_cant_p_21 != (self.rel_equip_cant_p_b_21 + self.rel_equip_cant_p_r_21 + self.rel_equip_cant_p_m_21):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 21 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_22', 'rel_equip_cant_c_b_22', 'rel_equip_cant_c_r_22', 'rel_equip_cant_c_m_22')
    def _check_verificacion_totales_c_22(self):
        if self.rel_equip_cant_c_22 != (self.rel_equip_cant_c_b_22 + self.rel_equip_cant_c_r_22 + self.rel_equip_cant_c_m_22):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 22 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_22', 'rel_equip_cant_p_b_22', 'rel_equip_cant_p_r_22', 'rel_equip_cant_p_m_22')
    def _check_verificacion_totales_p_22(self):
        if self.rel_equip_cant_p_22 != (self.rel_equip_cant_p_b_22 + self.rel_equip_cant_p_r_22 + self.rel_equip_cant_p_m_22):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 22 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_23', 'rel_equip_cant_c_b_23', 'rel_equip_cant_c_r_23', 'rel_equip_cant_c_m_23')
    def _check_verificacion_totales_c_23(self):
        if self.rel_equip_cant_c_23 != (self.rel_equip_cant_c_b_23 + self.rel_equip_cant_c_r_23 + self.rel_equip_cant_c_m_23):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 23 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_23', 'rel_equip_cant_p_b_23', 'rel_equip_cant_p_r_23', 'rel_equip_cant_p_m_23')
    def _check_verificacion_totales_p_23(self):
        if self.rel_equip_cant_p_23 != (self.rel_equip_cant_p_b_23 + self.rel_equip_cant_p_r_23 + self.rel_equip_cant_p_m_23):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 23 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_24', 'rel_equip_cant_c_b_24', 'rel_equip_cant_c_r_24', 'rel_equip_cant_c_m_24')
    def _check_verificacion_totales_c_24(self):
        if self.rel_equip_cant_c_24 != (self.rel_equip_cant_c_b_24 + self.rel_equip_cant_c_r_24 + self.rel_equip_cant_c_m_24):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 24 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_24', 'rel_equip_cant_p_b_24', 'rel_equip_cant_p_r_24', 'rel_equip_cant_p_m_24')
    def _check_verificacion_totales_p_24(self):
        if self.rel_equip_cant_p_24 != (self.rel_equip_cant_p_b_24 + self.rel_equip_cant_p_r_24 + self.rel_equip_cant_p_m_24):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 24 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_25', 'rel_equip_cant_c_b_25', 'rel_equip_cant_c_r_25', 'rel_equip_cant_c_m_25')
    def _check_verificacion_totales_c_25(self):
        if self.rel_equip_cant_c_25 != (self.rel_equip_cant_c_b_25 + self.rel_equip_cant_c_r_25 + self.rel_equip_cant_c_m_25):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 25 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_25', 'rel_equip_cant_p_b_25', 'rel_equip_cant_p_r_25', 'rel_equip_cant_p_m_25')
    def _check_verificacion_totales_p_25(self):
        if self.rel_equip_cant_p_25 != (self.rel_equip_cant_p_b_25 + self.rel_equip_cant_p_r_25 + self.rel_equip_cant_p_m_25):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 25 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_26', 'rel_equip_cant_c_b_26', 'rel_equip_cant_c_r_26', 'rel_equip_cant_c_m_26')
    def _check_verificacion_totales_c_26(self):
        if self.rel_equip_cant_c_26 != (self.rel_equip_cant_c_b_26 + self.rel_equip_cant_c_r_26 + self.rel_equip_cant_c_m_26):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 26 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_26', 'rel_equip_cant_p_b_26', 'rel_equip_cant_p_r_26', 'rel_equip_cant_p_m_26')
    def _check_verificacion_totales_p_26(self):
        if self.rel_equip_cant_p_26 != (self.rel_equip_cant_p_b_26 + self.rel_equip_cant_p_r_26 + self.rel_equip_cant_p_m_26):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 26 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_31', 'rel_equip_cant_c_b_31', 'rel_equip_cant_c_r_31', 'rel_equip_cant_c_m_31')
    def _check_verificacion_totales_c_31(self):
        if self.rel_equip_cant_c_31 != (self.rel_equip_cant_c_b_31 + self.rel_equip_cant_c_r_31 + self.rel_equip_cant_c_m_31):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 27 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_31', 'rel_equip_cant_p_b_31', 'rel_equip_cant_p_r_31', 'rel_equip_cant_p_m_31')
    def _check_verificacion_totales_p_31(self):
        if self.rel_equip_cant_p_31 != (self.rel_equip_cant_p_b_31 + self.rel_equip_cant_p_r_31 + self.rel_equip_cant_p_m_31):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 27 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_32', 'rel_equip_cant_c_b_32', 'rel_equip_cant_c_r_32', 'rel_equip_cant_c_m_32')
    def _check_verificacion_totales_c_32(self):
        if self.rel_equip_cant_c_32 != (self.rel_equip_cant_c_b_32 + self.rel_equip_cant_c_r_32 + self.rel_equip_cant_c_m_32):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 28 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_32', 'rel_equip_cant_p_b_32', 'rel_equip_cant_p_r_32', 'rel_equip_cant_p_m_32')
    def _check_verificacion_totales_p_32(self):
        if self.rel_equip_cant_p_32 != (self.rel_equip_cant_p_b_32 + self.rel_equip_cant_p_r_32 + self.rel_equip_cant_p_m_32):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 28 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_33', 'rel_equip_cant_c_b_33', 'rel_equip_cant_c_r_33', 'rel_equip_cant_c_m_33')
    def _check_verificacion_totales_c_33(self):
        if self.rel_equip_cant_c_33 != (self.rel_equip_cant_c_b_33 + self.rel_equip_cant_c_r_33 + self.rel_equip_cant_c_m_33):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 29 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_33', 'rel_equip_cant_p_b_33', 'rel_equip_cant_p_r_33', 'rel_equip_cant_p_m_33')
    def _check_verificacion_totales_p_33(self):
        if self.rel_equip_cant_p_33 != (self.rel_equip_cant_p_b_33 + self.rel_equip_cant_p_r_33 + self.rel_equip_cant_p_m_33):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 29 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_34', 'rel_equip_cant_c_b_34', 'rel_equip_cant_c_r_34', 'rel_equip_cant_c_m_34')
    def _check_verificacion_totales_c_34(self):
        if self.rel_equip_cant_c_34 != (self.rel_equip_cant_c_b_34 + self.rel_equip_cant_c_r_34 + self.rel_equip_cant_c_m_34):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 30 Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_34', 'rel_equip_cant_p_b_34', 'rel_equip_cant_p_r_34', 'rel_equip_cant_p_m_34')
    def _check_verificacion_totales_p_34(self):
        if self.rel_equip_cant_p_34 != (self.rel_equip_cant_p_b_34 + self.rel_equip_cant_p_r_34 + self.rel_equip_cant_p_m_34):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 30 Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_27', 'rel_equip_cant_c_b_27', 'rel_equip_cant_c_r_27', 'rel_equip_cant_c_m_27')
    def _check_verificacion_totales_c_27(self):
        if self.rel_equip_cant_c_27 != (self.rel_equip_cant_c_b_27 + self.rel_equip_cant_c_r_27 + self.rel_equip_cant_c_m_27):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 31 Segundo Grupo Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_27', 'rel_equip_cant_p_b_27', 'rel_equip_cant_p_r_27', 'rel_equip_cant_p_m_27')
    def _check_verificacion_totales_p_27(self):
        if self.rel_equip_cant_p_27 != (self.rel_equip_cant_p_b_27 + self.rel_equip_cant_p_r_27 + self.rel_equip_cant_p_m_27):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 31 Segundo Grupo Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_28', 'rel_equip_cant_c_b_28', 'rel_equip_cant_c_r_28', 'rel_equip_cant_c_m_28')
    def _check_verificacion_totales_c_28(self):
        if self.rel_equip_cant_c_28 != (self.rel_equip_cant_c_b_28 + self.rel_equip_cant_c_r_28 + self.rel_equip_cant_c_m_28):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 32 Segundo Grupo Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_28', 'rel_equip_cant_p_b_28', 'rel_equip_cant_p_r_28', 'rel_equip_cant_p_m_28')
    def _check_verificacion_totales_p_28(self):
        if self.rel_equip_cant_p_28 != (self.rel_equip_cant_p_b_28 + self.rel_equip_cant_p_r_28 + self.rel_equip_cant_p_m_28):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 32 Segundo Grupo Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_29', 'rel_equip_cant_c_b_29', 'rel_equip_cant_c_r_29', 'rel_equip_cant_c_m_29')
    def _check_verificacion_totales_c_29(self):
        if self.rel_equip_cant_c_29 != (self.rel_equip_cant_c_b_29 + self.rel_equip_cant_c_r_29 + self.rel_equip_cant_c_m_29):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 33 Segundo Grupo Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_29', 'rel_equip_cant_p_b_29', 'rel_equip_cant_p_r_29', 'rel_equip_cant_p_m_29')
    def _check_verificacion_totales_p_29(self):
        if self.rel_equip_cant_p_29 != (self.rel_equip_cant_p_b_29 + self.rel_equip_cant_p_r_29 + self.rel_equip_cant_p_m_29):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 33 Segundo Grupo Propios')

    @api.one
    @api.constrains('rel_equip_cant_c_30', 'rel_equip_cant_c_b_30', 'rel_equip_cant_c_r_30', 'rel_equip_cant_c_m_30')
    def _check_verificacion_totales_c_30(self):
        if self.rel_equip_cant_c_30 != (self.rel_equip_cant_c_b_30 + self.rel_equip_cant_c_r_30 + self.rel_equip_cant_c_m_30):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 34 Segundo Grupo Cesión de Uso')

    @api.one
    @api.constrains('rel_equip_cant_p_30', 'rel_equip_cant_p_b_30', 'rel_equip_cant_p_r_30', 'rel_equip_cant_p_m_30')
    def _check_verificacion_totales_p_30(self):
        if self.rel_equip_cant_p_30 != (self.rel_equip_cant_p_b_30 + self.rel_equip_cant_p_r_30 + self.rel_equip_cant_p_m_30):
            raise ValidationError('Error, no coinciden totales con cantidad de Buenos, Regulares y Malos del Grupo 34 Segundo Grupo Propios')
