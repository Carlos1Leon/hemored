# -*- coding: utf-8 -*-
{
    'name': "Stock Hemocomponentes",

    'summary': 'Aplicativo Web de Dirección General de Donaciones, Trasplantes y CHBS. ',

    'description': 'Aplicativo Web de Dirección General de Donaciones, Trasplantes y CHBS. Para obtener el stock de hemocomponentes de los CHBS',

    'author': "PRONAHEBAS",
    'website': "http://www.minsa.gob.pe",

    'category': 'Health',
    'version': '0.1',

    'depends': [
        'base',
        'hemored'
    ],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/stock_hemocomponente_views.xml',
        'views/configuracion_views.xml',
        'views/generar_ficha_stock.xml',
        'views_report/reporte_views.xml',
    ],
    'application': True,
}
