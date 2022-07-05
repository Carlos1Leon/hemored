# -*- coding: utf-8 -*-
{
    'name': "Tutores y Promotores",

    'summary': 'Aplicativo Web de Dirección General de Donaciones, Trasplantes y CHBS. ',

    'description': 'Aplicativo Web de Dirección General de Donaciones, Trasplantes y CHBS. Para registrar a los tutores y promotores de la DIBAN',

    'author': "PRONAHEBAS",
    'website': "http://www.minsa.gob.pe",

    'category': 'Health',
    'version': '0.1',

    'depends': [
        'base',
        'hemored',
        'consultadatos'
    ],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_promotore_tutores.views.xml',
        'views/hemored_tutor_promotor_views.xml',
        'views/hemored_actividad_views.xml',
        'views/tutor_res_users_views.xml',
    ],
    'application': True,
}
