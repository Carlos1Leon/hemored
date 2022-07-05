# -*- coding: utf-8 -*-

import io
import os
import tempfile

from openpyxl import load_workbook

from odoo import fields, api, models

from ..models import constants

MN_ReportEstadoFicha = '.'.join([constants.MODULO, 'report_estado_ficha'])


class ReportEstadoFicha(models.TransientModel):
    _name = MN_ReportEstadoFicha
    _inherit = ['mail.thread']
    _rec_name = 'fecha_reporte'

    anho_id = fields.Many2one(
        comodel_name='minsa.anho',
        string='Año',
        track_visibility='onchange',
    )
    periodo_ids = fields.Many2many(
        comodel_name='minsa.periodo',
        string='Periodo',
        track_visibility='onchange',
    )
    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='DIRIS/DIRESA/GERESA',
        track_visibility='onchange',
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='Banco',
        track_visibility='onchange',
    )
    tipo_banco = fields.Selection(
        '_selection_tipo_banco',
        'Tipo',
        track_visibility='onchange',
    )
    fecha_reporte = fields.Date(
        string='Fecha de reporte',
        track_visibility='onchange',
        default=fields.Date.today
    )
    state = fields.Selection(
        string='Estado',
        selection=constants.SELECTION_ESTADO_REPORTE,
        default=constants.BORRADOR,
        track_visibility='onchange'
    )
    porc_fichas_borrador = fields.Float(
        string='% de fichas en borrador',
    )
    porc_fichas_enviadas = fields.Float(
        string='% de fichas en enviadas',
    )
    porc_fichas_validadas = fields.Float(
        string='% de fichas en validadas',
    )

    @api.model
    def _selection_tipo_banco(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_banco')

    @api.model
    def create(self, vals):
        res = super(ReportEstadoFicha, self).create(vals)
        res.state = constants.REGISTRADO
        return res

    @api.one
    def action_generated(self):
        domain = []
        if self.anho_id and self.periodo_ids and self.diresa_id and self.tipo_banco:
            domain = [('anho_id', '=', self.anho_id.id), ('periodo_id', 'in', self.periodo_ids.ids), ('diresa_id', '=', self.diresa_id.id), ('tipo_banco', '=', self.tipo_banco)]
        elif self.anho_id and self.periodo_ids and self.diresa_id and self.banco_id:
            domain = [('anho_id', '=', self.anho_id.id), ('periodo_id', 'in', self.periodo_ids.ids), ('diresa_id', '=', self.diresa_id.id), ('banco_id', '=', self.banco_id.id)]
        elif self.anho_id and self.periodo_ids and self.diresa_id:
            domain = [('anho_id', '=', self.anho_id.id), ('periodo_id', 'in', self.periodo_ids.ids), ('diresa_id', '=', self.diresa_id.id)]
        elif self.anho_id and self.diresa_id and self.banco_id:
            domain = [('anho_id', '=', self.anho_id.id), ('diresa_id', '=', self.diresa_id.id), ('banco_id', '=', self.banco_id.id)]
        elif self.anho_id and self.periodo_ids:
            domain = [('anho_id', '=', self.anho_id.id), ('periodo_id', 'in', self.periodo_ids.ids)]
        elif self.anho_id and self.diresa_id:
            domain = [('anho_id', '=', self.anho_id.id), ('diresa_id', '=', self.diresa_id.id)]
        elif self.anho_id:
            domain = [('anho_id', '=', self.anho_id.id)]
        fichas_ids = self.env['hemored.ficha_estadistica'].search(domain)
        lista_fichas_borrador_filter = fichas_ids.filtered(lambda l: l.state == 'borrador')
        lista_fichas_enviadas_filter = fichas_ids.filtered(lambda l: l.state == 'enviado')
        lista_fichas_validad_filter = fichas_ids.filtered(lambda l: l.state == 'validado')
        self.update({
            'porc_fichas_borrador': (len(lista_fichas_borrador_filter) / len(fichas_ids)) * 100,
            'porc_fichas_enviadas': (len(lista_fichas_enviadas_filter) / len(fichas_ids)) * 100,
            'porc_fichas_validadas': (len(lista_fichas_validad_filter) / len(fichas_ids)) * 100,
            'state': constants.GENERADO,
        })

    @api.multi
    def print_excel_porcentaje(self):
        self.ensure_one()
        url = '/web/binary/download_export_porcentaje_ficha?id={}&filename=Estado_de_fichas_estadisticas.xlsx'.format(self.id)
        value = {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new'
        }
        return value

    @api.multi
    def action_export_excel(self):
        archivo = 'PORCENTAJE.xlsx'
        ruta = '{}/../documents/{}'.format(os.path.dirname(os.path.abspath(__file__)), archivo)
        book = load_workbook(ruta)
        fobj = tempfile.NamedTemporaryFile(suffix='.xlsx', dir='/tmp/', delete=False)
        fname = fobj.name
        fobj.close()

        name_periodo = []
        for periodo in self.periodo_ids:
            name_periodo.append(periodo.name)

        w_sheet = book.get_sheet_by_name('FORMATO PORCENAJTE')
        w_sheet['D3'] = self.anho_id.name or ''
        w_sheet['D4'] = str(name_periodo) or ''
        w_sheet['D5'] = self.diresa_id.name or ''
        w_sheet['D6'] = self.banco_id.name or ''
        w_sheet['D7'] = self.tipo_banco or ''
        w_sheet['G3'] = self.porc_fichas_borrador
        w_sheet['G4'] = self.porc_fichas_enviadas
        w_sheet['G5'] = self.porc_fichas_validadas

        fname = io.BytesIO()
        book.save(fname)
        fname.seek(0)
        data = fname.read()
        fname.close()
        return data
