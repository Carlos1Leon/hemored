# -*- coding: utf-8 -*-
{
    'name': "Infraestructura",

    'summary': 'Módulo encargado de la verificación de la infraestructura de los bancos de hemored',

    'description': 'Módulo para la verificación de la Infraestructura de los bancos',

    'author': "PRONAHEBAS - DIBAN",
    'website': "http://www.minsa.gob.pe",

    'category': 'Health',
    'version': '0.1',

    'depends': [
        'hemored'
    ],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/hemored_infraestructura_view.xml'
    ],
    'application': True,
}
