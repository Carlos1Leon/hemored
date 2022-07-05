# coding: utf-8

from datetime import datetime, timedelta

from odoo import fields, models, api
from odoo.exceptions import ValidationError

from ..models import constants


class HemoredWizardEliminacionSellos(models.TransientModel):
    _name = 'hemored.wizard.eliminacion.sellos'

    lines_ids = fields.One2many(
        comodel_name='hemored.wizard.eliminacion.sellos.line',
        inverse_name='eliminacion_id',
        default=lambda self: self._default_lines(),
        string='Lineas'
    )

    def _default_lines(self):
        active_ids = self._context.get('active_ids')
        list_detalles = []
        for active_id in active_ids:
            registro_id = self.env['hemored.sellos.calidad.registro'].browse(active_id)
            if registro_id.estado_registro == constants.ACTIVO:
                list_detalles.append([0, False, {
                    'eliminacion_id': self.id,
                    'registro_id': active_id,
                    'banco_id': registro_id.banco_id.id,
                    'serie': registro_id.serie,
                    'num_serie': registro_id.num_serie,
                    'componente': registro_id.componente,
                }])
        return list_detalles

    @api.multi
    def action_delete(self):
        self.ensure_one()
        for record in self.lines_ids:
            if record.registro_id.estado_registro == constants.ACTIVO:
                if record.num_unidad and record.grupo_sanguineo:
                    record.registro_id.num_unidad = record.num_unidad
                    record.registro_id.grupo_sanguineo = record.grupo_sanguineo
                    record.registro_id.estado_registro = constants.ELIMINADO
            else:
                raise ValidationError('No se puede eliminar registros con estado eliminado, (la ventana emergente se limpiara luego de esta acción)')


class HemoredWizardEliminacionSelloLine(models.TransientModel):
    _name = 'hemored.wizard.eliminacion.sellos.line'

    eliminacion_id = fields.Many2one(
        comodel_name='hemored.wizard.eliminacion.sellos',
        string='Eliminación de sello'
    )
    registro_id = fields.Many2one(
        comodel_name='hemored.sellos.calidad.registro',
        string='Registro de sello'
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS'
    )
    serie = fields.Char(
        string='Serie'
    )
    num_serie = fields.Char(
        string='Número de inicio'
    )
    componente = fields.Selection(
        string='Componente',
        selection=constants.SELECTION_COMPONENTES_SELLOS,
    )
    num_unidad = fields.Char(
        string='Número de unidad'
    )
    grupo_sanguineo = fields.Selection(
        string='Grupo sanguineo',
        selection=constants.SELECTION_GRUPOSANGUINEO,
    )


class HemoredEliminacionSellosActa(models.TransientModel):
    _name = 'hemored.eliminacion.sellos.acta'

    lines_ids = fields.One2many(
        comodel_name='hemored.eliminacion.sellos.acta.line',
        inverse_name='eliminacion_id',
        default=lambda self: self._default_lines(),
        string='Lineas'
    )

    def _default_lines(self):
        active_ids = self._context.get('active_ids')
        list_detalles = []
        for active_id in active_ids:
            registro_id = self.env['hemored.sellos.calidad.registro'].browse(active_id)
            list_detalles.append([0, False, {
                'eliminacion_id': self.id,
                'registro_id': active_id,
                'banco_id': registro_id.banco_id.id,
                'serie': registro_id.serie,
                'num_serie': registro_id.num_serie,
                'componente': registro_id.componente,
                'num_unidad': registro_id.num_unidad,
                'grupo_sanguineo': registro_id.grupo_sanguineo,
            }])
        return list_detalles

    def set_register(self):
        """Call when button 'Get Report' clicked."""
        fecha_ini = datetime.now() - timedelta(hours=5)
        hora = fecha_ini.time().strftime("%H:%M")
        dia_f = fields.Datetime.to_datetime(fecha_ini)
        dia = dia_f.day
        fecha = str(fecha_ini)
        mes = fecha[5:7]
        mes_f = constants.MONTH[mes]
        anio = fecha[:4]
        list_datos = []
        componente_name = ''
        for line in self.lines_ids:
            if line.registro_id.estado_registro == constants.ELIMINADO:
                line.registro_id.acta = True
                if line.registro_id.componente == constants.PLASMA:
                    componente_name = 'Plasma'
                elif line.registro_id.componente == constants.PLAQUETAS:
                    componente_name = 'Plaquetas'
                elif line.registro_id.componente == constants.CRIOPRECIPITADO:
                    componente_name = 'Crioprecipitado'
                elif line.registro_id.componente == constants.GLOBULOS_ROJOS:
                    componente_name = 'Globulos rojos'
                val = {
                    'num_unidad': line.registro_id.num_unidad,
                    'serie': line.registro_id.serie + line.registro_id.num_serie,
                    'componente': componente_name,
                    'grupo_sanguineo': line.registro_id.grupo_sanguineo,
                }
                list_datos.append(val)
        if list_datos:
            data = {
                'ids': self.ids,
                'model': self._name,
                'dia': str(dia),
                'mes': mes_f,
                'año': anio,
                'hora': hora,
                'responsable': self.env.user.banco_id.medico_coordinador_responsable,
                'establecimiento': self.env.user.banco_id.name,
                'datos': list_datos,
            }
            return self.env.ref('hemored_sellos_calidad.action_report_hemored_acta').report_action(self, data=data)
        else:
            raise ValidationError('No se puede generar acta de registros con estado activo, (la ventana emergente se limpiara luego de esta acción)')


class HemoredEliminacionSelloActaLine(models.TransientModel):
    _name = 'hemored.eliminacion.sellos.acta.line'

    eliminacion_id = fields.Many2one(
        comodel_name='hemored.eliminacion.sellos.acta',
        string='Eliminación de sello'
    )
    registro_id = fields.Many2one(
        comodel_name='hemored.sellos.calidad.registro',
        string='Registro de sello'
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS'
    )
    serie = fields.Char(
        string='Serie'
    )
    num_serie = fields.Char(
        string='Número de inicio'
    )
    componente = fields.Selection(
        string='Componente',
        selection=constants.SELECTION_COMPONENTES_SELLOS,
    )
    num_unidad = fields.Char(
        string='Número de unidad'
    )
    grupo_sanguineo = fields.Selection(
        string='Grupo sanguineo',
        selection=constants.SELECTION_GRUPOSANGUINEO,
    )
