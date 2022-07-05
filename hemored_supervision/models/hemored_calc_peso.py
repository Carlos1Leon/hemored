# -*- coding: utf-8 -*-

from odoo import fields, models, api
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    total_peso = fields.Integer()

    @api.multi
    def action_terminar(self):
        for obj in self:
            total = obj.p_rg_1 + obj.p_rg_2 + obj.p_rg_3 + obj.p_rg_4 + obj.p_rg_5 + obj.p_rg_6 + obj.p_rg_8 + obj.p_rg_9
            + obj.p_rg_10 + obj.p_rg_11 + obj.p_rg_12 + obj.p_rg_13 + obj.p_rg_14 + obj.p_rg_15 + obj.p_rg_16 + obj.p_rg_17
            + obj.p_rg_18 + obj.p_rg_19 + obj.p_rg_20 + obj.p_rg_21 + obj.p_rg_22 + obj.p_rg_23 + obj.p_rg_24 + obj.p_rg_25
            + obj.p_rg_26 + obj.p_rg_28 + obj.p_rg_29 + obj.p_rg_30 + obj.p_rh_1 + obj.p_rh_2 + obj.p_rh_3
            + obj.p_rh_4 + obj.p_rh_5 + obj.p_rh_6 + obj.p_rh_7 + obj.p_rh_8 + obj.p_rh_9 + obj.p_rh_10 + obj.p_pros_1
            + obj.p_pros_2 + obj.p_pros_3 + obj.p_pros_4 + obj.p_pros_5 + obj.p_pros_6 + obj.p_pros_7 + obj.p_pros_8
            + obj.p_pros_9 + obj.p_pros_10 + obj.p_pros_11 + obj.p_pros_12 + obj.p_pros_13 + obj.p_pros_14 + obj.p_pros_15
            + obj.p_pros_16 + obj.p_pros_17 + obj.p_pros_18 + obj.p_pros_19 + obj.p_pros_20 + obj.p_pros_21 + obj.p_pros_22
            + obj.p_pros_23 + obj.p_pros_24 + obj.p_pros_25 + obj.p_pros_26 + obj.p_pros_27 + obj.p_pros_28 + obj.p_pros_29
            + obj.p_pros_30 + obj.p_pros_31 + obj.p_pros_32 + obj.p_pros_33 + obj.p_pros_34 + obj.p_pros_35 + obj.p_pros_36
            + obj.p_pros_37 + obj.p_pros_38 + obj.p_pros_39 + obj.p_pros_40 + obj.p_pros_41 + obj.p_pros_42 + obj.p_pros_43
            + obj.p_pros_44 + obj.p_pros_45 + obj.p_pros_47 + obj.p_pros_49 + obj.p_pros_50 + obj.p_pros_51 + obj.p_pros_52
            + obj.p_pros_53 + obj.p_r_pros_53 + obj.p_pros_54 + obj.p_pros_55 + obj.p_pros_56 + obj.p_pros_57 + obj.p_pros_58
            + obj.p_pros_59 + obj.p_pros_60 + obj.p_pros_61 + obj.p_pros_62 + obj.p_pros_63 + obj.p_pros_64 + obj.p_pros_65
            + obj.p_pros_66 + obj.p_pros_68 + obj.p_pros_69 + obj.p_pros_70 + obj.p_pros_73
            + obj.p_pros_74 + obj.p_pros_75 + obj.p_pros_76 + obj.p_pros_77 + obj.p_pros_78 + obj.p_pros_79 + obj.p_pros_80
            + obj.p_pros_81 + obj.p_pros_82 + obj.p_pros_83 + obj.p_pros_84 + obj.p_pros_85 + obj.p_pros_87
            + obj.p_pros_88 + obj.p_pros_89 + obj.p_pros_90 + obj.p_pros_91 + obj.p_pros_92 + obj.p_pros_93 + obj.p_pros_94
            + obj.p_pros_96 + obj.p_pros_97 + obj.p_pros_98 + obj.p_cali_1 + obj.p_cali_2 + obj.p_cali_3 + obj.p_cali_4
            + obj.p_cali_5 + obj.p_cali_6 + obj.p_cali_7 + obj.p_cali_8 + obj.p_alm_1 + obj.p_alm_2
            + obj.p_alm_3 + obj.p_alm_4 + obj.p_alm_5 + obj.p_alm_6 + obj.p_alm_7 + obj.p_alm_8 + obj.p_alm_9 + obj.p_alm_10
            + obj.p_alm_11 + obj.p_alm_12 + obj.p_alm_13 + obj.p_alm_14 + obj.p_sis_inform_1 + obj.p_sis_inform_2 + obj.p_sis_inform_3
            + obj.p_sis_inform_4 + obj.p_sis_inform_5 + obj.p_clasf_bio_2 + obj.p_clasf_bio_3 + obj.p_clasf_bio_4
            + obj.p_clasf_bio_5 + obj.p_clasf_bio_6 + obj.p_clasf_bio_7 + obj.p_clasf_bio_8 + obj.p_clasf_bio_9 + obj.p_clasf_bio_14
            + obj.p_clasf_bio_15 + obj.p_clasf_bio_16 + obj.p_equip_1 + obj.p_equip_2 + obj.p_equip_3 + obj.p_equip_4
            + obj.p_equip_5 + obj.p_equip_6 + obj.p_equip_7 + obj.p_equip_8 + obj.p_equip_9 + obj.p_equip_10
            + obj.p_infra_instal_1 + obj.p_infra_instal_2 + obj.p_infra_instal_3 + obj.p_infra_instal_4 + obj.p_infra_instal_5
            + obj.p_infra_instal_6 + obj.p_infra_instal_7 + obj.p_infra_instal_8 + obj.p_infra_instal_9 + obj.p_infra_instal_10
            + obj.p_infra_instal_11 + obj.p_infra_instal_12 + obj.p_infra_instal_13 + obj.p_infra_instal_14 + obj.p_infra_instal_15
            + obj.p_infra_instal_16 + obj.p_infra_instal_17 + obj.p_infra_instal_18 + obj.p_infra_instal_19 + obj.p_infra_instal_20
            + obj.p_infra_instal_21 + obj.p_infra_instal_22 + obj.p_infra_instal_23 + obj.p_infra_instal_24 + obj.p_infra_instal_25
            + obj.p_infra_instal_26 + obj.p_infra_instal_27 + obj.p_infra_instal_28 + obj.p_bio_s_2 + obj.p_bio_s_3
            + obj.p_bio_s_4 + obj.p_bio_s_5
            obj.write({
                'total_peso': total,
                'state': constants.TERMINADO
            })
