# coding=utf-8

from odoo import SUPERUSER_ID
from odoo import api, fields, models
from odoo.addons.hemored.models import constants


class HemoredBancoSangre(models.Model):
    _inherit = 'hemored.banco_sangre'

    fichas_ids = fields.One2many(
        comodel_name='hemored.ficha_estadistica',
        inverse_name='banco_id',
        string='Fichas estadísticas'
    )
    body_periodo_borrador = fields.Char(
        string='Períodos de fichas que están en estado borrador',
    )
    body_anual_borrador = fields.Char(
        string='Fichas anuales que están en estado borrador',
    )
    porc_fichas_borrador = fields.Float(
        string='% de fichas en borrador',
    )
    porc_fichas_enviadas = fields.Float(
        string='% de fichas en enviadas',
    )
    porc_fichas_validadas = fields.Float(
        string='% de fichas en validadas',
    )

    def porcentaje_status(self):
        bancos_ids = self.env['hemored.banco_sangre'].search([])
        for bancos in bancos_ids:
            lista_borrador_filter = bancos.fichas_ids.filtered(lambda l: l.state == 'borrador')
            lista_enviadas_filter = bancos.fichas_ids.filtered(lambda l: l.state == 'enviado')
            lista_validad_filter = bancos.fichas_ids.filtered(lambda l: l.state == 'validado')
            if len(lista_borrador_filter) != 0 or len(lista_enviadas_filter) != 0 or len(lista_enviadas_filter) != 0 or len(bancos.fichas_ids) != 0:
                bancos.update({
                    'porc_fichas_borrador': (len(lista_borrador_filter) / len(bancos.fichas_ids)) * 100,
                    'porc_fichas_enviadas': (len(lista_enviadas_filter) / len(bancos.fichas_ids)) * 100,
                    'porc_fichas_validadas': (len(lista_validad_filter) / len(bancos.fichas_ids)) * 100,
                })

    @api.model
    def _cron_update_porcentaje_fichas_chbs(self):
        self.porcentaje_status()

    def data_chbs(self):
        periodo = []
        anho = []
        bancos_ids = self.env['hemored.banco_sangre'].search([])
        for banco in bancos_ids:
            if banco.fichas_ids:
                for fichas in banco.fichas_ids:
                    if fichas.state == constants.BORRADOR:
                        if fichas.periodo_id and fichas.anho_id:
                            periodo.append(fichas.periodo_id.name)
                        if fichas.anho_id and not fichas.periodo_id:
                            anho.append(fichas.anho_id.name)
                    else:
                        banco.body_periodo_borrador = False
                        banco.body_anual_borrador = False
                if periodo:
                    banco.body_periodo_borrador = periodo
                elif anho:
                    banco.body_anual_borrador = anho
                else:
                    periodo = []
                    anho = []

    @api.model
    def _cron_update_data_chbs(self):
        self.data_chbs()

    @api.model
    def _cron_reminder(self):
        su_id = self.env['res.company'].browse(SUPERUSER_ID)
        domain = [('login', '=', 'admin')]
        author_id = self.env['res.users'].search(domain, limit=1)
        for banco in self.search([]):
            if banco.body_periodo_borrador:
                template_id = self.env['ir.model.data'].get_object_reference(
                    'hemored_notification',
                    'email_template_hemored_notification_reminder')[1]
                email_template_obj = self.env['mail.template'].browse(template_id)
                if template_id:
                    values = email_template_obj.generate_email(banco.id, fields=None)
                    values['email_to'] = banco.email
                    values['reply_to'] = su_id.email
                    values['auto_delete'] = False
                    values['message_type'] = 'email'
                    values['res_id'] = False
                    values['author_id'] = author_id.partner_id.id
                    mail_mail_obj = self.env['mail.mail']
                    mail_mail_obj.create(values)
        return True

    def action_record_notification(self):
        self.ensure_one()
        values = {
            'default_remitente_id': self.env.user.id,
            'default_destinatario_id': self.usuario_id.id,
            'default_nombre_reponsable': self.medico_coordinador_responsable,
            'default_numero_destinatario': self.celular,
            'default_chbs': 'Estimado Banco de Sangre le escribe el Sr(a) {} de parte de Pronahebas: '.format(self.env.user.name),
            'default_fecha_notificacion': fields.Datetime.now(),
        }
        action = self.env.ref('hemored_notification.hemored_notification_action').read()[0]
        action['domain'] = [('destinatario_id', '=', self.usuario_id.id)]
        action['context'] = values
        return action
