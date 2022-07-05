# -*- coding: utf-8 -*-
{
    'name': "Sellos de calidad",

    'summary': 'Módulo encargado de gestionar los Sellos de Calidad',

    'description': 'Módulo encargado de registrar y gestionar los datos de los sellos de calidad',

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
        'views/hemored_sellos_calidad_view.xml',
        'views/hemored_sellos_calidad_registro_view.xml',
        'views_reports/report_views.xml',
        'wizard_views/hemored_wizard_eliminacion_view.xml',
        'views/menu_sellos_calidad_views.xml',
        'views_reports/acta_template_view.xml',
    ],
    'application': True,
}
