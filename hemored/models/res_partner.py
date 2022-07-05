# coding=utf-8
import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    signup_token = fields.Char(copy=False, groups='base.group_erp_manager,hemored.group_administrador')
    signup_type = fields.Char(string='Signup Token Type', copy=False, groups='base.group_erp_manager,hemored.group_administrador')
    signup_expiration = fields.Datetime(copy=False, groups='base.group_erp_manager,hemored.group_administrador')

    @api.one
    @api.constrains('email')
    def _check_email(self):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', self.email):
            raise ValidationError('E-mail no válido')

        domain = [
            ('id', '!=', self.id),
            ('email', '=', self.email),
        ]
        if self.search(domain, limit=1):
            raise ValidationError('Ya existe email registrado')
