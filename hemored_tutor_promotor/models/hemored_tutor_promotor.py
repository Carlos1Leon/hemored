# -*- coding: utf-8 -*-

from lxml import etree

from odoo import fields, models, api

from ..models import constants, res_users


class TutorRegistro(models.Model):
    _inherit = ['mail.thread', 'hemored.agente']
    _name = 'hemored.registro.tutor'
    _description = 'Registro de Tutores'
    _rec_name = 'name'

    tutor = fields.Boolean(
        string='Tutor',
    )

    _sql_constraints = [
        ('dni', 'unique(dni)',
         'Solo se permite un registro por dni'),
    ]

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(TutorRegistro, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        es_tutor = self.env.user.has_group('hemored_tutor_promotor.group_tutores_hemored')
        if view_type == 'form':
            doc_input_form_tutor = etree.XML(res['arch'])
            my_attrs1 = '{"readonly": true}'
            if es_tutor:
                for node in doc_input_form_tutor.xpath("//field[@name='dni']"):
                    node.set('modifiers', my_attrs1)
            res['arch'] = etree.tostring(doc_input_form_tutor)
        return res

    @api.model
    def create(self, vals):
        res = super(TutorRegistro, self).create(vals)
        res.accion_crear_usuarios()
        return res

    @api.multi
    def write(self, vals):
        res = super(TutorRegistro, self).write(vals)
        if 'correo' in vals:
            for obj in self:
                obj.action_change_email()
        return res

    @api.one
    def action_change_email(self):
        vals = {
            'email': self.correo,
        }
        self.usuario_id.sudo().write(vals)

    @api.one
    def accion_crear_usuarios(self):
        domain = [
            ('usuario_id', '=', False),
        ]
        if self.search(domain, limit=1):
            vals = {
                'name': self.name,
                'login': self.dni,
                'email': self.correo,
                'password': 'Minsa_{}'.format(self.dni),
                'tutor_promotor': constants.TUTOR,
                'tutor_id': self.id
            }
            usuario_id = self.env['res.users'].sudo().create(vals)
            self.write({'usuario_id': usuario_id.id})


class PromotorRegistro(models.Model):
    _inherit = ['mail.thread', 'hemored.agente']
    _name = 'hemored.registro.promotor'
    _description = 'Registro de Promotores'
    _rec_name = 'name'

    promotor = fields.Boolean(
        string='Promotor',
    )
    tutor_id = _id = fields.Many2one(
        comodel_name='hemored.registro.tutor',
        string='Tutor en cargado',
        default=lambda self: res_users._default_tutor(self),
    )

    _sql_constraints = [
        ('dni', 'unique(dni)',
         'Solo se permite un registro por dni'),
    ]

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(PromotorRegistro, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        es_tutor = self.env.user.has_group('hemored_tutor_promotor.group_tutores_hemored')
        if view_type == 'form':
            doc_input_form_tutor = etree.XML(res['arch'])
            my_attrs1 = '{"readonly": true}'
            if es_tutor:
                for node in doc_input_form_tutor.xpath("//field[@name='tutor_id']"):
                    node.set('modifiers', my_attrs1)
            res['arch'] = etree.tostring(doc_input_form_tutor)
        return res
