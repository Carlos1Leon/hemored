# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import content_disposition
from odoo.addons.website_form.controllers.main import WebsiteForm


class WebsiteForm(WebsiteForm):
    @http.route('/inscription_website', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('hemored.index', {})

    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True)
    def website_form(self, model_name, **kwargs):
        codigo = request.params.get('codigo_eess')
        if model_name == 'hemored.banco_sangre':
            banco = request.env['renipress.eess']
            request.params['renipress_id'] = banco.search([('codigo_eess', '=', codigo)], limit=1).id
            request.params['email'] = request.params.get('email')
        return super(WebsiteForm, self).website_form(model_name, **kwargs)

    def insert_record(self, request, model, values, custom, meta=None):
        values = request.params
        return super(WebsiteForm, self).insert_record(request, model, values, custom, meta=meta)


class ReportBinary(http.Controller):

    @http.route('/web/binary/download_export_ficha', type='http', auth='user')
    def download_exported_ficha(self, id, filename=None, **kw):
        obj = request.env['hemored.ficha_estadistica'].browse(map(lambda x: int(x), id.split(',')))
        filecontent = obj.action_export_excel()
        return request.make_response(filecontent, [
            ('Content-Type', 'application/octet-stream;charset=utf-8;'),
            ('Content-Disposition', content_disposition(filename))
        ])

    @http.route('/web/binary/download_export_ficha_consolidado', type='http', auth='user')
    def download_exported_ficha_consolidado(self, id, filename=None, **kw):
        obj = request.env['hemored.report_ficha'].browse(map(lambda x: int(x), id.split(',')))
        filecontent = obj.action_export_excel()
        return request.make_response(filecontent, [
            ('Content-Type', 'application/octet-stream;charset=utf-8;'),
            ('Content-Disposition', content_disposition(filename))
        ])

    @http.route('/web/binary/download_export_porcentaje_ficha', type='http', auth='user')
    def download_exported_estado_de_ficha(self, id, filename=None, **kw):
        obj = request.env['hemored.report_estado_ficha'].browse(map(lambda x: int(x), id.split(',')))
        filecontent = obj.action_export_excel()
        return request.make_response(filecontent, [
            ('Content-Type', 'application/octet-stream;charset=utf-8;'),
            ('Content-Disposition', content_disposition(filename))
        ])

    @http.route('/web/binary/download_export_porcentaje_programa_evaluacion', type='http', auth='user')
    def download_exported_programa_evaluacion_externa(self, id, filename=None, **kw):
        obj = request.env['hemored.report_programa_evaluacion'].browse(map(lambda x: int(x), id.split(',')))
        filecontent = obj.action_export_excel()
        return request.make_response(filecontent, [
            ('Content-Type', 'application/octet-stream;charset=utf-8;'),
            ('Content-Disposition', content_disposition(filename))
        ])

    @http.route('/web/binary/download_export_supervision', type='http', auth='user')
    def download_exported_supervision(self, id, filename=None, **kw):
        obj = request.env['hemored_supervision.record_supervision'].browse(map(lambda x: int(x), id.split(',')))
        filecontent = obj.descarga_excel_supervision()
        return request.make_response(filecontent, [
            ('Content-Type', 'application/octet-stream;charset=utf-8;'),
            ('Content-Disposition', content_disposition(filename))
        ])

    @http.route('/web/binary/download_export_hemovigilancia', type='http', auth='user')
    def download_exported_hemovigilancia(self, id, filename=None, **kw):
        obj = request.env['hemored_hemovigilancia.hemovigilancia'].browse(map(lambda x: int(x), id.split(',')))
        filecontent = obj.action_export_excel()
        return request.make_response(filecontent, [
            ('Content-Type', 'application/octet-stream;charset=utf-8;'),
            ('Content-Disposition', content_disposition(filename))
        ])
