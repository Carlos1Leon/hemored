# -*- coding: utf-8 -*-
import io
import os
import tempfile

from openpyxl import load_workbook

from odoo import api, models

from ..models import constants


class FichaEstadistica(models.Model):
    _inherit = 'hemored_supervision.record_supervision'

    @api.multi
    def cargar_excel_ficha(self):
        self.ensure_one()
        form = self.env.ref('hemored_update_supervision.hemored_update_supervision_form_view', False)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Carga Automática de Datos',
            'res_model': 'hemored_update_supervision.updateexcel',
            'views': [(form.id, 'form')],
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': form.id,
            'target': 'new'
        }

    @api.multi
    def print_excel(self):
        self.ensure_one()
        url = '/web/binary/download_export_supervision?id={}&filename=Ficha_Supervisión_{}_{}.xlsx'.format(self.id, self.banco_id.name, self.fecha_supervision)
        value = {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new'
        }
        return value

    @api.multi
    def descarga_excel_supervision(self):
        if(self.banco_id.renipress_id.institucion == '1'):
            institucion = constants.SELECTION_INSTITUCION_1
        elif (self.banco_id.renipress_id.institucion == '2'):
            institucion = constants.SELECTION_INSTITUCION_2
        elif (self.banco_id.renipress_id.institucion == '3'):
            institucion = constants.SELECTION_INSTITUCION_3
        elif (self.banco_id.renipress_id.institucion == '4'):
            institucion = constants.SELECTION_INSTITUCION_4
        elif (self.banco_id.renipress_id.institucion == '5'):
            institucion = constants.SELECTION_INSTITUCION_5
        elif (self.banco_id.renipress_id.institucion == '6'):
            institucion = constants.SELECTION_INSTITUCION_6
        elif (self.banco_id.renipress_id.institucion == '7'):
            institucion = constants.SELECTION_INSTITUCION_7
        elif (self.banco_id.renipress_id.institucion == '8'):
            institucion = constants.SELECTION_INSTITUCION_8
        elif (self.banco_id.renipress_id.institucion == '9'):
            institucion = constants.SELECTION_INSTITUCION_9
        elif (self.banco_id.renipress_id.institucion == '10'):
            institucion = constants.SELECTION_INSTITUCION_10
        elif (self.banco_id.renipress_id.institucion == '13'):
            institucion = constants.SELECTION_INSTITUCION_13
        elif (self.banco_id.renipress_id.institucion == '11'):
            institucion = constants.SELECTION_INSTITUCION_11
        else:
            institucion = ''

        if (self.tipo_banco == '1'):
            archivo = 'EXPORTAR_SUPERVISION_CHBS_TIPO_I.xlsx'
        else:
            archivo = 'EXPORTAR_SUPERVISION_CHBS_TIPO_II.xlsx'

        ruta = '{}/../documents/{}'.format(os.path.dirname(os.path.abspath(__file__)), archivo)
        book = load_workbook(ruta)
        fobj = tempfile.NamedTemporaryFile(suffix='.xlsx', dir='/tmp/', delete=False)
        fname = fobj.name
        fobj.close()

        w_sheet = book.get_sheet_by_name('GUIA_SUPERVISION')
        w_sheet['E11'] = self.banco_id.name
        w_sheet['E9'] = self.banco_id.renipress_id.codigo_eess
        w_sheet['E13'] = institucion
        w_sheet['E17'] = self.categoria
        w_sheet['E19'] = self.banco_id.renipress_id.direccion
        w_sheet['C21'] = self.telefono
        w_sheet['F21'] = self.telefono
        w_sheet['E23'] = self.director
        w_sheet['E25'] = self.jefe_cbhs
        w_sheet['E27'] = self.email_cbhs
        w_sheet['E29'] = self.nombre_entrevistad
        w_sheet['B572'] = self.observacion
        w_sheet['C576'] = self.hora
        w_sheet['E576'] = self.dia

        map_field_celda = constants.MAP_FIELD_CELDA

        fields = list(map_field_celda.keys())
        fields = ', '.join(fields)

        sql = '''
                SELECT {}
                FROM hemored_supervision_record_supervision
                WHERE id = {}
                LIMIT 1;
            '''.format(fields, self.id)

        self._cr.execute(sql)

        for field, valor in self._cr.dictfetchone().items():
            if valor == 'S':
                w_sheet[map_field_celda[field]] = 'SI'
            elif valor == 'N':
                w_sheet[map_field_celda[field]] = 'NO'
            elif not valor:
                w_sheet[map_field_celda[field]] = ''
            else:
                w_sheet[map_field_celda[field]] = valor

        map_field_celda2 = constants.MAP_FIELD_CELDA2

        fields = list(map_field_celda2.keys())
        fields = ', '.join(fields)

        sql = '''
                SELECT {}
                FROM hemored_supervision_record_supervision
                WHERE id = {}
                LIMIT 1;
            '''.format(fields, self.id)

        self._cr.execute(sql)

        for field, valor in self._cr.dictfetchone().items():
            if field == 't_rg_3':
                if valor == constants.SERVICIO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.DEPARTAMENTO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.AREA:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_rg_20':
                if valor == constants.NOMBRADO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.CAS:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.TERCERO:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_rg_22':
                if valor == constants.UNO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.DOS:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.TRES:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.CUATRO:
                    celda_final = int(map_field_celda2[field]) + 3
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.CINCO:
                    celda_final = int(map_field_celda2[field]) + 4
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.SEIS:
                    celda_final = int(map_field_celda2[field]) + 5
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field in ('t_pros_4_1', 't_pros_4_2', 't_pros_4_3', 't_pros_8_1', 't_pros_8_2', 't_pros_8_3',
                         't_infra_instal_2_1', 't_infra_instal_2_2', 't_infra_instal_2_3', 't_infra_instal_2_4'):
                if valor:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = 'NO'
            if field == 't_pros_7':
                if valor == constants.ENTREVISTA:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.AUTOAPLICADO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_12':
                if valor == constants.COMPLETO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.INCOMPLETO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_17':
                if valor == constants.PRE_DONACION:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.POST_DONACION:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.AMBOS:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_19':
                if valor == constants.EMAIL:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.PRESENCIAL:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_23':
                if valor == constants.MANUAL:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.SELLADOR_ELECTRONICO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_24':
                if valor == constants.DOBLE:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.TRIPLE:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.CUADRUPLE:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_34':
                if valor == constants.MANUAL:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.DIGITAL:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field in ('t_pros_38', 't_pros_39', 't_pros_40', 't_pros_41', 't_pros_42', 't_pros_43', 't_pros_44'):
                if valor == constants.ELISA:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.QUIMIOLUMINISCENCIA:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.ELECTROQUIMIOLUMINISCENCIA:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_47':
                if valor == constants.DIARIO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.INTERDIARIO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.MAYOR_A_UNA_SEMANA:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_50':
                if valor == constants.NUEVA_MUESTRA:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.CON_MUESTRA_ALMACENADA:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.PLASMA_DE_LA_UNIDAD_EXTRAIDA:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_56' or field == 't_pros_77':
                if valor == constants.MANUAL:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.SEMIAUTOMATICO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.AUTOMATICO:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_68':
                if valor == constants.PRODUCTOS_IRRADIADOS:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.PRODUCTO_LEUCORREDUCIDO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.COMPONENTES_EN_POOL:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_pros_93':
                if valor == constants.METODO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.EQUIPO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_cali_2':
                if valor == constants.PEVED:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.SO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.TO:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.OTRO:
                    celda_final = int(map_field_celda2[field]) + 3
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_sis_inform_4':
                if valor == constants.PROPIO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.CESION_DE_USO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_clasf_bio_5':
                if valor == constants.TECNOLOGO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.BIOLOGO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.OTRA_PROFESION:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_clasf_bio_9':
                if valor == constants.MENOR_UN_ANO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.DE_UNO_A_DOS:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.DE_DOS_A_TRES:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.DE_TRES_A_CUATRO:
                    celda_final = int(map_field_celda2[field]) + 3
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.DE_CINCO_A_MAS:
                    celda_final = int(map_field_celda2[field]) + 4
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_infra_instal_1':
                if valor == constants.SOTANO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.PRIMER_PISO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.SEGUNDO_PISO:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.OTRO:
                    celda_final = int(map_field_celda2[field]) + 3
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''
            if field == 't_infra_instal_21' or field == 't_infra_instal_23':
                if valor == constants.PROPIO:
                    w_sheet['H' + str(map_field_celda2[field])] = 'SI'
                elif valor == constants.COMPARTIDO:
                    celda_final = int(map_field_celda2[field]) + 1
                    w_sheet['H' + str(celda_final)] = 'SI'
                elif valor == constants.TERCERIZADO:
                    celda_final = int(map_field_celda2[field]) + 2
                    w_sheet['H' + str(celda_final)] = 'SI'
                else:
                    w_sheet['H' + str(map_field_celda2[field])] = ''

        fname = io.BytesIO()
        book.save(fname)
        fname.seek(0)
        data = fname.read()
        fname.close()
        return data
