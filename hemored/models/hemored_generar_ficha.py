# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


def _default_banco(self):
    bancos = self.env['hemored.banco_sangre'].search([])
    list_bancos = []
    if bancos:
        list_bancos = bancos.ids
    return [(6, 0, list_bancos)]


class GenerarFicha(models.Model):
    _name = 'hemored.generar_ficha'
    _rec_name = 'anho_id'

    anho_id = fields.Many2one(comodel_name='minsa.anho', string='Año', required=True)
    periodo_id = fields.Many2one(
        comodel_name='minsa.periodo',
        string='Periodo'
    )
    consolidado = fields.Boolean(
        string='Consolidado'
    )
    banco_ids = fields.Many2many(
        comodel_name='hemored.banco_sangre',
        string='Bancos de sangre',
        default=lambda self: _default_banco(self)
    )

    _sql_constraints = [
        ('anho_unico', 'unique(anho_id)',
         'Solo se permite un registro por año'),
    ]

    @api.onchange('consolidado')
    def _onchange_consolidado(self):
        if not self.consolidado:
            self.periodo_id = False

    def _crear_ficha(self):
        camp_obj = self.env['hemored.generar_ficha']
        fecha = fields.Date.today()
        domain_periodo = [('name', '=', str(fecha.year))]
        periodo_id = self.env['minsa.anho'].search(domain_periodo, limit=1)
        generar_ficha_ids = camp_obj.search([('anho_id', '=', periodo_id.id)])
        generar_ficha_ids.write({'periodo_id': False, 'consolidado': False})
        generar_ficha_ids.action_crear_ficha()
        return True

    @api.multi
    def action_crear_ficha(self):
        self.ensure_one()
        banco_objs = self.banco_ids
        consolidado = True
        fecha_hoy = fields.Date.today()
        mes = fecha_hoy.month - 1 if fecha_hoy.month != 1 else fecha_hoy.month
        anho = fecha_hoy.year
        domain_periodo = [
            ('month', '=', mes),
            ('year', '=', int(anho)),
        ]
        if not self.consolidado:
            if self.periodo_id:
                periodo_id = self.periodo_id
            else:
                periodo_id = self.env['minsa.periodo'].search(domain_periodo, limit=1)
            list_key_tuples = []
            for banco in banco_objs:
                if banco.fecha.year >= fecha_hoy.year:
                    if banco.fecha.month <= fecha_hoy.month:
                        list_key_tuples.append((banco, periodo_id))
                else:
                    list_key_tuples.append((banco, periodo_id))

            domain = [
                ('periodo_id', '=', periodo_id.id),
                ('banco_id', 'in', banco_objs.ids),
            ]

            key_tuples = []
            for obj in self.env['hemored.ficha_estadistica'].search(domain):
                key_tuples.append((obj.banco_id, obj.periodo_id))

            list_vals = []
            for vals in list(set(list_key_tuples) - set(key_tuples)):
                banco, periodo = vals

                vals = {
                    'periodo_id': periodo.id,
                    'banco_id': banco.id,
                    'tipo_banco': banco.tipo_banco,
                    'institucion': banco.institucion,
                    'diresa_id': banco.renipress_id.diresa_id.id,
                    'anho_id': self.anho_id.id,
                }
                list_vals.append(vals)

            for vals in list_vals:
                ficha = self.env['hemored.ficha_estadistica'].create(vals)
                ficha.fechas_registro()
        else:
            periodo_id = self.env['minsa.periodo'].search(domain_periodo, limit=1)
            date_start = fields.Date.from_string(periodo_id.date_start)
            fecha_inicio = date_start + relativedelta(months=1)
            fecha_fin = fecha_inicio + relativedelta(days=14)
            list_key_tuples = []
            for banco in banco_objs:
                list_key_tuples.append((banco, consolidado, self.anho_id))

            domain = [
                ('anho_id', '=', self.anho_id.id),
                ('consolidado', '=', consolidado),
                ('banco_id', 'in', banco_objs.ids),
            ]

            key_tuples = []
            for obj in self.env['hemored.ficha_estadistica'].search(domain):
                key_tuples.append((obj.banco_id, obj.consolidado, obj.anho_id))

            list_vals = []
            for vals in list(set(list_key_tuples) - set(key_tuples)):
                banco, consolidado, self.anho_id = vals

                vals = {
                    'consolidado': True,
                    'banco_id': banco.id,
                    'tipo_banco': banco.tipo_banco,
                    'institucion': banco.institucion,
                    'diresa_id': banco.renipress_id.diresa_id.id,
                    'anho_id': self.anho_id.id,
                    'inicio_fecha_registro': fecha_inicio,
                    'fin_fecha_registro': fecha_fin,
                }
                list_vals.append(vals)

            for vals in list_vals:
                self.env['hemored.ficha_estadistica'].create(vals)
