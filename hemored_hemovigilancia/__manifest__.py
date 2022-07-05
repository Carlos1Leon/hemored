# -*- coding: utf-8 -*-
{
    'name': "Hemovigilancia",

    'summary': 'Módulo encargado de generar reportes de Hemovigilancia de las estadísticas de  hemored',

    'description': 'Módulo de reportes de Hemovigilancia Hemored',

    'author': "PRONAHEBAS - DIBAN",
    'website': "http://www.minsa.gob.pe",

    'category': 'Health',
    'version': '0.1',

    'depends': [
        'hemored'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/hemored_hemovigilancia_view.xml'
    ],
    'application': True,
}
