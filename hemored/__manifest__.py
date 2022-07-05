# -*- coding: utf-8 -*-
{
    'name': "HEMORED",

    'summary': 'Aplicativo Web de Dirección General de Donaciones, Trasplantes y CHBS. ',

    'description': 'Aplicativo Web de Dirección General de Donaciones, Trasplantes y CHBS. Para verificar en tiempo real la producción, uso, demanda y transferencia de hemocomponentes, reacciones adversas graves relacionadas con las transfusiones, eliminación de sangre y hemocomponentes en CHBS',

    'author': "PRONAHEBAS",
    'website': "http://www.minsa.gob.pe",

    'category': 'Health',
    'version': '0.1',

    'depends': [
        'base',
        'mail',
        'renipress',
        'basecatalogo',
        'settings_app',
        'password_security',
        'minsa_periodo',
    ],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/res_users_view.xml',
        'data/hemored_catalogo.xml',
        'views/hemored_generar_ficha.xml',
        'views/hemored_banco_sangre_views.xml',
        'views/hemored_ficha_estadistica_views.xml',
        'views_report/hemored_report_ficha_view.xml',
        'views_report/hemored_report_view.xml',
        'views_report/hemored_report_donante_pivot_view.xml',
        'views_report/hemored_report_postulante_pivot_view.xml',
        'views_report/hemored_report_edad_pivot.xml',
        'views_report/hemored_sange_total_pivot.xml',
        'views_report/hemored_report_aferesis_pivot.xml',
        'views_report/hemored_report_unidad_sangre_pivot.xml',
        'views_report/hemored_report_acion_adversa_pivot.xml',
        'views_report/hemored_report_pivot_view.xml',
        'views_report/hemored_report_eliminacion_view.xml',
        'views_report/hemored_report_hemocomponente_view.xml',
        'views_report/hemored_report_estado_ficha.xml',
        'views_report/hemored_report_programa_evaluacion.xml',
        'data/reminder_cron.xml',
    ],
    'application': True,
}
