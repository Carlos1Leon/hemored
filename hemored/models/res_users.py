import re
import datetime

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='Diresa',
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS'
    )
    registro_web = fields.Boolean(
        string='Registro desde la web',
    )
    registrado = fields.Boolean(
        string='Banco registrado'
    )

    @api.onchange('diresa_id')
    def _onchange_diresa_id(self):
        self.banco_id = False

    @api.onchange('login')
    def onchange_login(self):
        if self.login:
            self.login = self.login.upper().replace(' ', '')

    @api.onchange('email')
    def _onchange_email(self):
        if self.email and not re.match(r'[^@]+@[^@]+\.[^@]+', self.email):
            return {
                'warning': {'message': u'E-mail no válido', },
                'value': {'email': False},
            }

    def set_groups(self, diresa, banco, login, registro_web, registrado):
        value = {}
        if diresa:
            if not banco:
                group_coordinador_diris_diresa = self.env.ref('hemored.group_coordinador_diris_diresa_hemored', False)
                if group_coordinador_diris_diresa:
                    value.update({
                        'in_group_{}'.format(group_coordinador_diris_diresa.id): 1,
                    })
            else:
                if registro_web and registrado is False:
                    grupo_pre_inscripcion = self.env.ref('hemored.group_pre_inscripcion_hemored', False)
                    if grupo_pre_inscripcion:
                        value.update({'in_group_{}'.format(grupo_pre_inscripcion.id): 1})
                else:
                    group_coordinador_establecimiento = self.env.ref('hemored.group_coordinador_establecimiento_hemored', False)
                    grupo_pre_inscripcion = self.env.ref('hemored.group_pre_inscripcion_hemored', False)
                    if group_coordinador_establecimiento:
                        value.update({'in_group_{}'.format(group_coordinador_establecimiento.id): 1})
                        value.update({'in_group_{}'.format(grupo_pre_inscripcion.id): 0})
        group_hr_user = self.env.ref('base.group_user', False)
        if group_hr_user:
            value.update({'sel_groups_{}'.format(group_hr_user.id): 1})
        return value

    @api.model
    def create(self, value):
        value.update(self.set_groups(value.get('diresa_id'), value.get('banco_id'), value.get('login'), value.get('registro_web'), value.get('registrado')))
        res = super(ResUsers, self).create(value)
        if res.diresa_id and not res.banco_id:
            res.password = 'Minsa_{}'.format(self.login)
        res.password_write_date = datetime.datetime.now() - datetime.timedelta(days=self.env.user.company_id.password_expiration + 2)
        res.odoobot_state = 'disabled'
        return res

    @api.multi
    def write(self, value):
        value.update(self.set_groups(value.get('diresa_id'), value.get('banco_id'), value.get('login'), value.get('registro_web'), value.get('registrado')))
        res = super(ResUsers, self).write(value)
        return res
