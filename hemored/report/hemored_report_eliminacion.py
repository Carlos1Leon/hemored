# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools

from ..models import constants


class EliminacionComponente(models.Model):
    _name = 'hemored.eliminacion_componente_report'
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
    cantidad_cv_hst = fields.Integer('Cantidad eliminados por vencimiento de Sangre Total')
    cantidad_cv_hgr = fields.Integer('Cantidad eliminados por vencimiento de globulos rojos')
    cantidad_cv_hpfc = fields.Integer('Cantidad eliminados por vencimiento de Plasma Fresco Congelado')
    cantidad_cv_hc = fields.Integer('Cantidad eliminados por vencimiento de Crioprecipitado')
    cantidad_cv_hp = fields.Integer('Cantidad eliminados por vencimiento de plaquetas')
    cantidad_cv_hap = fields.Integer('Cantidad eliminados por vencimiento de aféresis de plaquetas')
    cantidad_cv_hagr = fields.Integer('Cantidad eliminados por vencimiento de aféresis de globulos rojos')
    cantidad_cv_haplasma = fields.Integer('Cantidad eliminados por vencimiento de aféresis de plasma')
    cantidad_cv_total = fields.Integer('Cantidad eliminados por vencimiento de total')
    cantidad_cmitt_hst = fields.Integer('Cantidad eliminados por marcadores itt de Sangre Total')
    cantidad_cmitt_hgr = fields.Integer('Cantidad eliminados por marcadores itt de globulos rojos')
    cantidad_cmitt_hpfc = fields.Integer('Cantidad eliminados por marcadores itt de Plasma Fresco Congelado')
    cantidad_cmitt_hc = fields.Integer('Cantidad eliminados por marcadores itt de Crioprecipitado')
    cantidad_cmitt_hp = fields.Integer('Cantidad eliminados por marcadores itt de plaquetas')
    cantidad_cmitt_hap = fields.Integer('Cantidad eliminados por marcadores itt de aféresis de plaquetas')
    cantidad_cmitt_hagr = fields.Integer('Cantidad eliminados por marcadores itt de aféresis de globulos rojos')
    cantidad_cmitt_haplasma = fields.Integer('Cantidad eliminados por marcadores itt de aféresis de plasma')
    cantidad_cmitt_total = fields.Integer('Cantidad eliminados por marcadores itt de total')
    cantidad_ca_hst = fields.Integer('Cantidad eliminados por almacenamiento de Sangre Total')
    cantidad_ca_hgr = fields.Integer('Cantidad eliminados por almacenamiento de globulos rojos')
    cantidad_ca_hpfc = fields.Integer('Cantidad eliminados por almacenamiento de Plasma Fresco Congelado')
    cantidad_ca_hc = fields.Integer('Cantidad eliminados por almacenamiento de Crioprecipitado')
    cantidad_ca_hp = fields.Integer('Cantidad eliminados por almacenamiento de plaquetas')
    cantidad_ca_hap = fields.Integer('Cantidad eliminados por almacenamiento de aféresis de plaquetas')
    cantidad_ca_hagr = fields.Integer('Cantidad eliminados por almacenamiento de aféresis de globulos rojos')
    cantidad_ca_haplasma = fields.Integer('Cantidad eliminados por almacenamiento de aféresis de plasma')
    cantidad_ca_total = fields.Integer('Cantidad eliminados por almacenamiento de total')
    cantidad_ct_hst = fields.Integer('Cantidad eliminados por transporte de Sangre Total')
    cantidad_ct_hgr = fields.Integer('Cantidad eliminados por transporte de globulos rojos')
    cantidad_ct_hpfc = fields.Integer('Cantidad eliminados por transporte de Plasma Fresco Congelado')
    cantidad_ct_hc = fields.Integer('Cantidad eliminados por transporte de Crioprecipitado')
    cantidad_ct_hp = fields.Integer('Cantidad eliminados por transporte de plaquetas')
    cantidad_ct_hap = fields.Integer('Cantidad eliminados por transporte de aféresis de plaquetas')
    cantidad_ct_hagr = fields.Integer('Cantidad eliminados por transporte de aféresis de globulos rojos')
    cantidad_ct_haplasma = fields.Integer('Cantidad eliminados por transporte de aféresis de plasma')
    cantidad_ct_total = fields.Integer('Cantidad eliminados por transporte de total')
    cantidad_cp_hst = fields.Integer('Cantidad eliminados por procesamiento de Sangre Total')
    cantidad_cp_hgr = fields.Integer('Cantidad eliminados por procesamiento de globulos rojos')
    cantidad_cp_hpfc = fields.Integer('Cantidad eliminados por procesamiento de Plasma Fresco Congelado')
    cantidad_cp_hc = fields.Integer('Cantidad eliminados por procesamiento de Crioprecipitado')
    cantidad_cp_hp = fields.Integer('Cantidad eliminados por procesamiento de plaquetas')
    cantidad_cp_hap = fields.Integer('Cantidad eliminados por procesamiento de aféresis de plaquetas')
    cantidad_cp_hagr = fields.Integer('Cantidad eliminados por procesamiento de aféresis de globulos rojos')
    cantidad_cp_haplasma = fields.Integer('Cantidad eliminados por procesamiento de aféresis de plasma')
    cantidad_cp_total = fields.Integer('Cantidad eliminados por procesamiento de total')
    cantidad_co_hst = fields.Integer('Cantidad eliminados por otros de Sangre Total')
    cantidad_co_hgr = fields.Integer('Cantidad eliminados por otros de globulos rojos')
    cantidad_co_hpfc = fields.Integer('Cantidad eliminados por otros de Plasma Fresco Congelado')
    cantidad_co_hc = fields.Integer('Cantidad eliminados por otros de Crioprecipitado')
    cantidad_co_hp = fields.Integer('Cantidad eliminados por otros de plaquetas')
    cantidad_co_hap = fields.Integer('Cantidad eliminados por otros de aféresis de plaquetas')
    cantidad_co_hagr = fields.Integer('Cantidad eliminados por otros de aféresis de globulos rojos')
    cantidad_co_haplasma = fields.Integer('Cantidad eliminados por otros de aféresis de plasma')
    cantidad_co_total = fields.Integer('Cantidad eliminados por otros de total')
    cantidad_ctotal_hst = fields.Integer('Cantidad eliminados de sangre total')
    cantidad_ctotal_hgr = fields.Integer('Cantidad eliminados de globulos rojos')
    cantidad_ctotal_hpfc = fields.Integer('Cantidad eliminados de plasma fresco congelado')
    cantidad_ctotal_hc = fields.Integer('Cantidad eliminados de crioprecipitado')
    cantidad_ctotal_hp = fields.Integer('Cantidad eliminados de plaquetas')
    cantidad_ctotal_hap = fields.Integer('Cantidad eliminados de aféresis de plaquetas')
    cantidad_ctotal_hagr = fields.Integer('Cantidad eliminados de aféresis de globulos rojos')
    cantidad_ctotal_haplasma = fields.Integer('Cantidad eliminados de aféresis de plasma')

    @api.model
    def _selection_tipo_banco(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_banco')

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
                    CREATE VIEW hemored_eliminacion_componente_report AS (
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
                        data.cantidad_cv_hst,
                        data.cantidad_cv_hgr,
                        data.cantidad_cv_hpfc,
                        data.cantidad_cv_hc,
                        data.cantidad_cv_hp,
                        data.cantidad_cv_hap,
                        data.cantidad_cv_hagr,
                        data.cantidad_cv_haplasma,
                        data.cantidad_cv_total,
                        data.cantidad_cmitt_hst,
                        data.cantidad_cmitt_hgr,
                        data.cantidad_cmitt_hpfc,
                        data.cantidad_cmitt_hc,
                        data.cantidad_cmitt_hp,
                        data.cantidad_cmitt_hap,
                        data.cantidad_cmitt_hagr,
                        data.cantidad_cmitt_haplasma,
                        data.cantidad_cmitt_total,
                        data.cantidad_ca_hst,
                        data.cantidad_ca_hgr,
                        data.cantidad_ca_hpfc,
                        data.cantidad_ca_hc,
                        data.cantidad_ca_hp,
                        data.cantidad_ca_hap,
                        data.cantidad_ca_hagr,
                        data.cantidad_ca_haplasma,
                        data.cantidad_ca_total,
                        data.cantidad_ct_hst,
                        data.cantidad_ct_hgr,
                        data.cantidad_ct_hpfc,
                        data.cantidad_ct_hc,
                        data.cantidad_ct_hp,
                        data.cantidad_ct_hap,
                        data.cantidad_ct_hagr,
                        data.cantidad_ct_haplasma,
                        data.cantidad_ct_total,
                        data.cantidad_cp_hst,
                        data.cantidad_cp_hgr,
                        data.cantidad_cp_hpfc,
                        data.cantidad_cp_hc,
                        data.cantidad_cp_hp,
                        data.cantidad_cp_hap,
                        data.cantidad_cp_total,
                        data.cantidad_co_hst,
                        data.cantidad_co_hgr,
                        data.cantidad_co_hpfc,
                        data.cantidad_co_hc,
                        data.cantidad_co_hp,
                        data.cantidad_co_hap,
                        data.cantidad_co_hagr,
                        data.cantidad_co_haplasma,
                        data.cantidad_co_total,
                        data.cantidad_ctotal_hst,
                        data.cantidad_ctotal_hgr,
                        data.cantidad_ctotal_hpfc,
                        data.cantidad_ctotal_hc,
                        data.cantidad_ctotal_hp,
                        data.cantidad_ctotal_hap,
                        data.cantidad_ctotal_hagr,
                        data.cantidad_ctotal_haplasma
                    FROM hemored_ficha_estadistica data
                )
                """)
