# -*- coding: utf-8 -*-
{
    'name': "Módulo de Supervisión de Centros de Hemoterapia y Bancos de Sangre CHBS",

    'summary': 'Aplicativo Web de Dirección General de Donaciones, Trasplantes y CHBS. ',

    'description': 'Aplicativo Web de Dirección General de Donaciones, Trasplantes y CHBS. Para registrar las supervisiones a los Centros de Hemoterapia y Bancos de Sangre CHBS',

    'author': "PRONAHEBAS - DIBAN",
    'website': "http://www.minsa.gob.pe",

    'category': 'Health',
    'version': '0.1',

    'depends': [
        'hemored',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/hemored_supervision_redord_date_supervision.xml',
        'views/hemored_supervision_wizards.xml',
        'views/hemored_supervision_views.xml',
        'views/hemored_respon_gerencia_views.xml',
        'views/hemored_rrhh_views.xml',
        'views/hemored_proceso_views.xml',
        'views/hemored_sistema_calidad_views.xml',
        'views/hemored_almacenamiento_views.xml',
        'views/hemored_sistema_informatico_views.xml',
        'views/hemored_clasf_biologica_views.xml',
        'views/hemored_equipamiento_views.xml',
        'views/hemored_rel_equipamiento_views.xml',
        'views/hemored_infra_instal_views.xml',
        'views/hemored_bio_salud_views.xml',
        'views/hemored_supervision_monitoreo_views.xml',
        'views/hemored_m_respon_gerencia_views.xml',
        'views/hemored_m_rrhh_views.xml',
        'views/hemored_m_proceso_views.xml',
        'views/hemored_m_sistema_calidad_views.xml',
        'views/hemored_m_almacenamiento_views.xml',
        'views/hemored_m_sistema_informatico_views.xml',
        'views/hemored_m_clasf_biologica_views.xml',
        'views/hemored_m_equipamiento_views.xml',
        'views/hemored_m_rel_equipamiento_views.xml',
        'views/hemored_m_infra_instal_views.xml',
        'views/hemored_m_bio_salud_views.xml',
    ],
    'application': True,
}
