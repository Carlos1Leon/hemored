# -*- coding: utf-8 -*-

import datetime

from odoo import api, fields, models
from odoo.exceptions import ValidationError

from ..models import constants


class ResUsers(models.Model):
    _inherit = 'res.users'

    tutor_promotor = fields.Selection(
        string='Tutor ó promotor',
        selection=constants.SELECTION_TIPO_PERSONA,
    )
    tutor_id = fields.Many2one(
        comodel_name='hemored.registro.tutor',
        string='Tutor',
    )
    promotor_id = fields.Many2one(
        comodel_name='hemored.registro.promotor',
        string='Promotor',
    )
    dni = fields.Char(
        string='DNI'
    )

    def _default_tutor(self):
        es_tutor = self.env.user.has_group('hemored_tutor_promotor.group_tutores_hemored')
        if es_tutor:
            usuario = self.env.user.id
            tutor_id = self.env['hemored.registro.tutor'].search([('usuario_id', '=', usuario)], limit=1)
            return tutor_id.id
        else:
            return False

    @api.onchange('dni')
    def _onchange_dni(self):
        if self.dni:
            if len(self.dni) != 8 or not self.dni.isdigit():
                return {
                    'warning': {
                        'title': 'Error en el DNI',
                        'message': 'El DNI debe tener 8 números',
                    },
                }

            values = {}
            data = self.env['consultadatos.mpi'].ver(self.dni, '01')
            if 'error' in data:
                raise ValidationError(data['error'])

            if not data.get('es_persona_viva'):
                raise ValidationError('Persona fallecida')

            values = {
                'name': '%s %s %s' % (
                    data.get('nombres', ''),
                    data.get('apellido_paterno', ''),
                    data.get('apellido_materno', '')
                )
            }
            return {'value': values}

    def set_groups_tutor_promotor(self, tutor_promotor):
        value = {}
        if tutor_promotor:
            if tutor_promotor == constants.TUTOR:
                group_tutor = self.env.ref('hemored_tutor_promotor.group_tutores_hemored', False)
                if group_tutor:
                    value.update({
                        'in_group_{}'.format(group_tutor.id): 1
                    })
            else:
                grupo_promotor = self.env.ref('hemored_tutor_promotor.group_promotores_hemored', False)
                if grupo_promotor:
                    value.update({
                        'in_group_{}'.format(grupo_promotor.id): 1
                    })
        group_hr_user = self.env.ref('base.group_user', False)
        if group_hr_user:
            value.update({'sel_groups_{}'.format(group_hr_user.id): 1})
        return value

    @api.model
    def create(self, value):
        value.update(self.set_groups_tutor_promotor(value.get('tutor_promotor')))
        res = super(ResUsers, self).create(value)
        res.password_write_date = datetime.datetime.now() - datetime.timedelta(days=self.env.user.company_id.password_expiration + 2)
        res.odoobot_state = 'disabled'
        return res

    @api.multi
    def write(self, value):
        value.update(self.set_groups_tutor_promotor(value.get('tutor_promotor')))
        res = super(ResUsers, self).write(value)
        return res
