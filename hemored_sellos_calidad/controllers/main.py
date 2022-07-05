# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import content_disposition


class ReportBinary(http.Controller):

    @http.route('/web/binary/download_export_stock_sellos', type='http', auth='user')
    def download_exported_stock_sellos(self, id, filename=None, **kw):
        obj = request.env['stock_sellos.report_excel'].browse(map(lambda x: int(x), id.split(',')))
        filecontent = obj.generate_xlsx_report()
        return request.make_response(filecontent, [
            ('Content-Type', 'application/octet-stream;charset=utf-8;'),
            ('Content-Disposition', content_disposition(filename))
        ])
