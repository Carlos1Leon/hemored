# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools

from ..models import constants


class Hemocomponente(models.Model):
    _name = 'hemored.hemocomponente_report'
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
    cantidad_ctotal_hst = fields.Integer('Número de unidades de sangre total eliminados')
    cantidad_ptotal_st = fields.Integer('Número de sangre total producidas')
    porcentaje_st = fields.Float('% de unidades de sangre total eliminada')
    cantidad_ctotal_hgr = fields.Integer('Número de globulos rojos eliminados')
    cantidad_ptotal_gl = fields.Integer('Número de globulos rojos producidos')
    porcentaje_gl = fields.Float('% de unidades de globulos rojos eliminados')
    cantidad_ctotal_hpfc = fields.Integer('Número de plasma fresco congelado eliminado')
    cantidad_ptotal_pfc = fields.Integer('Número de plasma fresco congelado producido')
    porcentaje_pfc = fields.Float('% de unidades de plasma fresco congelado eliminado')
    cantidad_ctotal_hc = fields.Integer('Número de crioprecipitado eliminado')
    cantidad_ptotal_c = fields.Integer('Número de crioprecipitado producido')
    porcentaje_c = fields.Float('% de unidades de crioprecipitado eliminado')
    cantidad_ctotal_hp = fields.Integer('Número de plaquetas eliminadas')
    cantidad_ptotal_pla = fields.Integer('Número de plaquetas producidas')
    porcentaje_pla = fields.Float('% de unidades de plaquetas eliminadas')
    cantidad_ctotal_hap = fields.Integer('Número de aféresis de plaquetas eliminadas')
    cantidad_ptotal_af = fields.Integer('Número de aféresis de plaquetas producidas')
    porcentaje_af = fields.Float('% de unidades de aféresis de plaquetas eliminadas')
    cantidad_ctotal_hagr = fields.Integer('Número de aféresis de globulos rojos eliminados')
    cantidad_ptotal_afgl = fields.Integer('Número de aféresis de globulos rojos producidos')
    porcentaje_afgl = fields.Float('% de unidades de aféresis de globulos rojos eliminados')
    cantidad_ctotal_haplasma = fields.Integer('Número de aféresis de plasma eliminados')
    cantidad_ptotal_afpla = fields.Integer('Número de aféresis de plasma producidos')
    porcentaje_afpla = fields.Float('% de unidades de aféresis de plasma eliminados')

    @api.model
    def _selection_tipo_banco(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_banco')

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
                    CREATE VIEW hemored_hemocomponente_report AS (
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
                        data.cantidad_ctotal_hst,
                        data.cantidad_ptotal_st,
                        data.porcentaje_st,
                        data.cantidad_ctotal_hgr,
                        data.cantidad_ptotal_gl,
                        data.porcentaje_gl,
                        data.cantidad_ctotal_hpfc,
                        data.cantidad_ptotal_pfc,
                        data.porcentaje_pfc,
                        data.cantidad_ctotal_hc,
                        data.cantidad_ptotal_c,
                        data.porcentaje_c,
                        data.cantidad_ctotal_hp,
                        data.cantidad_ptotal_pla,
                        data.porcentaje_pla,
                        data.cantidad_ctotal_hap,
                        data.cantidad_ptotal_af,
                        data.porcentaje_af,
                        data.cantidad_ctotal_hagr,
                        data.cantidad_ptotal_afgl,
                        data.porcentaje_afgl,
                        data.cantidad_ctotal_haplasma,
                        data.cantidad_ptotal_afpla,
                        data.porcentaje_afpla
                    FROM hemored_ficha_estadistica data
                )
                """)
