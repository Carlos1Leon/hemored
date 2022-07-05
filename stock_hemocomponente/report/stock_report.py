# coding: utf-8

import io
from odoo import fields, models, api
from odoo.tools.misc import xlwt


class ExcelReport(models.TransientModel):
    _name = 'stock_hemocomponente.report_excel'

    fecha = fields.Date(
        string='Fecha',
        default=fields.Date.context_today
    )

    @api.onchange('fecha')
    def _onchange_fecha(self):
        if self.fecha:
            if self.fecha > fields.Date.context_today(self):
                return {
                    'warning': {'message': u'La fecha no debe ser mayor a la de hoy'},
                    'value': {'fecha': False},
                }

    @api.multi
    def print_excel(self):
        self.ensure_one()
        url = '/web/binary/download_export_stock?id={}&filename=consolidado_diario_{}_stock_hemocomponentes.xls'.format(self.id, self.fecha)
        value = {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new'
        }
        return value

    def generate_xlsx_report(self):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Sheet 1')

        xlwt.add_palette_colour("custom_colour", 0x21)
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

        s0_t = 0
        s0 = 1
        s1 = 2
        s2 = 3
        s3 = 4
        worksheet.col(0).width = 5000
        worksheet.col(1).width = 10500
        worksheet.col(21).width = 10000
        worksheet.col(22).width = 15000
        worksheet.col(23).width = 10000
        worksheet.col(24).width = 15000
        worksheet.col(25).width = 10000
        worksheet.col(26).width = 10000
        worksheet.col(27).width = 10000

        worksheet.write_merge(s0_t, s0_t, 7, 20, u'CONSOLIDADO DIARIO STOCK DE HEMOCOMPONENTES', style1)
        worksheet.write_merge(s0, s0, 0, 27, u'STOCK DE HEMOCOMPONENTES', style1)
        worksheet.write_merge(s1, s1, 3, 11, u'PAQUETE GLOBULAR', style1)
        worksheet.write_merge(s1, s1, 12, 20, u'PLASMA FRESCO CONGELADO ', style1)
        worksheet.write(s1, 21, u'TOTAL DE PLAQUETAS SIMPLES', style1)
        worksheet.write(s1, 22, u'TOTAL DE CONCENTRADO DE PLAQUETAS POR AFÉRESIS', style1)
        worksheet.write(s1, 23, u'TOTAL DE CRIOPRECIPITADO', style1)
        worksheet.write(s1, 24, u'TOTAL DE UNIDADES PENDIENTES DE TAMIZAJE', style1)
        worksheet.write(s1, 25, u'DONACIONES DE SANGRE / DÍA', style1)
        worksheet.write(s1, 26, u'TRANSFUSIONES DE P.GLOB./ DÍA', style1)
        worksheet.write(s1, 27, u'TRANSFUSIONES PLAQUETAS', style1)
        worksheet.write_merge(2, 3, 0, 0, u'REGION', style1)
        worksheet.write_merge(2, 3, 1, 2, u'EESS', style1)
        worksheet.write(s2, 3, u'O+', style1_1)
        worksheet.write(s2, 4, u'A+', style1_1)
        worksheet.write(s2, 5, u'B+', style1_1)
        worksheet.write(s2, 6, u'AB+', style1_1)
        worksheet.write(s2, 7, u'O-', style1_1)
        worksheet.write(s2, 8, u'A-', style1_1)
        worksheet.write(s2, 9, u'B-', style1_1)
        worksheet.write(s2, 10, u'AB-', style1_1)
        worksheet.write(s2, 11, u'TOTAL', style1_1)
        worksheet.write(s2, 12, u'O+', style1_1)
        worksheet.write(s2, 13, u'A+', style1_1)
        worksheet.write(s2, 14, u'B+', style1_1)
        worksheet.write(s2, 15, u'AB+', style1_1)
        worksheet.write(s2, 16, u'O-', style1_1)
        worksheet.write(s2, 17, u'A-', style1_1)
        worksheet.write(s2, 18, u'B-', style1_1)
        worksheet.write(s2, 19, u'AB-', style1_1)
        worksheet.write(s2, 20, u'TOTAL', style1_1)
        worksheet.write(s2, 21, u'TOTAL', style1_1)
        worksheet.write(s2, 22, u'TOTAL', style1_1)
        worksheet.write(s2, 23, u'TOTAL', style1_1)
        worksheet.write(s2, 24, u'TOTAL', style1_1)
        worksheet.write(s2, 25, u'TOTAL', style1_1)
        worksheet.write(s2, 26, u'TOTAL', style1_1)
        worksheet.write(s2, 27, u'TOTAL', style1_1)
        total_o_pg_positivo_c = 0
        total_a_pg_positivo_c = 0
        total_b_pg_positivo_c = 0
        total_ab_pg_positivo_c = 0
        total_o_pg_negativo_c = 0
        total_a_pg_negativo_c = 0
        total_b_pg_negativo_c = 0
        total_ab_pg_negativo_c = 0
        total_t_pg_c = 0
        total_o_p_positivo_c = 0
        total_a_p_positivo_c = 0
        total_b_p_positivo_c = 0
        total_ab_p_positivo_c = 0
        total_o_p_negativo_c = 0
        total_a_p_negativo_c = 0
        total_b_p_negativo_c = 0
        total_ab_p_negativo_c = 0
        total_t_p_c = 0
        total_t_ps_c = 0
        total_t_cpa_c = 0
        total_t_c_c = 0
        total_t_upt_c = 0
        total_t_dd_c = 0
        total_t_tpg_c = 0
        total_t_tp_c = 0

        for stock1 in self.env['stock_hemocomponente.hemocomponente'].search([('fecha', '=', self.fecha)], order='diresa_id asc'):
            values = {
                'region': stock1.diresa_id.name or '',
                'banco': stock1.banco_id.name or '',
                'o_positivo_paquete_globular': stock1.o_positivo_paquete_globular or '',
                'a_positivo_paquete_globular': stock1.a_positivo_paquete_globular or '',
                'b_positivo_paquete_globular': stock1.b_positivo_paquete_globular or '',
                'ab_positivo_paquete_globular': stock1.ab_positivo_paquete_globular or '',
                'o_negativo_paquete_globular': stock1.o_negativo_paquete_globular or '',
                'a_negativo_paquete_globular': stock1.a_negativo_paquete_globular or '',
                'b_negativo_paquete_globular': stock1.b_negativo_paquete_globular or '',
                'ab_negativo_paquete_globular': stock1.ab_negativo_paquete_globular or '',
                'total_paquete_globular': stock1.total_paquete_globular if stock1.total_paquete_globular else '',
                'o_positivo_plasma_fresco': stock1.o_positivo_plasma_fresco or '',
                'a_positivo_plasma_fresco': stock1.a_positivo_plasma_fresco or '',
                'b_positivo_plasma_fresco': stock1.b_positivo_plasma_fresco or '',
                'ab_positivo_plasma_fresco': stock1.ab_positivo_plasma_fresco or '',
                'o_negativo_plasma_fresco': stock1.o_negativo_plasma_fresco or '',
                'a_negativo_plasma_fresco': stock1.a_negativo_plasma_fresco or '',
                'b_negativo_plasma_fresco': stock1.b_negativo_plasma_fresco or '',
                'ab_negativo_plasma_fresco': stock1.ab_negativo_plasma_fresco or '',
                'total_plasma_fresco': stock1.total_plasma_fresco if stock1.total_plasma_fresco else '',
                'total_plaquetas_simple': stock1.total_plaquetas_simple or '',
                'total_concentrado_plaquetas': stock1.total_concentrado_plaquetas or '',
                'total_crioprecipitado': stock1.total_crioprecipitado or '',
                'total_unidades_pendientes_tamisaje': stock1.total_unidades_pendientes_tamisaje or '',
                'total_donaciones_sangre_x_dia': stock1.total_donaciones_sangre_x_dia or '',
                'total_transfuciones_x_dia': stock1.total_transfuciones_x_dia or '',
                'total_transfuciones_plaquetas_x_dia': stock1.total_transfuciones_plaquetas_x_dia or '',
            }
            worksheet.write(s3, 0, values.get('region'), style0)
            worksheet.write_merge(s3, s3, 1, 2, values.get('banco'), style0)
            worksheet.write(s3, 3, values.get('o_positivo_paquete_globular'), style0)
            worksheet.write(s3, 4, values.get('a_positivo_paquete_globular'), style0)
            worksheet.write(s3, 5, values.get('b_positivo_paquete_globular'), style0)
            worksheet.write(s3, 6, values.get('ab_positivo_paquete_globular'), style0)
            worksheet.write(s3, 7, values.get('o_negativo_paquete_globular'), style0)
            worksheet.write(s3, 8, values.get('a_negativo_paquete_globular'), style0)
            worksheet.write(s3, 9, values.get('b_negativo_paquete_globular'), style0)
            worksheet.write(s3, 10, values.get('ab_negativo_paquete_globular'), style0)
            worksheet.write(s3, 11, values.get('total_paquete_globular'), style0)
            worksheet.write(s3, 12, values.get('o_positivo_plasma_fresco'), style0)
            worksheet.write(s3, 13, values.get('a_positivo_plasma_fresco'), style0)
            worksheet.write(s3, 14, values.get('b_positivo_plasma_fresco'), style0)
            worksheet.write(s3, 15, values.get('ab_positivo_plasma_fresco'), style0)
            worksheet.write(s3, 16, values.get('o_negativo_plasma_fresco'), style0)
            worksheet.write(s3, 17, values.get('a_negativo_plasma_fresco'), style0)
            worksheet.write(s3, 18, values.get('b_negativo_plasma_fresco'), style0)
            worksheet.write(s3, 19, values.get('ab_negativo_plasma_fresco'), style0)
            worksheet.write(s3, 20, values.get('total_plasma_fresco'), style0)
            worksheet.write(s3, 21, values.get('total_plaquetas_simple'), style0)
            worksheet.write(s3, 22, values.get('total_concentrado_plaquetas'), style0)
            worksheet.write(s3, 23, values.get('total_crioprecipitado'), style0)
            worksheet.write(s3, 24, values.get('total_unidades_pendientes_tamisaje'), style0)
            worksheet.write(s3, 25, values.get('total_donaciones_sangre_x_dia'), style0)
            worksheet.write(s3, 26, values.get('total_transfuciones_x_dia'), style0)
            worksheet.write(s3, 27, values.get('total_transfuciones_plaquetas_x_dia'), style0)
            s3 += 1

            if stock1.o_positivo_paquete_globular:
                total_o_pg_positivo_c = total_o_pg_positivo_c + int(stock1.o_positivo_paquete_globular)
            if stock1.a_positivo_paquete_globular:
                total_a_pg_positivo_c = total_a_pg_positivo_c + int(stock1.a_positivo_paquete_globular)
            if stock1.b_positivo_paquete_globular:
                total_b_pg_positivo_c = total_b_pg_positivo_c + int(stock1.b_positivo_paquete_globular)
            if stock1.ab_positivo_paquete_globular:
                total_ab_pg_positivo_c = total_ab_pg_positivo_c + int(stock1.ab_positivo_paquete_globular)
            if stock1.o_negativo_paquete_globular:
                total_o_pg_negativo_c = total_o_pg_negativo_c + int(stock1.o_negativo_paquete_globular)
            if stock1.a_negativo_paquete_globular:
                total_a_pg_negativo_c = total_a_pg_negativo_c + int(stock1.a_negativo_paquete_globular)
            if stock1.b_negativo_paquete_globular:
                total_b_pg_negativo_c = total_b_pg_negativo_c + int(stock1.b_negativo_paquete_globular)
            if stock1.ab_negativo_paquete_globular:
                total_ab_pg_negativo_c = total_ab_pg_negativo_c + int(stock1.ab_negativo_paquete_globular)
            if stock1.total_paquete_globular:
                total_t_pg_c = total_t_pg_c + int(stock1.total_paquete_globular)
            if stock1.o_positivo_plasma_fresco:
                total_o_p_positivo_c = total_o_p_positivo_c + int(stock1.o_positivo_plasma_fresco)
            if stock1.a_positivo_plasma_fresco:
                total_a_p_positivo_c = total_a_p_positivo_c + int(stock1.a_positivo_plasma_fresco)
            if stock1.b_positivo_plasma_fresco:
                total_b_p_positivo_c = total_b_p_positivo_c + int(stock1.b_positivo_plasma_fresco)
            if stock1.ab_positivo_plasma_fresco:
                total_ab_p_positivo_c = total_ab_p_positivo_c + int(stock1.ab_positivo_plasma_fresco)
            if stock1.o_negativo_plasma_fresco:
                total_o_p_negativo_c = total_o_p_negativo_c + int(stock1.o_negativo_plasma_fresco)
            if stock1.a_negativo_plasma_fresco:
                total_a_p_negativo_c = total_a_p_negativo_c + int(stock1.a_negativo_plasma_fresco)
            if stock1.b_negativo_plasma_fresco:
                total_b_p_negativo_c = total_b_p_negativo_c + int(stock1.b_negativo_plasma_fresco)
            if stock1.ab_negativo_plasma_fresco:
                total_ab_p_negativo_c = total_ab_p_negativo_c + int(stock1.ab_negativo_plasma_fresco)
            if stock1.total_plasma_fresco:
                total_t_p_c = total_t_p_c + int(stock1.total_plasma_fresco)
            if stock1.total_plaquetas_simple:
                total_t_ps_c = total_t_ps_c + int(stock1.total_plaquetas_simple)
            if stock1.total_concentrado_plaquetas:
                total_t_cpa_c = total_t_cpa_c + int(stock1.total_concentrado_plaquetas)
            if stock1.total_crioprecipitado:
                total_t_c_c = total_t_c_c + int(stock1.total_crioprecipitado)
            if stock1.total_unidades_pendientes_tamisaje:
                total_t_upt_c = total_t_upt_c + int(stock1.total_unidades_pendientes_tamisaje)
            if stock1.total_donaciones_sangre_x_dia:
                total_t_dd_c = total_t_dd_c + int(stock1.total_donaciones_sangre_x_dia)
            if stock1.total_transfuciones_x_dia:
                total_t_tpg_c = total_t_tpg_c + int(stock1.total_transfuciones_x_dia)
            if stock1.total_transfuciones_plaquetas_x_dia:
                total_t_tp_c = total_t_tp_c + int(stock1.total_transfuciones_plaquetas_x_dia)

        worksheet.write((s3), 3, total_o_pg_positivo_c)
        worksheet.write((s3), 4, total_a_pg_positivo_c)
        worksheet.write((s3), 5, total_b_pg_positivo_c)
        worksheet.write((s3), 6, total_ab_pg_positivo_c)
        worksheet.write((s3), 7, total_o_pg_negativo_c)
        worksheet.write((s3), 8, total_a_pg_negativo_c)
        worksheet.write((s3), 9, total_b_pg_negativo_c)
        worksheet.write((s3), 10, total_ab_pg_negativo_c)
        worksheet.write((s3), 11, total_t_pg_c)
        worksheet.write((s3), 12, total_o_p_positivo_c)
        worksheet.write((s3), 13, total_a_p_positivo_c)
        worksheet.write((s3), 14, total_b_p_positivo_c)
        worksheet.write((s3), 15, total_ab_p_positivo_c)
        worksheet.write((s3), 16, total_o_p_negativo_c)
        worksheet.write((s3), 17, total_a_p_negativo_c)
        worksheet.write((s3), 18, total_b_p_negativo_c)
        worksheet.write((s3), 19, total_ab_p_negativo_c)
        worksheet.write((s3), 20, total_t_p_c)
        worksheet.write((s3), 21, total_t_ps_c)
        worksheet.write((s3), 22, total_t_cpa_c)
        worksheet.write((s3), 23, total_t_c_c)
        worksheet.write((s3), 24, total_t_upt_c)
        worksheet.write((s3), 25, total_t_dd_c)
        worksheet.write((s3), 26, total_t_tpg_c)
        worksheet.write((s3), 27, total_t_tp_c)

        file_data = io.BytesIO()
        workbook.save(file_data)
        file_data.seek(0)
        data = file_data.read()
        file_data.close()
        return data
