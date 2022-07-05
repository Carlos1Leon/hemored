# -*- coding: utf-8 -*-
{
    'name': "Convenio",

    'summary': 'Módulo encargado de los convenios entre bancos de hemored',

    'description': 'Módulo para el registro de convenios entre bancos',

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
        'views/hemored_convenio_view.xml'
    ],
    'application': True,
}
