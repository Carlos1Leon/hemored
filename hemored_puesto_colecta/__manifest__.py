# -*- coding: utf-8 -*-
{
    'name': "Puesto de Colecta",

    'summary': 'Módulo encargado de gestionar los Puestos de Colecta',

    'description': 'Módulo encargado de registrar y gestionar los datos de las donaciónes recaudados por los bancos de hemored en los Puestos de Colecta',

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
        'views/hemored_puesto_colecta_view.xml',
        'views/hemored_puesto_colecta_ficha_view.xml',
    ],
    'application': True,
}
