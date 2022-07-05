# -*- coding: utf-8 -*-

from datetime import date
from odoo import api, fields, models

from ..models import constants


def _default_bancos_tipo_ii(self):
    bancos = self.env['hemored.banco_sangre'].search([('tipo_banco', '=', '2')])
    list_bancos = []
    if bancos:
        list_bancos = bancos.ids
    return [(6, 0, list_bancos)]


def _get_company(self):
    return self.env.user.company_id


class GenerarFichaStock(models.Model):
    _name = 'stock_hemocomponente.generar_ficha'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: _get_company(self),
        track_visibility='onchange'
    )
    banco_ids = fields.Many2many(
        comodel_name='hemored.banco_sangre',
        string='Bancos de sangre',
        default=lambda self: _default_bancos_tipo_ii(self)
    )

    _sql_constraints = [
        ('company_id', 'unique(company_id)',
         'El registro debe ser único!'),
    ]

    @api.onchange('consolidado')
    def _onchange_consolidado(self):
        if not self.consolidado:
            self.periodo_id = False

    def _crear_ficha(self):
        camp_obj = self.env['stock_hemocomponente.generar_ficha']
        generar_ficha_ids = camp_obj.search([('company_id', '=', self.env.user.company_id.id)])
        generar_ficha_ids.action_crear_ficha()
        return True

    @api.multi
    def action_crear_ficha(self):
        self.ensure_one()
        for record in self:
            today = date.today()
            list_vals = []
            list_create = []
            lista_bancos_ficha = record.banco_ids.ids
            key_tuples = []
            for obj in self.env['stock_hemocomponente.hemocomponente'].search([('fecha', '=', today)]):
                key_tuples.append((obj.banco_id.id))

            for x in lista_bancos_ficha:
                if x not in key_tuples:
                    list_create.append(x)

            for i in self.env['hemored.banco_sangre'].browse(list_create):
                vals = {
                    'banco_id': i.id,
                    'diresa_id': i.renipress_id.diresa_id.id,
                    'state': constants.NO_REPORTO,
                }
                list_vals.append(vals)

            for j in list_vals:
                self.env['stock_hemocomponente.hemocomponente'].create(j)
