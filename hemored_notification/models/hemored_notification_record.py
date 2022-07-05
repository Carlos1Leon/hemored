# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import ValidationError
from ..models import constants

MN_NotificationRecord = '.'.join([constants.MODULO, 'notification_record'])


class NotificationRecord(models.Model):
    _inherit = 'mail.thread'
    _name = MN_NotificationRecord
    _description = 'Registro de notificación'
    _rec_name = 'tipo_notificacion'
    _order = 'fecha_notificacion asc'

    remitente_id = fields.Many2one(
        comodel_name='res.users',
        string='Remitente',
        track_visibility='onchange'
    )
    destinatario_id = fields.Many2one(
        comodel_name='res.users',
        string='Destinatario',
        track_visibility='onchange'
    )
    nombre_reponsable = fields.Char(
        string='Destinatario',
        track_visibility='onchange'
    )
    numero_destinatario = fields.Char(
        string='Número de celular de destinatario',
        track_visibility='onchange'
    )
    fecha_notificacion = fields.Datetime(
        string='Fecha de notificación',
        track_visibility='onchange'
    )
    tipo_notificacion = fields.Selection(
        string='Tipo de notificación',
        selection=constants.SELECTION_TYPE_NOTIFICATION,
        track_visibility='onchange'
    )
    mensaje = fields.Text(
        string='Mensaje',
        size=150,
        track_visibility='onchange'
    )
    mensaje_registrado = fields.Boolean(
        string='Mensaje registrado',
    )
    observacion = fields.Char(
        string='Observación',
        track_visibility='onchange'
    )
    accept_send = fields.Boolean(
        string='Aceptar uso de botón WhatsApp',
        track_visibility='onchange',
    )
    chbs = fields.Char(
        string='CHBS'
    )
    diris = fields.Char(
        string='DIRIS/DIRESA/GERESA'
    )

    def acion_send(self):
        if self.accept_send:
            if self.chbs:
                value = self.send_msg(self.chbs)
            elif self.diris:
                value = self.send_msg(self.diris)
            if not value.get('mensaje_registrado'):
                self.mensaje_registrado = True
                return value
            else:
                raise ValidationError('Cree un nuevo registro para enviar un mensaje')
        else:
            raise ValidationError(u'Lea los términos de uso del botón (Mensaje de WhatsApp) y acepte los términos de uso para enviar el mensaje')

    def send_msg(self, dest):
        intro = dest
        if self.mensaje and self.numero_destinatario:
            message_string = ''
            message = self.mensaje.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
            message_string = message_string[:(len(message_string) - 3)]
            value = {
                'type': 'ir.actions.act_url',
                'url': "https://api.whatsapp.com/send?phone=" + "+51" + self.numero_destinatario + "&text=" + intro + message_string,
                'target': 'new',
                'res_id': self.id,
            }
            if self.mensaje_registrado:
                value.update({
                    'mensaje_registrado': True,
                })
            else:
                value.update({
                    'mensaje_registrado': False,
                })
            return value
