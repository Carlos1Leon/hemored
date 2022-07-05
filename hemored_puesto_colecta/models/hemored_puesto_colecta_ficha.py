# -*- coding: utf-8 -*-
from lxml import etree

from odoo import api, fields, models
from odoo.exceptions import ValidationError

from ..models import constants


class FichaPuestoColecta(models.Model):
    _inherit = 'mail.thread'
    _name = 'hemored_puesto_colecta.ficha'

    _description = 'Ficha Estadística - Puesto de Colecta'

    hemored_puesto_colecta_id = fields.Many2one(
        comodel_name='hemored_puesto_colecta.puesto',
        string='Puesto de Colecta',
        required=True,
        track_visibility='onchange'
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='Banco',
        required=True,
        default=lambda self: self.env.user.banco_id,
        track_visibility='onchange'
    )
    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='DIRIS/DIRESA/GERESA',
        required=True,
        track_visibility='onchange'
    )
    fecha_ficha = fields.Date(
        string=u'Fecha de la Ficha',
        required=True,
        track_visibility='onchange'
    )
    fecha_llenado = fields.Date(
        string=u'Fecha del llenado',
        track_visibility='onchange'
    )
    estado = fields.Selection(
        string='Estado',
        selection=constants.SELECTION_STATE,
        default=constants.BORRADOR,
        track_visibility='onchange'
    )

    postulantes = fields.Integer(
        'Cantidad postulantes registrados',
        track_visibility='onchange'
    )

    donantes = fields.Integer(
        'Cantidad donantes registrados',
        track_visibility='onchange'
    )

    donantes_hombre = fields.Integer(
        'Cantidad donantes Hombres registrados',
        track_visibility='onchange'
    )

    donantes_mujer = fields.Integer(
        'Cantidad donantes Mujeres registrados',
        track_visibility='onchange'
    )

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(FichaPuestoColecta, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        es_coordinador_establecimiento = self.env.user.has_group('hemored.group_coordinador_establecimiento_hemored')
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            modifiers = '{"readonly": true}'
            if es_coordinador_establecimiento:
                for node in doc.xpath("//field[@name='hemored_puesto_colecta_id']"):
                    node.set('modifiers', modifiers)
                for node in doc.xpath("//field[@name='banco_id']"):
                    node.set('modifiers', modifiers)
                for node in doc.xpath("//field[@name='diresa_id']"):
                    node.set('modifiers', modifiers)
                for node in doc.xpath("//field[@name='fecha_ficha']"):
                    node.set('modifiers', modifiers)
                for node in doc.xpath("//field[@name='fecha_llenado']"):
                    node.set('modifiers', modifiers)
            res['arch'] = etree.tostring(doc)
        return res

    tuple_attrs = ('postulantes', 'donantes', 'donantes_hombre', 'donantes_mujer')

    @api.onchange(*tuple_attrs)
    def _onchange_tuple_attrs(self):
        def message_error(name):
            return {
                'warning': {'message': u'El valor ingresado de {}, deben ser positivos o iguales a 0 '.format(name)},
                'value': {name: 0},
            }

        for name in self.tuple_attrs:
            if getattr(self, name) < 0:
                return message_error(name)

    @api.one
    @api.constrains('donantes', 'donantes_hombre', 'donantes_mujer')
    def _check_donantes(self):
        if self.donantes and self.donantes_hombre and self.donantes_mujer and (self.donantes != (self.donantes_hombre + self.donantes_mujer)):
            raise ValidationError('La suma de donantes hombres y mujeres no concuerda con los donantes totales')

    @api.one
    @api.constrains('postulantes', 'donantes')
    def _check_postulantes_donantes(self):
        if self.donantes and self.postulantes and (self.donantes > self.postulantes):
            raise ValidationError('La cantidad de donantes registrados no puede ser mayor a la cantidad de postulantes')

    @api.one
    def action_send(self):
        self.estado = constants.ENVIADO

    @api.one
    def action_observed(self):
        self.estado = constants.BORRADOR

    @api.one
    def action_valid(self):
        self.estado = constants.VALIDADO
