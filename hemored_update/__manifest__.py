# -*- coding: utf-8 -*-
{
    'name': "UpdateExcel",

    'summary': 'Carga de un Excel para el Llenado Automático de Información',

    'description': 'Modulo para la carga Automatica de Información al Sistema HEMORED',

    'author': "PRONAHEBAS - DIBAN",
    'website': "http://www.minsa.gob.pe",

    'category': 'Health',
    'version': '0.1',

    'depends': [
        'hemored'
    ],

    'data': [
        'views/ficha_estadistica_view.xml',
        'views/update_excel_view.xml'
    ],
    'application': True,
}
