
from odoo import api, models


class FichaEstadistica(models.Model):
    _inherit = 'hemored.ficha_estadistica'

    @api.multi
    def cargar_excel_ficha(self):
        self.ensure_one()
        form = self.env.ref('hemored_update.hemored_update_form_view', False)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Carga Automática de Datos',
            'res_model': 'hemored_update.updateexcel',
            'views': [(form.id, 'form')],
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': form.id,
            'target': 'new'
        }
