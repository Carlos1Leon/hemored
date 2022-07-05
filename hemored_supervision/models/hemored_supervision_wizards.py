# coding: utf-8

from odoo import fields, models, api
from odoo.exceptions import ValidationError
from ..models import constants


class WizardConfirmSupervision(models.TransientModel):
    _name = 'hemored_supervision.wizarconfirm'

    fecha = fields.Date(
        string='Fecha de realización Supervisión'
    )

    @api.onchange('fecha')
    def _onchange_fecha(self):
        if self.fecha and self.fecha < fields.Date.context_today(self):
            return {
                'warning': {'message': u'La fecha no debe ser menor a la de hoy'},
                'value': {'fecha': False},
            }

    @api.multi
    def action_confirm(self):
        self.ensure_one()
        record_date = self.env.context.get('active_id')
        record_date_id = self.env['hemored_supervision.record_date_supervision'].browse(record_date)
        domain = [('fecha_ejecucion', '=', self.fecha), ('state', '=', constants.CONFIRMADO), ('banco_id', '=', record_date_id.banco_id.id)]
        record_date_ids = self.env['hemored_supervision.record_date_supervision'].sudo().search(domain)
        if not record_date_ids:
            record_date_id.fecha_ejecucion = self.fecha
            record_date_id.state = constants.CONFIRMADO
        else:
            raise ValidationError('Fecha para supervisión no disponible')


class WizardPostponedSupervision(models.TransientModel):
    _name = 'hemored_supervision.wizarpostponed'

    motivo = fields.Text(
        string='Motivo de postergación'
    )
    fecha = fields.Date(
        string='Fecha de realización Supervisión'
    )

    @api.onchange('fecha')
    def _onchange_fecha(self):
        if self.fecha and self.fecha < fields.Date.context_today(self):
            return {
                'warning': {'message': u'La fecha no debe ser menor a la de hoy'},
                'value': {'fecha': False},
            }

    @api.multi
    def action_postponed(self):
        self.ensure_one()
        record_date = self.env.context.get('active_id')
        record_date_id = self.env['hemored_supervision.record_date_supervision'].browse(record_date)
        domain = [('fecha_ejecucion', '=', self.fecha), ('state', 'in', (constants.CONFIRMADO, constants.POSTERGADO)), ('banco_id', '=', record_date_id.banco_id.id)]
        record_date_ids = self.env['hemored_supervision.record_date_supervision'].sudo().search(domain)
        if not record_date_ids:
            record_date_id.fecha_ejecucion = self.fecha
            record_date_id.state = constants.POSTERGADO
            record_date_id.observacion = self.motivo
        else:
            raise ValidationError('Fecha para supervisión no disponible')
