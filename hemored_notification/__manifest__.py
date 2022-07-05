# -*- coding: utf-8 -*-
{
    'name': "Notifications for Recording Statistics",

    'summary': 'Aplicativo Web de Dirección General de Donaciones, Trasplantes y CHBS. ',

    'description': 'Aplicativo Web de Dirección General de Donaciones, Trasplantes y CHBS. Para enviar notificaciones a los CHBS del estado del registro de las estadísticas',

    'author': "PRONAHEBAS - DIBAN",
    'website': "http://www.minsa.gob.pe",

    'category': 'Health',
    'version': '0.1',

    'depends': [
        'hemored',
        'fetchmail',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/hemored_notification_chbs_views.xml',
        'views/res_user_views.xml',
        'views/hemored_notification_record_views.xml',
        'views/reminder_cron.xml',
        'views/reminder_action_data.xml'
    ],
    'application': True,
}
