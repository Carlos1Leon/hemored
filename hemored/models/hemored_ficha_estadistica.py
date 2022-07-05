# -*- coding: utf-8 -*-
from lxml import etree
from dateutil.relativedelta import relativedelta
import io
import os
import tempfile

from openpyxl import load_workbook

from odoo import api, fields, models

from ..models import constants

MN_FichaEstadistica = '.'.join([constants.MODULO, 'ficha_estadistica'])

MN_FichaTotalDonante = '.'.join([constants.MODULO, 'ficha_total_donante', 'line'])

MN_FichaTotalPostulanteDiferidoExcluido = '.'.join([constants.MODULO, 'ficha_total_postulante_diferido_excluido', 'line'])

MN_FichaDonacionSegunGrupoEdadDonante = '.'.join([constants.MODULO, 'ficha_donacion_segun_grupo_edad_donante', 'line'])

MN_FichaDonacionSangreTotal = '.'.join([constants.MODULO, 'ficha_donacion_sangre_total', 'line'])

MN_FichaDonacionAferesis = '.'.join([constants.MODULO, 'ficha_donacion_aferesis', 'line'])

MN_FichaProduccionHemocomponenteUnidadSangre = '.'.join([constants.MODULO, 'ficha_produccion_unidad_sangre', 'line'])

MN_FichaProduccionHemocomponente = '.'.join([constants.MODULO, 'ficha_produccion_hemocomponente', 'line'])

MN_FichaCausaReaccionAdversa = '.'.join([constants.MODULO, 'ficha_causa_reaccion_adversa', 'line'])


def _default_motivo_diferido_excluido(self):
    detalles = self.env['basecatalogo.catalogo'].get_catalogo('_selection_motivo_diferido_excluido')

    list_detalles = []
    if detalles:
        for d in detalles:
            list_detalles.append([0, False, {
                'motivo_diferido_excluido': d[0]}])
        return list_detalles


def _default_grupo_edad_donante(self):
    detalles = self.env['basecatalogo.catalogo'].get_catalogo('_selection_grupo_edad_donante')

    list_detalles = []
    if detalles:
        for d in detalles:
            list_detalles.append([0, False, {
                'grupo_edad_donante': d[0]}])
        return list_detalles


def _default_tipo_donante(self):
    detalles = self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_donante')

    list_detalles = []
    if detalles:
        for d in detalles:
            list_detalles.append([0, False, {
                'tipo_donante': d[0]}])
        return list_detalles


def _default_tipo_donante2(self):
    detalles = self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_donante2') or []

    list_detalles = []
    for d in detalles:
        list_detalles.append([0, False, {'tipo_donante': d[0]}])
    return list_detalles


def _default_tipo_unidad_sangre(self):
    detalles = self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_unidad_sangre')

    list_detalles = []
    if detalles:
        for d in detalles:
            list_detalles.append([0, False, {
                'tipo_unidad_sangre': d[0]}])
        return list_detalles


def _default_hemocomponente(self):
    detalles = self.env['basecatalogo.catalogo'].get_catalogo('_selection_hemocomponente')

    list_detalles = []
    if detalles:
        for d in detalles:
            list_detalles.append([0, False, {
                'hemocomponente': d[0]}])
        return list_detalles


def _default_causa_reaccion_graves(self):
    detalles = self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_reaccion_adversa')

    list_detalles = []
    if detalles:
        for d in detalles:
            list_detalles.append([0, False, {
                'tipo_reaccion_adversa': d[0]}])
        return list_detalles


class MNFichaEstadistica(models.Model):
    _name = MN_FichaEstadistica
    _order = 'periodo_id asc'
    _inherit = ['mail.thread']

    _description = 'Ficha Estadística'

    @api.multi
    @api.depends('banco_id', 'periodo_id')
    def name_get(self):
        result = []
        for record in self:
            name = '[{}] {}'.format(record.banco_id.name, record.periodo_id.name)
            result.append((record.id, name))
        return result

    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='Banco',
        default=lambda self: self.env.user.banco_id,
        track_visibility='onchange'
    )
    anho_id = fields.Many2one(
        comodel_name='minsa.anho',
        string='Año',
        required=True,
        track_visibility='onchange'
    )
    periodo_id = fields.Many2one(
        comodel_name='minsa.periodo',
        string='Periodo',
        track_visibility='onchange'
    )
    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='DIRIS/DIRESA/GERESA',
        track_visibility='onchange'
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsable',
        readonly=True,
        default=lambda self: self.env.user,
        track_visibility='onchange'
    )
    tipo_banco = fields.Selection(
        '_selection_tipo_banco',
        'Tipo de Banco',
        required=True,
        track_visibility='onchange'
    )
    ficha_anual_mensual = fields.Selection(
        constants.SELECTION_FICHA,
        'Ficha mensual o anual',
        compute='_compute_anual_mensual',
        store=True
    )
    institucion = fields.Selection(
        constants.SELECTION_INSTITUCION,
        'Institución',
        track_visibility='onchange'
    )
    inicio_fecha_registro = fields.Date(
        string='Inicio de fecha de Registro',
        track_visibility='onchange'
    )
    fin_fecha_registro = fields.Date(
        string='Fin de fecha de Registro',
        track_visibility='onchange'
    )
    fecha_envio = fields.Date(
        string='Fecha de envio de ficha estadística',
        track_visibility='onchange'
    )
    fecha_validacion = fields.Date(
        string='Fecha de validación de ficha estadística',
        track_visibility='onchange'
    )
    consolidado = fields.Boolean(
        string='consolidado',
        track_visibility='onchange'
    )
    state = fields.Selection(
        string='Estado',
        selection=constants.SELECTION_STATE,
        default=constants.BORRADOR,
        track_visibility='onchange'
    )
    nombre_state = fields.Char(
        string='Estado',
        compute='_compute_status',
    )

    # Donación de Sangre

    cantidad_pe_x_ca = fields.Integer(
        'Cantidad postulantes excluidos por categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_pe_x_cvim = fields.Integer(
        'Cantidad postulantes excluidos por categoría voluntario IM',
        track_visibility='onchange'
    )

    cantidad_pe_x_cvem = fields.Integer(
        'Cantidad postulantes excluidos por categoría voluntario EM',
        track_visibility='onchange'
    )

    cantidad_pe_x_cr = fields.Integer(
        'Cantidad postulantes excluidos por categoría reposición',
        track_visibility='onchange'
    )

    cantidad_pe_x_cpr = fields.Integer(
        'Cantidad postulantes excluidos por categoría presuntamente remunerados',
        track_visibility='onchange'
    )

    cantidad_total_x_pe = fields.Integer(
        'Cantidad total postulantes excluidos',
        compute='_compute_cantidad_total_x_pe',
        store=True,
    )

    cantidad_pd_x_ca = fields.Integer(
        'Cantidad postulantes diferidos por categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_pd_x_cvim = fields.Integer(
        'Cantidad postulantes diferidos por categoría voluntario IM',
        track_visibility='onchange'
    )

    cantidad_pd_x_cvem = fields.Integer(
        'Cantidad postulantes diferidos por categoría voluntario EM',
        track_visibility='onchange'
    )

    cantidad_pd_x_cr = fields.Integer(
        'Cantidad postulantes diferidos por categoría reposición',
        track_visibility='onchange'
    )

    cantidad_pd_x_cpr = fields.Integer(
        'Cantidad postulantes diferidos por categoría presuntamente remunerados',
        track_visibility='onchange'
    )

    cantidad_total_x_pd = fields.Integer(
        'Cantidad total postulantes diferidos',
        compute='_compute_total_donaciones_pd',
        store=True,
    )

    cantidad_padi_x_ca = fields.Integer(
        'Cantidad postulantes donacion incompleta por categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_padi_x_cvim = fields.Integer(
        'Cantidad postulantes donacion incompleta por categoría voluntario IM',
        track_visibility='onchange'
    )

    cantidad_padi_x_cvem = fields.Integer(
        'Cantidad postulantes donacion incompleta por categoría voluntario EM',
        track_visibility='onchange'
    )

    cantidad_padi_x_cr = fields.Integer(
        'Cantidad postulantes donacion incompleta por categoría reposición',
        track_visibility='onchange'
    )

    cantidad_padi_x_cpr = fields.Integer(
        'Cantidad postulantes donacion incompleta por categoría presuntamente remunerados',
        track_visibility='onchange'
    )

    cantidad_total_x_padi = fields.Integer(
        'Cantidad total postulantes donacion incompleta',
        compute='_compute_total_donaciones_padi',
        store=True,
    )

    cantidad_padc_x_ca = fields.Integer(
        'Cantidad postulantes donacion completa por categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_padc_x_cvim = fields.Integer(
        'Cantidad postulantes donacion completa por categoría voluntario IM',
        track_visibility='onchange'
    )

    cantidad_padc_x_cvem = fields.Integer(
        'Cantidad postulantes donacion completa por categoría voluntario EM',
        track_visibility='onchange'
    )

    cantidad_padc_x_cr = fields.Integer(
        'Cantidad postulantes donacion completa por categoría reposición',
        track_visibility='onchange'
    )

    cantidad_padc_x_cpr = fields.Integer(
        'Cantidad postulantes donacion completa por categoría presuntamente remunerados',
        track_visibility='onchange'
    )

    cantidad_total_x_padc = fields.Integer(
        'Cantidad total postulantes donacion completa',
        compute='_compute_total_donaciones_padc',
        store=True,
    )

    cantidad_total_x_ca = fields.Integer(
        'Cantidad total categoría autólogos',
        compute='_compute_total_donaciones_ca',
        store=True,
    )

    cantidad_total_x_cvim = fields.Integer(
        'Cantidad total categoría voluntarios IM',
        compute='_compute_total_donaciones_cvim',
        store=True,
    )

    cantidad_total_x_cvem = fields.Integer(
        'Cantidad total categoría voluntarios EM',
        compute='_compute_total_donaciones_cvem',
        store=True,
    )

    cantidad_total_x_cr = fields.Integer(
        'Cantidad total categoría reposición',
        compute='_compute_total_donaciones_cr',
        store=True,
    )

    cantidad_total_x_cpr = fields.Integer(
        'Cantidad total categoría presuntamente remunerado',
        compute='_compute_total_donaciones_cpr',
        store=True,
    )

    cantidad_total_postulantes_donacion_sangre = fields.Integer(
        'Cantidad total de Postulantes que fueron a donar sangre',
        compute='_compute_total_postulantes_donaciones',
        store=True,
    )

    cantidad_total_categorias_donacion_sangre = fields.Integer(
        'Cantidad total por categorías que fueron a donar sangre',
        compute='_compute_total_categorias_donaciones',
        store=True,
    )

    cantidad_total_donacion_sangre = fields.Integer(
        'Cantidad total final fueron a donar sangre',
        compute='_compute_total_donaciones',
        store=True
    )

    cantidad_porcentaje_postulantes_donacion_completa = fields.Float(
        'Porcentaje de Postulantes que fueron a donar sangre',
        compute='_compute_porcentaje_postulantes_donacion_completa',
        store=True,
    )

    cantidad_porcentaje_postulantes_diferidos = fields.Float(
        'Porcentaje de Postulantes que fueron diferidos',
        compute='_compute_porcentaje_postulantes_diferidos',
        store=True,
    )

    cantidad_porcentaje_postulantes_excluidos = fields.Float(
        'Porcentaje de Postulantes que fueron excluidos',
        compute='_compute_porcentaje_postulantes_excluidos',
        store=True,
    )

    cantidad_total_voluntarios = fields.Integer(
        'Total de postulantes voluntarios',
        compute='_compute_cantidad_total_voluntarios',
        store=True,
    )

    cantidad_total_no_voluntarios = fields.Integer(
        'Total de postulantes que no son voluntarios',
        compute='_compute_cantidad_total_no_voluntarios',
        store=True,
    )

    porcentaje_total_voluntarios = fields.Float(
        'Porcentaje de postulantes voluntarios',
        compute='_compute_porcentaje_total_voluntarios',
        store=True,
    )

    # Total Donantes

    total_donante_ids = fields.One2many(
        'hemored.ficha_total_donante.line',
        'ficha_id',
        default=lambda self: _default_tipo_donante2(self),
        track_visibility='onchange'
    )

    cantidad_total_donante = fields.Integer(
        'Cantidad total de total donantes',
        compute='_compute_total_total_donante',
        store=True,
    )

    # Total de Postulantes que Fueron Diferidos o Excluidos

    total_postulante_diferido_excluido_ids = fields.One2many(
        'hemored.ficha_total_postulante_diferido_excluido.line',
        'ficha_id',
        default=lambda self: _default_motivo_diferido_excluido(self),
        track_visibility='onchange'
    )

    cantidad_total_postulante_diferido_excluido = fields.Integer(
        'Cantidad total de total postulante diferido excluido',
        compute='_compute_total_total_postulante_diferido_excluido',
        store=True,
    )

    # Total Donaciones por Genero

    cantidad_donacion_h = fields.Integer(
        'Cantidad donacion hombres',
        track_visibility='onchange'
    )

    cantidad_donacion_m = fields.Integer(
        'Cantidad donacion mujeres',
        track_visibility='onchange'
    )

    cantidad_donacion_total = fields.Integer(
        'Cantidad donacion total',
        compute='_compute_total_donaciones_sexo',
        store=True,
    )

    # Total de Donaciones Segun Grupo Edad

    donacion_segun_grupo_edad_donante_ids = fields.One2many(
        'hemored.ficha_donacion_segun_grupo_edad_donante.line',
        'ficha_id',
        default=lambda self: _default_grupo_edad_donante(self),
        track_visibility='onchange'
    )

    cantidad_total_donacion_segun_grupo_edad = fields.Integer(
        'Cantidad total de donacion segun grupo edad',
        compute='_compute_total_donacion_segun_grupo_edad',
        store=True,
    )

    # Donacion de Sangre Total

    donacion_sangre_total_ids = fields.One2many(
        'hemored.ficha_donacion_sangre_total.line',
        'ficha_id',
        default=lambda self: _default_tipo_donante(self),
        track_visibility='onchange'
    )

    cantidad_total_donacion_sangre_total = fields.Integer(
        'Cantidad total de donacion sangre total',
        compute='_compute_total_donacion_sangre_total',
        store=True,
    )

    # Donacion de Aferesis

    donacion_aferesis_ids = fields.One2many(
        'hemored.ficha_donacion_aferesis.line',
        'ficha_id',
        default=lambda self: _default_tipo_donante(self),
        track_visibility='onchange'
    )

    cantidad_total_donacion_aferesis = fields.Integer(
        'Cantidad total de donacion aféresis',
        compute='_compute_total_donacion_aferesis',
        store=True,
    )

    # Tamizaje Unidades

    cantidad_mvih_clt_cv = fields.Integer(
        'Cantidad marcador VIH clase tamizado categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mvih_clt_cr = fields.Integer(
        'Cantidad marcador VIH clase tamizado categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mvih_clt_cpr = fields.Integer(
        'Cantidad marcador VIH clase tamizado categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mvih_clt_ca = fields.Integer(
        'Cantidad marcador VIH clase tamizado categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mvih_clt_total = fields.Integer(
        'Cantidad total VIH tamizados',
        compute='_compute_total_tamizaje_mvih_clt',
        store=True,
    )

    # otra Clase

    cantidad_mvih_clr_cv = fields.Integer(
        'Cantidad marcador VIH clase reactivo categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mvih_clr_cr = fields.Integer(
        'Cantidad marcador VIH clase reactivo categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mvih_clr_cpr = fields.Integer(
        'Cantidad marcador VIH clase reactivo categoría presunto remunerado',
        track_visibility='onchange'
    )

    cantidad_mvih_clr_ca = fields.Integer(
        'Cantidad Cantidad marcador VIH clase reactivo categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mvih_clr_total = fields.Integer(
        'Cantidad total VIH reactivos',
        compute='_compute_total_tamizaje_mvih_clr',
        store=True,
    )

    # otra Clase

    cantidad_mvih_clzg_cv = fields.Integer(
        'Cantidad marcador VIH clase zona gris categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mvih_clzg_cr = fields.Integer(
        'Cantidad marcador VIH clase zona gris categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mvih_clzg_cpr = fields.Integer(
        'Cantidad marcador VIH clase zona gris categoría presunto remunerado',
        track_visibility='onchange'
    )

    cantidad_mvih_clzg_ca = fields.Integer(
        'Cantidad marcador VIH clase zona gris categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mvih_clzg_total = fields.Integer(
        'Cantidad total VIH zona gris',
        compute='_compute_total_tamizaje_mvih_clzg',
        store=True,
    )

    # Otro marcador

    cantidad_mhbsag_clt_cv = fields.Integer(
        'Cantidad marcador HBsAG clase tamizaje categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clt_cr = fields.Integer(
        'Cantidad marcador HBsAG clase tamizaje categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clt_cpr = fields.Integer(
        'Cantidad marcador HBsAG clase tamizaje categoría presunto remunerado',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clt_ca = fields.Integer(
        'Cantidad marcador HBsAG clase tamizaje categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clt_total = fields.Integer(
        'Cantidad total HBsAG tamizados',
        compute='_compute_total_tamizaje_mhbsag_clt',
        store=True,
    )

    # otra Clase

    cantidad_mhbsag_clr_cv = fields.Integer(
        'Cantidad marcador HBsAG clase reactivo categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clr_cr = fields.Integer(
        'Cantidad marcador HBsAG clase reactivo categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clr_cpr = fields.Integer(
        'Cantidad marcador HBsAG clase reactivo categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clr_ca = fields.Integer(
        'Cantidad marcador HBsAG clase reactivo categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clr_total = fields.Integer(
        'Cantidad total HBsAG reactivos',
        compute='_compute_total_tamizaje_mhbsag_clr',
        store=True,
    )

    # otra Clase

    cantidad_mhbsag_clzg_cv = fields.Integer(
        'Cantidad marcador HBsAG clase zona gris categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clzg_cr = fields.Integer(
        'Cantidad marcador HBsAG clase zona gris categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clzg_cpr = fields.Integer(
        'Cantidad marcador HBsAG clase zona gris categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clzg_ca = fields.Integer(
        'Cantidad marcador HBsAG clase zona gris categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mhbsag_clzg_total = fields.Integer(
        'Cantidad total HBsAG zona gris',
        compute='_compute_total_tamizaje_mhbsag_clzg',
        store=True,
    )

    # Otro marcador

    cantidad_mhepc_clt_cv = fields.Integer(
        'Cantidad marcador Hep C clase tamizados categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mhepc_clt_cr = fields.Integer(
        'Cantidad marcador Hep C clase tamizados categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mhepc_clt_cpr = fields.Integer(
        'Cantidad marcador Hep C clase tamizados categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mhepc_clt_ca = fields.Integer(
        'Cantidad marcador Hep C clase tamizados categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mhepc_clt_total = fields.Integer(
        'Cantidad total Hep C tamizados',
        compute='_compute_total_tamizaje_mhepc_clt',
        store=True,
    )

    # otra Clase

    cantidad_mhepc_clr_cv = fields.Integer(
        'Cantidad marcador Hep C clase reactivos categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mhepc_clr_cr = fields.Integer(
        'Cantidad marcador Hep C clase reactivos categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mhepc_clr_cpr = fields.Integer(
        'Cantidad marcador Hep C clase reactivos categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mhepc_clr_ca = fields.Integer(
        'Cantidad marcador Hep C clase reactivos categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mhepc_clr_total = fields.Integer(
        'Cantidad total Hep C reactivos',
        compute='_compute_total_tamizaje_mhepc_clr',
        store=True,
    )

    # otra Clase

    cantidad_mhepc_clzg_cv = fields.Integer(
        'Cantidad marcador Hep C clase zona gris categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mhepc_clzg_cr = fields.Integer(
        'Cantidad marcador Hep C clase zona gris categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mhepc_clzg_cpr = fields.Integer(
        'Cantidad marcador Hep C clase zona gris categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mhepc_clzg_ca = fields.Integer(
        'Cantidad marcador Hep C clase zona gris categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mhepc_clzg_total = fields.Integer(
        'Cantidad total Hep C zona gris',
        compute='_compute_total_tamizaje_mhepc_clzg',
        store=True,
    )

    # Otro marcador

    cantidad_mantihbc_clt_cv = fields.Integer(
        'Cantidad marcador Anti-HBc clase tamizados categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clt_cr = fields.Integer(
        'Cantidad marcador Anti-HBc clase tamizados categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clt_cpr = fields.Integer(
        'Cantidad marcador Anti-HBc clase tamizados categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clt_ca = fields.Integer(
        'Cantidad marcador Anti-HBc clase tamizados categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clt_total = fields.Integer(
        'Cantidad total Anti-HBc tamizados',
        compute='_compute_total_tamizaje_mantihbc_clt',
        store=True,
    )

    # otra Clase

    cantidad_mantihbc_clr_cv = fields.Integer(
        'Cantidad marcador Anti-HBc clase reactivos categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clr_cr = fields.Integer(
        'Cantidad marcador Anti-HBc clase reactivos categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clr_cpr = fields.Integer(
        'Cantidad marcador Anti-HBc clase reactivos categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clr_ca = fields.Integer(
        'Cantidad marcador Anti-HBc clase reactivos categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clr_total = fields.Integer(
        'Cantidad total Anti-HBc reactivos',
        compute='_compute_total_tamizaje_mantihbc_clr',
        store=True,
    )

    # otra Clase

    cantidad_mantihbc_clzg_cv = fields.Integer(
        'Cantidad marcador Anti-HBc clase zona gris categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clzg_cr = fields.Integer(
        'Cantidad marcador Anti-HBc clase zona gris categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clzg_cpr = fields.Integer(
        'Cantidad marcador Anti-HBc clase zona gris categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clzg_ca = fields.Integer(
        'Cantidad marcador Anti-HBc clase zona gris categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mantihbc_clzg_total = fields.Integer(
        'Cantidad total Anti-HBc zona gris',
        compute='_compute_total_tamizaje_mantihbc_clzg',
        store=True,
    )

    # Otro Marcador

    cantidad_mhtlv_clt_cv = fields.Integer(
        'Cantidad marcador HTLV I/II clase tamizados categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clt_cr = fields.Integer(
        'Cantidad marcador HTLV I/II clase tamizados categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clt_cpr = fields.Integer(
        'Cantidad marcador HTLV I/II clase tamizados categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clt_ca = fields.Integer(
        'Cantidad marcador HTLV I/II clase tamizados categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clt_total = fields.Integer(
        'Cantidad total HTLV I/II tamizados',
        compute='_compute_total_tamizaje_mhtlv_clt',
        store=True,
    )

    # otra Clase

    cantidad_mhtlv_clr_cv = fields.Integer(
        'Cantidad marcador HTLV I/II clase reactivos categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clr_cr = fields.Integer(
        'Cantidad marcador HTLV I/II clase reactivos categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clr_cpr = fields.Integer(
        'Cantidad marcador HTLV I/II clase reactivos categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clr_ca = fields.Integer(
        'Cantidad marcador HTLV I/II clase reactivos categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clr_total = fields.Integer(
        'Cantidad total HTLV I/II reactivos',
        compute='_compute_total_tamizaje_mhtlv_clr',
        store=True,
    )

    # otra Clase

    cantidad_mhtlv_clzg_cv = fields.Integer(
        'Cantidad marcador HTLV I/II clase zona gris categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clzg_cr = fields.Integer(
        'Cantidad marcador HTLV I/II clase zona gris categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clzg_cpr = fields.Integer(
        'Cantidad marcador HTLV I/II clase zona gris categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clzg_ca = fields.Integer(
        'Cantidad marcador HTLV I/II clase zona gris categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mhtlv_clzg_total = fields.Integer(
        'Cantidad total HTLV I/II zona gris',
        compute='_compute_total_tamizaje_mhtlv_clzg',
        store=True,
    )

    # Otro marcador

    cantidad_msifilis_clt_cv = fields.Integer(
        'Cantidad marcador sifilis clase tamizados categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_msifilis_clt_cr = fields.Integer(
        'Cantidad marcador sifilis clase tamizados categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_msifilis_clt_cpr = fields.Integer(
        'Cantidad marcador sifilis clase tamizados categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_msifilis_clt_ca = fields.Integer(
        'Cantidad marcador sifilis clase tamizados categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_msifilis_clt_total = fields.Integer(
        'Cantidad total sifilis tamizados',
        compute='_compute_total_tamizaje_msifilis_clt',
        store=True,
    )

    # otra Clase

    cantidad_msifilis_clr_cv = fields.Integer(
        'Cantidad marcador sifilis clase reactivos categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_msifilis_clr_cr = fields.Integer(
        'Cantidad marcador sifilis clase reactivos categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_msifilis_clr_cpr = fields.Integer(
        'Cantidad marcador sifilis clase reactivos categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_msifilis_clr_ca = fields.Integer(
        'Cantidad marcador sifilis clase reactivos categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_msifilis_clr_total = fields.Integer(
        'Cantidad total sifilis reactivos',
        compute='_compute_total_tamizaje_msifilis_clr',
        store=True,
    )

    # otra Clase

    cantidad_msifilis_clzg_cv = fields.Integer(
        'Cantidad marcador sifilis clase zona gris categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_msifilis_clzg_cr = fields.Integer(
        'Cantidad marcador sifilis clase zona gris categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_msifilis_clzg_cpr = fields.Integer(
        'Cantidad marcador sifilis clase zona gris categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_msifilis_clzg_ca = fields.Integer(
        'Cantidad marcador sifilis clase zona gris categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_msifilis_clzg_total = fields.Integer(
        'Cantidad total sifilis zona gris',
        compute='_compute_total_tamizaje_msifilis_clzg',
        store=True,
    )

    # Otro marcador

    cantidad_mchagas_clt_cv = fields.Integer(
        'Cantidad marcador chagas clase tamizados categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mchagas_clt_cr = fields.Integer(
        'Cantidad marcador chagas clase tamizados categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mchagas_clt_cpr = fields.Integer(
        'Cantidad marcador chagas clase tamizados categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mchagas_clt_ca = fields.Integer(
        'Cantidad marcador chagas clase tamizados categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mchagas_clt_total = fields.Integer(
        'Cantidad total chagas tamizados',
        compute='_compute_total_tamizaje_mchagas_clt',
        store=True,
    )

    # otra Clase

    cantidad_mchagas_clr_cv = fields.Integer(
        'Cantidad marcador chagas clase reactivos categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mchagas_clr_cr = fields.Integer(
        'Cantidad marcador chagas clase reactivos categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mchagas_clr_cpr = fields.Integer(
        'Cantidad marcador chagas clase reactivos categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mchagas_clr_ca = fields.Integer(
        'Cantidad marcador chagas clase reactivos categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mchagas_clr_total = fields.Integer(
        'Cantidad total chagas reactivos',
        compute='_compute_total_tamizaje_mchagas_clr',
        store=True,
    )

    # otra Clase

    cantidad_mchagas_clzg_cv = fields.Integer(
        'Cantidad marcador chagas clase zona gris categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_mchagas_clzg_cr = fields.Integer(
        'Cantidad marcador chagas clase zona gris categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_mchagas_clzg_cpr = fields.Integer(
        'Cantidad marcador chagas clase zona gris categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_mchagas_clzg_ca = fields.Integer(
        'Cantidad marcador chagas clase zona gris categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_mchagas_clzg_total = fields.Integer(
        'Cantidad total chagas zona gris',
        compute='_compute_total_tamizaje_mchagas_clzg',
        store=True,
    )

    # Otro marcador

    cantidad_motros_clt_cv = fields.Integer(
        'Cantidad marcador otros clase tamizados categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_motros_clt_cr = fields.Integer(
        'Cantidad marcador otros clase tamizados categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_motros_clt_cpr = fields.Integer(
        'Cantidad marcador otros clase tamizados categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_motros_clt_ca = fields.Integer(
        'Cantidad marcador otros clase tamizados categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_motros_clt_total = fields.Integer(
        'Cantidad total otros tamizados',
        compute='_compute_total_tamizaje_motros_clt',
        store=True,
    )

    # otra Clase

    cantidad_motros_clr_cv = fields.Integer(
        'Cantidad marcador otros clase reactividad categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_motros_clr_cr = fields.Integer(
        'Cantidad marcador otros clase reactividad categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_motros_clr_cpr = fields.Integer(
        'Cantidad marcador otros clase reactividad categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_motros_clr_ca = fields.Integer(
        'Cantidad marcador otros clase reactividad categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_motros_clr_total = fields.Integer(
        'Cantidad total otros reactividad',
        compute='_compute_total_tamizaje_motros_clr',
        store=True,
    )

    # otra Clase

    cantidad_motros_clzg_cv = fields.Integer(
        'Cantidad marcador otros clase zona gris categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_motros_clzg_cr = fields.Integer(
        'Cantidad marcador otros clase zona gris categoría reposicion',
        track_visibility='onchange'
    )

    cantidad_motros_clzg_cpr = fields.Integer(
        'Cantidad marcador otros clase zona gris categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_motros_clzg_ca = fields.Integer(
        'Cantidad marcador otros clase zona gris categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_motros_clzg_total = fields.Integer(
        'Cantidad total otros zona gris',
        compute='_compute_total_tamizaje_motros_clzg',
        store=True,
    )

    cantidad_total_tamizaje_unidad = fields.Integer(
        'Cantidad total de Tamizaje unidad',
        compute='_compute_total_tamizaje_unidad',
        store=True,
    )

    reactivos_tamizados_vih = fields.Float(
        'Division Reactivos entre Tamizados VIH',
        compute='_compute_reactivos_tamizados_vih',
        store=True,
    )

    reactivos_tamizados_hbsag = fields.Float(
        'Division Reactivos entre Tamizados HBsAG',
        compute='_compute_reactivos_tamizados_hbsag',
        store=True,
    )

    reactivos_tamizados_hepc = fields.Float(
        'Division Reactivos entre Tamizados Hep C',
        compute='_compute_reactivos_tamizados_hepc',
        store=True,
    )

    reactivos_tamizados_antihbc = fields.Float(
        'Division Reactivos entre Tamizados Anti-HBc',
        compute='_compute_reactivos_tamizados_antihbc',
        store=True,
    )

    reactivos_tamizados_htlv = fields.Float(
        'Division Reactivos entre Tamizados HTLV',
        compute='_compute_reactivos_tamizados_htlv',
        store=True,
    )

    reactivos_tamizados_sifilis = fields.Float(
        'Division Reactivos entre Tamizados Sifilis',
        compute='_compute_reactivos_tamizados_sifilis',
        store=True,
    )

    reactivos_tamizados_chagas = fields.Float(
        'Division Reactivos entre Tamizados Chagas',
        compute='_compute_reactivos_tamizados_chagas',
        store=True,
    )

    reactivos_tamizados_otros = fields.Float(
        'Division Reactivos entre Tamizados Otros',
        compute='_compute_reactivos_tamizados_otros',
        store=True,
    )

    # Reactividad

    cantidad_unr_cv = fields.Integer(
        'Cantidad no reactivo categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_unr_cr = fields.Integer(
        'Cantidad no reactivo categoría reactivo',
        track_visibility='onchange'
    )

    cantidad_unr_cpr = fields.Integer(
        'Cantidad no reactivo categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_unr_ca = fields.Integer(
        'Cantidad no reactivo categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_unr_total = fields.Integer(
        'Cantidad total no reactivos',
        compute='_compute_total_reactividad_unr',
        store=True,
    )

    # Reactivos

    cantidad_ur_cv = fields.Integer(
        'Cantidad reactivo categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_ur_cr = fields.Integer(
        'Cantidad reactivo categoría reactivo',
        track_visibility='onchange'
    )

    cantidad_ur_cpr = fields.Integer(
        'Cantidad reactivo categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_ur_ca = fields.Integer(
        'Cantidad reactivo categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_ur_total = fields.Integer(
        'Cantidad total reactivos',
        compute='_compute_total_reactividad_ur',
        store=True,
    )

    # Zona Gris

    cantidad_uzg_cv = fields.Integer(
        'Cantidad zona gris categoría voluntario',
        track_visibility='onchange'
    )

    cantidad_uzg_cr = fields.Integer(
        'Cantidad zona gris categoría reactivo',
        track_visibility='onchange'
    )

    cantidad_uzg_cpr = fields.Integer(
        'Cantidad zona gris categoría presuntamente remunerado',
        track_visibility='onchange'
    )

    cantidad_uzg_ca = fields.Integer(
        'Cantidad zona gris categoría autólogo',
        track_visibility='onchange'
    )

    cantidad_uzg_total = fields.Integer(
        'Cantidad total zona gris',
        compute='_compute_total_reactividad_uzg',
        store=True,
    )

    # PARTICIPACIÓN EN PROGRAMA DE EVALUACIÓN EXTERNA DE LA CALIDAD DE TAMIZAJE

    cantidad_mvih_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    cantidad_mhbsag_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    cantidad_mhepc_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    cantidad_mantihbc_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    cantidad_mhtlv_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    cantidad_msifilis_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    cantidad_mchagas_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    cantidad_motros_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )

    cantidad_mvih_s = fields.Boolean(
        'Cantidad marcador VIH si',
        track_visibility='onchange'
    )

    cantidad_mvih_n = fields.Boolean(
        'Cantidad marcador VIH no',
        track_visibility='onchange'
    )

    # Marcador

    cantidad_mhbsag_s = fields.Boolean(
        'Cantidad marcador VIH si',
        track_visibility='onchange'
    )

    cantidad_mhbsag_n = fields.Boolean(
        'Cantidad marcador VIH no',
        track_visibility='onchange'
    )

    # Marcador

    cantidad_mhepc_s = fields.Boolean(
        'Cantidad marcador Hep C si',
        track_visibility='onchange'
    )

    cantidad_mhepc_n = fields.Boolean(
        'Cantidad marcador Hep C no',
        track_visibility='onchange'
    )

    # Marcador

    cantidad_mantihbc_s = fields.Boolean(
        'Cantidad marcador Anti-HBc si',
        track_visibility='onchange'
    )

    cantidad_mantihbc_n = fields.Boolean(
        'Cantidad marcador Anti-HBc no',
        track_visibility='onchange'
    )

    # Marcador

    cantidad_mhtlv_s = fields.Boolean(
        'Cantidad marcador HTLV I/II si',
        track_visibility='onchange'
    )

    cantidad_mhtlv_n = fields.Boolean(
        'Cantidad marcador HTLV I/II no',
        track_visibility='onchange'
    )

    # Marcador

    cantidad_msifilis_s = fields.Boolean(
        'Cantidad marcador Sifilis si',
        track_visibility='onchange'
    )

    cantidad_msifilis_n = fields.Boolean(
        'Cantidad marcador Sifilis no',
        track_visibility='onchange'
    )

    # Marcador

    cantidad_mchagas_s = fields.Boolean(
        'Cantidad marcador Chagas si',
        track_visibility='onchange'
    )

    cantidad_mchagas_n = fields.Boolean(
        'Cantidad marcador Chagas no',
        track_visibility='onchange'
    )

    # Marcador

    cantidad_motros_s = fields.Boolean(
        'Cantidad marcador Otros si',
        track_visibility='onchange'
    )

    cantidad_motros_n = fields.Boolean(
        'Cantidad marcador Otros no',
        track_visibility='onchange'
    )

    # PRODUCCION DE HEMOCOMPONENTES UNIDAD SANGRE

    produccion_unidad_sangre_ids = fields.One2many(
        'hemored.ficha_produccion_unidad_sangre.line',
        'ficha_id',
        default=lambda self: _default_tipo_unidad_sangre(self),
        track_visibility='onchange'
    )

    cantidad_total_produccion_unidad_sangre = fields.Integer(
        'Cantidad total de producción unidad sangre',
        compute='_compute_total_produccion_unidad_sangre',
        store=True,
    )

    # PRODUCCION DE HEMOCOMPONENTES

    hemocomponente_ids = fields.One2many(
        'hemored.ficha_produccion_hemocomponente.line',
        'ficha_id',
        default=lambda self: _default_hemocomponente(self),
        track_visibility='onchange'
    )

    cantidad_total_hemocomponente = fields.Integer(
        'Cantidad total de producción hemocomponente',
        compute='_compute_total_hemocomponente',
        store=True,
    )

    # USO DE HEMOCOMPONENTES

    cantidad_gh1_pact = fields.Integer(
        'Cantidad grupo edad menor a 5 de pacientes transfundidos',
        track_visibility='onchange'
    )

    cantidad_gh1_hst = fields.Integer(
        'Cantidad grupo edad menor a 5 de Sangre Total',
        track_visibility='onchange'
    )

    cantidad_gh1_hgr = fields.Integer(
        'Cantidad grupo edad menor a 5 de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_gh1_hpfc = fields.Integer(
        'Cantidad grupo edad menor a 5 de Plasma Fresco Congelado',
        track_visibility='onchange'
    )

    cantidad_gh1_hc = fields.Integer(
        'Cantidad grupo edad menor a 5 de Crioprecipitado',
        track_visibility='onchange'
    )

    cantidad_gh1_hp = fields.Integer(
        'Cantidad grupo edad menor a 5 de plaquetas',
        track_visibility='onchange'
    )

    cantidad_gh1_hap = fields.Integer(
        'Cantidad grupo edad menor a 5 de aféresis de plaquetas',
        track_visibility='onchange'
    )

    cantidad_gh1_hagr = fields.Integer(
        'Cantidad grupo edad menor a 5 de aféresis de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_gh1_haplasma = fields.Integer(
        'Cantidad grupo edad menor a 5 de aféresis de plasma',
        track_visibility='onchange'
    )

    cantidad_gh1_total = fields.Integer(
        'Cantidad total de grupo edad menor a 5',
        compute='_compute_total_uso_hemocomponentes_gh1',
        store=True,
    )

    # Otro Grupo Edad

    cantidad_gh2_pact = fields.Integer(
        'Cantidad de pacientes transfundidos en grupo edad de 5-9 años',
        track_visibility='onchange'
    )

    cantidad_gh2_hst = fields.Integer(
        'Cantidad de Sangre Tota en grupo edad de 5-9 años',
        track_visibility='onchange'
    )

    cantidad_gh2_hgr = fields.Integer(
        'Cantidad de globulos rojos en grupo edad de 5-9 años',
        track_visibility='onchange'
    )

    cantidad_gh2_hpfc = fields.Integer(
        'Cantidad de Plasma Fresco Congelado en grupo edad de 5-9 años',
        track_visibility='onchange'
    )

    cantidad_gh2_hc = fields.Integer(
        'Cantidad de Crioprecipitado en grupo edad de 5-9 años',
        track_visibility='onchange'
    )

    cantidad_gh2_hp = fields.Integer(
        'Cantidad de plaquetas en grupo edad de 5-9 años',
        track_visibility='onchange'
    )

    cantidad_gh2_hap = fields.Integer(
        'Cantidad de aféresis de plaquetas en grupo edad de 5-9 años',
        track_visibility='onchange'
    )

    cantidad_gh2_hagr = fields.Integer(
        'Cantidad de aféresis de globulos rojos en grupo edad de 5-9 años',
        track_visibility='onchange'
    )

    cantidad_gh2_haplasma = fields.Integer(
        'Cantidad de aféresis de plasma en grupo edad de 5-9 años',
        track_visibility='onchange'
    )

    cantidad_gh2_total = fields.Integer(
        'Cantidad total de grupo edad de 5-9 años',
        compute='_compute_total_uso_hemocomponentes_gh2',
        store=True,
    )

    # Otro Grupo Edad

    cantidad_gh3_pact = fields.Integer(
        'Cantidad de pacientes transfundidos en grupo edad de 10-19 años',
        track_visibility='onchange'
    )

    cantidad_gh3_hst = fields.Integer(
        'Cantidad de Sangre Tota en grupo edad de 10-19 años',
        track_visibility='onchange'
    )

    cantidad_gh3_hgr = fields.Integer(
        'Cantidad de globulos rojos en grupo edad de 10-19 años',
        track_visibility='onchange'
    )

    cantidad_gh3_hpfc = fields.Integer(
        'Cantidad de Plasma Fresco Congelado en grupo edad de 10-19 años',
        track_visibility='onchange'
    )

    cantidad_gh3_hc = fields.Integer(
        'Cantidad de Crioprecipitado en grupo edad de 10-19 años',
        track_visibility='onchange'
    )

    cantidad_gh3_hp = fields.Integer(
        'Cantidad de plaquetas en grupo edad de 10-19 años',
        track_visibility='onchange'
    )

    cantidad_gh3_hap = fields.Integer(
        'Cantidad de aféresis de plaquetas en grupo edad de 10-19 años',
        track_visibility='onchange'
    )

    cantidad_gh3_hagr = fields.Integer(
        'Cantidad de aféresis de globulos rojos en grupo edad de 10-19 años',
        track_visibility='onchange'
    )

    cantidad_gh3_haplasma = fields.Integer(
        'Cantidad de aféresis de plasma en grupo edad de 10-19 años',
        track_visibility='onchange'
    )

    cantidad_gh3_total = fields.Integer(
        'Cantidad total de grupo edad de 10-19 años',
        compute='_compute_total_uso_hemocomponentes_gh3',
        store=True,
    )

    # Otro Grupo Edad

    cantidad_gh4_pact = fields.Integer(
        'Cantidad de pacientes transfundidos en grupo edad de 20-34 años',
        track_visibility='onchange'
    )

    cantidad_gh4_hst = fields.Integer(
        'Cantidad de Sangre Tota en grupo edad de 20-34 años',
        track_visibility='onchange'
    )

    cantidad_gh4_hgr = fields.Integer(
        'Cantidad de globulos rojos en grupo edad de 20-34 años',
        track_visibility='onchange'
    )

    cantidad_gh4_hpfc = fields.Integer(
        'Cantidad de Plasma Fresco Congelado en grupo edad de 20-34 años',
        track_visibility='onchange'
    )

    cantidad_gh4_hc = fields.Integer(
        'Cantidad de Crioprecipitado en grupo edad de 20-34 años',
        track_visibility='onchange'
    )

    cantidad_gh4_hp = fields.Integer(
        'Cantidad de plaquetas en grupo edad de 20-34 años',
        track_visibility='onchange'
    )

    cantidad_gh4_hap = fields.Integer(
        'Cantidad de aféresis de plaquetas en grupo edad de 20-34 años',
        track_visibility='onchange'
    )

    cantidad_gh4_hagr = fields.Integer(
        'Cantidad de aféresis de globulos rojos en grupo edad de 20-34 años',
        track_visibility='onchange'
    )

    cantidad_gh4_haplasma = fields.Integer(
        'Cantidad de aféresis de plasma en grupo edad de 20-34 años',
        track_visibility='onchange'
    )

    cantidad_gh4_total = fields.Integer(
        'Cantidad total de grupo edad de 20-34 años',
        compute='_compute_total_uso_hemocomponentes_gh4',
        store=True,
    )

    # Otro Grupo Edad

    cantidad_gh5_pact = fields.Integer(
        'Cantidad de pacientes transfundidos en grupo edad 35 - 49 años',
        track_visibility='onchange'
    )

    cantidad_gh5_hst = fields.Integer(
        'Cantidad de Sangre Tota en grupo edad 35 - 49 años',
        track_visibility='onchange'
    )

    cantidad_gh5_hgr = fields.Integer(
        'Cantidad de globulos rojos en grupo edad 35 - 49 años',
        track_visibility='onchange'
    )

    cantidad_gh5_hpfc = fields.Integer(
        'Cantidad de Plasma Fresco Congelado en grupo edad 35 - 49 años',
        track_visibility='onchange'
    )

    cantidad_gh5_hc = fields.Integer(
        'Cantidad de Crioprecipitado en grupo edad 35 - 49 años',
        track_visibility='onchange'
    )

    cantidad_gh5_hp = fields.Integer(
        'Cantidad de plaquetas en grupo edad 35 - 49 años',
        track_visibility='onchange'
    )

    cantidad_gh5_hap = fields.Integer(
        'Cantidad de aféresis de plaquetas en grupo edad 35 - 49 años',
        track_visibility='onchange'
    )

    cantidad_gh5_hagr = fields.Integer(
        'Cantidad de aféresis de globulos rojos en grupo edad 35 - 49 años',
        track_visibility='onchange'
    )

    cantidad_gh5_haplasma = fields.Integer(
        'Cantidad de aféresis de plasma en grupo edad 35 - 49 años',
        track_visibility='onchange'
    )

    cantidad_gh5_total = fields.Integer(
        'Cantidad total de grupo edad de 35 - 49 años',
        compute='_compute_total_uso_hemocomponentes_gh5',
        store=True,
    )

    # Otro Grupo Edad

    cantidad_gh6_pact = fields.Integer(
        'Cantidad de pacientes transfundidos en grupo edad 50 - 64 años',
        track_visibility='onchange'
    )

    cantidad_gh6_hst = fields.Integer(
        'Cantidad de Sangre Tota en grupo edad 50 - 64 años',
        track_visibility='onchange'
    )

    cantidad_gh6_hgr = fields.Integer(
        'Cantidad de globulos rojos en grupo edad 50 - 64 años',
        track_visibility='onchange'
    )

    cantidad_gh6_hpfc = fields.Integer(
        'Cantidad de Plasma Fresco Congelado en grupo edad 50 - 64 años',
        track_visibility='onchange'
    )

    cantidad_gh6_hc = fields.Integer(
        'Cantidad de Crioprecipitado en grupo edad 50 - 64 años',
        track_visibility='onchange'
    )

    cantidad_gh6_hp = fields.Integer(
        'Cantidad de plaquetas en grupo edad 50 - 64 años',
        track_visibility='onchange'
    )

    cantidad_gh6_hap = fields.Integer(
        'Cantidad de aféresis de plaquetas en grupo edad 50 - 64 años',
        track_visibility='onchange'

    )

    cantidad_gh6_hagr = fields.Integer(
        'Cantidad de aféresis de globulos rojos en grupo edad 50 - 64 años',
        track_visibility='onchange'
    )

    cantidad_gh6_haplasma = fields.Integer(
        'Cantidad de aféresis de plasma en grupo edad 50 - 64 años',
        track_visibility='onchange'
    )

    cantidad_gh6_total = fields.Integer(
        'Cantidad total de grupo edad de 50 - 64 años',
        compute='_compute_total_uso_hemocomponentes_gh6',
        store=True,
    )

    # Otro Grupo Edad

    cantidad_gh7_pact = fields.Integer(
        'Cantidad de pacientes transfundidos en grupo edad mayores a 64 años',
        track_visibility='onchange'
    )

    cantidad_gh7_hst = fields.Integer(
        'Cantidad de Sangre Tota en grupo edad mayores a 64 años',
        track_visibility='onchange'
    )

    cantidad_gh7_hgr = fields.Integer(
        'Cantidad de globulos rojos en grupo edad mayores a 64 años',
        track_visibility='onchange'
    )

    cantidad_gh7_hpfc = fields.Integer(
        'Cantidad de Plasma Fresco Congelado en grupo edad mayores a 64 años',
        track_visibility='onchange'
    )

    cantidad_gh7_hc = fields.Integer(
        'Cantidad de Crioprecipitado en grupo edad mayores a 64 años',
        track_visibility='onchange'
    )

    cantidad_gh7_hp = fields.Integer(
        'Cantidad de plaquetas en grupo edad mayores a 64 años',
        track_visibility='onchange'
    )

    cantidad_gh7_hap = fields.Integer(
        'Cantidad de aféresis de plaquetas en grupo edad mayores a 64 años',
        track_visibility='onchange'
    )

    cantidad_gh7_hagr = fields.Integer(
        'Cantidad de aféresis de globulos rojos en grupo edad mayores a 64 años',
        track_visibility='onchange'
    )

    cantidad_gh7_haplasma = fields.Integer(
        'Cantidad de aféresis de plasma en grupo edad mayores a 64 años',
        track_visibility='onchange'
    )

    cantidad_gh7_total = fields.Integer(
        'Cantidad total de grupo edad de mayores a 64 años',
        compute='_compute_total_uso_hemocomponentes_gh7',
        store=True,
    )

    # Totales

    cantidad_pact_total = fields.Integer(
        'Cantidad Total Paciente Transfundidos',
        compute='_compute_total_uso_hemocomponentes_pact',
        store=True,
    )

    cantidad_hst_total = fields.Integer(
        'Cantidad total hemocomponente sangre total',
        compute='_compute_total_uso_hemocomponentes_hst',
        store=True,
    )

    cantidad_hgr_total = fields.Integer(
        'Cantidad total hemocomponente globulos rojos',
        compute='_compute_total_uso_hemocomponentes_hgr',
        store=True,
    )

    cantidad_hpfc_total = fields.Integer(
        'Cantidad total hemocomponente plasma fresco congelado',
        compute='_compute_total_uso_hemocomponentes_hpfc',
        store=True,
    )

    cantidad_hc_total = fields.Integer(
        'Cantidad total hemocomponente crioprecipitado',
        compute='_compute_total_uso_hemocomponentes_hc',
        store=True,
    )

    cantidad_hp_total = fields.Integer(
        'Cantidad total hemocomponente plaquetas',
        compute='_compute_total_uso_hemocomponentes_hp',
        store=True,
    )

    cantidad_hap_total = fields.Integer(
        'Cantidad total hemocomponente aféresis plaquetas',
        compute='_compute_total_uso_hemocomponentes_hap',
        store=True,
    )

    cantidad_hagr_total = fields.Integer(
        'Cantidad total hemocomponente aféresis de globulos rojos',
        compute='_compute_total_uso_hemocomponentes_hagr',
        store=True,
    )

    cantidad_haplasma_total = fields.Integer(
        'Cantidad total hemocomponente aféresis de plasma',
        compute='_compute_total_uso_hemocomponentes_haplasma',
        store=True,
    )

    cantidad_uso_hemocomponentes_total_hemocomponentes = fields.Integer(
        'Cantidad total de hemocomponente',
        compute='_compute_total_uso_hemocomponentes_hemocomponentes',
        store=True,
    )

    cantidad_uso_hemocomponentes_total_gh = fields.Integer(
        'Cantidad total de hemocomponente',
        compute='_compute_total_uso_hemocomponentes_grupo_edad',
        store=True,
    )

    cantidad_uso_hemocomponentes_total = fields.Integer(
        'Cantidad total de hemocomponente',
        compute='_compute_total_uso_hemocomponentes',
        store=True,
    )

    # DEMANDA DE HEMOCOMPONENTES

    cantidad_ds_hgr = fields.Integer(
        'Cantidad demanda solicitada hemocomponente globulos rojos',
        track_visibility='onchange'
    )

    cantidad_ds_hpfc = fields.Integer(
        'Cantidad demanda solicitada hemocomponente plasma freso congelado',
        track_visibility='onchange'
    )

    cantidad_ds_hp = fields.Integer(
        'Cantidad demanda solicitada hemocomponente plasma',
        track_visibility='onchange'
    )

    cantidad_ds_hap = fields.Integer(
        'Cantidad demanda solicitada hemocomponente aféresis de plaquetas',
        track_visibility='onchange'
    )

    # no solicitadas

    cantidad_da_hgr = fields.Integer(
        'Cantidad demanda atendida hemocomponente globulos rojos',
        track_visibility='onchange'
    )

    cantidad_da_hpfc = fields.Integer(
        'Cantidad demanda atendida hemocomponente plasma freso congelado',
        track_visibility='onchange'
    )

    cantidad_da_hp = fields.Integer(
        'Cantidad demanda atendida hemocomponente plasma',
        track_visibility='onchange'
    )

    cantidad_da_hap = fields.Integer(
        'Cantidad demanda atendida hemocomponente aféresis de plaquetas',
        track_visibility='onchange'
    )

    # TRANSFERENCIA DE HEMOCOMPONENTES

    cantidad_tur_hst = fields.Integer(
        'Cantidad transferencia hemocomponente sangre total  recibidas',
        track_visibility='onchange'
    )

    cantidad_tur_hgr = fields.Integer(
        'Cantidad transferencia hemocomponente globulos rojos  recibidas',
        track_visibility='onchange'
    )

    cantidad_tur_hpfc = fields.Integer(
        'Cantidad transferencia hemocomponente plasma fresco congelado  recibidas',
        track_visibility='onchange'
    )

    cantidad_tur_hc = fields.Integer(
        'Cantidad transferencia hemocomponente crioprecipitado  recibidas',
        track_visibility='onchange'
    )

    cantidad_tur_hp = fields.Integer(
        'Cantidad transferencia hemocomponente plaquetas  recibidas',
        track_visibility='onchange'
    )

    cantidad_tur_hap = fields.Integer(
        'Cantidad transferencia hemocomponente aféresis de plaquetas  recibidas',
        track_visibility='onchange'
    )

    cantidad_tur_hagr = fields.Integer(
        'Cantidad transferencia hemocomponente aféresis de globulos rojos  recibidas',
        track_visibility='onchange'
    )

    cantidad_tur_total = fields.Integer(
        'Cantidad transferencia hemocomponente total recibidas',
        compute='_compute_total_transferencia_hemocomponentes_tur',
        store=True,
    )

    # Unidades Trasnferidas

    cantidad_tut_hst = fields.Integer(
        'Cantidad transferencia hemocomponente sangre total  transferidas',
        track_visibility='onchange'
    )

    cantidad_tut_hgr = fields.Integer(
        'Cantidad transferencia hemocomponente globulos rojos  transferidas',
        track_visibility='onchange'
    )

    cantidad_tut_hpfc = fields.Integer(
        'Cantidad transferencia hemocomponente plasma fresco congelado  transferidas',
        track_visibility='onchange'
    )

    cantidad_tut_hc = fields.Integer(
        'Cantidad transferencia hemocomponente crioprecipitado  transferidas',
        track_visibility='onchange'
    )

    cantidad_tut_hp = fields.Integer(
        'Cantidad transferencia hemocomponente plaquetas  transferidas',
        track_visibility='onchange'
    )

    cantidad_tut_hap = fields.Integer(
        'Cantidad transferencia hemocomponente aféresis de plaquetas  transferidas',
        track_visibility='onchange'
    )

    cantidad_tut_hagr = fields.Integer(
        'Cantidad transferencia hemocomponente aféresis de globulos rojos  transferidas',
        track_visibility='onchange'
    )

    cantidad_tut_total = fields.Integer(
        'Cantidad transferencia hemocomponente total transferidas',
        compute='_compute_total_transferencia_hemocomponentes_tut',
        store=True,
    )

    # CAUSAS REACCION ADVERSA

    causa_reaccion_adversa_ids = fields.One2many(
        'hemored.ficha_causa_reaccion_adversa.line',
        'ficha_id',
        default=lambda self: _default_causa_reaccion_graves(self),
        track_visibility='onchange'
    )

    cantidad_total_causa_reaccion_adversa = fields.Integer(
        'Cantidad total de producción causa reaccion adversa',
        compute='_compute_total_causa_reaccion_adversa',
        store=True,
    )

    # ELIMINACIÓN DE SANGRE Y HEMOCOMPONENTES

    cantidad_cv_hst = fields.Integer(
        'Cantidad eliminados por vencimiento de Sangre Total',
        track_visibility='onchange'
    )

    cantidad_cv_hgr = fields.Integer(
        'Cantidad eliminados por vencimiento de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_cv_hpfc = fields.Integer(
        'Cantidad eliminados por vencimiento de Plasma Fresco Congelado',
        track_visibility='onchange'
    )

    cantidad_cv_hc = fields.Integer(
        'Cantidad eliminados por vencimiento de Crioprecipitado',
        track_visibility='onchange'
    )

    cantidad_cv_hp = fields.Integer(
        'Cantidad eliminados por vencimiento de plaquetas',
        track_visibility='onchange'
    )

    cantidad_cv_hap = fields.Integer(
        'Cantidad eliminados por vencimiento de aféresis de plaquetas',
        track_visibility='onchange'
    )

    cantidad_cv_hagr = fields.Integer(
        'Cantidad eliminados por vencimiento de aféresis de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_cv_haplasma = fields.Integer(
        'Cantidad eliminados por vencimiento de aféresis de plasma',
        track_visibility='onchange'
    )

    cantidad_cv_total = fields.Integer(
        'Cantidad eliminados por vencimiento de total',
        compute='_compute_total_causas_eliminacion_hemocomponentes_cv',
        store=True,
    )

    # Otra Causa

    cantidad_cmitt_hst = fields.Integer(
        'Cantidad eliminados por marcadores itt de Sangre Total',
        track_visibility='onchange'
    )

    cantidad_cmitt_hgr = fields.Integer(
        'Cantidad eliminados por marcadores itt de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_cmitt_hpfc = fields.Integer(
        'Cantidad eliminados por marcadores itt de Plasma Fresco Congelado',
        track_visibility='onchange'
    )

    cantidad_cmitt_hc = fields.Integer(
        'Cantidad eliminados por marcadores itt de Crioprecipitado',
        track_visibility='onchange'
    )

    cantidad_cmitt_hp = fields.Integer(
        'Cantidad eliminados por marcadores itt de plaquetas',
        track_visibility='onchange'
    )

    cantidad_cmitt_hap = fields.Integer(
        'Cantidad eliminados por marcadores itt de aféresis de plaquetas',
        track_visibility='onchange'
    )

    cantidad_cmitt_hagr = fields.Integer(
        'Cantidad eliminados por marcadores itt de aféresis de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_cmitt_haplasma = fields.Integer(
        'Cantidad eliminados por marcadores itt de aféresis de plasma',
        track_visibility='onchange'
    )

    cantidad_cmitt_total = fields.Integer(
        'Cantidad eliminados por marcadores itt de total',
        compute='_compute_total_causas_eliminacion_hemocomponentes_cmitt',
        store=True,
    )

    # Otra Causa

    cantidad_ca_hst = fields.Integer(
        'Cantidad eliminados por almacenamiento de Sangre Total',
        track_visibility='onchange'
    )

    cantidad_ca_hgr = fields.Integer(
        'Cantidad eliminados por almacenamiento de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_ca_hpfc = fields.Integer(
        'Cantidad eliminados por almacenamiento de Plasma Fresco Congelado',
        track_visibility='onchange'
    )

    cantidad_ca_hc = fields.Integer(
        'Cantidad eliminados por almacenamiento de Crioprecipitado',
        track_visibility='onchange'
    )

    cantidad_ca_hp = fields.Integer(
        'Cantidad eliminados por almacenamiento de plaquetas',
        track_visibility='onchange'
    )

    cantidad_ca_hap = fields.Integer(
        'Cantidad eliminados por almacenamiento de aféresis de plaquetas',
        track_visibility='onchange'
    )

    cantidad_ca_hagr = fields.Integer(
        'Cantidad eliminados por almacenamiento de aféresis de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_ca_haplasma = fields.Integer(
        'Cantidad eliminados por almacenamiento de aféresis de plasma',
        track_visibility='onchange'
    )

    cantidad_ca_total = fields.Integer(
        'Cantidad eliminados por almacenamiento de total',
        compute='_compute_total_causas_eliminacion_hemocomponentes_ca',
        store=True,
    )

    # Otra Causa

    cantidad_ct_hst = fields.Integer(
        'Cantidad eliminados por transporte de Sangre Total',
        track_visibility='onchange'
    )

    cantidad_ct_hgr = fields.Integer(
        'Cantidad eliminados por transporte de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_ct_hpfc = fields.Integer(
        'Cantidad eliminados por transporte de Plasma Fresco Congelado',
        track_visibility='onchange'
    )

    cantidad_ct_hc = fields.Integer(
        'Cantidad eliminados por transporte de Crioprecipitado',
        track_visibility='onchange'
    )

    cantidad_ct_hp = fields.Integer(
        'Cantidad eliminados por transporte de plaquetas',
        track_visibility='onchange'
    )

    cantidad_ct_hap = fields.Integer(
        'Cantidad eliminados por transporte de aféresis de plaquetas',
        track_visibility='onchange'
    )

    cantidad_ct_hagr = fields.Integer(
        'Cantidad eliminados por transporte de aféresis de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_ct_haplasma = fields.Integer(
        'Cantidad eliminados por transporte de aféresis de plasma',
        track_visibility='onchange'
    )

    cantidad_ct_total = fields.Integer(
        'Cantidad eliminados por transporte de total',
        compute='_compute_total_causas_eliminacion_hemocomponentes_ct',
        store=True,
    )

    # Otra Causa

    cantidad_cp_hst = fields.Integer(
        'Cantidad eliminados por procesamiento de Sangre Total',
        track_visibility='onchange'
    )

    cantidad_cp_hgr = fields.Integer(
        'Cantidad eliminados por procesamiento de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_cp_hpfc = fields.Integer(
        'Cantidad eliminados por procesamiento de Plasma Fresco Congelado',
        track_visibility='onchange'
    )

    cantidad_cp_hc = fields.Integer(
        'Cantidad eliminados por procesamiento de Crioprecipitado',
        track_visibility='onchange'
    )

    cantidad_cp_hp = fields.Integer(
        'Cantidad eliminados por procesamiento de plaquetas',
        track_visibility='onchange'
    )

    cantidad_cp_hap = fields.Integer(
        'Cantidad eliminados por procesamiento de aféresis de plaquetas',
        track_visibility='onchange'
    )

    cantidad_cp_hagr = fields.Integer(
        'Cantidad eliminados por procesamiento de aféresis de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_cp_haplasma = fields.Integer(
        'Cantidad eliminados por procesamiento de aféresis de plasma',
        track_visibility='onchange'
    )

    cantidad_cp_total = fields.Integer(
        'Cantidad eliminados por procesamiento de total',
        compute='_compute_total_causas_eliminacion_hemocomponentes_cp',
        store=True,
    )

    # Otra Causa

    cantidad_co_hst = fields.Integer(
        'Cantidad eliminados por otros de Sangre Total',
        track_visibility='onchange'
    )

    cantidad_co_hgr = fields.Integer(
        'Cantidad eliminados por otros de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_co_hpfc = fields.Integer(
        'Cantidad eliminados por otros de Plasma Fresco Congelado',
        track_visibility='onchange'
    )

    cantidad_co_hc = fields.Integer(
        'Cantidad eliminados por otros de Crioprecipitado',
        track_visibility='onchange'
    )

    cantidad_co_hp = fields.Integer(
        'Cantidad eliminados por otros de plaquetas',
        track_visibility='onchange'
    )

    cantidad_co_hap = fields.Integer(
        'Cantidad eliminados por otros de aféresis de plaquetas',
        track_visibility='onchange'
    )

    cantidad_co_hagr = fields.Integer(
        'Cantidad eliminados por otros de aféresis de globulos rojos',
        track_visibility='onchange'
    )

    cantidad_co_haplasma = fields.Integer(
        'Cantidad eliminados por otros de aféresis de plasma',
        track_visibility='onchange'
    )

    cantidad_co_total = fields.Integer(
        'Cantidad eliminados por otros de total',
        compute='_compute_total_causas_eliminacion_hemocomponentes_co',
        store=True,
    )

    # Eliminacion y Produccion de Hemocomponentes

    cantidad_ctotal_hst = fields.Integer(
        'Cantidad eliminados de sangre total',
        compute='_compute_total_causas_eliminacion_hemocomponentes_hst',
        store=True,
    )
    cantidad_ptotal_st = fields.Integer(
        'Cantidad producida de sangre total',
        compute='_compute_total_producida_hemocomponente',
        store=True,
    )
    porcentaje_st = fields.Float(
        '% de unidades de sangre total eliminada',
        compute='_compute_st',
        store=True,
    )

    cantidad_ctotal_hgr = fields.Integer(
        'Cantidad eliminados de globulos rojos',
        compute='_compute_total_causas_eliminacion_hemocomponentes_hgr',
        store=True,
    )
    cantidad_ptotal_gl = fields.Integer(
        'Cantidad producida de globulo rojo',
        compute='_compute_total_producida_hemocomponente',
        store=True,
    )
    porcentaje_gl = fields.Float(
        '% de unidades de globulo rojo eliminada',
        compute='_compute_gl',
        store=True,
    )

    cantidad_ctotal_hpfc = fields.Integer(
        'Cantidad eliminados de plasma fresco congelado',
        compute='_compute_total_causas_eliminacion_hemocomponentes_hpfc',
        store=True,
    )
    cantidad_ptotal_pfc = fields.Integer(
        'Cantidad producida de plasma fresco congelado',
        compute='_compute_total_producida_hemocomponente',
        store=True,
    )
    porcentaje_pfc = fields.Float(
        '% de unidades de plasma fresco congelado eliminada',
        compute='_compute_pfc',
        store=True,
    )

    cantidad_ctotal_hc = fields.Integer(
        'Cantidad eliminados de crioprecipitado',
        compute='_compute_total_causas_eliminacion_hemocomponentes_hc',
        store=True,
    )
    cantidad_ptotal_c = fields.Integer(
        'Cantidad producida de crioprecipitado',
        compute='_compute_total_producida_hemocomponente',
        store=True,
    )
    porcentaje_c = fields.Float(
        '% de unidades de crioprecipitado eliminada',
        compute='_compute_c',
        store=True,
    )

    cantidad_ctotal_hp = fields.Integer(
        'Cantidad eliminados de plaquetas',
        compute='_compute_total_causas_eliminacion_hemocomponentes_hp',
        store=True,
    )
    cantidad_ptotal_pla = fields.Integer(
        'Cantidad producida de plaquetas',
        compute='_compute_total_producida_hemocomponente',
        store=True,
    )
    porcentaje_pla = fields.Float(
        '% de unidades de plaquetas eliminada',
        compute='_compute_pla',
        store=True,
    )

    cantidad_ctotal_hap = fields.Integer(
        'Cantidad eliminados de aféresis de plaquetas',
        compute='_compute_total_causas_eliminacion_hemocomponentes_hap',
        store=True,
    )
    cantidad_ptotal_af = fields.Integer(
        'Cantidad producida de aféresis de plaquetas',
        compute='_compute_total_producida_hemocomponente',
        store=True,
    )
    porcentaje_af = fields.Float(
        '% de unidades de aféresis de plaquetas eliminada',
        compute='_compute_af',
        store=True,
    )

    cantidad_ctotal_hagr = fields.Integer(
        'Cantidad eliminados de aféresis de globulos rojos',
        compute='_compute_total_causas_eliminacion_hemocomponentes_hagr',
        store=True,
    )
    cantidad_ptotal_afgl = fields.Integer(
        'Cantidad producida de aféresis de globulos rojos',
        compute='_compute_total_producida_hemocomponente',
        store=True,
    )
    porcentaje_afgl = fields.Float(
        '% de unidades de aféresis de globulos rojos eliminada',
        compute='_compute_afgl',
        store=True,
    )

    cantidad_ctotal_haplasma = fields.Integer(
        'Cantidad eliminados de aféresis de plasma',
        compute='_compute_total_causas_eliminacion_hemocomponentes_haplasma',
        store=True,
    )
    cantidad_ptotal_afpla = fields.Integer(
        'Cantidad producida de aféresis de plasma',
        compute='_compute_total_producida_hemocomponente',
        store=True,
    )
    porcentaje_afpla = fields.Float(
        '% de unidades de aféresis de plasma eliminada',
        compute='_compute_afpla',
        store=True,
    )

    cantidad_ctotal_hemocomponentes = fields.Integer(
        'Cantidad eliminados de hemocomponentes',
        compute='_compute_total_causas_eliminacion_hemocomponentes',
        store=True,
    )

    cantidad_ctotal_categorias = fields.Integer(
        'Cantidad eliminados de categorías',
        compute='_compute_total_causas_eliminacion_categorias',
        store=True,
    )

    cantidad_ctotal = fields.Integer(
        'Cantidad eliminados',
        compute='_compute_total_causas_eliminacion',
        store=True,
    )

    special = fields.Boolean(
        string='Especial',
        compute='_compute_especial',
    )

    @api.one
    @api.depends('state')
    def _compute_status(self):
        self.nombre_state = self.state.upper()

    @api.model
    def _selection_tipo_banco(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_banco')

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(MNFichaEstadistica, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        es_coordinador_establecimiento = self.env.user.has_group('hemored.group_coordinador_establecimiento_hemored')
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            modifiers = '{"readonly": true}'
            if es_coordinador_establecimiento:
                for node in doc.xpath("//field[@name='inicio_fecha_registro']"):
                    node.set('modifiers', modifiers)
                for node in doc.xpath("//field[@name='fin_fecha_registro']"):
                    node.set('modifiers', modifiers)
            res['arch'] = etree.tostring(doc)
        return res

    tuple_attrs = (
        'cantidad_pe_x_ca', 'cantidad_pe_x_cvim', 'cantidad_pe_x_cvem', 'cantidad_pe_x_cr',
        'cantidad_pe_x_cpr', 'cantidad_pd_x_ca', 'cantidad_pd_x_cvim', 'cantidad_pd_x_cvem',
        'cantidad_pd_x_cr', 'cantidad_pd_x_cpr', 'cantidad_padi_x_ca', 'cantidad_padi_x_cvim',
        'cantidad_padi_x_cvem', 'cantidad_padi_x_cr', 'cantidad_padi_x_cpr', 'cantidad_padc_x_ca',
        'cantidad_padc_x_cvim', 'cantidad_padc_x_cvem', 'cantidad_padc_x_cr', 'cantidad_padc_x_cpr',
        'cantidad_donacion_h', 'cantidad_donacion_m', 'cantidad_mvih_clt_cv', 'cantidad_mvih_clt_cr',
        'cantidad_mvih_clt_cpr', 'cantidad_mvih_clt_ca', 'cantidad_mvih_clr_cv',
        'cantidad_mvih_clr_cr', 'cantidad_mvih_clr_cpr', 'cantidad_mvih_clr_ca',
        'cantidad_mvih_clzg_cv', 'cantidad_mvih_clzg_cr', 'cantidad_mvih_clzg_cpr',
        'cantidad_mvih_clzg_ca', 'cantidad_mhbsag_clt_cv', 'cantidad_mhbsag_clt_cr',
        'cantidad_mhbsag_clt_cpr', 'cantidad_mhbsag_clt_ca', 'cantidad_mhbsag_clr_cv',
        'cantidad_mhbsag_clr_cr', 'cantidad_mhbsag_clr_cpr', 'cantidad_mhbsag_clr_ca',
        'cantidad_mhbsag_clzg_cv', 'cantidad_mhbsag_clzg_cr', 'cantidad_mhbsag_clzg_cpr',
        'cantidad_mhbsag_clzg_ca', 'cantidad_mhepc_clt_cv', 'cantidad_mhepc_clt_cr',
        'cantidad_mhepc_clt_cpr', 'cantidad_mhepc_clt_ca', 'cantidad_mhepc_clr_cv',
        'cantidad_mhepc_clr_cr', 'cantidad_mhepc_clr_cpr', 'cantidad_mhepc_clr_ca',
        'cantidad_mhepc_clzg_cv', 'cantidad_mhepc_clzg_cr', 'cantidad_mhepc_clzg_cpr',
        'cantidad_mhepc_clzg_ca', 'cantidad_mantihbc_clt_cv', 'cantidad_mantihbc_clt_cr',
        'cantidad_mantihbc_clt_cpr', 'cantidad_mantihbc_clt_ca', 'cantidad_mantihbc_clr_cv',
        'cantidad_mantihbc_clr_cr', 'cantidad_mantihbc_clr_cpr', 'cantidad_mantihbc_clr_ca',
        'cantidad_mantihbc_clzg_cv', 'cantidad_mantihbc_clzg_cr', 'cantidad_mantihbc_clzg_cpr',
        'cantidad_mantihbc_clzg_ca', 'cantidad_mhtlv_clt_cv', 'cantidad_mhtlv_clt_cr',
        'cantidad_mhtlv_clt_cpr', 'cantidad_mhtlv_clt_ca', 'cantidad_mhtlv_clr_cv',
        'cantidad_mhtlv_clr_cr', 'cantidad_mhtlv_clr_cpr', 'cantidad_mhtlv_clr_ca',
        'cantidad_mhtlv_clzg_cv', 'cantidad_mhtlv_clzg_cr', 'cantidad_mhtlv_clzg_cpr',
        'cantidad_mhtlv_clzg_ca', 'cantidad_msifilis_clt_cv', 'cantidad_msifilis_clt_cr',
        'cantidad_msifilis_clt_cpr', 'cantidad_msifilis_clt_ca', 'cantidad_msifilis_clr_cv',
        'cantidad_msifilis_clr_cr', 'cantidad_msifilis_clr_cpr', 'cantidad_msifilis_clr_ca',
        'cantidad_msifilis_clzg_cv', 'cantidad_msifilis_clzg_cr', 'cantidad_msifilis_clzg_cpr',
        'cantidad_msifilis_clzg_ca', 'cantidad_mchagas_clt_cv', 'cantidad_mchagas_clt_cr',
        'cantidad_mchagas_clt_cpr', 'cantidad_mchagas_clt_ca', 'cantidad_mchagas_clr_cv',
        'cantidad_mchagas_clr_cr', 'cantidad_mchagas_clr_cpr', 'cantidad_mchagas_clr_ca',
        'cantidad_mchagas_clzg_cv', 'cantidad_mchagas_clzg_cr', 'cantidad_mchagas_clzg_cpr',
        'cantidad_mchagas_clzg_ca', 'cantidad_motros_clt_cv', 'cantidad_motros_clt_cr',
        'cantidad_motros_clt_cpr', 'cantidad_motros_clt_ca', 'cantidad_motros_clr_cv',
        'cantidad_motros_clr_cr', 'cantidad_motros_clr_cpr', 'cantidad_motros_clr_ca',
        'cantidad_motros_clzg_cv', 'cantidad_motros_clzg_cr', 'cantidad_motros_clzg_cpr',
        'cantidad_motros_clzg_ca', 'cantidad_unr_cv', 'cantidad_unr_cr', 'cantidad_unr_cpr',
        'cantidad_unr_ca', 'cantidad_ur_cv', 'cantidad_ur_cr', 'cantidad_ur_cpr', 'cantidad_ur_ca',
        'cantidad_uzg_cv', 'cantidad_uzg_cr', 'cantidad_uzg_cpr', 'cantidad_uzg_ca',
        'cantidad_gh1_pact', 'cantidad_gh1_hst', 'cantidad_gh1_hgr', 'cantidad_gh1_hpfc',
        'cantidad_gh1_hc', 'cantidad_gh1_hp', 'cantidad_gh1_hap', 'cantidad_gh1_hagr',
        'cantidad_gh1_haplasma', 'cantidad_gh2_pact', 'cantidad_gh2_hst', 'cantidad_gh2_hgr',
        'cantidad_gh2_hpfc', 'cantidad_gh2_hc', 'cantidad_gh2_hp', 'cantidad_gh2_hap',
        'cantidad_gh2_hagr', 'cantidad_gh2_haplasma', 'cantidad_gh3_pact', 'cantidad_gh3_hst',
        'cantidad_gh3_hgr', 'cantidad_gh3_hpfc', 'cantidad_gh3_hc', 'cantidad_gh3_hp',
        'cantidad_gh3_hap', 'cantidad_gh3_hagr', 'cantidad_gh3_haplasma', 'cantidad_gh4_pact',
        'cantidad_gh4_hst', 'cantidad_gh4_hgr', 'cantidad_gh4_hpfc', 'cantidad_gh4_hc',
        'cantidad_gh4_hp', 'cantidad_gh4_hap', 'cantidad_gh4_hagr', 'cantidad_gh4_haplasma',
        'cantidad_gh5_pact', 'cantidad_gh5_hst', 'cantidad_gh5_hgr', 'cantidad_gh5_hpfc',
        'cantidad_gh5_hc', 'cantidad_gh5_hp', 'cantidad_gh5_hap', 'cantidad_gh5_hagr',
        'cantidad_gh5_haplasma', 'cantidad_gh6_pact', 'cantidad_gh6_hst', 'cantidad_gh6_hgr',
        'cantidad_gh6_hpfc', 'cantidad_gh6_hc', 'cantidad_gh6_hp', 'cantidad_gh6_hap',
        'cantidad_gh6_hagr', 'cantidad_gh6_haplasma', 'cantidad_gh7_pact', 'cantidad_gh7_hst',
        'cantidad_gh7_hgr', 'cantidad_gh7_hpfc', 'cantidad_gh7_hc', 'cantidad_gh7_hp',
        'cantidad_gh7_hap', 'cantidad_gh7_hagr', 'cantidad_gh7_haplasma', 'cantidad_ds_hgr',
        'cantidad_ds_hpfc', 'cantidad_ds_hp', 'cantidad_ds_hap', 'cantidad_da_hgr',
        'cantidad_da_hpfc', 'cantidad_da_hp', 'cantidad_da_hap', 'cantidad_tur_hst',
        'cantidad_tur_hgr', 'cantidad_tur_hpfc', 'cantidad_tur_hc', 'cantidad_tur_hp',
        'cantidad_tur_hap', 'cantidad_tur_hagr', 'cantidad_tut_hst', 'cantidad_tut_hgr',
        'cantidad_tut_hpfc', 'cantidad_tut_hc', 'cantidad_tut_hp', 'cantidad_tut_hap',
        'cantidad_tut_hagr', 'cantidad_cv_hst', 'cantidad_cv_hgr', 'cantidad_cv_hpfc',
        'cantidad_cv_hc', 'cantidad_cv_hp', 'cantidad_cv_hap', 'cantidad_cv_hagr',
        'cantidad_cv_haplasma', 'cantidad_cmitt_hst', 'cantidad_cmitt_hgr', 'cantidad_cmitt_hpfc',
        'cantidad_cmitt_hc', 'cantidad_cmitt_hp', 'cantidad_cmitt_hap', 'cantidad_cmitt_hagr',
        'cantidad_cmitt_haplasma', 'cantidad_ca_hst', 'cantidad_ca_hgr', 'cantidad_ca_hpfc',
        'cantidad_ca_hc', 'cantidad_ca_hp', 'cantidad_ca_hap', 'cantidad_ca_hagr',
        'cantidad_ca_haplasma', 'cantidad_ct_hst', 'cantidad_ct_hgr', 'cantidad_ct_hpfc',
        'cantidad_ct_hc', 'cantidad_ct_hp', 'cantidad_ct_hap', 'cantidad_ct_hagr',
        'cantidad_ct_haplasma', 'cantidad_cp_hst', 'cantidad_cp_hgr', 'cantidad_cp_hpfc',
        'cantidad_cp_hc', 'cantidad_cp_hp', 'cantidad_cp_hap', 'cantidad_cp_hagr',
        'cantidad_cp_haplasma', 'cantidad_co_hst', 'cantidad_co_hgr', 'cantidad_co_hpfc',
        'cantidad_co_hc', 'cantidad_co_hp', 'cantidad_co_hap', 'cantidad_co_hagr',
        'cantidad_co_haplasma')

    @api.onchange(*tuple_attrs)
    def _onchange_tuple_attrs(self):
        def message_error(name):
            return {
                'warning': {'message': u'El valor ingresado de {}, deben ser positivos o iguales a 0 '.format(name)},
                'value': {name: 0},
            }

        for name in self.tuple_attrs:
            if getattr(self, name) < 0:
                return message_error(name)

    @api.one
    def fechas_registro(self):
        date_start = fields.Date.from_string(self.periodo_id.date_start)
        if self.periodo_id.month < 13:
            date_inicio = date_start + relativedelta(months=1)
            date_fin = date_inicio + relativedelta(days=14)
            self.inicio_fecha_registro = date_inicio
            self.fin_fecha_registro = date_fin

    @api.one
    @api.depends('inicio_fecha_registro', 'fin_fecha_registro')
    def _compute_especial(self):
        if self.inicio_fecha_registro and self.fin_fecha_registro:
            if self.inicio_fecha_registro <= fields.Date.today() <= self.fin_fecha_registro:
                self.special = False
            else:
                self.special = True

    @api.one
    @api.depends('periodo_id', 'anho_id')
    def _compute_anual_mensual(self):
        if self.periodo_id and self.anho_id:
            self.ficha_anual_mensual = constants.FICHA_MENSUAL
        else:
            self.ficha_anual_mensual = constants.FICHA_ANUAL

    @api.one
    @api.depends('cantidad_pe_x_ca', 'cantidad_pe_x_cvim', 'cantidad_pe_x_cvem', 'cantidad_pe_x_cr', 'cantidad_pe_x_cpr')
    def _compute_cantidad_total_x_pe(self):
        self.cantidad_total_x_pe = self.cantidad_pe_x_ca + self.cantidad_pe_x_cvim + self.cantidad_pe_x_cvem + self.cantidad_pe_x_cr + self.cantidad_pe_x_cpr

    @api.one
    @api.depends('cantidad_pd_x_ca', 'cantidad_pd_x_cvim', 'cantidad_pd_x_cvem', 'cantidad_pd_x_cr', 'cantidad_pd_x_cpr')
    def _compute_total_donaciones_pd(self):
        self.cantidad_total_x_pd = self.cantidad_pd_x_ca + self.cantidad_pd_x_cvim + self.cantidad_pd_x_cvem + self.cantidad_pd_x_cr + self.cantidad_pd_x_cpr

    @api.one
    @api.depends('cantidad_padi_x_ca', 'cantidad_padi_x_cvim', 'cantidad_padi_x_cvem', 'cantidad_padi_x_cr', 'cantidad_padi_x_cpr')
    def _compute_total_donaciones_padi(self):
        self.cantidad_total_x_padi = self.cantidad_padi_x_ca + self.cantidad_padi_x_cvim + self.cantidad_padi_x_cvem + self.cantidad_padi_x_cr + self.cantidad_padi_x_cpr

    @api.one
    @api.depends('cantidad_padc_x_ca', 'cantidad_padc_x_cvim', 'cantidad_padc_x_cvem', 'cantidad_padc_x_cr', 'cantidad_padc_x_cpr')
    def _compute_total_donaciones_padc(self):
        self.cantidad_total_x_padc = self.cantidad_padc_x_ca + self.cantidad_padc_x_cvim + self.cantidad_padc_x_cvem + self.cantidad_padc_x_cr + self.cantidad_padc_x_cpr

    @api.one
    @api.depends('cantidad_pe_x_ca', 'cantidad_pd_x_ca', 'cantidad_padi_x_ca', 'cantidad_padc_x_ca')
    def _compute_total_donaciones_ca(self):
        self.cantidad_total_x_ca = self.cantidad_pe_x_ca + self.cantidad_pd_x_ca + self.cantidad_padi_x_ca + self.cantidad_padc_x_ca

    @api.one
    @api.depends('cantidad_pe_x_cvim', 'cantidad_pd_x_cvim', 'cantidad_padi_x_cvim', 'cantidad_padc_x_cvim')
    def _compute_total_donaciones_cvim(self):
        self.cantidad_total_x_cvim = self.cantidad_pe_x_cvim + self.cantidad_pd_x_cvim + self.cantidad_padi_x_cvim + self.cantidad_padc_x_cvim

    @api.one
    @api.depends('cantidad_pe_x_cvem', 'cantidad_pd_x_cvem', 'cantidad_padi_x_cvem', 'cantidad_padc_x_cvem')
    def _compute_total_donaciones_cvem(self):
        self.cantidad_total_x_cvem = self.cantidad_pe_x_cvem + self.cantidad_pd_x_cvem + self.cantidad_padi_x_cvem + self.cantidad_padc_x_cvem

    @api.one
    @api.depends('cantidad_pe_x_cr', 'cantidad_pd_x_cr', 'cantidad_padi_x_cr', 'cantidad_padc_x_cr')
    def _compute_total_donaciones_cr(self):
        self.cantidad_total_x_cr = self.cantidad_pe_x_cr + self.cantidad_pd_x_cr + self.cantidad_padi_x_cr + self.cantidad_padc_x_cr

    @api.one
    @api.depends('cantidad_pe_x_cpr', 'cantidad_pd_x_cpr', 'cantidad_padi_x_cpr', 'cantidad_padc_x_cpr')
    def _compute_total_donaciones_cpr(self):
        self.cantidad_total_x_cpr = self.cantidad_pe_x_cpr + self.cantidad_pd_x_cpr + self.cantidad_padi_x_cpr + self.cantidad_padc_x_cpr

    @api.one
    @api.depends('cantidad_donacion_h', 'cantidad_donacion_m')
    def _compute_total_donaciones_sexo(self):
        self.cantidad_donacion_total = self.cantidad_donacion_h + self.cantidad_donacion_m

    @api.one
    @api.depends('cantidad_mvih_clt_cv', 'cantidad_mvih_clt_cr', 'cantidad_mvih_clt_cpr', 'cantidad_mvih_clt_ca')
    def _compute_total_tamizaje_mvih_clt(self):
        self.cantidad_mvih_clt_total = self.cantidad_mvih_clt_cv + self.cantidad_mvih_clt_cr + self.cantidad_mvih_clt_cpr + self.cantidad_mvih_clt_ca

    @api.one
    @api.depends('cantidad_mvih_clr_cv', 'cantidad_mvih_clr_cr', 'cantidad_mvih_clr_cpr', 'cantidad_mvih_clr_ca')
    def _compute_total_tamizaje_mvih_clr(self):
        self.cantidad_mvih_clr_total = self.cantidad_mvih_clr_cv + self.cantidad_mvih_clr_cr + self.cantidad_mvih_clr_cpr + self.cantidad_mvih_clr_ca

    @api.one
    @api.depends('cantidad_mvih_clzg_cv', 'cantidad_mvih_clzg_cr', 'cantidad_mvih_clzg_cpr', 'cantidad_mvih_clzg_ca')
    def _compute_total_tamizaje_mvih_clzg(self):
        self.cantidad_mvih_clzg_total = self.cantidad_mvih_clzg_cv + self.cantidad_mvih_clzg_cr + self.cantidad_mvih_clzg_cpr + self.cantidad_mvih_clzg_ca

    @api.one
    @api.depends('cantidad_mhbsag_clt_cv', 'cantidad_mhbsag_clt_cr', 'cantidad_mhbsag_clt_cpr', 'cantidad_mhbsag_clt_ca')
    def _compute_total_tamizaje_mhbsag_clt(self):
        self.cantidad_mhbsag_clt_total = self.cantidad_mhbsag_clt_cv + self.cantidad_mhbsag_clt_cr + self.cantidad_mhbsag_clt_cpr + self.cantidad_mhbsag_clt_ca

    @api.one
    @api.depends('cantidad_mhbsag_clr_cv', 'cantidad_mhbsag_clr_cr', 'cantidad_mhbsag_clr_cpr', 'cantidad_mhbsag_clr_ca')
    def _compute_total_tamizaje_mhbsag_clr(self):
        self.cantidad_mhbsag_clr_total = self.cantidad_mhbsag_clr_cv + self.cantidad_mhbsag_clr_cr + self.cantidad_mhbsag_clr_cpr + self.cantidad_mhbsag_clr_ca

    @api.one
    @api.depends('cantidad_mhbsag_clzg_cv', 'cantidad_mhbsag_clzg_cr', 'cantidad_mhbsag_clzg_cpr', 'cantidad_mhbsag_clzg_ca')
    def _compute_total_tamizaje_mhbsag_clzg(self):
        self.cantidad_mhbsag_clzg_total = self.cantidad_mhbsag_clzg_cv + self.cantidad_mhbsag_clzg_cr + self.cantidad_mhbsag_clzg_cpr + self.cantidad_mhbsag_clzg_ca

    @api.one
    @api.depends('cantidad_mhepc_clt_cv', 'cantidad_mhepc_clt_cr', 'cantidad_mhepc_clt_cpr', 'cantidad_mhepc_clt_ca')
    def _compute_total_tamizaje_mhepc_clt(self):
        self.cantidad_mhepc_clt_total = self.cantidad_mhepc_clt_cv + self.cantidad_mhepc_clt_cr + self.cantidad_mhepc_clt_cpr + self.cantidad_mhepc_clt_ca

    @api.one
    @api.depends('cantidad_mhepc_clr_cv', 'cantidad_mhepc_clr_cr', 'cantidad_mhepc_clr_cpr', 'cantidad_mhepc_clr_ca')
    def _compute_total_tamizaje_mhepc_clr(self):
        self.cantidad_mhepc_clr_total = self.cantidad_mhepc_clr_cv + self.cantidad_mhepc_clr_cr + self.cantidad_mhepc_clr_cpr + self.cantidad_mhepc_clr_ca

    @api.one
    @api.depends('cantidad_mhepc_clzg_cv', 'cantidad_mhepc_clzg_cr', 'cantidad_mhepc_clzg_cpr', 'cantidad_mhepc_clzg_ca')
    def _compute_total_tamizaje_mhepc_clzg(self):
        self.cantidad_mhepc_clzg_total = self.cantidad_mhepc_clzg_cv + self.cantidad_mhepc_clzg_cr + self.cantidad_mhepc_clzg_cpr + self.cantidad_mhepc_clzg_ca

    @api.one
    @api.depends('cantidad_mantihbc_clt_cv', 'cantidad_mantihbc_clt_cr', 'cantidad_mantihbc_clt_cpr', 'cantidad_mantihbc_clt_ca')
    def _compute_total_tamizaje_mantihbc_clt(self):
        self.cantidad_mantihbc_clt_total = self.cantidad_mantihbc_clt_cv + self.cantidad_mantihbc_clt_cr + self.cantidad_mantihbc_clt_cpr + self.cantidad_mantihbc_clt_ca

    @api.one
    @api.depends('cantidad_mantihbc_clr_cv', 'cantidad_mantihbc_clr_cr', 'cantidad_mantihbc_clr_cpr', 'cantidad_mantihbc_clr_ca')
    def _compute_total_tamizaje_mantihbc_clr(self):
        self.cantidad_mantihbc_clr_total = self.cantidad_mantihbc_clr_cv + self.cantidad_mantihbc_clr_cr + self.cantidad_mantihbc_clr_cpr + self.cantidad_mantihbc_clr_ca

    @api.one
    @api.depends('cantidad_mantihbc_clzg_cv', 'cantidad_mantihbc_clzg_cr', 'cantidad_mantihbc_clzg_cpr', 'cantidad_mantihbc_clzg_ca')
    def _compute_total_tamizaje_mantihbc_clzg(self):
        self.cantidad_mantihbc_clzg_total = self.cantidad_mantihbc_clzg_cv + self.cantidad_mantihbc_clzg_cr + self.cantidad_mantihbc_clzg_cpr + self.cantidad_mantihbc_clzg_ca

    @api.one
    @api.depends('cantidad_mhtlv_clt_cv', 'cantidad_mhtlv_clt_cr', 'cantidad_mhtlv_clt_cpr', 'cantidad_mhtlv_clt_ca')
    def _compute_total_tamizaje_mhtlv_clt(self):
        self.cantidad_mhtlv_clt_total = self.cantidad_mhtlv_clt_cv + self.cantidad_mhtlv_clt_cr + self.cantidad_mhtlv_clt_cpr + self.cantidad_mhtlv_clt_ca

    @api.one
    @api.depends('cantidad_mhtlv_clr_cv', 'cantidad_mhtlv_clr_cr', 'cantidad_mhtlv_clr_cpr', 'cantidad_mhtlv_clr_ca')
    def _compute_total_tamizaje_mhtlv_clr(self):
        self.cantidad_mhtlv_clr_total = self.cantidad_mhtlv_clr_cv + self.cantidad_mhtlv_clr_cr + self.cantidad_mhtlv_clr_cpr + self.cantidad_mhtlv_clr_ca

    @api.one
    @api.depends('cantidad_mhtlv_clzg_cv', 'cantidad_mhtlv_clzg_cr', 'cantidad_mhtlv_clzg_cpr', 'cantidad_mhtlv_clzg_ca')
    def _compute_total_tamizaje_mhtlv_clzg(self):
        self.cantidad_mhtlv_clzg_total = self.cantidad_mhtlv_clzg_cv + self.cantidad_mhtlv_clzg_cr + self.cantidad_mhtlv_clzg_cpr + self.cantidad_mhtlv_clzg_ca

    @api.one
    @api.depends('cantidad_msifilis_clt_cv', 'cantidad_msifilis_clt_cr', 'cantidad_msifilis_clt_cpr', 'cantidad_msifilis_clt_ca')
    def _compute_total_tamizaje_msifilis_clt(self):
        self.cantidad_msifilis_clt_total = self.cantidad_msifilis_clt_cv + self.cantidad_msifilis_clt_cr + self.cantidad_msifilis_clt_cpr + self.cantidad_msifilis_clt_ca

    @api.one
    @api.depends('cantidad_msifilis_clr_cv', 'cantidad_msifilis_clr_cr', 'cantidad_msifilis_clr_cpr', 'cantidad_msifilis_clr_ca')
    def _compute_total_tamizaje_msifilis_clr(self):
        self.cantidad_msifilis_clr_total = self.cantidad_msifilis_clr_cv + self.cantidad_msifilis_clr_cr + self.cantidad_msifilis_clr_cpr + self.cantidad_msifilis_clr_ca

    @api.one
    @api.depends('cantidad_msifilis_clzg_cv', 'cantidad_msifilis_clzg_cr', 'cantidad_msifilis_clzg_cpr', 'cantidad_msifilis_clzg_ca')
    def _compute_total_tamizaje_msifilis_clzg(self):
        self.cantidad_msifilis_clzg_total = self.cantidad_msifilis_clzg_cv + self.cantidad_msifilis_clzg_cr + self.cantidad_msifilis_clzg_cpr + self.cantidad_msifilis_clzg_ca

    @api.one
    @api.depends('cantidad_mchagas_clt_cv', 'cantidad_mchagas_clt_cr', 'cantidad_mchagas_clt_cpr', 'cantidad_mchagas_clt_ca')
    def _compute_total_tamizaje_mchagas_clt(self):
        self.cantidad_mchagas_clt_total = self.cantidad_mchagas_clt_cv + self.cantidad_mchagas_clt_cr + self.cantidad_mchagas_clt_cpr + self.cantidad_mchagas_clt_ca

    @api.one
    @api.depends('cantidad_mchagas_clr_cv', 'cantidad_mchagas_clr_cr', 'cantidad_mchagas_clr_cpr', 'cantidad_mchagas_clr_ca')
    def _compute_total_tamizaje_mchagas_clr(self):
        self.cantidad_mchagas_clr_total = self.cantidad_mchagas_clr_cv + self.cantidad_mchagas_clr_cr + self.cantidad_mchagas_clr_cpr + self.cantidad_mchagas_clr_ca

    @api.one
    @api.depends('cantidad_mchagas_clzg_cv', 'cantidad_mchagas_clzg_cr', 'cantidad_mchagas_clzg_cpr', 'cantidad_mchagas_clzg_ca')
    def _compute_total_tamizaje_mchagas_clzg(self):
        self.cantidad_mchagas_clzg_total = self.cantidad_mchagas_clzg_cv + self.cantidad_mchagas_clzg_cr + self.cantidad_mchagas_clzg_cpr + self.cantidad_mchagas_clzg_ca

    @api.one
    @api.depends('cantidad_motros_clt_cv', 'cantidad_motros_clt_cr', 'cantidad_motros_clt_cpr', 'cantidad_motros_clt_ca')
    def _compute_total_tamizaje_motros_clt(self):
        self.cantidad_motros_clt_total = self.cantidad_motros_clt_cv + self.cantidad_motros_clt_cr + self.cantidad_motros_clt_cpr + self.cantidad_motros_clt_ca

    @api.one
    @api.depends('cantidad_motros_clr_cv', 'cantidad_motros_clr_cr', 'cantidad_motros_clr_cpr', 'cantidad_motros_clr_ca')
    def _compute_total_tamizaje_motros_clr(self):
        self.cantidad_motros_clr_total = self.cantidad_motros_clr_cv + self.cantidad_motros_clr_cr + self.cantidad_motros_clr_cpr + self.cantidad_motros_clr_ca

    @api.one
    @api.depends('cantidad_motros_clzg_cv', 'cantidad_motros_clzg_cr', 'cantidad_motros_clzg_cpr', 'cantidad_motros_clzg_ca')
    def _compute_total_tamizaje_motros_clzg(self):
        self.cantidad_motros_clzg_total = self.cantidad_motros_clzg_cv + self.cantidad_motros_clzg_cr + self.cantidad_motros_clzg_cpr + self.cantidad_motros_clzg_ca

    @api.one
    @api.depends('cantidad_unr_cv', 'cantidad_unr_cr', 'cantidad_unr_cpr', 'cantidad_unr_ca')
    def _compute_total_reactividad_unr(self):
        self.cantidad_unr_total = self.cantidad_unr_cv + self.cantidad_unr_cr + self.cantidad_unr_cpr + self.cantidad_unr_ca

    @api.one
    @api.depends('cantidad_ur_cv', 'cantidad_ur_cr', 'cantidad_ur_cpr', 'cantidad_ur_ca')
    def _compute_total_reactividad_ur(self):
        self.cantidad_ur_total = self.cantidad_ur_cv + self.cantidad_ur_cr + self.cantidad_ur_cpr + self.cantidad_ur_ca

    @api.one
    @api.depends('cantidad_uzg_cv', 'cantidad_uzg_cr', 'cantidad_uzg_cpr', 'cantidad_uzg_ca')
    def _compute_total_reactividad_uzg(self):
        self.cantidad_uzg_total = self.cantidad_uzg_cv + self.cantidad_uzg_cr + self.cantidad_uzg_cpr + self.cantidad_uzg_ca

    @api.one
    @api.depends('cantidad_gh1_hst', 'cantidad_gh1_hgr', 'cantidad_gh1_hpfc', 'cantidad_gh1_hc', 'cantidad_gh1_hp', 'cantidad_gh1_hap', 'cantidad_gh1_hagr', 'cantidad_gh1_haplasma')
    def _compute_total_uso_hemocomponentes_gh1(self):
        self.cantidad_gh1_total = self.cantidad_gh1_hst + self.cantidad_gh1_hgr + self.cantidad_gh1_hpfc + self.cantidad_gh1_hc + self.cantidad_gh1_hp + self.cantidad_gh1_hap + self.cantidad_gh1_hagr + self.cantidad_gh1_haplasma

    @api.one
    @api.depends('cantidad_gh2_hst', 'cantidad_gh2_hgr', 'cantidad_gh2_hpfc', 'cantidad_gh2_hc', 'cantidad_gh2_hp', 'cantidad_gh2_hap', 'cantidad_gh2_hagr', 'cantidad_gh2_haplasma')
    def _compute_total_uso_hemocomponentes_gh2(self):
        self.cantidad_gh2_total = self.cantidad_gh2_hst + self.cantidad_gh2_hgr + self.cantidad_gh2_hpfc + self.cantidad_gh2_hc + self.cantidad_gh2_hp + self.cantidad_gh2_hap + self.cantidad_gh2_hagr + self.cantidad_gh2_haplasma

    @api.one
    @api.depends('cantidad_gh3_hst', 'cantidad_gh3_hgr', 'cantidad_gh3_hpfc', 'cantidad_gh3_hc', 'cantidad_gh3_hp', 'cantidad_gh3_hap', 'cantidad_gh3_hagr', 'cantidad_gh3_haplasma')
    def _compute_total_uso_hemocomponentes_gh3(self):
        self.cantidad_gh3_total = self.cantidad_gh3_hst + self.cantidad_gh3_hgr + self.cantidad_gh3_hpfc + self.cantidad_gh3_hc + self.cantidad_gh3_hp + self.cantidad_gh3_hap + self.cantidad_gh3_hagr + self.cantidad_gh3_haplasma

    @api.one
    @api.depends('cantidad_gh4_hst', 'cantidad_gh4_hgr', 'cantidad_gh4_hpfc', 'cantidad_gh4_hc', 'cantidad_gh4_hp', 'cantidad_gh4_hap', 'cantidad_gh4_hagr', 'cantidad_gh4_haplasma')
    def _compute_total_uso_hemocomponentes_gh4(self):
        self.cantidad_gh4_total = self.cantidad_gh4_hst + self.cantidad_gh4_hgr + self.cantidad_gh4_hpfc + self.cantidad_gh4_hc + self.cantidad_gh4_hp + self.cantidad_gh4_hap + self.cantidad_gh4_hagr + self.cantidad_gh4_haplasma

    @api.one
    @api.depends('cantidad_gh5_hst', 'cantidad_gh5_hgr', 'cantidad_gh5_hpfc', 'cantidad_gh5_hc', 'cantidad_gh5_hp', 'cantidad_gh5_hap', 'cantidad_gh5_hagr', 'cantidad_gh5_haplasma')
    def _compute_total_uso_hemocomponentes_gh5(self):
        self.cantidad_gh5_total = self.cantidad_gh5_hst + self.cantidad_gh5_hgr + self.cantidad_gh5_hpfc + self.cantidad_gh5_hc + self.cantidad_gh5_hp + self.cantidad_gh5_hap + self.cantidad_gh5_hagr + self.cantidad_gh5_haplasma

    @api.one
    @api.depends('cantidad_gh6_hst', 'cantidad_gh6_hgr', 'cantidad_gh6_hpfc', 'cantidad_gh6_hc', 'cantidad_gh6_hp', 'cantidad_gh6_hap', 'cantidad_gh6_hagr', 'cantidad_gh6_haplasma')
    def _compute_total_uso_hemocomponentes_gh6(self):
        self.cantidad_gh6_total = self.cantidad_gh6_hst + self.cantidad_gh6_hgr + self.cantidad_gh6_hpfc + self.cantidad_gh6_hc + self.cantidad_gh6_hp + self.cantidad_gh6_hap + self.cantidad_gh6_hagr + self.cantidad_gh6_haplasma

    @api.one
    @api.depends('cantidad_gh7_hst', 'cantidad_gh7_hgr', 'cantidad_gh7_hpfc', 'cantidad_gh7_hc', 'cantidad_gh7_hp', 'cantidad_gh7_hap', 'cantidad_gh7_hagr', 'cantidad_gh7_haplasma')
    def _compute_total_uso_hemocomponentes_gh7(self):
        self.cantidad_gh7_total = self.cantidad_gh7_hst + self.cantidad_gh7_hgr + self.cantidad_gh7_hpfc + self.cantidad_gh7_hc + self.cantidad_gh7_hp + self.cantidad_gh7_hap + self.cantidad_gh7_hagr + self.cantidad_gh7_haplasma

    @api.one
    @api.depends('cantidad_gh1_pact', 'cantidad_gh2_pact', 'cantidad_gh3_pact', 'cantidad_gh4_pact', 'cantidad_gh5_pact', 'cantidad_gh6_pact', 'cantidad_gh7_pact')
    def _compute_total_uso_hemocomponentes_pact(self):
        self.cantidad_pact_total = self.cantidad_gh1_pact + self.cantidad_gh2_pact + self.cantidad_gh3_pact + self.cantidad_gh4_pact + self.cantidad_gh5_pact + self.cantidad_gh6_pact + self.cantidad_gh7_pact

    @api.one
    @api.depends('cantidad_gh1_hst', 'cantidad_gh2_hst', 'cantidad_gh3_hst', 'cantidad_gh4_hst', 'cantidad_gh5_hst', 'cantidad_gh6_hst', 'cantidad_gh7_hst')
    def _compute_total_uso_hemocomponentes_hst(self):
        self.cantidad_hst_total = self.cantidad_gh1_hst + self.cantidad_gh2_hst + self.cantidad_gh3_hst + self.cantidad_gh4_hst + self.cantidad_gh5_hst + self.cantidad_gh6_hst + self.cantidad_gh7_hst

    @api.one
    @api.depends('cantidad_gh1_hgr', 'cantidad_gh2_hgr', 'cantidad_gh3_hgr', 'cantidad_gh4_hgr', 'cantidad_gh5_hgr', 'cantidad_gh6_hgr', 'cantidad_gh7_hgr')
    def _compute_total_uso_hemocomponentes_hgr(self):
        self.cantidad_hgr_total = self.cantidad_gh1_hgr + self.cantidad_gh2_hgr + self.cantidad_gh3_hgr + self.cantidad_gh4_hgr + self.cantidad_gh5_hgr + self.cantidad_gh6_hgr + self.cantidad_gh7_hgr

    @api.one
    @api.depends('cantidad_gh1_hpfc', 'cantidad_gh2_hpfc', 'cantidad_gh3_hpfc', 'cantidad_gh4_hpfc', 'cantidad_gh5_hpfc', 'cantidad_gh6_hpfc', 'cantidad_gh7_hpfc')
    def _compute_total_uso_hemocomponentes_hpfc(self):
        self.cantidad_hpfc_total = self.cantidad_gh1_hpfc + self.cantidad_gh2_hpfc + self.cantidad_gh3_hpfc + self.cantidad_gh4_hpfc + self.cantidad_gh5_hpfc + self.cantidad_gh6_hpfc + self.cantidad_gh7_hpfc

    @api.one
    @api.depends('cantidad_gh1_hc', 'cantidad_gh2_hc', 'cantidad_gh3_hc', 'cantidad_gh4_hc', 'cantidad_gh5_hc', 'cantidad_gh6_hc', 'cantidad_gh7_hc')
    def _compute_total_uso_hemocomponentes_hc(self):
        self.cantidad_hc_total = self.cantidad_gh1_hc + self.cantidad_gh2_hc + self.cantidad_gh3_hc + self.cantidad_gh4_hc + self.cantidad_gh5_hc + self.cantidad_gh6_hc + self.cantidad_gh7_hc

    @api.one
    @api.depends('cantidad_gh1_hp', 'cantidad_gh2_hp', 'cantidad_gh3_hp', 'cantidad_gh4_hp', 'cantidad_gh5_hp', 'cantidad_gh6_hp', 'cantidad_gh7_hp')
    def _compute_total_uso_hemocomponentes_hp(self):
        self.cantidad_hp_total = self.cantidad_gh1_hp + self.cantidad_gh2_hp + self.cantidad_gh3_hp + self.cantidad_gh4_hp + self.cantidad_gh5_hp + self.cantidad_gh6_hp + self.cantidad_gh7_hp

    @api.one
    @api.depends('cantidad_gh1_hap', 'cantidad_gh2_hap', 'cantidad_gh3_hap', 'cantidad_gh4_hap', 'cantidad_gh5_hap', 'cantidad_gh6_hap', 'cantidad_gh7_hap')
    def _compute_total_uso_hemocomponentes_hap(self):
        self.cantidad_hap_total = self.cantidad_gh1_hap + self.cantidad_gh2_hap + self.cantidad_gh3_hap + self.cantidad_gh4_hap + self.cantidad_gh5_hap + self.cantidad_gh6_hap + self.cantidad_gh7_hap

    @api.one
    @api.depends('cantidad_gh1_hagr', 'cantidad_gh2_hagr', 'cantidad_gh3_hagr', 'cantidad_gh4_hagr', 'cantidad_gh5_hagr', 'cantidad_gh6_hagr', 'cantidad_gh7_hagr')
    def _compute_total_uso_hemocomponentes_hagr(self):
        self.cantidad_hagr_total = self.cantidad_gh1_hagr + self.cantidad_gh2_hagr + self.cantidad_gh3_hagr + self.cantidad_gh4_hagr + self.cantidad_gh5_hagr + self.cantidad_gh6_hagr + self.cantidad_gh7_hagr

    @api.one
    @api.depends('cantidad_gh1_haplasma', 'cantidad_gh2_haplasma', 'cantidad_gh3_haplasma', 'cantidad_gh4_haplasma', 'cantidad_gh5_haplasma', 'cantidad_gh6_haplasma', 'cantidad_gh7_haplasma')
    def _compute_total_uso_hemocomponentes_haplasma(self):
        self.cantidad_haplasma_total = self.cantidad_gh1_haplasma + self.cantidad_gh2_haplasma + self.cantidad_gh3_haplasma + self.cantidad_gh4_haplasma + self.cantidad_gh5_haplasma + self.cantidad_gh6_haplasma + self.cantidad_gh7_haplasma

    @api.one
    @api.depends('cantidad_hst_total', 'cantidad_hgr_total', 'cantidad_hpfc_total', 'cantidad_hc_total', 'cantidad_hp_total', 'cantidad_hap_total', 'cantidad_hagr_total', 'cantidad_haplasma_total')
    def _compute_total_uso_hemocomponentes_hemocomponentes(self):
        self.cantidad_uso_hemocomponentes_total_hemocomponentes = self.cantidad_hst_total + self.cantidad_hgr_total + self.cantidad_hpfc_total + self.cantidad_hc_total + self.cantidad_hp_total + self.cantidad_hap_total + self.cantidad_hagr_total + self.cantidad_haplasma_total

    @api.one
    @api.depends('cantidad_gh1_total', 'cantidad_gh2_total', 'cantidad_gh3_total', 'cantidad_gh4_total', 'cantidad_gh5_total', 'cantidad_gh6_total', 'cantidad_gh7_total')
    def _compute_total_uso_hemocomponentes_grupo_edad(self):
        self.cantidad_uso_hemocomponentes_total_gh = self.cantidad_gh1_total + self.cantidad_gh2_total + self.cantidad_gh3_total + self.cantidad_gh4_total + self.cantidad_gh5_total + self.cantidad_gh6_total + self.cantidad_gh7_total

    @api.one
    @api.depends('cantidad_uso_hemocomponentes_total_hemocomponentes', 'cantidad_uso_hemocomponentes_total_gh')
    def _compute_total_uso_hemocomponentes(self):
        self.cantidad_uso_hemocomponentes_total = self.cantidad_uso_hemocomponentes_total_hemocomponentes + self.cantidad_uso_hemocomponentes_total_gh

    @api.one
    @api.depends('cantidad_tur_hst', 'cantidad_tur_hgr', 'cantidad_tur_hpfc', 'cantidad_tur_hc', 'cantidad_tur_hp', 'cantidad_tur_hap', 'cantidad_tur_hagr')
    def _compute_total_transferencia_hemocomponentes_tur(self):
        self.cantidad_tur_total = self.cantidad_tur_hst + self.cantidad_tur_hgr + self.cantidad_tur_hpfc + self.cantidad_tur_hc + self.cantidad_tur_hp + self.cantidad_tur_hap + self.cantidad_tur_hagr

    @api.one
    @api.depends('cantidad_tut_hst', 'cantidad_tut_hgr', 'cantidad_tut_hpfc', 'cantidad_tut_hc', 'cantidad_tut_hp', 'cantidad_tut_hap', 'cantidad_tut_hagr')
    def _compute_total_transferencia_hemocomponentes_tut(self):
        self.cantidad_tut_total = self.cantidad_tut_hst + self.cantidad_tut_hgr + self.cantidad_tut_hpfc + self.cantidad_tut_hc + self.cantidad_tut_hp + self.cantidad_tut_hap + self.cantidad_tut_hagr

    @api.one
    @api.depends('cantidad_cv_hst', 'cantidad_cv_hgr', 'cantidad_cv_hpfc', 'cantidad_cv_hc', 'cantidad_cv_hp', 'cantidad_cv_hap', 'cantidad_cv_hagr', 'cantidad_cv_haplasma')
    def _compute_total_causas_eliminacion_hemocomponentes_cv(self):
        self.cantidad_cv_total = self.cantidad_cv_hst + self.cantidad_cv_hgr + self.cantidad_cv_hpfc + self.cantidad_cv_hc + self.cantidad_cv_hp + self.cantidad_cv_hap + self.cantidad_cv_hagr + self.cantidad_cv_haplasma

    @api.one
    @api.depends('cantidad_cmitt_hst', 'cantidad_cmitt_hgr', 'cantidad_cmitt_hpfc', 'cantidad_cmitt_hc', 'cantidad_cmitt_hp', 'cantidad_cmitt_hap', 'cantidad_cmitt_hagr', 'cantidad_cmitt_haplasma')
    def _compute_total_causas_eliminacion_hemocomponentes_cmitt(self):
        self.cantidad_cmitt_total = self.cantidad_cmitt_hst + self.cantidad_cmitt_hgr + self.cantidad_cmitt_hpfc + self.cantidad_cmitt_hc + self.cantidad_cmitt_hp + self.cantidad_cmitt_hap + self.cantidad_cmitt_hagr + self.cantidad_cmitt_haplasma

    @api.one
    @api.depends('cantidad_ca_hst', 'cantidad_ca_hgr', 'cantidad_ca_hpfc', 'cantidad_ca_hc', 'cantidad_ca_hp', 'cantidad_ca_hap', 'cantidad_ca_hagr', 'cantidad_ca_haplasma')
    def _compute_total_causas_eliminacion_hemocomponentes_ca(self):
        self.cantidad_ca_total = self.cantidad_ca_hst + self.cantidad_ca_hgr + self.cantidad_ca_hpfc + self.cantidad_ca_hc + self.cantidad_ca_hp + self.cantidad_ca_hap + self.cantidad_ca_hagr + self.cantidad_ca_haplasma

    @api.one
    @api.depends('cantidad_ct_hst', 'cantidad_ct_hgr', 'cantidad_ct_hpfc', 'cantidad_ct_hc', 'cantidad_ct_hp', 'cantidad_ct_hap', 'cantidad_ct_hagr', 'cantidad_ct_haplasma')
    def _compute_total_causas_eliminacion_hemocomponentes_ct(self):
        self.cantidad_ct_total = self.cantidad_ct_hst + self.cantidad_ct_hgr + self.cantidad_ct_hpfc + self.cantidad_ct_hc + self.cantidad_ct_hp + self.cantidad_ct_hap + self.cantidad_ct_hagr + self.cantidad_ct_haplasma

    @api.one
    @api.depends('cantidad_cp_hst', 'cantidad_cp_hgr', 'cantidad_cp_hpfc', 'cantidad_cp_hc', 'cantidad_cp_hp', 'cantidad_cp_hap', 'cantidad_cp_hagr', 'cantidad_cp_haplasma')
    def _compute_total_causas_eliminacion_hemocomponentes_cp(self):
        self.cantidad_cp_total = self.cantidad_cp_hst + self.cantidad_cp_hgr + self.cantidad_cp_hpfc + self.cantidad_cp_hc + self.cantidad_cp_hp + self.cantidad_cp_hap + self.cantidad_cp_hagr + self.cantidad_cp_haplasma

    @api.one
    @api.depends('cantidad_co_hst', 'cantidad_co_hgr', 'cantidad_co_hpfc', 'cantidad_co_hc', 'cantidad_co_hp', 'cantidad_co_hap', 'cantidad_co_hagr', 'cantidad_co_haplasma')
    def _compute_total_causas_eliminacion_hemocomponentes_co(self):
        self.cantidad_co_total = self.cantidad_co_hst + self.cantidad_co_hgr + self.cantidad_co_hpfc + self.cantidad_co_hc + self.cantidad_co_hp + self.cantidad_co_hap + self.cantidad_co_hagr + self.cantidad_co_haplasma

    @api.one
    @api.depends('cantidad_cv_hst', 'cantidad_cmitt_hst', 'cantidad_ca_hst', 'cantidad_ct_hst', 'cantidad_cp_hst', 'cantidad_co_hst')
    def _compute_total_causas_eliminacion_hemocomponentes_hst(self):
        self.cantidad_ctotal_hst = self.cantidad_cv_hst + self.cantidad_cmitt_hst + self.cantidad_ca_hst + self.cantidad_ct_hst + self.cantidad_cp_hst + self.cantidad_co_hst

    @api.one
    @api.depends('cantidad_cv_hgr', 'cantidad_cmitt_hgr', 'cantidad_ca_hgr', 'cantidad_ct_hgr', 'cantidad_cp_hgr', 'cantidad_co_hgr')
    def _compute_total_causas_eliminacion_hemocomponentes_hgr(self):
        self.cantidad_ctotal_hgr = self.cantidad_cv_hgr + self.cantidad_cmitt_hgr + self.cantidad_ca_hgr + self.cantidad_ct_hgr + self.cantidad_cp_hgr + self.cantidad_co_hgr

    @api.one
    @api.depends('cantidad_cv_hpfc', 'cantidad_cmitt_hpfc', 'cantidad_ca_hpfc', 'cantidad_ct_hpfc', 'cantidad_cp_hpfc', 'cantidad_co_hpfc')
    def _compute_total_causas_eliminacion_hemocomponentes_hpfc(self):
        self.cantidad_ctotal_hpfc = self.cantidad_cv_hpfc + self.cantidad_cmitt_hpfc + self.cantidad_ca_hpfc + self.cantidad_ct_hpfc + self.cantidad_cp_hpfc + self.cantidad_co_hpfc

    @api.one
    @api.depends('cantidad_cv_hc', 'cantidad_cmitt_hc', 'cantidad_ca_hc', 'cantidad_ct_hc', 'cantidad_cp_hc', 'cantidad_co_hc')
    def _compute_total_causas_eliminacion_hemocomponentes_hc(self):
        self.cantidad_ctotal_hc = self.cantidad_cv_hc + self.cantidad_cmitt_hc + self.cantidad_ca_hc + self.cantidad_ct_hc + self.cantidad_cp_hc + self.cantidad_co_hc

    @api.one
    @api.depends('cantidad_cv_hp', 'cantidad_cmitt_hp', 'cantidad_ca_hp', 'cantidad_ct_hp', 'cantidad_cp_hp', 'cantidad_co_hp')
    def _compute_total_causas_eliminacion_hemocomponentes_hp(self):
        self.cantidad_ctotal_hp = self.cantidad_cv_hp + self.cantidad_cmitt_hp + self.cantidad_ca_hp + self.cantidad_ct_hp + self.cantidad_cp_hp + self.cantidad_co_hp

    @api.one
    @api.depends('cantidad_cv_hap', 'cantidad_cmitt_hap', 'cantidad_ca_hap', 'cantidad_ct_hap', 'cantidad_cp_hap', 'cantidad_co_hap')
    def _compute_total_causas_eliminacion_hemocomponentes_hap(self):
        self.cantidad_ctotal_hap = self.cantidad_cv_hap + self.cantidad_cmitt_hap + self.cantidad_ca_hap + self.cantidad_ct_hap + self.cantidad_cp_hap + self.cantidad_co_hap

    @api.one
    @api.depends('cantidad_cv_hagr', 'cantidad_cmitt_hagr', 'cantidad_ca_hagr', 'cantidad_ct_hagr', 'cantidad_cp_hagr', 'cantidad_co_hagr')
    def _compute_total_causas_eliminacion_hemocomponentes_hagr(self):
        self.cantidad_ctotal_hagr = self.cantidad_cv_hagr + self.cantidad_cmitt_hagr + self.cantidad_ca_hagr + self.cantidad_ct_hagr + self.cantidad_cp_hagr + self.cantidad_co_hagr

    @api.one
    @api.depends('cantidad_cv_haplasma', 'cantidad_cmitt_haplasma', 'cantidad_ca_haplasma', 'cantidad_ct_haplasma', 'cantidad_cp_haplasma', 'cantidad_co_haplasma')
    def _compute_total_causas_eliminacion_hemocomponentes_haplasma(self):
        self.cantidad_ctotal_haplasma = self.cantidad_cv_haplasma + self.cantidad_cmitt_haplasma + self.cantidad_ca_haplasma + self.cantidad_ct_haplasma + self.cantidad_cp_haplasma + self.cantidad_co_haplasma

    @api.one
    @api.depends('cantidad_ctotal_hst', 'cantidad_ctotal_hgr', 'cantidad_ctotal_hpfc', 'cantidad_ctotal_hc', 'cantidad_ctotal_hp', 'cantidad_ctotal_hap', 'cantidad_ctotal_hagr', 'cantidad_ctotal_haplasma')
    def _compute_total_causas_eliminacion_hemocomponentes(self):
        self.cantidad_ctotal_hemocomponentes = self.cantidad_ctotal_hst + self.cantidad_ctotal_hgr + self.cantidad_ctotal_hpfc + self.cantidad_ctotal_hc + self.cantidad_ctotal_hp + self.cantidad_ctotal_hap + self.cantidad_ctotal_hagr + self.cantidad_ctotal_haplasma

    @api.one
    @api.depends('cantidad_cv_total', 'cantidad_cmitt_total', 'cantidad_ca_total', 'cantidad_ct_total', 'cantidad_cp_total', 'cantidad_co_total')
    def _compute_total_causas_eliminacion_categorias(self):
        self.cantidad_ctotal_categorias = self.cantidad_cv_total + self.cantidad_cmitt_total + self.cantidad_ca_total + self.cantidad_ct_total + self.cantidad_cp_total + self.cantidad_co_total

    @api.one
    @api.depends('cantidad_ctotal_hemocomponentes', 'cantidad_ctotal_categorias')
    def _compute_total_causas_eliminacion(self):
        self.cantidad_ctotal = self.cantidad_ctotal_hemocomponentes + self.cantidad_ctotal_categorias

    @api.one
    @api.depends('total_donante_ids')
    def _compute_total_total_donante(self):
        sumtotal = 0
        for total_donante in self.total_donante_ids:
            sumtotal += total_donante.cantidad
        self.cantidad_total_donante = sumtotal

    @api.one
    @api.depends('total_postulante_diferido_excluido_ids')
    def _compute_total_total_postulante_diferido_excluido(self):
        sumtotal = 0
        for total_postulante_diferido_excluido in self.total_postulante_diferido_excluido_ids:
            sumtotal += total_postulante_diferido_excluido.cantidad
        self.cantidad_total_postulante_diferido_excluido = sumtotal

    @api.one
    @api.depends('donacion_segun_grupo_edad_donante_ids')
    def _compute_total_donacion_segun_grupo_edad(self):
        sumtotal = 0
        for total_donacion_segun_grupo_edad in self.donacion_segun_grupo_edad_donante_ids:
            sumtotal += total_donacion_segun_grupo_edad.cantidad
        self.cantidad_total_donacion_segun_grupo_edad = sumtotal

    @api.one
    @api.depends('donacion_sangre_total_ids')
    def _compute_total_donacion_sangre_total(self):
        sumtotal = 0
        for total_donacion_sangre_total in self.donacion_sangre_total_ids:
            sumtotal += total_donacion_sangre_total.cantidad
        self.cantidad_total_donacion_sangre_total = sumtotal

    @api.one
    @api.depends('donacion_aferesis_ids')
    def _compute_total_donacion_aferesis(self):
        sumtotal = 0
        for total_donacion_aferesis in self.donacion_aferesis_ids:
            sumtotal += total_donacion_aferesis.cantidad
        self.cantidad_total_donacion_aferesis = sumtotal

    @api.one
    @api.depends('produccion_unidad_sangre_ids')
    def _compute_total_produccion_unidad_sangre(self):
        sumtotal = 0
        for total_produccion_unidad_sangre in self.produccion_unidad_sangre_ids:
            sumtotal += total_produccion_unidad_sangre.cantidad_tipo_unidad_sangre
        self.cantidad_total_produccion_unidad_sangre = sumtotal

    @api.one
    @api.depends('hemocomponente_ids')
    def _compute_total_hemocomponente(self):
        sumtotal = 0
        for total_hemocomponente in self.hemocomponente_ids:
            sumtotal += total_hemocomponente.cantidad_hemocomponente
        self.cantidad_total_hemocomponente = sumtotal

    @api.one
    @api.depends('causa_reaccion_adversa_ids')
    def _compute_total_causa_reaccion_adversa(self):
        sumtotal = 0
        for total_causa_reaccion_adversa in self.causa_reaccion_adversa_ids:
            sumtotal += total_causa_reaccion_adversa.cantidad
        self.cantidad_total_causa_reaccion_adversa = sumtotal

    @api.one
    @api.depends('cantidad_mvih_clt_total', 'cantidad_mvih_clr_total', 'cantidad_mvih_clzg_total', 'cantidad_mhbsag_clt_total', 'cantidad_mhbsag_clr_total', 'cantidad_mhbsag_clzg_total', 'cantidad_mhepc_clt_total', 'cantidad_mhepc_clr_total', 'cantidad_mhepc_clzg_total', 'cantidad_mantihbc_clt_total', 'cantidad_mantihbc_clr_total', 'cantidad_mantihbc_clzg_total', 'cantidad_mhtlv_clt_total', 'cantidad_mhtlv_clr_total', 'cantidad_mhtlv_clzg_total', 'cantidad_msifilis_clt_total', 'cantidad_msifilis_clr_total', 'cantidad_msifilis_clzg_total', 'cantidad_mchagas_clt_total', 'cantidad_mchagas_clr_total', 'cantidad_mchagas_clzg_total', 'cantidad_motros_clt_total', 'cantidad_motros_clr_total', 'cantidad_motros_clzg_total')
    def _compute_total_tamizaje_unidad(self):
        self.cantidad_total_tamizaje_unidad = self.cantidad_mvih_clt_total + self.cantidad_mvih_clr_total + self.cantidad_mvih_clzg_total + self.cantidad_mhbsag_clt_total + self.cantidad_mhbsag_clr_total + self.cantidad_mhbsag_clzg_total + self.cantidad_mhepc_clt_total + self.cantidad_mhepc_clr_total + self.cantidad_mhepc_clzg_total + self.cantidad_mantihbc_clt_total + self.cantidad_mantihbc_clr_total + self.cantidad_mantihbc_clzg_total + self.cantidad_mhtlv_clt_total + self.cantidad_mhtlv_clr_total + self.cantidad_mhtlv_clzg_total + self.cantidad_msifilis_clt_total + self.cantidad_msifilis_clr_total + self.cantidad_msifilis_clzg_total + self.cantidad_mchagas_clt_total + self.cantidad_mchagas_clr_total + self.cantidad_mchagas_clzg_total + self.cantidad_motros_clt_total + self.cantidad_motros_clr_total + self.cantidad_motros_clzg_total

    @api.one
    @api.depends('cantidad_total_x_pe', 'cantidad_total_x_pd', 'cantidad_total_x_padi', 'cantidad_total_x_padc')
    def _compute_total_postulantes_donaciones(self):
        self.cantidad_total_postulantes_donacion_sangre = self.cantidad_total_x_pe + self.cantidad_total_x_pd + self.cantidad_total_x_padi + self.cantidad_total_x_padc

    @api.one
    @api.depends('cantidad_total_x_ca', 'cantidad_total_x_cvim', 'cantidad_total_x_cvem', 'cantidad_total_x_cr', 'cantidad_total_x_cpr')
    def _compute_total_categorias_donaciones(self):
        self.cantidad_total_categorias_donacion_sangre = self.cantidad_total_x_ca + self.cantidad_total_x_cvim + self.cantidad_total_x_cvem + self.cantidad_total_x_cr + self.cantidad_total_x_cpr

    @api.one
    @api.depends('cantidad_total_postulantes_donacion_sangre', 'cantidad_total_categorias_donacion_sangre')
    def _compute_total_donaciones(self):
        self.cantidad_total_donacion_sangre = self.cantidad_total_postulantes_donacion_sangre + self.cantidad_total_categorias_donacion_sangre

    @api.one
    @api.depends('cantidad_padi_x_cvim', 'cantidad_padc_x_cvim', 'cantidad_padi_x_cvem', 'cantidad_padc_x_cvem', 'cantidad_total_x_padi', 'cantidad_total_x_padc')
    def _compute_porcentaje_postulantes_donacion_completa(self):
        if (self.cantidad_total_x_padi > 0 or self.cantidad_total_x_padc > 0):
            self.cantidad_porcentaje_postulantes_donacion_completa = ((self.cantidad_padi_x_cvim + self.cantidad_padc_x_cvim + self.cantidad_padi_x_cvem + self.cantidad_padc_x_cvem) / (self.cantidad_total_x_padi + self.cantidad_total_x_padc)) * 100

    @api.one
    @api.depends('cantidad_total_x_pd', 'cantidad_total_postulantes_donacion_sangre')
    def _compute_porcentaje_postulantes_diferidos(self):
        if (self.cantidad_total_postulantes_donacion_sangre > 0):
            self.cantidad_porcentaje_postulantes_diferidos = (self.cantidad_total_x_pd / self.cantidad_total_postulantes_donacion_sangre) * 100

    @api.one
    @api.depends('cantidad_total_x_pe', 'cantidad_total_postulantes_donacion_sangre')
    def _compute_porcentaje_postulantes_excluidos(self):
        if (self.cantidad_total_postulantes_donacion_sangre > 0):
            self.cantidad_porcentaje_postulantes_excluidos = (self.cantidad_total_x_pe / self.cantidad_total_postulantes_donacion_sangre) * 100

    @api.one
    @api.depends('cantidad_total_x_cvim', 'cantidad_total_x_cvem')
    def _compute_cantidad_total_voluntarios(self):
        self.cantidad_total_voluntarios = self.cantidad_total_x_cvim + self.cantidad_total_x_cvem

    @api.one
    @api.depends('cantidad_padc_x_cvem', 'cantidad_padc_x_cvim', 'cantidad_total_x_padc')
    def _compute_porcentaje_total_voluntarios(self):
        if (self.cantidad_total_x_padc > 0):
            self.porcentaje_total_voluntarios = ((self.cantidad_padc_x_cvem + self.cantidad_padc_x_cvim) / self.cantidad_total_x_padc) * 100

    @api.one
    @api.depends('cantidad_padc_x_cvem', 'cantidad_padc_x_cvim', 'cantidad_total_x_padc')
    def _compute_cantidad_total_no_voluntarios(self):
        self.cantidad_total_no_voluntarios = (self.cantidad_total_x_padc - (self.cantidad_padc_x_cvem + self.cantidad_padc_x_cvim)) * 100

    @api.one
    @api.depends('cantidad_mvih_clt_total', 'cantidad_mvih_clr_total')
    def _compute_reactivos_tamizados_vih(self):
        if (self.cantidad_mvih_clt_total > 0):
            self.reactivos_tamizados_vih = (self.cantidad_mvih_clr_total / self.cantidad_mvih_clt_total) * 1000

    @api.one
    @api.depends('cantidad_mhbsag_clt_total', 'cantidad_mhbsag_clr_total')
    def _compute_reactivos_tamizados_hbsag(self):
        if (self.cantidad_mhbsag_clt_total > 0):
            self.reactivos_tamizados_hbsag = (self.cantidad_mhbsag_clr_total / self.cantidad_mhbsag_clt_total) * 1000

    @api.one
    @api.depends('cantidad_mhepc_clt_total', 'cantidad_mhepc_clr_total')
    def _compute_reactivos_tamizados_hepc(self):
        if (self.cantidad_mhepc_clt_total > 0):
            self.reactivos_tamizados_hepc = (self.cantidad_mhepc_clr_total / self.cantidad_mhepc_clt_total) * 1000

    @api.one
    @api.depends('cantidad_mantihbc_clt_total', 'cantidad_mantihbc_clr_total')
    def _compute_reactivos_tamizados_antihbc(self):
        if (self.cantidad_mantihbc_clt_total > 0):
            self.reactivos_tamizados_antihbc = (self.cantidad_mantihbc_clr_total / self.cantidad_mantihbc_clt_total) * 1000

    @api.one
    @api.depends('cantidad_mhtlv_clt_total', 'cantidad_mhtlv_clr_total')
    def _compute_reactivos_tamizados_htlv(self):
        if (self.cantidad_mhtlv_clt_total > 0):
            self.reactivos_tamizados_htlv = (self.cantidad_mhtlv_clr_total / self.cantidad_mhtlv_clt_total) * 1000

    @api.one
    @api.depends('cantidad_msifilis_clt_total', 'cantidad_msifilis_clr_total')
    def _compute_reactivos_tamizados_sifilis(self):
        if (self.cantidad_msifilis_clt_total > 0):
            self.reactivos_tamizados_sifilis = (self.cantidad_msifilis_clr_total / self.cantidad_msifilis_clt_total) * 1000

    @api.one
    @api.depends('cantidad_mchagas_clt_total', 'cantidad_mchagas_clr_total')
    def _compute_reactivos_tamizados_chagas(self):
        if (self.cantidad_mchagas_clt_total > 0):
            self.reactivos_tamizados_chagas = (self.cantidad_mchagas_clr_total / self.cantidad_mchagas_clt_total) * 1000

    @api.one
    @api.depends('cantidad_motros_clt_total', 'cantidad_motros_clr_total')
    def _compute_reactivos_tamizados_otros(self):
        if (self.cantidad_motros_clt_total > 0):
            self.reactivos_tamizados_otros = (self.cantidad_motros_clr_total / self.cantidad_motros_clt_total) * 1000

    @api.one
    @api.depends('hemocomponente_ids')
    def _compute_total_producida_hemocomponente(self):
        for sangre_total in self.hemocomponente_ids:
            if sangre_total.hemocomponente == 'hst':
                self.cantidad_ptotal_st = sangre_total.cantidad_hemocomponente
            elif sangre_total.hemocomponente == 'hgr':
                self.cantidad_ptotal_gl = sangre_total.cantidad_hemocomponente
            elif sangre_total.hemocomponente == 'hpfc':
                self.cantidad_ptotal_pfc = sangre_total.cantidad_hemocomponente
            elif sangre_total.hemocomponente == 'hc':
                self.cantidad_ptotal_c = sangre_total.cantidad_hemocomponente
            elif sangre_total.hemocomponente == 'hp':
                self.cantidad_ptotal_pla = sangre_total.cantidad_hemocomponente
            elif sangre_total.hemocomponente == 'hap':
                self.cantidad_ptotal_af = sangre_total.cantidad_hemocomponente
            elif sangre_total.hemocomponente == 'hagr':
                self.cantidad_ptotal_afgl = sangre_total.cantidad_hemocomponente
            elif sangre_total.hemocomponente == 'haplasma':
                self.cantidad_ptotal_afpla = sangre_total.cantidad_hemocomponente

    @api.one
    @api.depends('cantidad_ctotal_hst', 'cantidad_ptotal_st')
    def _compute_st(self):
        if (self.cantidad_ptotal_st > 0):
            self.porcentaje_st = (float(self.cantidad_ctotal_hst) / self.cantidad_ptotal_st) * 100

    @api.one
    @api.depends('cantidad_ctotal_hgr', 'cantidad_ptotal_gl')
    def _compute_gl(self):
        if (self.cantidad_ptotal_gl > 0):
            self.porcentaje_gl = (float(self.cantidad_ctotal_hgr) / self.cantidad_ptotal_gl) * 100

    @api.one
    @api.depends('cantidad_ctotal_hpfc', 'cantidad_ptotal_pfc')
    def _compute_pfc(self):
        if (self.cantidad_ptotal_pfc > 0):
            self.porcentaje_pfc = (float(self.cantidad_ctotal_hpfc) / self.cantidad_ptotal_pfc) * 100

    @api.one
    @api.depends('cantidad_ctotal_hc', 'cantidad_ptotal_c')
    def _compute_c(self):
        if (self.cantidad_ptotal_c > 0):
            self.porcentaje_c = (float(self.cantidad_ctotal_hc) / self.cantidad_ptotal_c) * 100

    @api.one
    @api.depends('cantidad_ctotal_hp', 'cantidad_ptotal_pla')
    def _compute_pla(self):
        if (self.cantidad_ptotal_pla > 0):
            self.porcentaje_pla = (float(self.cantidad_ctotal_hp) / self.cantidad_ptotal_pla) * 100

    @api.one
    @api.depends('cantidad_ctotal_hap', 'cantidad_ptotal_af')
    def _compute_af(self):
        if (self.cantidad_ptotal_af > 0):
            self.porcentaje_af = (float(self.cantidad_ctotal_hap) / self.cantidad_ptotal_af) * 100

    @api.one
    @api.depends('cantidad_ctotal_hagr', 'cantidad_ptotal_afgl')
    def _compute_afgl(self):
        if (self.cantidad_ptotal_afgl > 0):
            self.porcentaje_afgl = (float(self.cantidad_ctotal_hagr) / self.cantidad_ptotal_afgl) * 100

    @api.one
    @api.depends('cantidad_ctotal_haplasma', 'cantidad_ptotal_afpla')
    def _compute_afpla(self):
        if (self.cantidad_ptotal_afpla > 0):
            self.porcentaje_afpla = (float(self.cantidad_ctotal_haplasma) / self.cantidad_ptotal_afpla) * 100

    @api.one
    def action_draft(self):
        self.state = constants.BORRADOR

    @api.one
    def action_send(self):
        self.state = constants.ENVIADO
        self.fecha_envio = fields.Date.today()

    @api.one
    def action_validate(self):
        self.state = constants.VALIDADO
        self.fecha_validacion = fields.Date.today()

    @api.multi
    def print_excel(self):
        self.ensure_one()
        url = '/web/binary/download_export_ficha?id={}&filename=Ficha_Estadística_{}_{}.xlsx'.format(self.id, self.ficha_anual_mensual, self.periodo_id.name or self.anho_id.name)
        value = {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new'
        }
        return value

    @api.multi
    def action_export_excel(self):
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

        if(self.banco_id.tipo_banco == '1'):
            tipo_banco = constants.TIPO_BANCO_1
        elif (self.banco_id.tipo_banco == '2'):
            tipo_banco = constants.TIPO_BANCO_2
        else:
            tipo_banco = ''

        archivo = 'FORMATO_FICHA_ESTADISTICA_2022.xlsx'
        ruta = '{}/../documents/{}'.format(os.path.dirname(os.path.abspath(__file__)), archivo)
        book = load_workbook(ruta)
        fobj = tempfile.NamedTemporaryFile(suffix='.xlsx', dir='/tmp/', delete=False)
        fname = fobj.name
        fobj.close()

        w_sheet = book.get_sheet_by_name('FORMATO ESTADISTICO')
        w_sheet['D3'] = self.banco_id.name
        w_sheet['J3'] = self.banco_id.renipress_id.codigo_eess
        w_sheet['J4'] = self.banco_id.renipress_id.diresa_id.name
        w_sheet['E5'] = tipo_banco
        w_sheet['D6'] = institucion
        w_sheet['E7'] = self.banco_id.renipress_id.direccion
        w_sheet['F8'] = self.banco_id.medico_coordinador_responsable
        w_sheet['C9'] = self.banco_id.num_camas
        w_sheet['F9'] = self.banco_id.telefono
        w_sheet['I9'] = self.banco_id.celular
        w_sheet['C10'] = self.banco_id.email
        w_sheet['I10'] = self.periodo_id.name

        map_field_celda = constants.MAP_FIELD_CELDA

        fields = list(map_field_celda.keys())
        fields = ', '.join(fields)

        sql = '''
                SELECT {}
                FROM hemored_ficha_estadistica
                WHERE id = {}
                LIMIT 1;
            '''.format(fields, self.id)

        self._cr.execute(sql)

        for field, valor in self._cr.dictfetchone().items():
            if valor:
                w_sheet[map_field_celda[field]] = valor
            else:
                w_sheet[map_field_celda[field]] = 0

        map_field_celda2 = ({
            # PARTICIPACIÓN EN PROGRAMA DE EVALUACIÓN EXTERNA DE LA CALIDAD DE TAMIZAJE
            'cantidad_mvih_s_o_n': 'C69',
            'cantidad_mhbsag_s_o_n': 'D69',
            'cantidad_mhepc_s_o_n': 'E69',
            'cantidad_mantihbc_s_o_n': 'F69',
            'cantidad_mhtlv_s_o_n': 'G69',
            'cantidad_msifilis_s_o_n': 'H69',
            'cantidad_mchagas_s_o_n': 'I69',
        })

        fields = list(map_field_celda2.keys())
        fields = ', '.join(fields)

        sql = '''
                SELECT {}
                FROM hemored_ficha_estadistica
                WHERE id = {}
                LIMIT 1;
            '''.format(fields, self.id)

        self._cr.execute(sql)

        for field, valor in self._cr.dictfetchone().items():
            if valor == 'S':
                w_sheet[map_field_celda2[field]] = 'X'

        sql = '''
                SELECT tipo_donante, cantidad
                FROM hemored_ficha_total_donante_line
                WHERE ficha_id = {};
            '''.format(self.id)

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
                SELECT motivo_diferido_excluido, cantidad
                FROM hemored_ficha_total_postulante_diferido_excluido_line
                WHERE ficha_id = {};
            '''.format(self.id)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if(val[0] == '1'):
                w_sheet['G26'] = valor
            elif(val[0] == '2'):
                w_sheet['H26'] = valor
            elif(val[0] == '3'):
                w_sheet['I26'] = valor
            elif(val[0] == '4'):
                w_sheet['J26'] = valor
            elif(val[0] == '5'):
                w_sheet['K26'] = valor
            elif(val[0] == '6'):
                w_sheet['L26'] = valor

        sql = '''
                SELECT grupo_edad_donante, cantidad
                FROM hemored_ficha_donacion_segun_grupo_edad_donante_line
                WHERE ficha_id = {};
            '''.format(self.id)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if(val[0] == '1'):
                w_sheet['E31'] = valor
            elif(val[0] == '2'):
                w_sheet['F31'] = valor
            elif(val[0] == '3'):
                w_sheet['G31'] = valor
            elif(val[0] == '4'):
                w_sheet['H31'] = valor
            elif(val[0] == '5'):
                w_sheet['I31'] = valor

        sql = '''
                SELECT tipo_donante, cantidad
                FROM hemored_ficha_donacion_sangre_total_line
                WHERE ficha_id = {};
            '''.format(self.id)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if(val[0] == 'dvpv'):
                w_sheet['B36'] = valor
            elif(val[0] == 'dvr'):
                w_sheet['C36'] = valor
            elif(val[0] == 'dr'):
                w_sheet['D36'] = valor
            elif(val[0] == 'dpr'):
                w_sheet['E36'] = valor
            elif(val[0] == 'da'):
                w_sheet['F36'] = valor

        sql = '''
                SELECT tipo_donante, cantidad
                FROM hemored_ficha_donacion_aferesis_line
                WHERE ficha_id = {};
            '''.format(self.id)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if(val[0] == 'dvpv'):
                w_sheet['H36'] = valor
            elif(val[0] == 'dvr'):
                w_sheet['I36'] = valor
            elif(val[0] == 'dr'):
                w_sheet['J36'] = valor
            elif(val[0] == 'dpr'):
                w_sheet['K36'] = valor
            elif(val[0] == 'da'):
                w_sheet['L36'] = valor

        sql = '''
                SELECT tipo_unidad_sangre, cantidad_tipo_unidad_sangre
                FROM hemored_ficha_produccion_unidad_sangre_line
                WHERE ficha_id = {};
            '''.format(self.id)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if(val[0] == '1'):
                w_sheet['B77'] = valor
            elif(val[0] == '2'):
                w_sheet['C77'] = valor
            elif(val[0] == '3'):
                w_sheet['D77'] = valor
            elif(val[0] == '4'):
                w_sheet['E77'] = valor

        sql = '''
                SELECT hemocomponente, cantidad_hemocomponente
                FROM hemored_ficha_produccion_hemocomponente_line
                WHERE ficha_id = {};
            '''.format(self.id)

        self._cr.execute(sql)

        vals = self.env.cr.fetchall()
        for val in vals:
            if val[1]:
                valor = val[1]
            else:
                valor = 0
            if(val[0] == 'hgr'):
                w_sheet['F77'] = valor
            elif(val[0] == 'hpfc'):
                w_sheet['G77'] = valor
            elif(val[0] == 'hc'):
                w_sheet['H77'] = valor
            elif(val[0] == 'hp'):
                w_sheet['I77'] = valor
            elif(val[0] == 'hap'):
                w_sheet['J77'] = valor
            elif(val[0] == 'hagr'):
                w_sheet['K77'] = valor
            elif(val[0] == 'haplasma'):
                w_sheet['L77'] = valor

        sql = '''
                SELECT tipo_reaccion_adversa, cantidad
                FROM hemored_ficha_causa_reaccion_adversa_line
                WHERE ficha_id = {};
            '''.format(self.id)

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


class FichaTotalDonante(models.Model):

    _name = MN_FichaTotalDonante
    _rec_name = 'ficha_id'

    ficha_id = fields.Many2one(
        comodel_name='hemored.ficha_estadistica',
    )
    banco_id = fields.Many2one(related='ficha_id.banco_id', store=True)
    anho_id = fields.Many2one(related='ficha_id.anho_id', store=True)
    periodo_id = fields.Many2one(related='ficha_id.periodo_id', store=True)
    diresa_id = fields.Many2one(related='ficha_id.diresa_id', store=True)
    tipo_banco = fields.Selection(related='ficha_id.tipo_banco', store=True)
    institucion = fields.Selection(related='ficha_id.institucion', store=True)
    inicio_fecha_registro = fields.Date(related='ficha_id.inicio_fecha_registro', store=True)
    fin_fecha_registro = fields.Date(related='ficha_id.fin_fecha_registro', store=True)
    state = fields.Selection(related='ficha_id.state', store=True)
    tipo_donante = fields.Selection('_selection_tipo_donante', 'Tipo Donante', required=True)

    cantidad = fields.Integer(
        'Cantidad',
        track_visibility='onchange',
    )

    @api.model
    def _selection_tipo_donante(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_donante2')

    @api.onchange('cantidad')
    def _onchange_valorespositvos_cantidad(self):
        if self.cantidad <= 0:
            return {
                'warning': {'message': u'El valor ingresado de cantidad, deben ser positivos o iguales a 0 ', },
                'value': {'cantidad': 0},
            }


class FichaTotalPostulanteDiferidoExcluido(models.Model):

    _name = MN_FichaTotalPostulanteDiferidoExcluido
    _rec_name = 'ficha_id'

    ficha_id = fields.Many2one(
        comodel_name='hemored.ficha_estadistica',
    )
    banco_id = fields.Many2one(related='ficha_id.banco_id', store=True)
    anho_id = fields.Many2one(related='ficha_id.anho_id', store=True)
    periodo_id = fields.Many2one(related='ficha_id.periodo_id', store=True)
    diresa_id = fields.Many2one(related='ficha_id.diresa_id', store=True)
    tipo_banco = fields.Selection(related='ficha_id.tipo_banco', store=True)
    institucion = fields.Selection(related='ficha_id.institucion', store=True)
    inicio_fecha_registro = fields.Date(related='ficha_id.inicio_fecha_registro', store=True)
    fin_fecha_registro = fields.Date(related='ficha_id.fin_fecha_registro', store=True)
    state = fields.Selection(related='ficha_id.state', store=True)
    motivo_diferido_excluido = fields.Selection('_selection_motivo_diferido_excluido', 'Categoría Postulante', required=True)

    cantidad = fields.Integer(
        'Cantidad',
        track_visibility='onchange',
    )

    @api.model
    def _selection_motivo_diferido_excluido(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_motivo_diferido_excluido')

    @api.onchange('cantidad')
    def _onchange_valorespositvos_cantidad(self):
        if self.cantidad <= 0:
            return {
                'warning': {'message': u'El valor ingresado de cantidad, deben ser positivos o iguales a 0 ', },
                'value': {'cantidad': 0},
            }


class FichaDonacionSegunGrupoEdadDonante(models.Model):

    _name = MN_FichaDonacionSegunGrupoEdadDonante
    _rec_name = 'ficha_id'

    ficha_id = fields.Many2one(
        comodel_name='hemored.ficha_estadistica',
    )
    banco_id = fields.Many2one(related='ficha_id.banco_id', store=True)
    anho_id = fields.Many2one(related='ficha_id.anho_id', store=True)
    periodo_id = fields.Many2one(related='ficha_id.periodo_id', store=True)
    diresa_id = fields.Many2one(related='ficha_id.diresa_id', store=True)
    tipo_banco = fields.Selection(related='ficha_id.tipo_banco', store=True)
    institucion = fields.Selection(related='ficha_id.institucion', store=True)
    inicio_fecha_registro = fields.Date(related='ficha_id.inicio_fecha_registro', store=True)
    fin_fecha_registro = fields.Date(related='ficha_id.fin_fecha_registro', store=True)
    state = fields.Selection(related='ficha_id.state', store=True)
    grupo_edad_donante = fields.Selection('_selection_grupo_edad_donante', 'Grupo Edad Donante', required=True)

    cantidad = fields.Integer(
        'Cantidad',
        track_visibility='onchange',
    )

    @api.model
    def _selection_grupo_edad_donante(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_grupo_edad_donante')

    @api.onchange('cantidad')
    def _onchange_valorespositvos_cantidad(self):
        if self.cantidad <= 0:
            return {
                'warning': {'message': u'El valor ingresado de cantidad, deben ser positivos o iguales a 0 ', },
                'value': {'cantidad': 0},
            }


class FichaDonacionSangreTotal(models.Model):

    _name = MN_FichaDonacionSangreTotal
    _rec_name = 'ficha_id'

    ficha_id = fields.Many2one(
        comodel_name='hemored.ficha_estadistica',
    )
    banco_id = fields.Many2one(related='ficha_id.banco_id', store=True)
    anho_id = fields.Many2one(related='ficha_id.anho_id', store=True)
    periodo_id = fields.Many2one(related='ficha_id.periodo_id', store=True)
    diresa_id = fields.Many2one(related='ficha_id.diresa_id', store=True)
    tipo_banco = fields.Selection(related='ficha_id.tipo_banco', store=True)
    institucion = fields.Selection(related='ficha_id.institucion', store=True)
    inicio_fecha_registro = fields.Date(related='ficha_id.inicio_fecha_registro', store=True)
    fin_fecha_registro = fields.Date(related='ficha_id.fin_fecha_registro', store=True)
    state = fields.Selection(related='ficha_id.state', store=True)
    tipo_donante = fields.Selection('_selection_tipo_donante', 'Tipo Donante', required=True)

    cantidad = fields.Integer(
        'Cantidad',
        track_visibility='onchange',
    )

    @api.model
    def _selection_tipo_donante(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_donante')

    @api.onchange('cantidad')
    def _onchange_valorespositvos_cantidad(self):
        if self.cantidad <= 0:
            return {
                'warning': {'message': u'El valor ingresado de cantidad, deben ser positivos o iguales a 0 ', },
                'value': {'cantidad': 0},
            }


class FichaDonacionAferesis(models.Model):

    _name = MN_FichaDonacionAferesis
    _rec_name = 'ficha_id'

    ficha_id = fields.Many2one(
        comodel_name='hemored.ficha_estadistica',
    )
    banco_id = fields.Many2one(related='ficha_id.banco_id', store=True)
    anho_id = fields.Many2one(related='ficha_id.anho_id', store=True)
    periodo_id = fields.Many2one(related='ficha_id.periodo_id', store=True)
    diresa_id = fields.Many2one(related='ficha_id.diresa_id', store=True)
    tipo_banco = fields.Selection(related='ficha_id.tipo_banco', store=True)
    institucion = fields.Selection(related='ficha_id.institucion', store=True)
    inicio_fecha_registro = fields.Date(related='ficha_id.inicio_fecha_registro', store=True)
    fin_fecha_registro = fields.Date(related='ficha_id.fin_fecha_registro', store=True)
    state = fields.Selection(related='ficha_id.state', store=True)
    tipo_donante = fields.Selection('_selection_tipo_donante', 'Tipo Donante', required=True)

    cantidad = fields.Integer(
        'Cantidad',
        track_visibility='onchange',
    )

    @api.model
    def _selection_tipo_donante(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_donante')

    @api.onchange('cantidad')
    def _onchange_valorespositvos_cantidad(self):
        if self.cantidad <= 0:
            return {
                'warning': {'message': u'El valor ingresado de cantidad, deben ser positivos o iguales a 0 ', },
                'value': {'cantidad': 0},
            }


class FichaProduccionHemocomponenteUnidadSangre(models.Model):

    _name = MN_FichaProduccionHemocomponenteUnidadSangre
    _rec_name = 'ficha_id'

    ficha_id = fields.Many2one(
        comodel_name='hemored.ficha_estadistica',
    )
    banco_id = fields.Many2one(related='ficha_id.banco_id', store=True)
    anho_id = fields.Many2one(related='ficha_id.anho_id', store=True)
    periodo_id = fields.Many2one(related='ficha_id.periodo_id', store=True)
    diresa_id = fields.Many2one(related='ficha_id.diresa_id', store=True)
    tipo_banco = fields.Selection(related='ficha_id.tipo_banco', store=True)
    institucion = fields.Selection(related='ficha_id.institucion', store=True)
    inicio_fecha_registro = fields.Date(related='ficha_id.inicio_fecha_registro', store=True)
    fin_fecha_registro = fields.Date(related='ficha_id.fin_fecha_registro', store=True)
    state = fields.Selection(related='ficha_id.state', store=True)
    tipo_unidad_sangre = fields.Selection('_selection_tipo_unidad_sangre', 'Tipo de Unidad de Sangre', required=True)

    cantidad_tipo_unidad_sangre = fields.Integer(
        'Cantidad unidad de sangre',
        track_visibility='onchange',
    )

    @api.model
    def _selection_tipo_unidad_sangre(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_unidad_sangre')

    @api.onchange('cantidad_tipo_unidad_sangre')
    def _onchange_valorespositvos_cantidad_tipo_unidad_sangre(self):
        if self.cantidad_tipo_unidad_sangre <= 0:
            return {
                'warning': {'message': u'El valor ingresado de cantidad_tipo_unidad_sangre, deben ser positivos o iguales a 0 ', },
                'value': {'cantidad_tipo_unidad_sangre': 0},
            }


class FichaProduccionHemocomponente(models.Model):

    _name = MN_FichaProduccionHemocomponente
    _rec_name = 'ficha_id'

    ficha_id = fields.Many2one(
        comodel_name='hemored.ficha_estadistica',
    )
    banco_id = fields.Many2one(related='ficha_id.banco_id', store=True)
    anho_id = fields.Many2one(related='ficha_id.anho_id', store=True)
    periodo_id = fields.Many2one(related='ficha_id.periodo_id', store=True)
    diresa_id = fields.Many2one(related='ficha_id.diresa_id', store=True)
    tipo_banco = fields.Selection(related='ficha_id.tipo_banco', store=True)
    institucion = fields.Selection(related='ficha_id.institucion', store=True)
    inicio_fecha_registro = fields.Date(related='ficha_id.inicio_fecha_registro', store=True)
    fin_fecha_registro = fields.Date(related='ficha_id.fin_fecha_registro', store=True)
    state = fields.Selection(related='ficha_id.state', store=True)
    hemocomponente = fields.Selection('_selection_hemocomponente', 'Hemocomponente', required=True)

    cantidad_hemocomponente = fields.Integer(
        'Cantidad hemocomponente',
        track_visibility='onchange',
    )

    @api.model
    def _selection_hemocomponente(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_hemocomponente')

    @api.onchange('cantidad_hemocomponente')
    def _onchange_valorespositvos_cantidad_hemocomponente(self):
        if self.cantidad_hemocomponente <= 0:
            return {
                'warning': {'message': u'El valor ingresado de cantidad_hemocomponente, deben ser positivos o iguales a 0 ', },
                'value': {'cantidad_hemocomponente': 0},
            }


class FichaCausaReaccionAdversa(models.Model):

    _name = MN_FichaCausaReaccionAdversa
    _rec_name = 'ficha_id'

    ficha_id = fields.Many2one(
        comodel_name='hemored.ficha_estadistica',
    )
    banco_id = fields.Many2one(related='ficha_id.banco_id', store=True)
    anho_id = fields.Many2one(related='ficha_id.anho_id', store=True)
    periodo_id = fields.Many2one(related='ficha_id.periodo_id', store=True)
    diresa_id = fields.Many2one(related='ficha_id.diresa_id', store=True)
    tipo_banco = fields.Selection(related='ficha_id.tipo_banco', store=True)
    institucion = fields.Selection(related='ficha_id.institucion', store=True)
    inicio_fecha_registro = fields.Date(related='ficha_id.inicio_fecha_registro', store=True)
    fin_fecha_registro = fields.Date(related='ficha_id.fin_fecha_registro', store=True)
    state = fields.Selection(related='ficha_id.state', store=True)
    tipo_reaccion_adversa = fields.Selection('_selection_tipo_reaccion_adversa', 'Tipo Reaccion Adversa', required=True)

    cantidad = fields.Integer(
        'Cantidad',
        track_visibility='onchange',
    )

    @api.model
    def _selection_tipo_reaccion_adversa(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_reaccion_adversa')

    @api.onchange('cantidad')
    def _onchange_valorespositvos_cantidad(self):
        if self.cantidad <= 0:
            return {
                'warning': {'message': u'El valor ingresado de cantidad, deben ser positivos o iguales a 0 ', },
                'value': {'cantidad': 0},
            }
