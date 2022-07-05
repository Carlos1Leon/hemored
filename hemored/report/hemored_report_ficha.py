# -*- coding: utf-8 -*-

import io
import os
import tempfile

from openpyxl import load_workbook
from lxml import etree

from odoo import fields, api, models

from ..models import constants

MN_ReportFicha = '.'.join([constants.MODULO, 'report_ficha'])


class ReportFicha(models.TransientModel):
    _name = MN_ReportFicha

    def es_diresa(self):
        return self.env.user.has_group('hemored.group_coordinador_diris_diresa_hemored')

    def _default_diresa(self):
        if self.es_diresa():
            return self.env.user.diresa_id.id
        return False

    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='Banco',
    )
    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='DIRIS/DIRESA/GERESA',
        default=lambda self: self._default_diresa(),
    )
    anho_id = fields.Many2one(
        comodel_name='minsa.anho',
        string='Año',
    )
    periodo_id = fields.Many2one(
        comodel_name='minsa.periodo',
        string='Periodo',
    )
    tipo_banco = fields.Selection(
        '_selection_tipo_banco',
        'Tipo',
    )
    institucion = fields.Selection(
        constants.SELECTION_INSTITUCION,
        'Institución'
    )
    estado_validacion = fields.Selection(
        constants.SELECTION_ESTADO_FICHA,
        'Estado validación',
    )

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(ReportFicha, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        es_diresa = self.env.user.has_group('hemored.group_coordinador_diris_diresa_hemored')
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            my_attrs = '{"readonly": true}'
            if es_diresa:
                for node in doc.xpath("//field[@name='diresa_id']"):
                    node.set('modifiers', my_attrs)
            res['arch'] = etree.tostring(doc)
        return res

    @api.model
    def _selection_tipo_banco(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_banco')

    @api.onchange('diresa_id')
    def _onchange_diresa_id(self):
        self.ensure_one()
        if self.diresa_id:
            self.banco_id = False

    @api.onchange('banco_id')
    def _onchange_banco_id(self):
        self.ensure_one()
        if self.banco_id:
            self.tipo_banco = False
            self.institucion = False

    @api.multi
    def print_excel(self):
        self.ensure_one()
        url = '/web/binary/download_export_ficha_consolidado?id={}&filename=Ficha_Estadística.xlsx'.format(self.id)
        value = {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new'
        }
        return value

    @api.multi
    def action_export_excel(self):
        self.ensure_one()
        archivo = 'FORMATO_FICHA_ESTADISTICA_2022.xlsx'
        ruta = '{}/../documents/{}'.format(os.path.dirname(os.path.abspath(__file__)), archivo)
        book = load_workbook(ruta)

        fobj = tempfile.NamedTemporaryFile(suffix='.xlsx', dir='/tmp/', delete=False)
        fname = fobj.name
        fobj.close()

        w_sheet = book.get_sheet_by_name('FORMATO ESTADISTICO')
        w_sheet['D3'] = ''
        w_sheet['J3'] = ''
        w_sheet['J4'] = ''
        w_sheet['E5'] = ''
        w_sheet['D6'] = ''
        w_sheet['E7'] = ''
        w_sheet['F8'] = ''
        w_sheet['C9'] = ''
        w_sheet['F9'] = ''
        w_sheet['I9'] = ''
        w_sheet['C10'] = ''
        w_sheet['I10'] = ''

        constrains = []
        if self.institucion:
            constrains.append('institucion = \'{}\''.format(self.institucion))
            if self.institucion == '1':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_1
            elif self.institucion == '2':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_2
            elif self.institucion == '3':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_3
            elif self.institucion == '4':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_4
            elif self.institucion == '5':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_5
            elif self.institucion == '6':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_6
            elif self.institucion == '7':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_7
            elif self.institucion == '8':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_8
            elif self.institucion == '9':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_9
            elif self.institucion == '10':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_10
            elif self.institucion == '11':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_11

        if self.banco_id.id:
            constrains.append('banco_id = {}'.format(self.banco_id.id))
            w_sheet['D3'] = self.banco_id.name
            w_sheet['J3'] = self.banco_id.renipress_id.codigo_eess
            w_sheet['J4'] = self.banco_id.diresa_id.name
            if self.banco_id.tipo_banco == '1':
                w_sheet['E5'] = constants.TIPO_BANCO_1
            elif self.banco_id.tipo_banco == '2':
                w_sheet['E5'] = constants.TIPO_BANCO_2
            if self.banco_id.renipress_id.institucion == '1':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_1
            elif self.banco_id.renipress_id.institucion == '2':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_2
            elif self.banco_id.renipress_id.institucion == '3':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_3
            elif self.banco_id.renipress_id.institucion == '4':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_4
            elif self.banco_id.renipress_id.institucion == '5':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_5
            elif self.banco_id.renipress_id.institucion == '6':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_6
            elif self.banco_id.renipress_id.institucion == '7':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_7
            elif self.banco_id.renipress_id.institucion == '8':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_8
            elif self.banco_id.renipress_id.institucion == '9':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_9
            elif self.banco_id.renipress_id.institucion == '10':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_10
            elif self.banco_id.renipress_id.institucion == '11':
                w_sheet['D6'] = constants.SELECTION_INSTITUCION_11
            w_sheet['E7'] = self.banco_id.renipress_id.direccion
            w_sheet['F8'] = self.banco_id.medico_coordinador_responsable
            w_sheet['C9'] = self.banco_id.num_camas
            w_sheet['F9'] = self.banco_id.telefono
            w_sheet['I9'] = self.banco_id.celular
            w_sheet['C10'] = self.banco_id.email

        if self.diresa_id.id:
            constrains.append('diresa_id = {}'.format(self.diresa_id.id))
            w_sheet['J4'] = self.diresa_id.name

        if self.anho_id.id:
            constrains.append('anho_id = {}'.format(self.anho_id.id))
            w_sheet['I10'] = self.anho_id.name

        if self.periodo_id.id:
            constrains.append('periodo_id = {}'.format(self.periodo_id.id))
            w_sheet['I10'] = self.periodo_id.name

        if self.tipo_banco:
            constrains.append('tipo_banco = \'{}\''.format(self.tipo_banco))
            if self.tipo_banco == '1':
                w_sheet['E5'] = constants.TIPO_BANCO_1
            elif self.tipo_banco == '2':
                w_sheet['E5'] = constants.TIPO_BANCO_2

        if self.estado_validacion:
            constrains.append('state = \'{}\''.format(self.estado_validacion))

        constrains = ' AND '.join(constrains) or 'true'

        map_field_celda = constants.MAP_FIELD_CELDA

        fields = [
            'SUM({field}) as {field}'.format(field=field)
            for field in map_field_celda.keys()
        ]

        fields = ', '.join(fields)

        sql = '''
                SELECT {}
                FROM hemored_ficha_estadistica
                WHERE {}
                LIMIT 1;
        '''.format(fields, constrains)

        self._cr.execute(sql)

        for field, valor in self._cr.dictfetchone().items():
            if valor:
                w_sheet[map_field_celda[field]] = valor
            else:
                w_sheet[map_field_celda[field]] = 0

        sql = '''
                SELECT tipo_donante, SUM(cantidad) as cantidad
                FROM hemored_ficha_total_donante_line
                WHERE {}
                GROUP BY tipo_donante;
            '''.format(constrains)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if (val[0] == 'dv'):
                w_sheet['B26'] = valor
            elif (val[0] == 'dr'):
                w_sheet['C26'] = valor
            elif (val[0] == 'dpr'):
                w_sheet['D26'] = valor
            elif (val[0] == 'da'):
                w_sheet['E26'] = valor

        sql = '''
                SELECT motivo_diferido_excluido, SUM(cantidad) as cantidad
                FROM hemored_ficha_total_postulante_diferido_excluido_line
                WHERE {}
                GROUP BY motivo_diferido_excluido;
            '''.format(constrains)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if (val[0] == '1'):
                w_sheet['G26'] = valor
            elif (val[0] == '2'):
                w_sheet['H26'] = valor
            elif (val[0] == '3'):
                w_sheet['I26'] = valor
            elif (val[0] == '4'):
                w_sheet['J26'] = valor
            elif (val[0] == '5'):
                w_sheet['K26'] = valor
            elif (val[0] == '6'):
                w_sheet['L26'] = valor

        sql = '''
                SELECT grupo_edad_donante, SUM(cantidad) as cantidad
                FROM hemored_ficha_donacion_segun_grupo_edad_donante_line
                WHERE {}
                GROUP BY grupo_edad_donante;
            '''.format(constrains)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if (val[0] == '1'):
                w_sheet['E31'] = valor
            elif (val[0] == '2'):
                w_sheet['F31'] = valor
            elif (val[0] == '3'):
                w_sheet['G31'] = valor
            elif (val[0] == '4'):
                w_sheet['H31'] = valor
            elif (val[0] == '5'):
                w_sheet['I31'] = valor

        sql = '''
                SELECT tipo_donante, SUM(cantidad) as cantidad
                FROM hemored_ficha_donacion_sangre_total_line
                WHERE {}
                GROUP BY tipo_donante;
            '''.format(constrains)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if (val[0] == 'dvpv'):
                w_sheet['B36'] = valor
            elif (val[0] == 'dvr'):
                w_sheet['C36'] = valor
            elif (val[0] == 'dr'):
                w_sheet['D36'] = valor
            elif (val[0] == 'dpr'):
                w_sheet['E36'] = valor
            elif (val[0] == 'da'):
                w_sheet['F36'] = valor

        sql = '''
                SELECT tipo_donante, SUM(cantidad) as cantidad
                FROM hemored_ficha_donacion_aferesis_line
                WHERE {}
                GROUP BY tipo_donante;
            '''.format(constrains)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if (val[0] == 'dvpv'):
                w_sheet['H36'] = valor
            elif (val[0] == 'dvr'):
                w_sheet['I36'] = valor
            elif (val[0] == 'dr'):
                w_sheet['J36'] = valor
            elif (val[0] == 'dpr'):
                w_sheet['K36'] = valor
            elif (val[0] == 'da'):
                w_sheet['L36'] = valor

        sql = '''
                SELECT tipo_unidad_sangre, SUM(cantidad_tipo_unidad_sangre) as cantidad
                FROM hemored_ficha_produccion_unidad_sangre_line
                WHERE {}
                GROUP BY tipo_unidad_sangre;
            '''.format(constrains)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if (val[0] == '1'):
                w_sheet['B77'] = valor
            elif (val[0] == '2'):
                w_sheet['C77'] = valor
            elif (val[0] == '3'):
                w_sheet['D77'] = valor
            elif (val[0] == '4'):
                w_sheet['E77'] = valor

        sql = '''
                SELECT hemocomponente, SUM(cantidad_hemocomponente) as cantidad
                FROM hemored_ficha_produccion_hemocomponente_line
                WHERE {}
                GROUP BY hemocomponente;
            '''.format(constrains)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if (val[0] == 'hgr'):
                w_sheet['F77'] = valor
            elif (val[0] == 'hpfc'):
                w_sheet['G77'] = valor
            elif (val[0] == 'hc'):
                w_sheet['H77'] = valor
            elif (val[0] == 'hp'):
                w_sheet['I77'] = valor
            elif (val[0] == 'hap'):
                w_sheet['J77'] = valor
            elif (val[0] == 'hagr'):
                w_sheet['K77'] = valor
            elif (val[0] == 'haplasma'):
                w_sheet['L77'] = valor

        sql = '''
                SELECT tipo_reaccion_adversa, SUM(cantidad) as cantidad
                FROM hemored_ficha_causa_reaccion_adversa_line
                WHERE {}
                GROUP BY tipo_reaccion_adversa;
            '''.format(constrains)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if (val[0] == '1'):
                w_sheet['E106'] = valor
            elif (val[0] == '2'):
                w_sheet['E107'] = valor
            elif (val[0] == '3'):
                w_sheet['E108'] = valor
            elif (val[0] == '4'):
                w_sheet['E109'] = valor
            elif (val[0] == '5'):
                w_sheet['E110'] = valor
            elif (val[0] == '6'):
                w_sheet['E111'] = valor
            elif (val[0] == '7'):
                w_sheet['E112'] = valor
            elif (val[0] == '8'):
                w_sheet['E113'] = valor
            elif (val[0] == '9'):
                w_sheet['E114'] = valor
            elif (val[0] == '10'):
                w_sheet['E115'] = valor
            elif (val[0] == '11'):
                w_sheet['E116'] = valor
            elif (val[0] == '12'):
                w_sheet['E117'] = valor
            elif (val[0] == '13'):
                w_sheet['E118'] = valor
            elif (val[0] == '14'):
                w_sheet['E119'] = valor
            elif (val[0] == '15'):
                w_sheet['E120'] = valor
            elif (val[0] == '16'):
                w_sheet['E121'] = valor

        fname = io.BytesIO()
        book.save(fname)
        fname.seek(0)
        data = fname.read()
        fname.close()
        return data
