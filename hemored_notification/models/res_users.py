from odoo import SUPERUSER_ID
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.addons.hemored.models import constants


class ResUsers(models.Model):
    _inherit = 'res.users'

    coordinador = fields.Boolean(string='Es Coordinador')
    body_periodo_enviado = fields.Char(
        string='Períodos de fichas que están en estado enviado',
    )
    body_anual_enviado = fields.Char(
        string='Fichas anuales que están en estado enviado',
    )

    @api.model
    def create(self, vals):
        if vals.get('mobile'):
            if (len(vals.get('mobile')) < 9 or not vals.get('mobile').isdigit()):
                raise ValidationError('El número de celular no debe tener letras y no debe ser menor a 9 digitos')
            if (len(vals.get('mobile')) > 9 or not vals.get('mobile').isdigit()):
                raise ValidationError('El número de celular no debe tener letras y no debe ser mayor a 9 digitos')
        res = super(ResUsers, self).create(vals)
        return res

    @api.multi
    def write(self, vals):
        res = super(ResUsers, self).write(vals)
        if 'mobile' in vals:
            if vals.get('mobile'):
                if (len(vals.get('mobile')) < 9 or not vals.get('mobile').isdigit()):
                    raise ValidationError('El número de celular no debe tener letras y no debe ser menor a 9 digitos')
                if (len(vals.get('mobile')) > 9 or not vals.get('mobile').isdigit()):
                    raise ValidationError('El número de celular no debe tener letras y no debe ser mayor a 9 digitos')
        return res

    @api.multi
    def data_coordinador(self):
        periodo = []
        anho = []
        domain = [('coordinador', '=', True)]
        user_ids = self.env['res.users'].search(domain)
        for user in user_ids:
            domain = [
                ('diresa_id', '=', user.diresa_id.id),
                ('state', '=', constants.ENVIADO),
            ]
            fichas_ids = self.env['hemored.ficha_estadistica'].search(domain)
            if fichas_ids:
                for fichas in fichas_ids:
                    if fichas.state == constants.ENVIADO:
                        if fichas.periodo_id and fichas.anho_id:
                            values_periodo_nombre = {
                                'ficha_mensual': fichas.periodo_id.name,
                                'Nombre': fichas.banco_id.name
                            }
                            periodo.append(values_periodo_nombre)
                        if fichas.anho_id and not fichas.periodo_id:
                            values_anho_nombre = {
                                'ficha_anual': fichas.anho_id.name,
                                'nombre': fichas.banco_id.name
                            }
                            anho.append(values_anho_nombre)
                    else:
                        user.body_periodo_enviado = False
                        user.body_anual_enviado = False

                if periodo:
                    user.body_periodo_enviado = periodo
                if anho:
                    user.body_anual_enviado = anho

    @api.model
    def _cron_update_data_coordinador(self):
        self.data_coordinador()

    @api.model
    def _cron_reminder_coordinador(self):
        su_id = self.env['res.company'].browse(SUPERUSER_ID)
        domain = [('coordinador', '=', True)]
        domain_author = [('login', '=', 'admin')]
        author_id = self.env['res.users'].search(domain_author, limit=1)
        for coordinador in self.search(domain):
            if coordinador:
                template_id = self.env['ir.model.data'].get_object_reference(
                    'hemored_notification',
                    'email_template_hemored_notification_reminder_coordinador')[1]
                email_template_obj = self.env['mail.template'].browse(template_id)
                if template_id:
                    values = email_template_obj.generate_email(coordinador.id, fields=None)
                    values['email_from'] = su_id.email
                    values['email_to'] = coordinador.email
                    values['reply_to'] = su_id.email
                    values['res_id'] = False
                    values['author_id'] = author_id.partner_id.id
                    mail_mail_obj = self.env['mail.mail']
                    msg_id = mail_mail_obj.sudo().create(values)
                    if msg_id:
                        msg_id.sudo().send()
        return True

    def action_record_notification(self):
        self.ensure_one()
        values = {
            'default_remitente_id': self.env.user.id,
            'default_destinatario_id': self.id,
            'default_nombre_reponsable': self.name,
            'default_numero_destinatario': self.mobile,
            'default_diris': 'Estimado Coordinador le escribe el Sr(a) {} de parte de Pronahebas: '.format(self.env.user.name),
            'default_fecha_notificacion': fields.Datetime.now(),
        }
        action = self.env.ref('hemored_notification.hemored_notification_action').read()[0]
        action['domain'] = [('destinatario_id', '=', self.id)]
        action['context'] = values
        return action
