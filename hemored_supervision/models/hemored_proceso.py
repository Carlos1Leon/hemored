# -*- coding: utf-8 -*-

from odoo import fields, models, api
from ..models import constants


class HemoredSupervisionRecordSupervision(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    obs_pros_1 = fields.Text()
    esp_pros_1 = fields.Text()
    p_pros_1 = fields.Integer(
        default=0
    )
    g_pros_1 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    pros_2 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_2 = fields.Text()
    p_pros_2 = fields.Integer()
    g_pros_2 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_3 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_3 = fields.Text()
    p_pros_3 = fields.Integer()
    g_pros_3 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_4_1 = fields.Boolean(
        string='DNI',
        default=False
    )
    t_pros_4_2 = fields.Boolean(
        string='Pasaporte',
        default=False
    )
    t_pros_4_3 = fields.Boolean(
        string='Carnet de extranjeria',
        default=False
    )
    obs_pros_4 = fields.Text()
    p_pros_4 = fields.Integer(
        default=0
    )
    g_pros_4 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_5 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_5 = fields.Text()
    p_pros_5 = fields.Integer()
    g_pros_5 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_6 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_6 = fields.Text()
    p_pros_6 = fields.Integer()
    g_pros_6 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_7 = fields.Selection(
        selection=constants.SELECTION_TIPO_METODOLOGIA,
    )
    obs_pros_7 = fields.Text()
    p_pros_7 = fields.Integer()
    g_pros_7 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_8_1 = fields.Boolean(default=False)
    t_pros_8_2 = fields.Boolean(default=False)
    t_pros_8_3 = fields.Boolean(default=False)
    obs_pros_8 = fields.Text()
    p_pros_8 = fields.Integer()
    g_pros_8 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_9 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_9 = fields.Text()
    p_pros_9 = fields.Integer()
    g_pros_9 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_10 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_10 = fields.Text()
    p_pros_10 = fields.Integer()
    g_pros_10 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_11 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_11 = fields.Text()
    p_pros_11 = fields.Integer()
    g_pros_11 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_12 = fields.Selection(
        selection=constants.SELECTION_TIPO_EXAM,
    )
    obs_pros_12 = fields.Text()
    p_pros_12 = fields.Integer()
    g_pros_12 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_13 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_13 = fields.Text()
    p_pros_13 = fields.Integer()
    g_pros_13 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_14 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_14 = fields.Text()
    p_pros_14 = fields.Integer()
    g_pros_14 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_15 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_15 = fields.Text()
    p_pros_15 = fields.Integer()
    g_pros_15 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_16 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_16 = fields.Text()
    p_pros_16 = fields.Integer()
    g_pros_16 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_17 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    t_pros_17 = fields.Selection(
        selection=constants.SELECTION_TIPO_TAMIZAJE,
    )
    obs_pros_17 = fields.Text()
    p_pros_17 = fields.Integer()
    g_pros_17 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_18 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_18 = fields.Text()
    p_pros_18 = fields.Integer()
    g_pros_18 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_19 = fields.Selection(
        selection=constants.SELECTION_TIPO_ENVIO,
    )
    obs_pros_19 = fields.Text()
    p_pros_19 = fields.Integer(
        default=0
    )
    g_pros_19 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    esp_pros_20 = fields.Text()
    obs_pros_20 = fields.Text()
    p_pros_20 = fields.Integer(
        default=0
    )
    g_pros_20 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO,
    )
    pros_21 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_21 = fields.Text()
    p_pros_21 = fields.Integer()
    g_pros_21 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_22 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_22 = fields.Text()
    p_pros_22 = fields.Integer()
    g_pros_22 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    obs_pros_23 = fields.Text()
    p_pros_23 = fields.Integer(
        default=0
    )
    g_pros_23 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    t_pros_23 = fields.Selection(
        selection=constants.SELECTION_TIPO_SELLADO_TABULADURA,
    )
    obs_pros_24 = fields.Text()
    p_pros_24 = fields.Integer(
        default=0
    )
    g_pros_24 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    t_pros_24 = fields.Selection(
        selection=constants.SELECTION_TIPO_BOLSA_COLECTORA,
    )
    pros_25 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_25 = fields.Text()
    p_pros_25 = fields.Integer(
        default=0
    )
    g_pros_25 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_26 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_26 = fields.Text()
    p_pros_26 = fields.Integer(
        default=0
    )
    g_pros_26 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_27 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_27 = fields.Text()
    p_pros_27 = fields.Integer(
        default=0
    )
    g_pros_27 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_28 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_28 = fields.Text()
    p_pros_28 = fields.Integer(
        default=0
    )
    g_pros_28 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_29 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_29 = fields.Text()
    p_pros_29 = fields.Integer(
        default=0
    )
    g_pros_29 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_30 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_30 = fields.Text()
    p_pros_30 = fields.Integer(
        default=0
    )
    g_pros_30 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_31 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_31 = fields.Text()
    p_pros_31 = fields.Integer(
        default=0
    )
    g_pros_31 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_32 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_32 = fields.Text()
    p_pros_32 = fields.Integer(
        default=0
    )
    g_pros_32 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_33 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_33 = fields.Text()
    p_pros_33 = fields.Integer(
        default=0
    )
    g_pros_33 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_34 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_34 = fields.Text()
    p_pros_34 = fields.Integer()
    g_pros_34 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_34 = fields.Selection(
        selection=constants.SELECTION_TIPO_TRAZABILIDAD_COMPONENTES,
    )
    pros_35 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_35 = fields.Text()
    p_pros_35 = fields.Integer()
    g_pros_35 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_36 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_36 = fields.Text()
    p_pros_36 = fields.Integer()
    g_pros_36 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_37 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_37 = fields.Text()
    p_pros_37 = fields.Integer()
    g_pros_37 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_38 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_38 = fields.Text()
    p_pros_38 = fields.Integer()
    g_pros_38 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_38 = fields.Selection(
        selection=constants.SELECTION_TIPO_REACTIVO_MARCADOR,
    )
    pros_39 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_39 = fields.Text()
    p_pros_39 = fields.Integer()
    g_pros_39 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_39 = fields.Selection(
        selection=constants.SELECTION_TIPO_REACTIVO_MARCADOR,
    )
    pros_40 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_40 = fields.Text()
    p_pros_40 = fields.Integer()
    g_pros_40 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_40 = fields.Selection(
        selection=constants.SELECTION_TIPO_REACTIVO_MARCADOR,
    )
    pros_41 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_41 = fields.Text()
    p_pros_41 = fields.Integer()
    g_pros_41 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_41 = fields.Selection(
        selection=constants.SELECTION_TIPO_REACTIVO_MARCADOR,
    )
    pros_42 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_42 = fields.Text()
    p_pros_42 = fields.Integer()
    g_pros_42 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_42 = fields.Selection(
        selection=constants.SELECTION_TIPO_REACTIVO_MARCADOR,
    )
    pros_43 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_43 = fields.Text()
    p_pros_43 = fields.Integer()
    g_pros_43 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_43 = fields.Selection(
        selection=constants.SELECTION_TIPO_REACTIVO_MARCADOR,
    )
    pros_44 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_44 = fields.Text()
    p_pros_44 = fields.Integer()
    g_pros_44 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_44 = fields.Selection(
        selection=constants.SELECTION_TIPO_REACTIVO_MARCADOR,
    )
    pros_45 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_pros_45 = fields.Text()
    obs_pros_45 = fields.Text()
    p_pros_45 = fields.Integer(
        default=0
    )
    g_pros_45 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    obs_pros_47 = fields.Text()
    p_pros_47 = fields.Integer(
        default=0
    )
    g_pros_47 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    t_pros_47 = fields.Selection(
        selection=constants.SELECTION_TIPO_FREC_TAMIZAJE_SEROLOGICO,
    )
    esp_pros_48 = fields.Text()
    obs_pros_48 = fields.Text()
    pros_49 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_49 = fields.Text()
    p_pros_49 = fields.Integer()
    g_pros_49 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_50 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_50 = fields.Text()
    p_pros_50 = fields.Integer()
    g_pros_50 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_50 = fields.Selection(
        selection=constants.SELECTION_TIPO_MUESTRAS_REACTIVAS,
    )
    pros_51 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_51 = fields.Text()
    p_pros_51 = fields.Integer()
    g_pros_51 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_52 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_52 = fields.Text()
    p_pros_52 = fields.Integer()
    g_pros_52 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_53 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_53 = fields.Text()
    p_pros_53 = fields.Integer()
    g_pros_53 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    r_pros_53 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    r_obs_53 = fields.Text()
    p_r_pros_53 = fields.Integer()
    g_r_pros_53 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_54 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_54 = fields.Text()
    p_pros_54 = fields.Integer()
    g_pros_54 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_55 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_55 = fields.Text()
    p_pros_55 = fields.Integer()
    g_pros_55 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    obs_pros_56 = fields.Text()
    p_pros_56 = fields.Integer(
        default=0
    )
    g_pros_56 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    t_pros_56 = fields.Selection(
        selection=constants.SELECTION_TIPO_MANUAL_SEMI_AUTO,
    )
    pros_57 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_57 = fields.Text()
    p_pros_57 = fields.Integer()
    g_pros_57 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_58 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_58 = fields.Text()
    p_pros_58 = fields.Integer()
    g_pros_58 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_59 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_59 = fields.Text()
    p_pros_59 = fields.Integer()
    g_pros_59 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_60 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_60 = fields.Text()
    p_pros_60 = fields.Integer()
    g_pros_60 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_61 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_61 = fields.Text()
    p_pros_61 = fields.Integer()
    g_pros_61 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_62 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_62 = fields.Text()
    p_pros_62 = fields.Integer()
    g_pros_62 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_63 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_63 = fields.Text()
    p_pros_63 = fields.Integer()
    g_pros_63 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_64 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_64 = fields.Text()
    p_pros_64 = fields.Integer()
    g_pros_64 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_65 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_65 = fields.Text()
    p_pros_65 = fields.Integer()
    g_pros_65 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_66 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    esp_pros_66 = fields.Text()
    obs_pros_66 = fields.Text()
    p_pros_66 = fields.Integer()
    g_pros_66 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_68 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    p_pros_68 = fields.Integer(
        default=0
    )
    g_pros_68 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    t_pros_68 = fields.Selection(
        selection=constants.SELECTION_TIPO_PROC_ETIQ_ESPECIALES,
    )
    obs_pros_68 = fields.Text()
    pros_69 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_69 = fields.Text()
    p_pros_69 = fields.Integer()
    g_pros_69 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_70 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_70 = fields.Text()
    p_pros_70 = fields.Integer()
    g_pros_70 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_72 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_72 = fields.Text()
    p_pros_72 = fields.Integer()
    g_pros_72 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_73 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_73 = fields.Text()
    p_pros_73 = fields.Integer()
    g_pros_73 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_74 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_74 = fields.Text()
    p_pros_74 = fields.Integer()
    g_pros_74 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_75 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_75 = fields.Text()
    p_pros_75 = fields.Integer()
    g_pros_75 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_76 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_76 = fields.Text()
    p_pros_76 = fields.Integer()
    g_pros_76 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_77 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_77 = fields.Text()
    p_pros_77 = fields.Integer()
    g_pros_77 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_77 = fields.Selection(
        selection=constants.SELECTION_TIPO_MANUAL_SEMI_AUTO,
    )
    pros_78 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_78 = fields.Text()
    p_pros_78 = fields.Integer()
    g_pros_78 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_79 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_79 = fields.Text()
    p_pros_79 = fields.Integer()
    g_pros_79 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_80 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_80 = fields.Text()
    p_pros_80 = fields.Integer()
    g_pros_80 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_81 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_81 = fields.Text()
    p_pros_81 = fields.Integer(
        default=0
    )
    g_pros_81 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_82 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_82 = fields.Text()
    p_pros_82 = fields.Integer(
        default=0
    )
    g_pros_82 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_83 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_83 = fields.Text()
    p_pros_83 = fields.Integer(
        default=0
    )
    g_pros_83 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_84 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_84 = fields.Text()
    p_pros_84 = fields.Integer(
        default=0
    )
    g_pros_84 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_85 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_85 = fields.Text()
    p_pros_85 = fields.Integer()
    g_pros_85 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_87 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_87 = fields.Text()
    p_pros_87 = fields.Integer(
        default=0
    )
    g_pros_87 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_88 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_88 = fields.Text()
    p_pros_88 = fields.Integer(
        default=0
    )
    g_pros_88 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_89 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_89 = fields.Text()
    p_pros_89 = fields.Integer(
        default=0
    )
    g_pros_89 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_90 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_90 = fields.Text()
    p_pros_90 = fields.Integer(
        default=0
    )
    g_pros_90 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_91 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_91 = fields.Text()
    p_pros_91 = fields.Integer(
        default=0
    )
    g_pros_91 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_92 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_92 = fields.Text()
    p_pros_92 = fields.Integer(
        default=0
    )
    g_pros_92 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_93 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_93 = fields.Text()
    p_pros_93 = fields.Integer()
    g_pros_93 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    t_pros_93 = fields.Selection(
        selection=constants.SELECTION_TIPO_PROCED_COLECT_CELULAR,
    )
    pros_94 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_94 = fields.Text()
    p_pros_94 = fields.Integer()
    g_pros_94 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_95 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_95 = fields.Text()
    p_pros_95 = fields.Integer()
    g_pros_95 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_96 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_96 = fields.Text()
    p_pros_96 = fields.Integer(
        default=0
    )
    g_pros_96 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_97 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_97 = fields.Text()
    p_pros_97 = fields.Integer(
        default=0
    )
    g_pros_97 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )
    pros_98 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_98 = fields.Text()
    p_pros_98 = fields.Integer()
    g_pros_98 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )
    pros_99 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_99 = fields.Text()
    p_pros_99 = fields.Integer()
    g_pros_99 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
    )

    pros_100 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_100 = fields.Text()
    p_pros_100 = fields.Integer(
        default=0
    )
    g_pros_100 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )

    pros_101 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_101 = fields.Text()
    p_pros_101 = fields.Integer(
        default=0
    )
    g_pros_101 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )

    pros_102 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_102 = fields.Text()
    p_pros_102 = fields.Integer(
        default=0
    )
    g_pros_102 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )

    pros_103 = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
    )
    obs_pros_103 = fields.Text()
    p_pros_103 = fields.Integer(
        default=0
    )
    g_pros_103 = fields.Selection(
        selection=constants.SELECTION_GRAVEDAD,
        default=constants.NULO
    )

    @api.onchange('pros_2')
    def _onchange_pros_2(self):
        if self.pros_2 == constants.SI:
            self.p_pros_2 = 5
            self.g_pros_2 = constants.NULO
        elif self.pros_2 == constants.NO:
            self.p_pros_2 = 0
            self.g_pros_2 = constants.MODERADO
        else:
            self.p_pros_2 = 0
            self.g_pros_2 = False

    @api.onchange('pros_3')
    def _onchange_pros_3(self):
        if self.pros_3 == constants.SI:
            self.p_pros_3 = 5
            self.g_pros_3 = constants.NULO
        elif self.pros_3 == constants.NO:
            self.p_pros_3 = 0
            self.g_pros_3 = constants.MODERADO
        else:
            self.p_pros_3 = 0
            self.g_pros_3 = False

    @api.onchange('pros_5')
    def _onchange_pros_5(self):
        if self.pros_5 == constants.SI:
            self.p_pros_5 = 5
            self.g_pros_5 = constants.NULO
        elif self.pros_5 == constants.NO:
            self.p_pros_5 = 0
            self.g_pros_5 = constants.MODERADO
        else:
            self.p_pros_5 = 0
            self.g_pros_5 = False

    @api.onchange('pros_6')
    def _onchange_pros_6(self):
        if self.pros_6 == constants.SI:
            self.p_pros_6 = 5
            self.g_pros_6 = constants.NULO
        elif self.pros_6 == constants.NO:
            self.p_pros_6 = 0
            self.g_pros_6 = constants.MODERADO
        else:
            self.p_pros_6 = 0
            self.g_pros_6 = False

    @api.onchange('t_pros_7')
    def _onchange_t_pros_7(self):
        if self.t_pros_7 == constants.ENTREVISTA:
            self.p_pros_7 = 4
            self.g_pros_7 = constants.NULO
        elif self.t_pros_7 == constants.AUTOAPLICADO:
            self.p_pros_7 = 0
            self.g_pros_7 = constants.MODERADO
        else:
            self.p_pros_7 = 0
            self.g_pros_7 = False

    @api.onchange('t_pros_8')
    def _onchange_t_pros_8(self):
        if self.t_pros_8 == constants.MEDICO:
            self.p_pros_8 = 5
            self.g_pros_8 = constants.NULO
        elif self.t_pros_8 == constants.TECNOLOGO:
            self.p_pros_8 = 4
            self.g_pros_8 = constants.NULO
        elif self.t_pros_8 == constants.OTRO:
            self.p_pros_8 = 3
            self.g_pros_8 = constants.LEVE
        else:
            self.p_pros_8 = 0
            self.g_pros_8 = False

    @api.onchange('pros_9')
    def _onchange_pros_9(self):
        if self.pros_9 == constants.SI:
            self.p_pros_9 = 5
            self.g_pros_9 = constants.NULO
        elif self.pros_9 == constants.NO:
            self.p_pros_9 = 0
            self.g_pros_9 = constants.GRAVE
        else:
            self.p_pros_9 = 0
            self.g_pros_9 = False

    @api.onchange('pros_10')
    def _onchange_pros_10(self):
        if self.pros_10 == constants.SI:
            self.p_pros_10 = 4
            self.g_pros_10 = constants.NULO
        elif self.pros_10 == constants.NO:
            self.p_pros_10 = 0
            self.g_pros_10 = constants.MODERADO
        else:
            self.p_pros_10 = 0
            self.g_pros_10 = False

    @api.onchange('pros_11')
    def _onchange_pros_11(self):
        if self.pros_11 == constants.SI:
            self.p_pros_11 = 4
            self.g_pros_11 = constants.NULO
        elif self.pros_11 == constants.NO:
            self.p_pros_11 = 0
            self.g_pros_11 = constants.MODERADO
        else:
            self.p_pros_11 = 0
            self.g_pros_11 = False

    @api.onchange('t_pros_12')
    def _onchange_t_pros_12(self):
        if self.t_pros_12 == constants.COMPLETO:
            self.p_pros_12 = 5
            self.g_pros_12 = constants.NULO
        elif self.t_pros_12 == constants.INCOMPLETO:
            self.p_pros_12 = 5
            self.g_pros_12 = constants.MODERADO
        else:
            self.p_pros_12 = 0
            self.g_pros_12 = False

    @api.onchange('pros_13')
    def _onchange_pros_13(self):
        if self.pros_13 == constants.SI:
            self.p_pros_13 = 4
            self.g_pros_13 = constants.NULO
        elif self.pros_13 == constants.NO:
            self.p_pros_13 = 0
            self.g_pros_13 = constants.MODERADO
        else:
            self.p_pros_13 = 0
            self.g_pros_13 = False

    @api.onchange('pros_14')
    def _onchange_pros_14(self):
        if self.pros_14 == constants.SI:
            self.p_pros_14 = 4
            self.g_pros_14 = constants.NULO
        elif self.pros_14 == constants.NO:
            self.p_pros_14 = 0
            self.g_pros_14 = constants.MODERADO
        else:
            self.p_pros_14 = 0
            self.g_pros_14 = False

    @api.onchange('pros_15')
    def _onchange_pros_15(self):
        if self.pros_15 == constants.SI:
            self.p_pros_15 = 4
            self.g_pros_15 = constants.NULO
        elif self.pros_15 == constants.NO:
            self.p_pros_15 = 0
            self.g_pros_15 = constants.MODERADO
        else:
            self.p_pros_15 = 0
            self.g_pros_15 = False

    @api.onchange('pros_16')
    def _onchange_pros_16(self):
        if self.pros_16 == constants.SI:
            self.p_pros_16 = 5
            self.g_pros_16 = constants.NULO
        elif self.pros_16 == constants.NO:
            self.p_pros_16 = 0
            self.g_pros_16 = constants.GRAVE
        else:
            self.p_pros_16 = 0
            self.g_pros_16 = False

    @api.onchange('pros_17')
    def _onchange_pros_17(self):
        if self.pros_17 == constants.SI:
            self.p_pros_17 = 5
            self.g_pros_17 = constants.NULO
        elif self.pros_17 == constants.NO:
            self.p_pros_17 = 0
            self.g_pros_17 = constants.GRAVE
        else:
            self.p_pros_17 = 0
            self.g_pros_17 = False

    @api.onchange('pros_18')
    def _onchange_pros_18(self):
        if self.pros_18 == constants.SI:
            self.p_pros_18 = 4
            self.g_pros_18 = constants.NULO
        elif self.pros_18 == constants.NO:
            self.p_pros_18 = 0
            self.g_pros_18 = constants.MODERADO
        else:
            self.p_pros_18 = 0
            self.g_pros_18 = False

    @api.onchange('pros_21')
    def _onchange_pros_21(self):
        if self.pros_21 == constants.SI:
            self.p_pros_21 = 3
            self.g_pros_21 = constants.NULO
        elif self.pros_21 == constants.NO:
            self.p_pros_21 = 0
            self.g_pros_21 = constants.MODERADO
        else:
            self.p_pros_21 = 0
            self.g_pros_21 = False

    @api.onchange('pros_22')
    def _onchange_pros_22(self):
        if self.pros_22 == constants.SI:
            self.p_pros_22 = 5
            self.g_pros_22 = constants.NULO
        elif self.pros_22 == constants.NO:
            self.p_pros_22 = 0
            self.g_pros_22 = constants.GRAVE
        else:
            self.p_pros_22 = 0
            self.g_pros_22 = False

    @api.onchange('pros_34')
    def _onchange_pros_34(self):
        if self.pros_34 == constants.SI:
            self.p_pros_34 = 4
            self.g_pros_34 = constants.NULO
        elif self.pros_34 == constants.NO:
            self.p_pros_34 = 0
            self.g_pros_34 = constants.MODERADO
        else:
            self.p_pros_34 = 0
            self.g_pros_34 = False

    @api.onchange('pros_35')
    def _onchange_pros_35(self):
        if self.pros_35 == constants.SI:
            self.p_pros_35 = 4
            self.g_pros_35 = constants.NULO
        elif self.pros_35 == constants.NO:
            self.p_pros_35 = 0
            self.g_pros_35 = constants.MODERADO
        else:
            self.p_pros_35 = 0
            self.g_pros_35 = False

    @api.onchange('pros_36')
    def _onchange_pros_36(self):
        if self.pros_36 == constants.SI:
            self.p_pros_36 = 5
            self.g_pros_36 = constants.NULO
        elif self.pros_36 == constants.NO:
            self.p_pros_36 = 0
            self.g_pros_36 = constants.GRAVE
        else:
            self.p_pros_36 = 0
            self.g_pros_36 = False

    @api.onchange('pros_37')
    def _onchange_pros_37(self):
        if self.pros_37 == constants.SI:
            self.p_pros_37 = 5
            self.g_pros_37 = constants.NULO
        elif self.pros_37 == constants.NO:
            self.p_pros_37 = 0
            self.g_pros_37 = constants.GRAVE
        else:
            self.p_pros_37 = 0
            self.g_pros_37 = False

    @api.onchange('pros_38')
    def _onchange_pros_38(self):
        if self.pros_38 == constants.SI:
            self.p_pros_38 = 5
            self.g_pros_38 = constants.NULO
        elif self.pros_38 == constants.NO:
            self.p_pros_38 = 0
            self.g_pros_38 = constants.GRAVE
        else:
            self.p_pros_38 = 0
            self.g_pros_38 = False

    @api.onchange('pros_39')
    def _onchange_pros_39(self):
        if self.pros_39 == constants.SI:
            self.p_pros_39 = 5
            self.g_pros_39 = constants.NULO
        elif self.pros_39 == constants.NO:
            self.p_pros_39 = 0
            self.g_pros_39 = constants.GRAVE
        else:
            self.p_pros_39 = 0
            self.g_pros_39 = False

    @api.onchange('pros_40')
    def _onchange_pros_40(self):
        if self.pros_40 == constants.SI:
            self.p_pros_40 = 5
            self.g_pros_40 = constants.NULO
        elif self.pros_40 == constants.NO:
            self.p_pros_40 = 0
            self.g_pros_40 = constants.GRAVE
        else:
            self.p_pros_40 = 0
            self.g_pros_40 = False

    @api.onchange('pros_41')
    def _onchange_pros_41(self):
        if self.pros_41 == constants.SI:
            self.p_pros_41 = 5
            self.g_pros_41 = constants.NULO
        elif self.pros_41 == constants.NO:
            self.p_pros_41 = 0
            self.g_pros_41 = constants.GRAVE
        else:
            self.p_pros_41 = 0
            self.g_pros_41 = False

    @api.onchange('pros_42')
    def _onchange_pros_42(self):
        if self.pros_42 == constants.SI:
            self.p_pros_42 = 5
            self.g_pros_42 = constants.NULO
        elif self.pros_42 == constants.NO:
            self.p_pros_42 = 0
            self.g_pros_42 = constants.GRAVE
        else:
            self.p_pros_42 = 0
            self.g_pros_42 = False

    @api.onchange('pros_43')
    def _onchange_pros_43(self):
        if self.pros_43 == constants.SI:
            self.p_pros_43 = 5
            self.g_pros_43 = constants.NULO
        elif self.pros_43 == constants.NO:
            self.p_pros_43 = 0
            self.g_pros_43 = constants.GRAVE
        else:
            self.p_pros_43 = 0
            self.g_pros_43 = False

    @api.onchange('pros_44')
    def _onchange_pros_44(self):
        if self.pros_44 == constants.SI:
            self.p_pros_44 = 5
            self.g_pros_44 = constants.NULO
        elif self.pros_44 == constants.NO:
            self.p_pros_44 = 0
            self.g_pros_44 = constants.GRAVE
        else:
            self.p_pros_44 = 0
            self.g_pros_44 = False

    @api.onchange('pros_49')
    def _onchange_pros_49(self):
        if self.pros_49 == constants.SI:
            self.p_pros_49 = 5
            self.g_pros_49 = constants.NULO
        elif self.pros_49 == constants.NO:
            self.p_pros_49 = 0
            self.g_pros_49 = constants.GRAVE
        else:
            self.p_pros_49 = 0
            self.g_pros_49 = False

    @api.onchange('pros_50')
    def _onchange_pros_50(self):
        if self.pros_50 == constants.SI:
            self.p_pros_50 = 5
            self.g_pros_50 = constants.NULO
        elif self.pros_50 == constants.NO:
            self.p_pros_50 = 0
            self.g_pros_50 = constants.GRAVE
        else:
            self.p_pros_50 = 0
            self.g_pros_50 = False

    @api.onchange('pros_51')
    def _onchange_pros_51(self):
        if self.pros_51 == constants.SI:
            self.p_pros_51 = 5
            self.g_pros_51 = constants.NULO
        elif self.pros_51 == constants.NO:
            self.p_pros_51 = 0
            self.g_pros_51 = constants.GRAVE
        else:
            self.p_pros_51 = 0
            self.g_pros_51 = False

    @api.onchange('pros_52')
    def _onchange_pros_52(self):
        if self.pros_52 == constants.SI:
            self.p_pros_52 = 5
            self.g_pros_52 = constants.NULO
        elif self.pros_52 == constants.NO:
            self.p_pros_52 = 0
            self.g_pros_52 = constants.GRAVE
        else:
            self.p_pros_52 = 0
            self.g_pros_52 = False

    @api.onchange('pros_53')
    def _onchange_pros_53(self):
        if self.pros_53 == constants.SI:
            self.p_pros_53 = 5
            self.g_pros_53 = constants.NULO
        elif self.pros_53 == constants.NO:
            self.p_pros_53 = 0
            self.g_pros_53 = constants.GRAVE
        else:
            self.p_pros_53 = 0
            self.g_pros_53 = False

    @api.onchange('r_pros_53')
    def _onchange_r_pros_53(self):
        if self.r_pros_53 == constants.SI:
            self.p_r_pros_53 = 5
            self.g_r_pros_53 = constants.NULO
        elif self.r_pros_53 == constants.NO:
            self.p_r_pros_53 = 0
            self.g_r_pros_53 = constants.GRAVE
        else:
            self.p_r_pros_53 = 0
            self.g_r_pros_53 = False

    @api.onchange('pros_54')
    def _onchange_pros_54(self):
        if self.pros_54 == constants.SI:
            self.p_pros_54 = 5
            self.g_pros_54 = constants.NULO
        elif self.pros_54 == constants.NO:
            self.p_pros_54 = 0
            self.g_pros_54 = constants.GRAVE
        else:
            self.p_pros_54 = 0
            self.g_pros_54 = False

    @api.onchange('pros_55')
    def _onchange_pros_55(self):
        if self.pros_55 == constants.SI:
            self.p_pros_55 = 5
            self.g_pros_55 = constants.NULO
        elif self.pros_55 == constants.NO:
            self.p_pros_55 = 0
            self.g_pros_55 = constants.GRAVE
        else:
            self.p_pros_55 = 0
            self.g_pros_55 = False

    @api.onchange('pros_57')
    def _onchange_pros_57(self):
        if self.pros_57 == constants.SI:
            self.p_pros_57 = 4
            self.g_pros_57 = constants.NULO
        elif self.pros_57 == constants.NO:
            self.p_pros_57 = 0
            self.g_pros_57 = constants.MODERADO
        else:
            self.p_pros_57 = 0
            self.g_pros_57 = False

    @api.onchange('pros_58')
    def _onchange_pros_58(self):
        if self.pros_58 == constants.SI:
            self.p_pros_58 = 4
            self.g_pros_58 = constants.NULO
        elif self.pros_58 == constants.NO:
            self.p_pros_58 = 0
            self.g_pros_58 = constants.MODERADO
        else:
            self.p_pros_58 = 0
            self.g_pros_58 = False

    @api.onchange('pros_59')
    def _onchange_pros_59(self):
        if self.pros_59 == constants.SI:
            self.p_pros_59 = 4
            self.g_pros_59 = constants.NULO
        elif self.pros_59 == constants.NO:
            self.p_pros_59 = 0
            self.g_pros_59 = constants.MODERADO
        else:
            self.p_pros_59 = 0
            self.g_pros_59 = False

    @api.onchange('pros_60')
    def _onchange_pros_60(self):
        if self.pros_60 == constants.SI:
            self.p_pros_60 = 4
            self.g_pros_60 = constants.NULO
        elif self.pros_60 == constants.NO:
            self.p_pros_60 = 0
            self.g_pros_60 = constants.MODERADO
        else:
            self.p_pros_60 = 0
            self.g_pros_60 = False

    @api.onchange('pros_61')
    def _onchange_pros_61(self):
        if self.pros_61 == constants.SI:
            self.p_pros_61 = 4
            self.g_pros_61 = constants.NULO
        elif self.pros_61 == constants.NO:
            self.p_pros_61 = 0
            self.g_pros_61 = constants.MODERADO
        else:
            self.p_pros_61 = 0
            self.g_pros_61 = False

    @api.onchange('pros_62')
    def _onchange_pros_62(self):
        if self.pros_62 == constants.SI:
            self.p_pros_62 = 4
            self.g_pros_62 = constants.NULO
        elif self.pros_62 == constants.NO:
            self.p_pros_62 = 0
            self.g_pros_62 = constants.MODERADO
        else:
            self.p_pros_62 = 0
            self.g_pros_62 = False

    @api.onchange('pros_63')
    def _onchange_pros_63(self):
        if self.pros_63 == constants.SI:
            self.p_pros_63 = 4
            self.g_pros_63 = constants.NULO
        elif self.pros_63 == constants.NO:
            self.p_pros_63 = 0
            self.g_pros_63 = constants.MODERADO
        else:
            self.p_pros_63 = 0
            self.g_pros_63 = False

    @api.onchange('pros_64')
    def _onchange_pros_64(self):
        if self.pros_64 == constants.SI:
            self.p_pros_64 = 4
            self.g_pros_64 = constants.NULO
        elif self.pros_64 == constants.NO:
            self.p_pros_64 = 0
            self.g_pros_64 = constants.MODERADO
        else:
            self.p_pros_64 = 0
            self.g_pros_64 = False

    @api.onchange('pros_65')
    def _onchange_pros_65(self):
        if self.pros_65 == constants.SI:
            self.p_pros_65 = 4
            self.g_pros_65 = constants.NULO
        elif self.pros_65 == constants.NO:
            self.p_pros_65 = 0
            self.g_pros_65 = constants.MODERADO
        else:
            self.p_pros_65 = 0
            self.g_pros_65 = False

    @api.onchange('pros_66')
    def _onchange_pros_66(self):
        if self.pros_66 == constants.SI:
            self.p_pros_66 = 0
            self.g_pros_66 = constants.NULO
        elif self.pros_66 == constants.NO:
            self.p_pros_66 = 0
            self.g_pros_66 = constants.NULO
        else:
            self.p_pros_66 = 0
            self.g_pros_66 = False

    @api.onchange('pros_69')
    def _onchange_pros_69(self):
        if self.pros_69 == constants.SI:
            self.p_pros_69 = 5
            self.g_pros_69 = constants.NULO
        elif self.pros_69 == constants.NO:
            self.p_pros_69 = 0
            self.g_pros_69 = constants.GRAVE
        else:
            self.p_pros_69 = 0
            self.g_pros_69 = False

    @api.onchange('pros_70')
    def _onchange_pros_70(self):
        if self.pros_70 == constants.SI:
            self.p_pros_70 = 5
            self.g_pros_70 = constants.NULO
        elif self.pros_70 == constants.NO:
            self.p_pros_70 = 0
            self.g_pros_70 = constants.GRAVE
        else:
            self.p_pros_70 = 0
            self.g_pros_70 = False

    @api.onchange('pros_73')
    def _onchange_pros_73(self):
        if self.pros_73 == constants.SI:
            self.p_pros_73 = 5
            self.g_pros_73 = constants.NULO
        elif self.pros_73 == constants.NO:
            self.p_pros_73 = 0
            self.g_pros_73 = constants.GRAVE
        else:
            self.p_pros_73 = 0
            self.g_pros_73 = False

    @api.onchange('pros_74')
    def _onchange_pros_74(self):
        if self.pros_74 == constants.SI:
            self.p_pros_74 = 5
            self.g_pros_74 = constants.NULO
        elif self.pros_74 == constants.NO:
            self.p_pros_74 = 0
            self.g_pros_74 = constants.GRAVE
        else:
            self.p_pros_74 = 0
            self.g_pros_74 = False

    @api.onchange('pros_75')
    def _onchange_pros_75(self):
        if self.pros_75 == constants.SI:
            self.p_pros_75 = 5
            self.g_pros_75 = constants.NULO
        elif self.pros_75 == constants.NO:
            self.p_pros_75 = 0
            self.g_pros_75 = constants.GRAVE
        else:
            self.p_pros_75 = 0
            self.g_pros_75 = False

    @api.onchange('pros_76')
    def _onchange_pros_76(self):
        if self.pros_76 == constants.SI:
            self.p_pros_76 = 4
            self.g_pros_76 = constants.NULO
        elif self.pros_76 == constants.NO:
            self.p_pros_76 = 0
            self.g_pros_76 = constants.MODERADO
        else:
            self.p_pros_76 = 0
            self.g_pros_76 = False

    @api.onchange('pros_77')
    def _onchange_pros_77(self):
        if self.pros_77 == constants.SI:
            self.p_pros_77 = 5
            self.g_pros_77 = constants.NULO
        elif self.pros_77 == constants.NO:
            self.p_pros_77 = 0
            self.g_pros_77 = constants.GRAVE
        else:
            self.p_pros_77 = 0
            self.g_pros_77 = False

    @api.onchange('pros_78')
    def _onchange_pros_78(self):
        if self.pros_78 == constants.SI:
            self.p_pros_78 = 5
            self.g_pros_78 = constants.NULO
        elif self.pros_78 == constants.NO:
            self.p_pros_78 = 0
            self.g_pros_78 = constants.MODERADO
        else:
            self.p_pros_78 = 0
            self.g_pros_78 = False

    @api.onchange('pros_79')
    def _onchange_pros_79(self):
        if self.pros_79 == constants.SI:
            self.p_pros_79 = 4
            self.g_pros_79 = constants.NULO
        elif self.pros_79 == constants.NO:
            self.p_pros_79 = 0
            self.g_pros_79 = constants.MODERADO
        else:
            self.p_pros_79 = 0
            self.g_pros_79 = False

    @api.onchange('pros_80')
    def _onchange_pros_80(self):
        if self.pros_80 == constants.SI:
            self.p_pros_80 = 5
            self.g_pros_80 = constants.NULO
        elif self.pros_80 == constants.NO:
            self.p_pros_80 = 0
            self.g_pros_80 = constants.GRAVE
        else:
            self.p_pros_80 = 0
            self.g_pros_80 = False

    @api.onchange('pros_85')
    def _onchange_pros_85(self):
        if self.pros_85 == constants.SI:
            self.p_pros_85 = 4
            self.g_pros_85 = constants.NULO
        elif self.pros_85 == constants.NO:
            self.p_pros_85 = 0
            self.g_pros_85 = constants.MODERADO
        else:
            self.p_pros_85 = 0
            self.g_pros_85 = False

    @api.onchange('pros_93')
    def _onchange_pros_93(self):
        if self.pros_93 == constants.SI:
            self.p_pros_93 = 4
            self.g_pros_93 = constants.NULO
        elif self.pros_93 == constants.NO:
            self.p_pros_93 = 0
            self.g_pros_93 = constants.NULO
        else:
            self.p_pros_93 = 0
            self.g_pros_93 = False

    @api.onchange('pros_94')
    def _onchange_pros_94(self):
        if self.pros_94 == constants.SI:
            self.p_pros_94 = 5
            self.g_pros_94 = constants.NULO
        elif self.pros_94 == constants.NO:
            self.p_pros_94 = 0
            self.g_pros_94 = constants.MODERADO
        else:
            self.p_pros_94 = 0
            self.g_pros_94 = False

    @api.onchange('pros_95')
    def _onchange_pros_95(self):
        if self.pros_95 == constants.SI:
            self.p_pros_95 = 5
            self.g_pros_95 = constants.NULO
        elif self.pros_95 == constants.NO:
            self.p_pros_95 = 0
            self.g_pros_95 = constants.MODERADO
        else:
            self.p_pros_95 = 0
            self.g_pros_95 = False

    @api.onchange('pros_98')
    def _onchange_pros_98(self):
        if self.pros_98 == constants.SI:
            self.p_pros_98 = 5
            self.g_pros_98 = constants.NULO
        elif self.pros_98 == constants.NO:
            self.p_pros_98 = 0
            self.g_pros_98 = constants.GRAVE
        else:
            self.p_pros_98 = 0
            self.g_pros_98 = False
