# coding: utf-8

import io
import datetime

from odoo import fields, models, api
from odoo.tools.misc import xlwt


class ExcelReportSellos(models.TransientModel):
    _name = 'stock_sellos.report_excel'

    anho_id = fields.Many2one(
        comodel_name='minsa.anho',
        string='Año',
    )
    periodo_inicio_id = fields.Many2one(
        comodel_name='minsa.periodo',
        string='Periodo inicio',
    )
    periodo_fin_id = fields.Many2one(
        comodel_name='minsa.periodo',
        string='Periodo fin',
    )
    consolidated = fields.Boolean(
        string='Consolidado',
    )
    is_period = fields.Boolean(
        string='Periodo'
    )
    date_start = fields.Date(
        string='Fecha inicio'
    )
    date_stop = fields.Date(
        string='Fecha fin'
    )

    @api.onchange('is_period')
    def _onchange_is_period(self):
        if self.is_period:
            self.date_start = False
            self.date_stop = False
        else:
            self.anho_id = False
            self.periodo_inicio_id = False
            self.periodo_fin_id = False

    @api.onchange('periodo_inicio_id')
    def _onchange_periodo_inicio_id(self):
        if self.periodo_inicio_id and self.periodo_fin_id:
            if self.periodo_inicio_id.date_start > self.periodo_fin_id.date_stop:
                return {
                    'warning': {'message': u'El periodo de inicio no debe ser mayor al periodo fin'},
                    'value': {'periodo_inicio_id': False},
                }

    @api.onchange('periodo_fin_id')
    def _onchange_periodo_fin_id(self):
        if self.periodo_inicio_id and self.periodo_fin_id:
            if self.periodo_inicio_id.date_start > self.periodo_fin_id.date_stop:
                return {
                    'warning': {'message': u'El periodo de fin no debe ser menor al periodo inicio'},
                    'value': {'periodo_fin_id': False},
                }

    @api.onchange('date_start')
    def _onchange_date_start(self):
        if self.date_start and self.date_stop:
            if self.date_start > self.date_stop:
                return {
                    'warning': {'message': u'La fecha inicio no debe ser mayor a la fecha de fin'},
                    'value': {'date_start': False},
                }

    @api.onchange('date_stop')
    def _onchange_date_stop(self):
        if self.date_start and self.date_stop:
            if self.date_start > self.date_stop:
                return {
                    'warning': {'message': u'La fecha inicio no debe ser mayor a la fecha de fin'},
                    'value': {'date_stop': False},
                }

    @api.multi
    def print_excel(self):
        self.ensure_one()
        if self.periodo_inicio_id and self.periodo_fin_id:
            mes_i = self.periodo_inicio_id.name
            mes_f = self.periodo_fin_id.name
        elif self.periodo_inicio_id and not self.periodo_fin_id:
            mes_i = self.periodo_inicio_id.name
            mes_f = self.periodo_inicio_id.name
        elif self.date_start and self.date_stop:
            mes_i = self.date_start
            mes_f = self.date_stop
        date = datetime.datetime.now() - datetime.timedelta(hours=5)
        url = '/web/binary/download_export_stock_sellos?id={}&filename=Inicio_{}_fin_{}_consolidado_sellos_de_calidad_entregados_{}.xls'.format(self.id, mes_i, mes_f, date)
        value = {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new'
        }
        return value

    def generate_xlsx_report(self):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Sheet 1')

        xlwt.add_palette_colour('custom_colour', 0x21)
        workbook.set_colour_RGB(0x21, 68, 114, 196)

        style0 = xlwt.easyxf(
            'font: height 200, name Calibri, colour_index black; borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;'
        )
        style1 = xlwt.easyxf(
            'font: height 200, name Calibri, colour_index white;pattern: pattern solid, fore_colour custom_colour; align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;'
        )
        style1_1 = xlwt.easyxf(
            'font: height 200, name Calibri, colour_index white;pattern: pattern solid, fore_colour custom_colour; align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;'
        )
        date_style = xlwt.easyxf(
            'font: height 200, name Calibri, colour_index black; borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;',
            num_format_str='DD/MM/YYYY'
        )

        s0_t = 1
        s2 = 3
        s3 = 4
        s4 = 6
        s5 = 7

        worksheet.write_merge(s0_t, s0_t, 1, 10, u'CONSOLIDADO DE SELLOS DE CALIDAD ENTREGADOS', style1)
        if self.is_period:
            worksheet.write_merge(s2, s2, 1, 2, u'Año', style1_1)
            worksheet.write_merge(s3, s3, 1, 2, u'Periodo inicio', style1_1)
            worksheet.write(s3, 5, u'Periodo fin', style1_1)

            worksheet.write(s2, 3, self.anho_id.code, style0)
            worksheet.write(s3, 3, self.periodo_inicio_id.code, style0)
            worksheet.write(s3, 6, self.periodo_fin_id.code or self.periodo_inicio_id.code, style0)
        else:
            worksheet.write_merge(s2, s2, 1, 2, u'Año', style1_1)
            worksheet.write_merge(s3, s3, 1, 2, u'Fecha inicio', style1_1)
            worksheet.write(s3, 5, u'Fecha fin', style1_1)

            worksheet.write(s2, 3, fields.Date.from_string(self.date_start).year, style0)
            worksheet.write(s3, 3, self.date_start, date_style)
            worksheet.write(s3, 6, self.date_stop, date_style)

        if self.is_period and self.periodo_inicio_id and self.periodo_fin_id:
            domain_period = [
                ('fecha_entrega', '>', fields.Date.from_string(self.periodo_inicio_id.date_start)),
                ('fecha_entrega', '<', fields.Date.from_string(self.periodo_fin_id.date_stop)),
            ]
        elif self.is_period and self.periodo_inicio_id and not self.periodo_fin_id:
            domain_period = [
                ('fecha_entrega', '>=', fields.Date.from_string(self.periodo_inicio_id.date_start)),
                ('fecha_entrega', '<=', fields.Date.from_string(self.periodo_inicio_id.date_stop)),
            ]
        elif not self.is_period and self.date_start and self.date_stop:
            domain_period = [
                ('fecha_entrega', '>=', fields.Date.from_string(self.date_start)),
                ('fecha_entrega', '<=', fields.Date.from_string(self.date_stop)),
            ]

        if self.consolidated:
            valores = self.env['hemored.solicitud.line'].search(domain_period)
            suma = round(sum(int(line.cant_entregada) for line in valores))

            worksheet.write_merge(s4, s4, 1, 2, u'Total de sellos entregados', style1_1)
            worksheet.write(s4, 3, suma or 0, style0)
        else:
            worksheet.col(1).width = 11000
            worksheet.write_merge(s4, s4, 1, 2, u'Banco de Sangre', style1_1)
            worksheet.write_merge(s4, s4, 3, 4, u'Fecha de solicitud', style1_1)
            worksheet.write_merge(s4, s4, 5, 6, u'Número de expediente', style1_1)
            worksheet.write_merge(s4, s4, 7, 8, u'Fecha de entrega', style1_1)
            worksheet.write_merge(s4, s4, 9, 10, u'Cantidad entregada', style1_1)
            line_ids = self.env['hemored.solicitud.line'].search(domain_period)
            for line in line_ids:
                worksheet.write_merge(s5, s5, 1, 2, line.sellos_id.banco_id.name, style0)
                worksheet.write_merge(s5, s5, 3, 4, line.fecha_solicitud, date_style)
                worksheet.write_merge(s5, s5, 5, 6, line.num_expediente, style0)
                worksheet.write_merge(s5, s5, 7, 8, line.fecha_entrega, date_style)
                worksheet.write_merge(s5, s5, 9, 10, line.cant_entregada, style0)

                s5 += 1

        file_data = io.BytesIO()
        workbook.save(file_data)
        file_data.seek(0)
        data = file_data.read()
        file_data.close()
        return data
