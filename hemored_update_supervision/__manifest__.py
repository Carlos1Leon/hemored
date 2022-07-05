# -*- coding: utf-8 -*-
{
    'name': "UpdateExcel Supervision",

    'summary': 'Carga de un Excel para el llenado automático de información - Módulo de Supervisión',

    'description': 'Módulo para la carga automática de información de la Supervisión realizada a través Sistema HEMORED',

    'author': "PRONAHEBAS - DIBAN",
    'website': "http://www.minsa.gob.pe",

    'category': 'Health',
    'version': '0.1',

    'depends': [
        'hemored'
    ],

    'data': [
        'views/ficha_supervision_view.xml',
        'views/update_excel_view.xml'
    ],
    'application': True,
}
