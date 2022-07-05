# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError
from ..models import constants

MN_RecordDateSupervision = '.'.join([constants.MODULO, 'record_date_supervision'])
MN_RecordSupervision = '.'.join([constants.MODULO, 'record_supervision'])


class RecordDateSupervision(models.Model):
    _inherit = 'mail.thread'
    _name = MN_RecordDateSupervision
    _description = 'Registro de fechas de supervisión'
    _rec_name = 'banco_id'
    _order = 'fecha_registro asc'

    @api.model
    def _selection_tipo_banco(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_banco')

    @api.multi
    def _add_domain(self):
        domain = [
            ('diresa_id', '=', False),
            ('banco_id', '=', False),
        ]
        usuarios_ids = self.env['res.users'].search(domain)
        if usuarios_ids:
            domain = [('id', 'in', usuarios_ids.ids)]
        else:
            domain = [('id', '=', -1)]
        return domain

    fecha_registro = fields.Date(
        string='Fecha de registro',
        default=fields.Date.today
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS',
    )
    tipo_banco = fields.Selection(
        '_selection_tipo_banco',
        'Tipo de CHBS',
        related='banco_id.tipo_banco',
        store=True
    )
    fecha_realizacion = fields.Date(
        string='Fecha propuesta de supervisión',
    )
    fecha_ejecucion = fields.Date(
        string='Fecha de supervisión',
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsable asignado',
        domain=_add_domain,
    )
    observacion = fields.Text(
        string='Observación'
    )
    state = fields.Selection(
        constants.SELECTION_ESTADO_SUPERVISION_BANCO,
        string='Estado',
        default=constants.BORRADOR,
    )

    @api.one
    @api.constrains('fecha_realizacion')
    def _check_fecha_realizacion(self):
        domain = [
            ('id', '!=', self.id),
            ('banco_id', '=', self.banco_id.id),
            ('fecha_realizacion', '=', self.fecha_realizacion),
        ]
        if self.search(domain, limit=1):
            raise ValidationError('Solo puede haber un registro de supervisión para el mismo CHBS en la misma fecha')

    @api.onchange('fecha_realizacion')
    def _onchange_fecha_realizacion(self):
        if self.fecha_realizacion:
            if self.fecha_registro > self.fecha_realizacion:
                return {
                    'warning': {'message': u'La fecha de la realización de supervisión no debe ser menor a la de hoy'},
                    'value': {'fecha_realizacion': False},
                }

    @api.onchange('fecha_ejecucion')
    def _onchange_fecha_ejecucion(self):
        if self.fecha_ejecucion:
            if self.fecha_realizacion > self.fecha_ejecucion:
                return {
                    'warning': {'message': u'La fecha de la ejecución de supervisión no debe ser menor a la fecha de realización'},
                    'value': {'fecha_ejecucion': False},
                }

    @api.model
    def create(self, vals):
        res = super(RecordDateSupervision, self).create(vals)
        res.state = constants.PROPUESTO
        return res

    @api.multi
    def action_confirmar(self):
        self.ensure_one()
        form = self.env.ref('hemored_supervision.hemored_supervision_wizarconfirm_form_view', False)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Confirmar supervisión',
            'res_model': 'hemored_supervision.wizarconfirm',
            'views': [(form.id, 'form')],
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': form.id,
            'target': 'new',
        }

    @api.multi
    def action_postergar(self):
        self.ensure_one()
        form = self.env.ref('hemored_supervision.hemored_supervision_wizarpostponed_form_view', False)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Postergar supervisión',
            'res_model': 'hemored_supervision.wizarpostponed',
            'views': [(form.id, 'form')],
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': form.id,
            'target': 'new',
        }

    def action_record_supervision(self):
        self.ensure_one()
        if self.state in (constants.CONFIRMADO, constants.POSTERGADO):
            values = {
                'default_banco_id': self.banco_id.id,
                'default_fecha_supervision': self.fecha_ejecucion,
                'default_tipo_formulario': constants.SUPERVISION,
            }
            action = self.env.ref('hemored_supervision.hemored_supervision_action').read()[0]
            tree_view_id = self.env.ref('hemored_supervision.ecord_supervision_tree_view').id
            form_view_id = self.env.ref('hemored_supervision.record_supervision_form_view').id
            action['domain'] = [('banco_id', '=', self.banco_id.id),
                                ('tipo_formulario', '=', constants.SUPERVISION),
                                ('fecha_supervision', '=', self.fecha_ejecucion),
                                ]
            action['context'] = values
            action['views'] = [(tree_view_id, 'tree'), (form_view_id, 'form')]
            return action
        else:
            raise ValidationError('El estado del registro debe ser confirmado o postergado')


class RecordSupervision(models.Model):
    _inherit = 'mail.thread'
    _name = MN_RecordSupervision
    _description = 'Registro de supervisión'
    _rec_name = 'banco_id'
    _order = 'fecha_supervision asc'

    @api.model
    def _selection_tipo_banco(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_banco')

    fecha_supervision = fields.Date(
        string='Fecha de supervisión',
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS',
        track_visibility='onchange',
    )
    tipo_banco = fields.Selection(
        '_selection_tipo_banco',
        'Tipo de CHBS',
        related='banco_id.tipo_banco',
        store=True
    )
    dirrecion = fields.Char(
        string='Direccion del CHBS',
        related='banco_id.direccion',
        store=True
    )
    categoria = fields.Selection(
        string='Categoría',
        related='banco_id.renipress_id.categoria',
        store=True
    )
    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='Diresa',
        related='banco_id.diresa_id',
        store=True
    )
    telefono = fields.Char(
        string='Teléfono',
        related='banco_id.renipress_id.telefono',
        store=True
    )
    anexo = fields.Char(
        string='Anexo',
        related='banco_id.anexo',
        store=True
    )
    director = fields.Char(
        string='Director de EESS',
        related='banco_id.renipress_id.responsable',
        store=True
    )
    jefe_cbhs = fields.Char(
        string='Jefe de CHBS',
        related='banco_id.medico_coordinador_responsable',
        store=True
    )
    email_cbhs = fields.Char(
        string='Email de CHBS',
        related='banco_id.email',
        store=True
    )
    telefono_cbhs = fields.Char(
        string='Email de CHBS',
        related='banco_id.telefono',
        store=True
    )
    nombre_entrevistad = fields.Char(
        string='Nombre del entrevistado',
        track_visibility='onchange',
    )
    num_camas_cbhs = fields.Integer(
        string='Número de camas en el CHBS',
        related='banco_id.num_camas',
        store=True
    )
    hora_inicio = fields.Char(
        string='Hora inicio de supervisión',
        track_visibility='onchange',
    )
    hora_fin = fields.Char(
        string='Hora fin de supervisión',
        track_visibility='onchange',
    )
    responsable_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsable asignado',
        track_visibility='onchange',
    )
    observacion = fields.Text(
        string='Observación',
        track_visibility='onchange',
    )
    dia = fields.Date(
        string='Día'
    )
    hora = fields.Char(
        string='Hora'
    )
    state = fields.Selection(
        constants.SELECTION_ESTADO_FORMULARIO_SUPERVISION_BANCO,
        string='Estado',
        default=constants.BORRADOR,
        track_visibility='onchange',
    )
    tipo_formulario = fields.Selection(
        constants.SELECTION_TIPO_FORMULARIO,
        string='Tipo formulario',
    )

    @api.one
    @api.constrains('fecha_supervision')
    def _check_fecha_supervision(self):
        domain = [
            ('id', '!=', self.id),
            ('banco_id', '=', self.banco_id.id),
            ('fecha_supervision', '=', self.fecha_supervision),
            ('tipo_formulario', '=', constants.SUPERVISION),
        ]
        if self.search(domain, limit=1):
            raise ValidationError('Solo puede haber un registro por fecha de supervisión')

    @api.one
    def action_supervisar(self):
        self.state = constants.SUPERVISION

    @api.one
    def action_observar(self):
        self.state = constants.OBSERVADO

    def action_record_monitoreo(self):
        self.ensure_one()
        if self.state == constants.TERMINADO:
            values = {
                'default_banco_id': self.banco_id.id,
                'default_fecha_supervision': fields.Date.today(),
                'default_tipo_formulario': constants.MONITOREO,
            }
            action = self.env.ref('hemored_supervision.hemored_monitoreo_action').read()[0]
            tree_view_id = self.env.ref('hemored_supervision.ecord_monitoreo_tree_view').id
            form_view_id = self.env.ref('hemored_supervision.record_monitoreo_form_view').id
            action['domain'] = [('banco_id', '=', self.banco_id.id), ('tipo_formulario', '=', constants.MONITOREO)]
            action['context'] = values
            action['views'] = [(tree_view_id, 'tree'), (form_view_id, 'form')]
            return action
        else:
            raise ValidationError('El estado del registro debe ser Terminado')
