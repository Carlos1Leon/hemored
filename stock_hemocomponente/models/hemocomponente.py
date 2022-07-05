# -*- coding: utf-8 -*-

from lxml import etree
from dateutil.relativedelta import relativedelta

from odoo import fields, models, api
from odoo.exceptions import ValidationError

from ..models import constants

MN_StockHemocomponente = '.'.join([constants.MODULO, 'hemocomponente'])


class StockHemocomponente(models.Model):
    _inherit = 'mail.thread'
    _name = MN_StockHemocomponente
    _description = 'Stock Hemocomponentes'
    _rec_name = 'banco_id'
    _order = 'diresa_id asc'

    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS',
        default=lambda self: self.env.user.banco_id
    )
    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='Región',
        default=lambda self: self.env.user.diresa_id
    )
    state = fields.Selection(
        string='Estado',
        selection=constants.SELECTION_ESTADO_STOCK,
        default=constants.NO_REPORTO,
        track_visibility='onchange'
    )
    fecha = fields.Date(
        string='Fecha de ingreso de información',
        default=fields.Date.today
    )
    o_positivo_paquete_globular = fields.Char(
        string='Paquete globular - O+',
        track_visibility='onchange'
    )
    a_positivo_paquete_globular = fields.Char(
        string=u'Paquete globular - A+',
        track_visibility='onchange'
    )
    b_positivo_paquete_globular = fields.Char(
        string='Paquete globular - B+',
        track_visibility='onchange'
    )
    ab_positivo_paquete_globular = fields.Char(
        string='Paquete globular - AB+',
        track_visibility='onchange'
    )
    o_negativo_paquete_globular = fields.Char(
        string='Paquete globular - O-',
        track_visibility='onchange'
    )
    a_negativo_paquete_globular = fields.Char(
        string='Paquete globular - A-',
        track_visibility='onchange'
    )
    b_negativo_paquete_globular = fields.Char(
        string='Paquete globular - B-',
        track_visibility='onchange'
    )
    ab_negativo_paquete_globular = fields.Char(
        string='Paquete globular - AB-',
        track_visibility='onchange'
    )
    total_paquete_globular = fields.Char(
        string='Total paquete globular',
        compute='_compute_total_globular',
        store=True,
        track_visibility='onchange'
    )
    o_positivo_plasma_fresco = fields.Char(
        string='Plasma fresco congelado - O+',
        track_visibility='onchange'
    )
    a_positivo_plasma_fresco = fields.Char(
        string=u'Plasma fresco congelado - A+',
        track_visibility='onchange'
    )
    b_positivo_plasma_fresco = fields.Char(
        string='Plasma fresco congelado - B+',
        track_visibility='onchange'
    )
    ab_positivo_plasma_fresco = fields.Char(
        string='Plasma fresco congelado - AB+',
        track_visibility='onchange'
    )
    o_negativo_plasma_fresco = fields.Char(
        string='Plasma fresco congelado - O-',
        track_visibility='onchange'
    )
    a_negativo_plasma_fresco = fields.Char(
        string='Plasma fresco congelado - A-',
        track_visibility='onchange'
    )
    b_negativo_plasma_fresco = fields.Char(
        string='Plasma fresco congelado - B-',
        track_visibility='onchange'
    )
    ab_negativo_plasma_fresco = fields.Char(
        string='Plasma fresco congelado - AB-',
        track_visibility='onchange'
    )
    total_plasma_fresco = fields.Char(
        string='Total plasma fresco congelado',
        compute='_compute_total_plasma_fresco',
        store=True,
        track_visibility='onchange'
    )
    total_plaquetas_simple = fields.Char(
        string='Total de Plaquetas simples',
        track_visibility='onchange'
    )
    total_concentrado_plaquetas = fields.Char(
        string='Total de concentrado de plaquetas por aféresis',
        track_visibility='onchange'
    )
    total_crioprecipitado = fields.Char(
        string='Total de Crioprecipitado',
        track_visibility='onchange'
    )
    total_unidades_pendientes_tamisaje = fields.Char(
        string='Total de unidades pendientes de tamizaje',
        track_visibility='onchange'
    )
    total_donaciones_sangre_x_dia = fields.Char(
        string='Donaciones de sangre / día',
        track_visibility='onchange'
    )
    total_transfuciones_x_dia = fields.Char(
        string='Transfusiones de P. Glob. / día',
        track_visibility='onchange'
    )
    total_transfuciones_plaquetas_x_dia = fields.Char(
        string='Transfusiones de plaquetas',
        track_visibility='onchange'
    )

    @api.one
    def action_draft(self):
        self.state = constants.NO_REPORTO

    @api.one
    def action_send(self):
        self.state = constants.REPORTO

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(StockHemocomponente, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        es_admin = self.env.user.has_group('hemored.group_administrador')
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            my_attrs = '{"readonly": true}'
            if not es_admin:
                for node in doc.xpath("//field[@name='banco_id']"):
                    node.set('modifiers', my_attrs)
                for node in doc.xpath("//field[@name='diresa_id']"):
                    node.set('modifiers', my_attrs)
            res['arch'] = etree.tostring(doc)
        return res

    @api.onchange('banco_id')
    def _onchange_diresa(self):
        if self.banco_id:
            self.diresa_id = self.banco_id.diresa_id

    @api.onchange('o_positivo_paquete_globular')
    def _onchange_o_positivo_paquete_globular(self):
        if self.o_positivo_paquete_globular and not self.o_positivo_paquete_globular.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Paquete globular - O+, deben ser un número'},
                'value': {'o_positivo_paquete_globular': False},
            }

    @api.onchange('a_positivo_paquete_globular')
    def _onchange_a_positivo_paquete_globular(self):
        if self.a_positivo_paquete_globular and not self.a_positivo_paquete_globular.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Paquete globular - A+, deben ser un número'},
                'value': {'a_positivo_paquete_globular': False},
            }

    @api.onchange('b_positivo_paquete_globular')
    def _onchange_b_positivo_paquete_globular(self):
        if self.b_positivo_paquete_globular and not self.b_positivo_paquete_globular.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Paquete globular - B+, deben ser un número'},
                'value': {'b_positivo_paquete_globular': False},
            }

    @api.onchange('o_negativo_paquete_globular')
    def _onchange_o_negativo_paquete_globular(self):
        if self.o_negativo_paquete_globular and not self.o_negativo_paquete_globular.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Paquete globular - O-, deben ser un número'},
                'value': {'o_negativo_paquete_globular': False},
            }

    @api.onchange('a_negativo_paquete_globular')
    def _onchange_a_negativo_paquete_globular(self):
        if self.a_negativo_paquete_globular and not self.a_negativo_paquete_globular.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Paquete globular - A-, deben ser un número'},
                'value': {'a_negativo_paquete_globular': False},
            }

    @api.onchange('b_negativo_paquete_globular')
    def _onchange_b_negativo_paquete_globular(self):
        if self.b_negativo_paquete_globular and not self.b_negativo_paquete_globular.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Paquete globular - B-, deben ser un número'},
                'value': {'b_negativo_paquete_globular': False},
            }

    @api.onchange('ab_negativo_paquete_globular')
    def _onchange_ab_negativo_paquete_globular(self):
        if self.ab_negativo_paquete_globular and not self.ab_negativo_paquete_globular.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Paquete globular - AB-, deben ser un número'},
                'value': {'ab_negativo_paquete_globular': False},
            }

    @api.onchange('ab_positivo_paquete_globular')
    def _onchange_ab_positivo_paquete_globular(self):
        if self.ab_positivo_paquete_globular and not self.ab_positivo_paquete_globular.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Paquete globular - AB+, deben ser un número'},
                'value': {'ab_positivo_paquete_globular': False},
            }

    @api.one
    @api.depends('o_positivo_paquete_globular', 'a_positivo_paquete_globular', 'b_positivo_paquete_globular',
                 'o_negativo_paquete_globular', 'a_negativo_paquete_globular', 'b_negativo_paquete_globular',
                 'ab_negativo_paquete_globular', 'ab_positivo_paquete_globular')
    def _compute_total_globular(self):
        if not self.o_positivo_paquete_globular and not self.a_positivo_paquete_globular and not self.b_positivo_paquete_globular and not self.o_negativo_paquete_globular and not self.a_negativo_paquete_globular and not self.b_negativo_paquete_globular and not self.ab_negativo_paquete_globular and not self.ab_positivo_paquete_globular:
            self.total_paquete_globular = ''
        else:
            if self.o_positivo_paquete_globular:
                o_positivo_paquete_globular = int(self.o_positivo_paquete_globular)
            else:
                o_positivo_paquete_globular = 0
            if self.a_positivo_paquete_globular:
                a_positivo_paquete_globular = int(self.a_positivo_paquete_globular)
            else:
                a_positivo_paquete_globular = 0
            if self.b_positivo_paquete_globular:
                b_positivo_paquete_globular = int(self.b_positivo_paquete_globular)
            else:
                b_positivo_paquete_globular = 0
            if self.ab_positivo_paquete_globular:
                ab_positivo_paquete_globular = int(self.ab_positivo_paquete_globular)
            else:
                ab_positivo_paquete_globular = 0
            if self.o_negativo_paquete_globular:
                o_negativo_paquete_globular = int(self.o_negativo_paquete_globular)
            else:
                o_negativo_paquete_globular = 0
            if self.a_negativo_paquete_globular:
                a_negativo_paquete_globular = int(self.a_negativo_paquete_globular)
            else:
                a_negativo_paquete_globular = 0
            if self.b_negativo_paquete_globular:
                b_negativo_paquete_globular = int(self.b_negativo_paquete_globular)
            else:
                b_negativo_paquete_globular = 0
            if self.ab_negativo_paquete_globular:
                ab_negativo_paquete_globular = int(self.ab_negativo_paquete_globular)
            else:
                ab_negativo_paquete_globular = 0
            self.total_paquete_globular = o_positivo_paquete_globular + a_positivo_paquete_globular + b_positivo_paquete_globular + ab_positivo_paquete_globular \
                + o_negativo_paquete_globular + a_negativo_paquete_globular + b_negativo_paquete_globular + ab_negativo_paquete_globular

    @api.onchange('o_positivo_plasma_fresco')
    def _onchange_o_positivo_plasma_fresco(self):
        if self.o_positivo_plasma_fresco and not self.o_positivo_plasma_fresco.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Plasma fresco congelado - O+, deben ser un número'},
                'value': {'o_positivo_plasma_fresco': False},
            }

    @api.onchange('a_positivo_plasma_fresco')
    def _onchange_a_positivo_plasma_fresco(self):
        if self.a_positivo_plasma_fresco and not self.a_positivo_plasma_fresco.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Plasma fresco congelado - A+, deben ser un número'},
                'value': {'a_positivo_plasma_fresco': False},
            }

    @api.onchange('b_positivo_plasma_fresco')
    def _onchange_b_positivo_plasma_fresco(self):
        if self.b_positivo_plasma_fresco and not self.b_positivo_plasma_fresco.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Plasma fresco congelado - B+, deben ser un número'},
                'value': {'b_positivo_plasma_fresco': False},
            }

    @api.onchange('ab_positivo_plasma_fresco')
    def _onchange_ab_positivo_plasma_fresco(self):
        if self.ab_positivo_plasma_fresco and not self.ab_positivo_plasma_fresco.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Plasma fresco congelado - AB+, deben ser un número'},
                'value': {'ab_positivo_plasma_fresco': False},
            }

    @api.onchange('o_negativo_plasma_fresco')
    def _onchange_o_negativo_plasma_fresco(self):
        if self.o_negativo_plasma_fresco and not self.o_negativo_plasma_fresco.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Plasma fresco congelado - O-, deben ser un número'},
                'value': {'o_negativo_plasma_fresco': False},
            }

    @api.onchange('a_negativo_plasma_fresco')
    def _onchange_a_negativo_plasma_fresco(self):
        if self.a_negativo_plasma_fresco and not self.a_negativo_plasma_fresco.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Plasma fresco congelado - A-, deben ser un número'},
                'value': {'a_negativo_plasma_fresco': False},
            }

    @api.onchange('b_negativo_plasma_fresco')
    def _onchange_b_negativo_plasma_fresco(self):
        if self.b_negativo_plasma_fresco and not self.b_negativo_plasma_fresco.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Plasma fresco congelado - B-, deben ser un número'},
                'value': {'b_negativo_plasma_fresco': False},
            }

    @api.onchange('ab_negativo_plasma_fresco')
    def _onchange_ab_negativo_plasma_fresco(self):
        if self.ab_negativo_plasma_fresco and not self.ab_negativo_plasma_fresco.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Plasma fresco congelado - AB-, deben ser un número'},
                'value': {'ab_negativo_plasma_fresco': False},
            }

    @api.one
    @api.depends('o_positivo_plasma_fresco', 'a_positivo_plasma_fresco', 'b_positivo_plasma_fresco',
                 'ab_positivo_plasma_fresco', 'o_negativo_plasma_fresco', 'a_negativo_plasma_fresco',
                 'b_negativo_plasma_fresco', 'ab_negativo_plasma_fresco')
    def _compute_total_plasma_fresco(self):
        if not self.o_positivo_plasma_fresco and not self.a_positivo_plasma_fresco and not self.b_positivo_plasma_fresco and not self.ab_positivo_plasma_fresco and not self.o_negativo_plasma_fresco and not self.a_negativo_plasma_fresco and not self.b_negativo_plasma_fresco and not self.ab_negativo_plasma_fresco:
            self.total_plasma_fresco = ''
        else:
            if self.o_positivo_plasma_fresco:
                o_positivo_plasma_fresco = int(self.o_positivo_plasma_fresco)
            else:
                o_positivo_plasma_fresco = 0
            if self.a_positivo_plasma_fresco:
                a_positivo_plasma_fresco = int(self.a_positivo_plasma_fresco)
            else:
                a_positivo_plasma_fresco = 0
            if self.b_positivo_plasma_fresco:
                b_positivo_plasma_fresco = int(self.b_positivo_plasma_fresco)
            else:
                b_positivo_plasma_fresco = 0
            if self.ab_positivo_plasma_fresco:
                ab_positivo_plasma_fresco = int(self.ab_positivo_plasma_fresco)
            else:
                ab_positivo_plasma_fresco = 0
            if self.o_negativo_plasma_fresco:
                o_negativo_plasma_fresco = int(self.o_negativo_plasma_fresco)
            else:
                o_negativo_plasma_fresco = 0
            if self.a_negativo_plasma_fresco:
                a_negativo_plasma_fresco = int(self.a_negativo_plasma_fresco)
            else:
                a_negativo_plasma_fresco = 0
            if self.b_negativo_plasma_fresco:
                b_negativo_plasma_fresco = int(self.b_negativo_plasma_fresco)
            else:
                b_negativo_plasma_fresco = 0
            if self.ab_negativo_plasma_fresco:
                ab_negativo_plasma_fresco = int(self.ab_negativo_plasma_fresco)
            else:
                ab_negativo_plasma_fresco = 0
            self.total_plasma_fresco = o_positivo_plasma_fresco + a_positivo_plasma_fresco + b_positivo_plasma_fresco + ab_positivo_plasma_fresco \
                + o_negativo_plasma_fresco + a_negativo_plasma_fresco + b_negativo_plasma_fresco + ab_negativo_plasma_fresco

    @api.onchange('total_plaquetas_simple')
    def _onchange_total_plaquetas_simple(self):
        if self.total_plaquetas_simple and not self.total_plaquetas_simple.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Total de Plaquetas simples, deben ser un número'},
                'value': {'total_plaquetas_simple': False},
            }

    @api.onchange('total_concentrado_plaquetas')
    def _onchange_total_concentrado_plaquetas(self):
        if self.total_concentrado_plaquetas and not self.total_concentrado_plaquetas.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Total de concentrado de plaquetas por aféresis, deben ser un número'},
                'value': {'total_concentrado_plaquetas': False},
            }

    @api.onchange('total_crioprecipitado')
    def _onchange_total_crioprecipitado(self):
        if self.total_crioprecipitado and not self.total_crioprecipitado.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Total de Crioprecipitado, deben ser un número'},
                'value': {'total_crioprecipitado': False},
            }

    @api.onchange('total_unidades_pendientes_tamisaje')
    def _onchange_total_unidades_pendientes_tamisaje(self):
        if self.total_unidades_pendientes_tamisaje and not self.total_unidades_pendientes_tamisaje.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Total de unidades pendientes de tamizaje, deben ser un número'},
                'value': {'total_unidades_pendientes_tamisaje': False},
            }

    @api.onchange('total_donaciones_sangre_x_dia')
    def _onchange_total_donaciones_sangre_x_dia(self):
        if self.total_donaciones_sangre_x_dia and not self.total_donaciones_sangre_x_dia.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Donaciones de sangre / día, deben ser un número'},
                'value': {'total_donaciones_sangre_x_dia': False},
            }

    @api.onchange('total_transfuciones_x_dia')
    def _onchange_total_transfuciones_x_dia(self):
        if self.total_transfuciones_x_dia and not self.total_transfuciones_x_dia.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de Transfuciones de P. Glob. / día, deben ser un número'},
                'value': {'total_transfuciones_x_dia': False},
            }

    @api.onchange('total_transfuciones_plaquetas_x_dia')
    def _onchange_total_transfuciones_plaquetas_x_dia(self):
        if self.total_transfuciones_plaquetas_x_dia and not self.total_transfuciones_plaquetas_x_dia.isdigit():
            return {
                'warning': {'message': u'El valor ingresado de transfuciones de plaquetas, deben ser un número'},
                'value': {'total_transfuciones_plaquetas_x_dia': False},
            }

    @api.constrains('fecha')
    def _check_registro(self):
        domain = [
            ('id', 'not in', self.ids),
            ('banco_id', '=', self.banco_id.id),
            ('fecha', '=', self.fecha),
        ]
        domain_quince = [
            ('id', 'not in', self.ids),
            ('banco_id', '=', self.banco_id.id),
        ]
        fecha = fields.Date.from_string(self.fecha)
        fecha_ultimoregistro = fields.Date.from_string(self.search(domain_quince, limit=1, order='fecha DESC').fecha)
        confg = self.env['stock_hemocomponente.configuracion'].sudo().search([], limit=1)
        if self.search(domain, limit=1) and confg.periodicidad == constants.DIARIO:
            raise ValidationError('Ya existe registro de stock de hemocomponentes para esta fecha')
        if self.search(domain_quince, limit=1) and confg.periodicidad == constants.QUINCENAL:
            fecha_registro_quince = fecha_ultimoregistro + relativedelta(days=15)
            if fecha_registro_quince != fecha:
                raise ValidationError('El registro de stock se debe realizar cada 15 días')
        if self.search(domain_quince, limit=1) and confg.periodicidad == constants.MENSUAL:
            fecha_registro_treinta = fecha_ultimoregistro + relativedelta(days=30)
            if fecha_registro_treinta != fecha:
                raise ValidationError('El registro de stock se debe realizar cada 30 días')
