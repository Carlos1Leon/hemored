# -*- coding: utf-8 -*-

from odoo import api, _, fields, models
from odoo.exceptions import ValidationError
from ..models import constants


class SellosCalidad(models.Model):
    _name = 'hemored.sellos.calidad'
    _inherit = 'mail.thread'
    _rec_name = 'banco_id'
    _description = 'Sellos de Calidad'

    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='Diresa',
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS'
    )
    solicitud_ids = fields.One2many(
        comodel_name='hemored.solicitud.line',
        inverse_name='sellos_id',
        string='Solicitudes'
    )

    @api.one
    @api.constrains('banco_id')
    def _check_banco_id(self):
        domain = [
            ('id', '!=', self.id),
            ('banco_id', '=', self.banco_id.id),
        ]
        if self.search(domain, limit=1):
            raise ValidationError('Solo puede haber un registro por CHBS')


class HemoredSolicitudLine(models.Model):
    _name = 'hemored.solicitud.line'
    _description = 'Solicitud de Sellos de Calidad'
    _order = 'fecha_solicitud asc,id'

    fecha_solicitud = fields.Date(
        string='Fecha de solicitud'
    )
    num_expediente = fields.Char(
        string='Número de expediente'
    )
    cant_solicitada = fields.Char(
        string='Cantidad solicitada'
    )
    cant_entregada = fields.Char(
        string='Cantidad entregada'
    )
    fecha_entrega = fields.Date(
        string='Fecha de entrega'
    )
    sellos_id = fields.Many2one(
        comodel_name='hemored.sellos.calidad',
        string='Sello',
        ondelete='cascade'
    )
    serie_ids = fields.One2many(
        comodel_name='hemored.serie.line',
        inverse_name='solicitud_id',
        string='Series'
    )

    def unlink(self):
        for serie in self.serie_ids:
            if serie.is_generate:
                raise ValidationError(_('No puede eliminar registros con sellos generados para número de expediente "%s" en el formulario') % self.num_expediente)
        return super(HemoredSolicitudLine, self).unlink()

    @api.one
    @api.constrains('num_expediente')
    def _check_num_expediente(self):
        domain = [
            ('id', '!=', self.id),
            ('num_expediente', '=', self.num_expediente),
        ]
        if self.search(domain, limit=1):
            raise ValidationError(_('Solo puede haber un registro con el mismo expediente "%s" en el formulario') % self.num_expediente)

    @api.onchange('fecha_entrega')
    def _onchange_fecha_entrega(self):
        if self.fecha_entrega and self.fecha_solicitud:
            if self.fecha_entrega < self.fecha_solicitud:
                return {
                    'warning': {'message': u'La fecha de entrega no debe ser menor a la fecha de solicitud de sellos de calidad'},
                    'value': {'fecha_entrega': False},
                }

    @api.onchange('fecha_solicitud')
    def _onchange_fecha_solicitud(self):
        if self.fecha_solicitud and self.fecha_entrega:
            if self.fecha_entrega < self.fecha_solicitud:
                return {
                    'warning': {
                        'message': u'La fecha de solicitud no debe ser mayor a la fecha de entrega de sellos de calidad'},
                    'value': {'fecha_solicitud': False},
                }

    @api.onchange('cant_entregada')
    def _onchange_cant_entregada(self):
        if self.cant_entregada:
            if not self.cant_entregada.isdigit():
                return {
                    'warning': {'message': u'La cantidad entregada, debe ser un número'},
                    'value': {'cant_entregada': False},
                }
            if self.cant_solicitada and self.cant_entregada and int(self.cant_entregada) > int(self.cant_solicitada):
                return {
                    'warning': {'message': u'La cantidad de sellos entregados no debe ser mayor a la cantidad de sellos de calidad solicitados'},
                    'value': {'cant_entregada': False},
                }
            if int(self.cant_entregada) == 0:
                return {
                    'warning': {'message': u'La cantidad entregada, no debe ser cero'},
                    'value': {'cant_entregada': False},
                }

    @api.onchange('cant_solicitada')
    def _onchange_cant_solicitada(self):
        if self.cant_solicitada:
            if not self.cant_solicitada.isdigit():
                return {
                    'warning': {'message': u'La cantidad solicitada, debe ser un número'},
                    'value': {'cant_solicitada': False},
                }
            if self.cant_entregada and int(self.cant_entregada) > int(self.cant_solicitada):
                return {
                    'warning': {
                        'message': u'La cantidad de sellos solicitada no debe ser menor a la cantidad de sellos de calidad entregada'},
                    'value': {'cant_solicitada': False},
                }
            if int(self.cant_solicitada) == 0:
                return {
                    'warning': {'message': u'La cantidad solicitada, no debe ser cero'},
                    'value': {'cant_solicitada': False},
                }


class HemoredSerieLine(models.Model):
    _name = 'hemored.serie.line'
    _description = 'Serie de solicitud de Sellos de Calidad'

    serie = fields.Char(
        string='Serie'
    )
    num_inicio = fields.Char(
        string='Número de inicio'
    )
    num_fin = fields.Char(
        string='Número de fin'
    )
    solicitud_id = fields.Many2one(
        comodel_name='hemored.solicitud.line',
        string='Solicitud',
        ondelete='cascade'
    )
    is_generate = fields.Boolean(
        string='Generado'
    )

    def unlink(self):
        for serie in self:
            if serie.is_generate:
                raise ValidationError(_('No puede eliminar registros con sellos generados para la serie "%s" en el formulario') % serie.serie)
        return super(HemoredSerieLine, self).unlink()

    @api.one
    @api.constrains('num_inicio', 'num_fin')
    def _check_num_inicio_num_fin(self):
        domain = [
            ('id', '!=', self.id),
            ('serie', '=', self.serie),
            ('num_inicio', '=', self.num_inicio),
            ('num_fin', '=', self.num_fin),
        ]
        if self.search(domain, limit=1):
            raise ValidationError(_('Número de inicio %s y número de fin %s se esta duplicando para el expediente %s') % (self.num_inicio, self.num_fin, self.solicitud_id.num_expediente))

    @api.onchange('num_inicio')
    def _onchange_num_inicio(self):
        if self.num_inicio:
            if not self.num_inicio.isdigit():
                return {
                    'warning': {'message': u'El número de inicio, debe ser un número'},
                    'value': {'num_inicio': False},
                }
            if int(self.num_inicio) == 0:
                return {
                    'warning': {'message': u'El número de inicio, no debe ser cero'},
                    'value': {'num_inicio': False},
                }

    @api.onchange('num_fin')
    def _onchange_num_fin(self):
        if self.num_fin:
            if not self.num_fin.isdigit():
                return {
                    'warning': {'message': u'El número de fin, debe ser un número'},
                    'value': {'num_fin': False},
                }
            if self.num_inicio and int(self.num_fin) < int(self.num_inicio):
                return {
                    'warning': {'message': u'El numero de fin no debe ser menor al número de inicio'},
                    'value': {'num_fin': False},
                }
            if int(self.num_fin) == 0:
                return {
                    'warning': {'message': u'El número de fin, no debe ser cero'},
                    'value': {'num_fin': False},
                }

    @api.multi
    def action_crear_registros(self):
        list_componentes = ['globulos_rojos', 'plasma', 'plaquetas', 'crioprecipitado']
        for record in self:
            if not record.is_generate:
                for lc in list_componentes:
                    regitros_obj = self.env['hemored.sellos.calidad.registro'].search(
                        [
                            ('series_id', '=', record.id),
                            ('componente', '=', lc)
                        ],
                        limit=1
                    )
                    if not regitros_obj:
                        for n in range(int(record.num_inicio), int(record.num_fin) + 1, 1):
                            vals = {
                                'banco_id': record.solicitud_id.sellos_id.banco_id.id,
                                'diresa_id': record.solicitud_id.sellos_id.diresa_id.id,
                                'serie': record.serie,
                                'num_serie': n,
                                'series_id': record.id,
                                'componente': lc,
                                'estado_registro': constants.ACTIVO,
                            }
                            self.env['hemored.sellos.calidad.registro'].create(vals)
                record.is_generate = True
