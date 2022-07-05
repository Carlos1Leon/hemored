# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools

from ..models import constants


class FichaEstadistica(models.Model):
    _name = 'hemored.ficha_estadistica_report'
    _rec_name = 'banco_id'
    _order = 'periodo_id asc'
    _auto = False

    banco_id = fields.Many2one('hemored.banco_sangre', 'Banco')
    anho_id = fields.Many2one('minsa.anho', 'Año')
    periodo_id = fields.Many2one('minsa.periodo', 'Periodo')
    diresa_id = fields.Many2one('renipress.diresa', 'Diresa')
    user_id = fields.Many2one('res.users', 'Responsable')
    tipo_banco = fields.Selection('_selection_tipo_banco', 'Tipo de Banco')
    institucion = fields.Selection(constants.SELECTION_INSTITUCION, 'Institución')
    inicio_fecha_registro = fields.Date('Inicio de fecha de Registro')
    fin_fecha_registro = fields.Date('Fin de fecha de Registro')
    state = fields.Selection(constants.SELECTION_STATE, 'Estado')
    cantidad_total_x_pe = fields.Integer('Total postulantes diferidos permanentemente')
    cantidad_total_x_pd = fields.Integer('Total postulantes diferidos temporalmente')
    cantidad_total_x_padi = fields.Integer('Total postulantes donacion incompleta')
    cantidad_total_x_padc = fields.Integer('Total de unidades colectadas')
    cantidad_total_x_ca = fields.Integer('Total autólogos')
    cantidad_total_x_cvim = fields.Integer('Total voluntarios IM')
    cantidad_total_x_cvem = fields.Integer('Total voluntarios EM')
    cantidad_total_x_cr = fields.Integer('Total reposición')
    cantidad_total_x_cpr = fields.Integer('Total presuntamente remunerado')
    cantidad_total_postulantes_donacion_sangre = fields.Integer('Total de postulantes')
    cantidad_porcentaje_postulantes_donacion_completa = fields.Float('% de postulantes que lograron donar')
    cantidad_porcentaje_postulantes_diferidos = fields.Float('% de postulantes diferidos temporales')
    cantidad_porcentaje_postulantes_excluidos = fields.Float('% de postulantes diferidos permanentemente')
    cantidad_total_voluntarios = fields.Integer('Total unidades colectadas de donantes voluntarios')
    cantidad_total_no_voluntarios = fields.Integer('Total de donantes que no son voluntarios')
    porcentaje_total_voluntarios = fields.Float('% donacion voluntaria')
    cantidad_total_donante = fields.Integer('Total de donantes')
    cantidad_total_postulante_diferido_excluido = fields.Integer('Total de total postulante diferido excluido')
    cantidad_mvih_clt_total = fields.Integer('Total VIH tamizados')
    cantidad_mvih_clr_total = fields.Integer('Total VIH reactivos')
    cantidad_mvih_clzg_total = fields.Integer('Total VIH zona gris')
    reactivos_tamizados_vih = fields.Float('Division Reactivos entre Tamizados VIH')
    cantidad_mhbsag_clt_total = fields.Integer('Total HBsAG tamizados')
    cantidad_mhbsag_clr_total = fields.Integer('Total HBsAG reactivos')
    cantidad_mhbsag_clzg_total = fields.Integer('Total HBsAG zona gris')
    reactivos_tamizados_hbsag = fields.Float('Division Reactivos entre Tamizados HBsAG')
    cantidad_mhepc_clt_total = fields.Integer('Total Hep C tamizados')
    cantidad_mhepc_clr_total = fields.Integer('Total Hep C reactivos')
    cantidad_mhepc_clzg_total = fields.Integer('Total Hep C zona gris')
    reactivos_tamizados_hepc = fields.Float('Division Reactivos entre Tamizados Hep C')
    cantidad_mantihbc_clt_total = fields.Integer('Total Anti-HBc tamizados')
    cantidad_mantihbc_clr_total = fields.Integer('Total Anti-HBc reactivos')
    cantidad_mantihbc_clzg_total = fields.Integer('Total Anti-HBc zona gris')
    reactivos_tamizados_antihbc = fields.Float('Division Reactivos entre Tamizados Anti-HBc')
    cantidad_msifilis_clt_total = fields.Integer('Total sifilis tamizados')
    cantidad_msifilis_clr_total = fields.Integer('Total sifilis reactivos')
    cantidad_msifilis_clzg_total = fields.Integer('Total sifilis zona gris')
    reactivos_tamizados_sifilis = fields.Float('Division Reactivos entre Tamizados Sifilis')
    cantidad_mchagas_clt_total = fields.Integer('Total chagas tamizados')
    cantidad_mchagas_clr_total = fields.Integer('Total chagas reactivos')
    cantidad_mchagas_clzg_total = fields.Integer('Total chagas zona gris')
    reactivos_tamizados_chagas = fields.Float('Division Reactivos entre Tamizados Chagas')
    cantidad_motros_clt_total = fields.Integer('Total otros tamizados')
    cantidad_motros_clr_total = fields.Integer('Total otros reactividad')
    cantidad_motros_clzg_total = fields.Integer('Total otros zona gris')
    reactivos_tamizados_otros = fields.Float('Division Reactivos entre Tamizados Otros')
    cantidad_mhtlv_clt_total = fields.Integer('Total HTLV I/II tamizados')
    cantidad_mhtlv_clr_total = fields.Integer('Total HTLV I/II reactivos')
    cantidad_mhtlv_clzg_total = fields.Integer('Total HTLV I/II zona gris')
    cantidad_total_tamizaje_unidad = fields.Integer('Total de Tamizaje')
    reactivos_tamizados_htlv = fields.Float('Division Reactivos entre Tamizados HTLV')
    cantidad_unr_total = fields.Integer('Total no reactivos')
    cantidad_ur_total = fields.Integer('Total reactivos')
    cantidad_uzg_total = fields.Integer('Total zona gris')
    cantidad_total_produccion_unidad_sangre = fields.Integer('Total de Producción unidad sangre')
    cantidad_total_hemocomponente = fields.Integer('Total hemocomponentes en Producción')
    cantidad_total_causa_reaccion_adversa = fields.Integer('Total de Producción causa reaccion adversa')

    @api.model
    def _selection_tipo_banco(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_banco')

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
                CREATE VIEW hemored_ficha_estadistica_report AS (
                SELECT
                    data.id,
                    data.banco_id,
                    data.anho_id,
                    data.periodo_id,
                    data.diresa_id,
                    data.user_id,
                    data.tipo_banco,
                    data.institucion,
                    data.inicio_fecha_registro,
                    data.fin_fecha_registro,
                    data.state,
                    data.cantidad_total_x_pe,
                    data.cantidad_total_x_pd,
                    data.cantidad_total_x_padi,
                    data.cantidad_total_x_padc,
                    data.cantidad_total_x_ca,
                    data.cantidad_total_x_cvim,
                    data.cantidad_total_x_cvem,
                    data.cantidad_total_x_cr,
                    data.cantidad_total_x_cpr,
                    data.cantidad_total_postulantes_donacion_sangre,
                    data.cantidad_porcentaje_postulantes_donacion_completa,
                    data.cantidad_porcentaje_postulantes_diferidos,
                    data.cantidad_porcentaje_postulantes_excluidos,
                    data.cantidad_total_voluntarios,
                    data.cantidad_total_no_voluntarios,
                    data.porcentaje_total_voluntarios,
                    data.cantidad_total_donante,
                    data.cantidad_total_postulante_diferido_excluido,
                    data.cantidad_mvih_clt_total,
                    data.cantidad_mvih_clr_total,
                    data.cantidad_mvih_clzg_total,
                    data.cantidad_mhbsag_clt_total,
                    data.cantidad_mhbsag_clr_total,
                    data.cantidad_mhbsag_clzg_total,
                    data.cantidad_mhepc_clt_total,
                    data.cantidad_mhepc_clr_total,
                    data.cantidad_mhepc_clzg_total,
                    data.cantidad_mantihbc_clt_total,
                    data.cantidad_mantihbc_clr_total,
                    data.cantidad_mantihbc_clzg_total,
                    data.cantidad_mhtlv_clt_total,
                    data.cantidad_mhtlv_clr_total,
                    data.cantidad_mhtlv_clzg_total,
                    data.cantidad_msifilis_clt_total,
                    data.cantidad_msifilis_clr_total,
                    data.cantidad_msifilis_clzg_total,
                    data.cantidad_mchagas_clt_total,
                    data.cantidad_mchagas_clr_total,
                    data.cantidad_mchagas_clzg_total,
                    data.cantidad_motros_clt_total,
                    data.cantidad_motros_clr_total,
                    data.cantidad_motros_clzg_total,
                    data.cantidad_total_tamizaje_unidad,
                    data.reactivos_tamizados_vih,
                    data.reactivos_tamizados_hbsag,
                    data.reactivos_tamizados_hepc,
                    data.reactivos_tamizados_antihbc,
                    data.reactivos_tamizados_htlv,
                    data.reactivos_tamizados_sifilis,
                    data.reactivos_tamizados_chagas,
                    data.reactivos_tamizados_otros,
                    data.cantidad_unr_total,
                    data.cantidad_ur_total,
                    data.cantidad_uzg_total,
                    data.cantidad_total_produccion_unidad_sangre,
                    data.cantidad_total_hemocomponente,
                    data.cantidad_total_causa_reaccion_adversa
                FROM hemored_ficha_estadistica data
            )
            """)
