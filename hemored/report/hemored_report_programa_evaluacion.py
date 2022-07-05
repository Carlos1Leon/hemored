# -*- coding: utf-8 -*-

import io
import os
import tempfile

from openpyxl import load_workbook

from odoo import fields, api, models

from ..models import constants

MN_ReportProgramaEvaluacion = '.'.join([constants.MODULO, 'report_programa_evaluacion'])


class ReportProgramaEvaluacion(models.TransientModel):
    _name = MN_ReportProgramaEvaluacion
    _inherit = ['mail.thread']
    _rec_name = 'fecha_reporte'

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
    porc_vih = fields.Float(
        string='% de Bancos que participan en el programa de evaluación externo de calidad de tamizaje (VIH)',
    )
    porc_hbsag = fields.Float(
        string='% de Bancos que participan en el programa de evaluación externo de calidad de tamizaje (HBsAg)',
    )
    porc_hep_c = fields.Float(
        string='% de Bancos que participan en el programa de evaluación externo de calidad de tamizaje (Hep C)',
    )
    porc_anti_hbc = fields.Float(
        string='% de Bancos que participan en el programa de evaluación externo de calidad de tamizaje (Anti-HBc)',
    )
    porc_htlv_i_ii = fields.Float(
        string='% de Bancos que participan en el programa de evaluación externo de calidad de tamizaje (HTLV I/II)',
    )
    porc_sifilis = fields.Float(
        string='% de Bancos que participan en el programa de evaluación externo de calidad de tamizaje (Sifilis)',
    )
    porc_chagas = fields.Float(
        string='% de Bancos que participan en el programa de evaluación externo de calidad de tamizaje (Chagas)',
    )
    porc_otros = fields.Float(
        string='% de Bancos que participan en el programa de evaluación externo de calidad de tamizaje (Otros)',
    )

    @api.model
    def create(self, vals):
        res = super(ReportProgramaEvaluacion, self).create(vals)
        res.state = constants.REGISTRADO
        return res

    @api.one
    def action_generated(self):
        domain = [('tipo_banco', '=', '2')]
        bancos_ids = self.env['hemored.banco_sangre'].search(domain)
        cant_bancos_vih = bancos_ids.filtered(lambda l: l.select_mvih_s_o_n == 'S')
        cant_bancos_hbsag = bancos_ids.filtered(lambda l: l.select_mhbsag_s_o_n == 'S')
        cant_bancos_hepc = bancos_ids.filtered(lambda l: l.select_mhepc_s_o_n == 'S')
        cant_bancos_mantih = bancos_ids.filtered(lambda l: l.select_mantihbc_s_o_n == 'S')
        cant_bancos_mhtlv = bancos_ids.filtered(lambda l: l.select_mhtlv_s_o_n == 'S')
        cant_bancos_sifilis = bancos_ids.filtered(lambda l: l.select_msifilis_s_o_n == 'S')
        cant_bancos_chagas = bancos_ids.filtered(lambda l: l.select_mchagas_s_o_n == 'S')
        cant_bancos_otros = bancos_ids.filtered(lambda l: l.select_motros_s_o_n == 'S')
        self.update({
            'porc_vih': (len(cant_bancos_vih) / len(bancos_ids)) * 100,
            'porc_hbsag': (len(cant_bancos_hbsag) / len(bancos_ids)) * 100,
            'porc_hep_c': (len(cant_bancos_hepc) / len(bancos_ids)) * 100,
            'porc_anti_hbc': (len(cant_bancos_mantih) / len(bancos_ids)) * 100,
            'porc_htlv_i_ii': (len(cant_bancos_mhtlv) / len(bancos_ids)) * 100,
            'porc_sifilis': (len(cant_bancos_sifilis) / len(bancos_ids)) * 100,
            'porc_chagas': (len(cant_bancos_chagas) / len(bancos_ids)) * 100,
            'porc_otros': (len(cant_bancos_otros) / len(bancos_ids)) * 100,
            'state': constants.GENERADO,
        })

    @api.multi
    def print_excel_porcentaje(self):
        self.ensure_one()
        url = '/web/binary/download_export_porcentaje_programa_evaluacion?id={}&filename=Porcentaje_programa_evaluacion_externa.xlsx'.format(self.id)
        value = {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new'
        }
        return value

    @api.multi
    def action_export_excel(self):
        archivo = 'PROGRAMA_EVALUACION.xlsx'
        ruta = '{}/../documents/{}'.format(os.path.dirname(os.path.abspath(__file__)), archivo)
        book = load_workbook(ruta)
        fobj = tempfile.NamedTemporaryFile(suffix='.xlsx', dir='/tmp/', delete=False)
        fname = fobj.name
        fobj.close()

        w_sheet = book.get_sheet_by_name('FORMATO PORCENAJTE')
        w_sheet['D3'] = self.fecha_reporte or ''
        w_sheet['F3'] = self.porc_vih or 0.0
        w_sheet['F4'] = self.porc_hbsag or 0.0
        w_sheet['F5'] = self.porc_hep_c or 0.0
        w_sheet['F6'] = self.porc_anti_hbc or 0.0
        w_sheet['F7'] = self.porc_htlv_i_ii or 0.0
        w_sheet['F8'] = self.porc_sifilis or 0.0
        w_sheet['F9'] = self.porc_chagas or 0.0
        w_sheet['F10'] = self.porc_otros or 0.0

        fname = io.BytesIO()
        book.save(fname)
        fname.seek(0)
        data = fname.read()
        fname.close()
        return data
