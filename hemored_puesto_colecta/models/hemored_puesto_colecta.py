# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

from ..models import constants


class PuestoColecta(models.Model):
    _inherit = 'mail.thread'
    _name = 'hemored_puesto_colecta.puesto'
    _description = 'Puesto de colecta'

    name = fields.Char(
        string='Nombre del Puesto de Colecta',
        required=True
    )
    direccion = fields.Char(
        string='Dirección del Puesto de Colecta',
        required=True
    )
    diresa_id = fields.Many2many(
        'renipress.diresa',
        'puesto_diresa_rel',
        'puesto_id',
        'diresa_id',
        'Diresa',
        required=True
    )
    fecha_inicio = fields.Date(
        string='Fecha de Inicio',
        store=True,
        required=True
    )
    fecha_fin = fields.Date(
        string='Fecha de Fin',
        store=True,
        required=True
    )
    lunes_banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='Bancos de sangre'
    )
    lunes_fecha_inicio = fields.Date(
        string='Fecha de Inicio',
        store=True
    )
    lunes_fecha_fin = fields.Date(
        string='Fecha de Fin',
        store=True
    )
    lunes_estado = fields.Selection(
        constants.SELECTION_ESTADO_PUESTO_DE_COLECTA,
        string='Estado',
        default=constants.CERRADO
    )
    martes_banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='Bancos de sangre'
    )
    martes_fecha_inicio = fields.Date(
        string='Fecha de Inicio',
        store=True
    )
    martes_fecha_fin = fields.Date(
        string='Fecha de Fin',
        store=True
    )
    martes_estado = fields.Selection(
        constants.SELECTION_ESTADO_PUESTO_DE_COLECTA,
        string='Estado',
        default=constants.CERRADO
    )
    miercoles_banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='Bancos de sangre'
    )
    miercoles_fecha_inicio = fields.Date(
        string='Fecha de Inicio',
        store=True
    )
    miercoles_fecha_fin = fields.Date(
        string='Fecha de Fin',
        store=True
    )
    miercoles_estado = fields.Selection(
        constants.SELECTION_ESTADO_PUESTO_DE_COLECTA,
        string='Estado',
        default=constants.CERRADO
    )
    jueves_banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='Bancos de sangre'
    )
    jueves_fecha_inicio = fields.Date(
        string='Fecha de Inicio',
        store=True
    )
    jueves_fecha_fin = fields.Date(
        string='Fecha de Fin',
        store=True
    )
    jueves_estado = fields.Selection(
        constants.SELECTION_ESTADO_PUESTO_DE_COLECTA,
        string='Estado',
        default=constants.CERRADO
    )
    viernes_banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='Bancos de sangre'
    )
    viernes_fecha_inicio = fields.Date(
        string='Fecha de Inicio',
        store=True
    )
    viernes_fecha_fin = fields.Date(
        string='Fecha de Fin',
        store=True
    )
    viernes_estado = fields.Selection(
        constants.SELECTION_ESTADO_PUESTO_DE_COLECTA,
        string='Estado',
        default=constants.CERRADO
    )
    sabado_banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='Bancos de sangre'
    )
    sabado_fecha_inicio = fields.Date(
        string='Fecha de Inicio',
        store=True
    )
    sabado_fecha_fin = fields.Date(
        string='Fecha de Fin',
        store=True
    )
    sabado_estado = fields.Selection(
        constants.SELECTION_ESTADO_PUESTO_DE_COLECTA,
        string='Estado',
        default=constants.CERRADO
    )
    estado = fields.Selection(
        constants.SELECTION_ESTADO_PUESTO_DE_COLECTA,
        string='Estado',
        default=constants.ACTIVO
    )

    @api.one
    def action_close(self):
        self.estado = constants.CERRADO

    @api.one
    def action_reopen(self):
        self.estado = constants.ACTIVO

    @api.one
    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fecha(self):
        if self.fecha_inicio and self.fecha_fin and self.fecha_inicio > self.fecha_fin:
            raise ValidationError('Fecha de Finalización no puede ser menor a Fecha de Inicio')

    @api.one
    @api.constrains('fecha_inicio', 'fecha_fin', 'lunes_fecha_inicio', 'lunes_fecha_fin')
    def _check_fecha_lunes(self):
        if self.fecha_inicio and self.lunes_fecha_inicio and self.fecha_inicio > self.lunes_fecha_inicio:
            raise ValidationError('Fecha de inicio del día Lunes no puede ser mayor a la fecha de Apertura del Puesto de Colecta')
        if self.fecha_fin and self.lunes_fecha_fin and self.fecha_fin < self.lunes_fecha_fin:
            raise ValidationError('Fecha de finalización del día Lunes no puede ser mayor a la fecha de Cierre del Puesto de Colecta')

    @api.one
    @api.constrains('fecha_inicio', 'fecha_fin', 'martes_fecha_inicio', 'martes_fecha_fin')
    def _check_fecha_martes(self):
        if self.fecha_inicio and self.martes_fecha_inicio and self.fecha_inicio > self.martes_fecha_inicio:
            raise ValidationError('Fecha de inicio del día Martes no puede ser mayor a la fecha de Apertura del Puesto de Colecta')
        if self.fecha_fin and self.martes_fecha_fin and self.fecha_fin < self.martes_fecha_fin:
            raise ValidationError('Fecha de finalización del día Martes no puede ser mayor a la fecha de Cierre del Puesto de Colecta')

    @api.one
    @api.constrains('fecha_inicio', 'fecha_fin', 'miercoles_fecha_inicio', 'miercoles_fecha_fin')
    def _check_fecha_miercoles(self):
        if self.fecha_inicio and self.miercoles_fecha_inicio and self.fecha_inicio > self.miercoles_fecha_inicio:
            raise ValidationError('Fecha de inicio del día Miercoles no puede ser mayor a la fecha de Apertura del Puesto de Colecta')
        if self.fecha_fin and self.miercoles_fecha_fin and self.fecha_fin < self.miercoles_fecha_fin:
            raise ValidationError('Fecha de finalización del día Miercoles no puede ser mayor a la fecha de Cierre del Puesto de Colecta')

    @api.one
    @api.constrains('fecha_inicio', 'fecha_fin', 'jueves_fecha_inicio', 'jueves_fecha_fin')
    def _check_fecha_jueves(self):
        if self.fecha_inicio and self.jueves_fecha_inicio and self.fecha_inicio > self.jueves_fecha_inicio:
            raise ValidationError('Fecha de inicio del día Jueves no puede ser mayor a la fecha de Apertura del Puesto de Colecta')
        if self.fecha_fin and self.jueves_fecha_fin and self.fecha_fin < self.jueves_fecha_fin:
            raise ValidationError('Fecha de finalización del día Jueves no puede ser mayor a la fecha de Cierre del Puesto de Colecta')

    @api.one
    @api.constrains('fecha_inicio', 'fecha_fin', 'viernes_fecha_inicio', 'viernes_fecha_fin')
    def _check_fecha_viernes(self):
        if self.fecha_inicio and self.viernes_fecha_inicio and self.fecha_inicio > self.viernes_fecha_inicio:
            raise ValidationError('Fecha de inicio del día Viernes no puede ser mayor a la fecha de Apertura del Puesto de Colecta')
        if self.fecha_fin and self.viernes_fecha_fin and self.fecha_fin < self.viernes_fecha_fin:
            raise ValidationError('Fecha de finalización del día Viernes no puede ser mayor a la fecha de Cierre del Puesto de Colecta')

    @api.one
    @api.constrains('fecha_inicio', 'fecha_fin', 'sabado_fecha_inicio', 'sabado_fecha_fin')
    def _check_fecha_sabado(self):
        if self.fecha_inicio and self.sabado_fecha_inicio and self.fecha_inicio > self.sabado_fecha_inicio:
            raise ValidationError('Fecha de inicio del día Sabado no puede ser mayor a la fecha de Apertura del Puesto de Colecta')
        if self.fecha_fin and self.sabado_fecha_fin and self.fecha_fin < self.sabado_fecha_fin:
            raise ValidationError('Fecha de finalización del día Sabado no puede ser mayor a la fecha de Cierre del Puesto de Colecta')

    @api.model
    def _verificar_fecha(self):
        for obj in self.env['hemored_puesto_colecta.puesto'].search([]):
            obj.action_vencimiento()
        return True

    @api.one
    def action_vencimiento(self):
        fecha_hoy = fields.Date.today()
        if self.estado == constants.ACTIVO:
            if self.fecha_fin and self.fecha_fin <= fecha_hoy:
                self.estado = constants.VENCIDO
            elif self.lunes_fecha_fin and self.lunes_fecha_fin <= fecha_hoy:
                self.lunes_estado = constants.VENCIDO
            elif self.martes_fecha_fin and self.martes_fecha_fin <= fecha_hoy:
                self.martes_estado = constants.VENCIDO
            elif self.miercoles_fecha_fin and self.miercoles_fecha_fin <= fecha_hoy:
                self.miercoles_estado = constants.VENCIDO
            elif self.jueves_fecha_fin and self.jueves_fecha_fin <= fecha_hoy:
                self.jueves_estado = constants.VENCIDO
            elif self.viernes_fecha_fin and self.viernes_fecha_fin <= fecha_hoy:
                self.viernes_estado = constants.VENCIDO
            elif self.sabado_fecha_fin and self.sabado_fecha_fin <= fecha_hoy:
                self.sabado_estado = constants.VENCIDO

    @api.model
    def _generar_ficha_puesto_colecta(self):
        for obj in self.env['hemored_puesto_colecta.puesto'].search([('estado', '=', constants.ACTIVO)]):
            obj.action_generar_ficha()
        return True

    @api.one
    def action_generar_ficha(self):
        fecha_hoy = fields.Date.today()
        list_vals = []
        if self.lunes_estado and self.lunes_estado == constants.ACTIVO and fecha_hoy.weekday() == 0:
            vals = {
                'hemored_puesto_colecta_id': self.id,
                'banco_id': self.lunes_banco_id.id,
                'diresa_id': self.lunes_banco_id.renipress_id.diresa_id.id,
                'fecha_ficha': fecha_hoy,
            }
            list_vals.append(vals)
        if self.martes_estado and self.martes_estado == constants.ACTIVO and fecha_hoy.weekday() == 1:
            vals = {
                'hemored_puesto_colecta_id': self.id,
                'banco_id': self.martes_banco_id.id,
                'diresa_id': self.martes_banco_id.renipress_id.diresa_id.id,
                'fecha_ficha': fecha_hoy,
            }
            list_vals.append(vals)
        if self.miercoles_estado and self.miercoles_estado == constants.ACTIVO and fecha_hoy.weekday() == 2:
            vals = {
                'hemored_puesto_colecta_id': self.id,
                'banco_id': self.miercoles_banco_id.id,
                'diresa_id': self.miercoles_banco_id.renipress_id.diresa_id.id,
                'fecha_ficha': fecha_hoy,
            }
            list_vals.append(vals)
        if self.jueves_estado and self.jueves_estado == constants.ACTIVO and fecha_hoy.weekday() == 3:
            vals = {
                'hemored_puesto_colecta_id': self.id,
                'banco_id': self.jueves_banco_id.id,
                'diresa_id': self.jueves_banco_id.renipress_id.diresa_id.id,
                'fecha_ficha': fecha_hoy,
            }
            list_vals.append(vals)
        if self.viernes_estado and self.viernes_estado == constants.ACTIVO and fecha_hoy.weekday() == 4:
            vals = {
                'hemored_puesto_colecta_id': self.id,
                'banco_id': self.viernes_banco_id.id,
                'diresa_id': self.viernes_banco_id.renipress_id.diresa_id.id,
                'fecha_ficha': fecha_hoy,
            }
            list_vals.append(vals)
        if self.sabado_estado and self.sabado_estado == constants.ACTIVO and fecha_hoy.weekday() == 5:
            vals = {
                'hemored_puesto_colecta_id': self.id,
                'banco_id': self.sabado_banco_id.id,
                'diresa_id': self.sabado_banco_id.renipress_id.diresa_id.id,
                'fecha_ficha': fecha_hoy,
            }
            list_vals.append(vals)
        for vals in list_vals:
            self.env['hemored_puesto_colecta.ficha'].create(vals)
