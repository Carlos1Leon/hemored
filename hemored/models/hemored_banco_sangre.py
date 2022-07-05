# -*- coding: utf-8 -*-
import re

from lxml import etree

from odoo import fields, models, api
from odoo.exceptions import ValidationError

from ..models import constants

MN_BancoSangre = '.'.join([constants.MODULO, 'banco_sangre'])


class BancoSangre(models.Model):
    _inherits = {'renipress.eess': 'renipress_id'}
    _inherit = 'mail.thread'
    _name = MN_BancoSangre
    _description = 'Centro de Hemoterapia y Banco de Sangre'

    renipress_id = fields.Many2one(
        'renipress.eess',
        'Establecimiento de Salud',
        ondelete='cascade',
    )
    usuario_id = fields.Many2one(
        comodel_name='res.users',
        string='Usuario',
    )
    tipo_banco = fields.Selection(
        '_selection_tipo_banco',
        'Tipo de CHBS',
        required=True,
        track_visibility='onchange'
    )
    medico_coordinador_responsable = fields.Char(
        'Responsable del CHBS',
        required=True,
        size=250,
        track_visibility='onchange'
    )
    telefono = fields.Char(
        'Teléfono',
        required=True,
        size=9,
        track_visibility='onchange'
    )
    anexo = fields.Char(
        'Anexo',
        size=4,
        track_visibility='onchange'
    )
    celular = fields.Char(
        'Celular del responsable de CHBS',
        size=9,
        track_visibility='onchange'
    )
    email = fields.Char(
        'Email del responsable de CHBS o del CHBS',
        required=True,
        size=50,
        track_visibility='onchange'
    )
    num_camas = fields.Integer(
        'Número de Camas del CHBS',
        required=True,
        track_visibility='onchange',
        default='0'
    )
    fecha = fields.Date(
        string='Fecha inicio en HEMORED',
        track_visibility='onchange',
        default=fields.Date.today
    )
    estado = fields.Selection(
        constants.SELECTION_ESTADO_BANCO,
        string='Estado',
        default=constants.PRE_INSCRIPCION,
        track_visibility='onchange',
    )
    fecha_revision = fields.Date(
        string='Fecha de envío a revisión',
        track_visibility='onchange'
    )
    fecha_observacion = fields.Date(
        string='Fecha de notificación de observaciones encontradas',
        track_visibility='onchange'
    )
    fecha_registro = fields.Date(
        string='Fecha de inscripción en el Registro Nacional de CHBS',
        track_visibility='onchange'
    )
    motivo_suspension = fields.Char(
        'Motivo de suspensión',
        track_visibility='onchange'
    )
    fecha_suspension = fields.Date(
        string='Fecha de suspensión',
        track_visibility='onchange'
    )
    motivo_anulacion = fields.Char(
        'Motivo de anulación',
        track_visibility='onchange'
    )
    fecha_anulacion = fields.Date(
        string='Fecha de anulación',
        track_visibility='onchange'
    )
    posicion_organigrama = fields.Selection(
        constants.SELECTION_ESTRUCTURA,
        'De acuerdo a la estructura organizacional de su establecimiento de salud, el CHBS esta considerado como: ',
        track_visibility='onchange'
    )
    aferesis_terapeutica = fields.Selection(
        constants.SELECTION_RESPUESTA,
        '¿Realiza aféresis terapéutica?',
        track_visibility='onchange'
    )
    recambio_plasmatico = fields.Selection(
        constants.SELECTION_RESPUESTA,
        '¿Realiza recambio plasmático?',
        track_visibility='onchange'
    )
    colecta_celulas = fields.Selection(
        constants.SELECTION_RESPUESTA,
        '¿Realiza colecta de células progenitoras hematopoyéticas?',
        track_visibility='onchange'
    )
    leucoaferesis_terapeutica = fields.Selection(
        constants.SELECTION_RESPUESTA,
        '¿Realiza leucoaféresis terapéutica?',
        track_visibility='onchange'
    )
    eritroaferesis_terapeutica = fields.Selection(
        constants.SELECTION_RESPUESTA,
        '¿Realiza eritroaféresis terapéutica?',
        track_visibility='onchange'
    )
    plaquetoaferesis_terapeutica = fields.Selection(
        constants.SELECTION_RESPUESTA,
        '¿Realiza plaquetoaféresis terapéutica?',
        track_visibility='onchange'
    )
    personal_exclusivo = fields.Selection(
        constants.SELECTION_RESPUESTA,
        '¿El personal es exclusivo del CHBS?',
        track_visibility='onchange'
    )
    horario_donantes = fields.Char(
        'Horario de atención de donantes de sangre/aféresis',
        track_visibility='onchange'
    )
    prueba_biomolecular_inmunoserologia = fields.Selection(
        constants.SELECTION_RESPUESTA,
        '¿Realiza pruebas de biología molecular en Inmunoserología?',
        track_visibility='onchange'
    )
    prueba_biomolecular_inmunohematologia = fields.Selection(
        constants.SELECTION_RESPUESTA,
        '¿Realiza pruebas de biología molecular en Inmunohematología?',
        track_visibility='onchange'
    )
    personal_tiempo_completo = fields.Selection(
        constants.SELECTION_RESPUESTA,
        '¿Cuenta con personal profesional para la atención del CHBS las 24 horas del día?',
        track_visibility='onchange'
    )
    registro_web = fields.Boolean(
        string='Registro desde la web'
    )
    responsable_id = fields.Many2one(
        comodel_name='res.users',
        string='Evaluador',
    )
    archivo = fields.Binary(
        string='Constancia de inscripción',
        attachment=True
    )
    archivo_nombre = fields.Char(
        string='Nombre Constancia de inscripción'
    )
    archivo_suspension = fields.Binary(
        string='Constancia de suspensión',
        attachment=True
    )
    archivo_suspension_nombre = fields.Char(
        string='Nombre Constancia de suspensión'
    )
    archivo_anulacion = fields.Binary(
        string='Constancia de anulación',
        attachment=True
    )
    archivo_anulacion_nombre = fields.Char(
        string='Nombre Constancia de anulación'
    )
    horario_atencion = fields.Char(
        string='Horario de atención del EESS'
    )
    num_registro = fields.Char(
        string='Nº de inscripción',
        track_visibility='onchange'
    )
    region_prov_dist = fields.Char(
        string='Región/Provincia/Distrito',
        compute='_compute_region_prov_dist',
        store=True
    )
    director_eess = fields.Char(
        string='Director del establecimiento de salud'
    )
    observacion = fields.Text(
        string='Observaciones'
    )

    # PARTICIPACIÓN EN PROGRAMA DE EVALUACIÓN EXTERNA DE LA CALIDAD DE TAMIZAJE

    select_mvih_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    select_mhbsag_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    select_mhepc_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    select_mantihbc_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    select_mhtlv_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    select_msifilis_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    select_mchagas_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )
    select_motros_s_o_n = fields.Selection(
        selection=constants.SELECTION_RESPUESTA,
        default=constants.NO,
        track_visibility='onchange'
    )

    @api.one
    @api.depends('renipress_id')
    def _compute_region_prov_dist(self):
        if self.renipress_id:
            self.region_prov_dist = self.renipress_id.departamento_id.name + "/" + self.renipress_id.provincia_id.name + "/" + self.renipress_id.distrito_id.name

    def action_update_data(self):
        domain_banco = [('tipo_banco', '=', '2')]
        bancos_ids = self.env['hemored.banco_sangre'].search(domain_banco)
        for record in bancos_ids:
            domain = [('banco_id', '=', record.id), ('state', '!=', constants.BORRADOR)]
            fichas_ids = self.env['hemored.ficha_estadistica'].search(domain)
            if fichas_ids:
                ultimo = fichas_ids.ids.pop()
                ficha_id = self.env['hemored.ficha_estadistica'].browse(ultimo)
                if ficha_id:
                    record.update({
                        'select_mvih_s_o_n': ficha_id.cantidad_mvih_s_o_n,
                        'select_mhbsag_s_o_n': ficha_id.cantidad_mhbsag_s_o_n,
                        'select_mhepc_s_o_n': ficha_id.cantidad_mhepc_s_o_n,
                        'select_mantihbc_s_o_n': ficha_id.cantidad_mantihbc_s_o_n,
                        'select_mhtlv_s_o_n': ficha_id.cantidad_mhtlv_s_o_n,
                        'select_msifilis_s_o_n': ficha_id.cantidad_msifilis_s_o_n,
                        'select_mchagas_s_o_n': ficha_id.cantidad_mchagas_s_o_n,
                        'select_motros_s_o_n': ficha_id.cantidad_motros_s_o_n,
                    })

    @api.model
    def _cron_update_data_chbs_programa_evaluacion(self):
        self.action_update_data()

    _sql_constraints = [
        ('codigo_name', 'unique(renipress_id)',
         'El nombre del Banco debe ser único!'),
    ]

    def _es_eess(self):
        return self.env.user.has_group('hemored.group_coordinador_establecimiento_hemored')

    @api.multi
    def action_verificar(self):
        self.ensure_one()
        documento_requisito = {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
        }
        form = self.env.ref('hemored.hemored_chek_requisito_form_view', False)
        if self.requisito_id:
            documento_requisito.update({
                'name': 'Requisitos',
                'res_model': 'hemored.chek_requisito',
                'views': [(form.id, 'form')],
                'view_id': form.id,
                'res_id': self.requisito_id.id,
            })
        else:
            if self._es_eess():
                raise ValidationError('Aun no tiene asociado los requisitos')
            else:
                documento_requisito.update({
                    'name': 'Requisitos',
                    'res_model': 'hemored.chek_requisito',
                    'views': [(form.id, 'form')],
                    'view_id': form.id,
                    'context': {'default_banco_id': self.id}
                })
        return documento_requisito

    @api.one
    def action_revision(self):
        if self.estado in (constants.PRE_INSCRIPCION, constants.OBSERVADO):
            self.estado = constants.REVISION
            self.fecha_revision = fields.Date.today()

    @api.one
    def action_observar(self):
        if self.estado == constants.REVISION:
            self.estado = constants.OBSERVADO
            self.fecha_observacion = fields.Date.today()

    @api.one
    def action_aprobar(self):
        if self.estado == constants.REVISION:
            self.estado = constants.REGISTRADO
            self.fecha_registro = fields.Date.today()
            vals = {
                'diresa_id': self.diresa_id.id,
                'banco_id': self.id,
                'registrado': True,
            }
            self.sudo().usuario_id.write(vals)

    @api.one
    def action_suspender(self):
        self.write({
            'estado': constants.SUSPENDIDO,
            'fecha_suspension': fields.Date.today(),
        })

    @api.one
    def action_anular(self):
        self.write({
            'estado': constants.ANULADO,
            'fecha_anulacion': fields.Date.today(),
        })

    @api.one
    @api.constrains('telefono')
    def _check_telefono(self):
        if self.telefono and (len(self.telefono) < 6 or not self.telefono.isdigit()):
            raise ValidationError('Teléfono no válido')

    @api.one
    @api.constrains('anexo')
    def _check_anexo(self):
        if self.anexo and (len(self.anexo) < 3 or not self.anexo.isdigit()):
            raise ValidationError('Anexo no válido')

    @api.one
    @api.constrains('celular')
    def _check_celular(self):
        if self.celular:
            if (len(self.celular) < 9 or not self.celular.isdigit()):
                raise ValidationError('El número de celular no debe tener letras y no debe ser menor a 9 digitos')
            if (len(self.celular) > 9 or not self.celular.isdigit()):
                raise ValidationError('El número de celular no debe tener letras y no debe ser mayor a 9 digitos')

    @api.one
    @api.constrains('email')
    def _check_email(self):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', self.email):
            raise ValidationError('E-mail no válido')

        domain = [
            ('id', '!=', self.id),
            ('email', '=', self.email),
        ]
        if self.search(domain, limit=1):
            raise ValidationError('Ya existe email registrado')

    @api.model
    def _selection_tipo_banco(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_banco')

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(BancoSangre, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        es_coordinador_establecimiento = self.env.user.has_group('hemored.group_coordinador_establecimiento_hemored')
        es_pre_inscrito = self.env.user.has_group('hemored.group_pre_inscripcion_hemored')
        if view_type == 'form':
            doc_input_diresa = etree.XML(res['arch'])
            my_attrs1 = '{"readonly": true}'
            if es_coordinador_establecimiento or es_pre_inscrito:
                for node in doc_input_diresa.xpath("//field[@name='renipress_id']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='tipo_banco']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='fecha']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='num_registro']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='fecha_registro']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='responsable_id']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='archivo']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='archivo_suspension']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='motivo_suspension']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='archivo_anulacion']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='motivo_anulacion']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='observacion']"):
                    node.set('modifiers', my_attrs1)
                for node in doc_input_diresa.xpath("//field[@name='archivo']"):
                    node.set('modifiers', my_attrs1)
            res['arch'] = etree.tostring(doc_input_diresa)
        return res

    @api.model
    def create(self, vals):
        if not vals.get('registro_web'):
            vals['estado'] = constants.REGISTRADO
        res = super(BancoSangre, self).create(vals)
        res.accion_crear_usuarios()
        return res

    @api.multi
    def write(self, vals):
        res = super(BancoSangre, self).write(vals)
        if 'email' in vals:
            for obj in self:
                obj.action_change_email()
        return res

    @api.model
    def _update_user(self):
        for obj in self.env['hemored.banco_sangre'].search([]):
            obj.accion_crear_usuarios()
        return True

    @api.one
    def action_change_email(self):
        vals = {
            'email': self.email,
        }
        self.usuario_id.sudo().write(vals)

    @api.one
    def accion_crear_usuarios(self):
        domain = [
            ('usuario_id', '=', False),
        ]
        if self.search(domain, limit=1):
            vals = {
                'name': self.name,
                'login': self.codigo_eess,
                'email': self.email,
                'password': 'Minsa_{}'.format(self.codigo_eess),
                'diresa_id': self.diresa_id.id,
                'banco_id': self.id,
                'registro_web': self.registro_web,
                'registrado': False,
            }
            usuario_id = self.env['res.users'].sudo().create(vals)
            self.write({'usuario_id': usuario_id.id})

    def get_name_item_catalogo(self, key):
        domain = [('code', '=', key)]
        return self.env['basecatalogo.catalogo'].search(domain, limit=1).name

    def get_name_catalogo_proceso(self, key):
        return self.get_name_item_catalogo('_selection_pregunta_proceso_{}'.format(key))

    def get_name_catalogo_proceso_pregunta(self, key):
        return self.get_name_item_catalogo('_selection_observacion_proceso_{}'.format(key))

    def get_texto_equipamiento(self, key):
        return self.get_name_item_catalogo('_selection_equipamiento{}'.format(key))

    def get_texto_infraestructura(self, key):
        return self.get_name_item_catalogo('_selection_infraestructura{}'.format(key))

    def get_texto_rrhh(self, key):
        return self.get_name_item_catalogo('_selection_rrhh{}'.format(key))

    def get_texto_registro(self, key):
        return self.get_name_item_catalogo('_selection_text_registro{}'.format(key))

    def get_observacion_registro(self, key):
        return self.get_name_item_catalogo('_selection_observacion_registro{}'.format(key))

    def get_responsabilidad_pregunta(self, key):
        return self.get_name_item_catalogo('_selection_pregunta_responsabilidad_{}'.format(key))

    def get_responsabilidad_observacion(self, key):
        return self.get_name_item_catalogo('_selection_observacion_responsabilidad_{}'.format(key))

    def get_informatico_pregunta(self, key):
        return self.get_name_item_catalogo('_selection_pregunta_informatico_{}'.format(key))

    def get_seguirdad_pregunta(self, key):
        return self.get_name_item_catalogo('_selection_pregunta_seguridad_{}'.format(key))

    def get_seguirdad_observacion(self, key):
        return self.get_name_item_catalogo('_selection_observacion_seguridad_{}'.format(key))

    def get_plaquetas(self):
        return self.get_name_item_catalogo('_selection_plaquetas')

    def get_globular(self):
        return self.get_name_item_catalogo('_selection_globular')

    def get_plasma(self):
        return self.get_name_item_catalogo('_selection_plasma')

    def get_crioprecipitado(self):
        return self.get_name_item_catalogo('_selection_crioprecipitado')

    def get_reactivo(self):
        return self.get_name_item_catalogo('_selection_reactivo')

    def get_tubo(self):
        return self.get_name_item_catalogo('_selection_tubo')

    def get_gel(self):
        return self.get_name_item_catalogo('_selection_gel')

    def get_otros(self):
        return self.get_name_item_catalogo('_selection_otros')

    def get_valor_pregunta_rrhh36(self):
        return self.get_name_item_catalogo('_selection_pregunta_rrhh36')

    def get_valor_observacion_rrhh36(self):
        return self.get_name_item_catalogo('_selection_observacion_rrhh36')

    def get_valor_observacion_rrhh39(self):
        return self.get_name_item_catalogo('_selection_observacion_rrhh39')

    def get_observacion_rrh11(self):
        return self.get_name_item_catalogo('_selection_observacion_rrhh11')

    def get_valor_observacion_proceso37(self):
        return self.get_name_item_catalogo('_selection_observacion_proceso_37')

    def get_informatico_observacion1(self):
        return self.get_name_item_catalogo('_selection_observacion_informatico_1')

    def get_informatico_observacion5(self):
        return self.get_name_item_catalogo('_selection_observacion_informatico_5')

    def get_observacion_responsabilidad_9(self):
        return self.get_name_item_catalogo('_selection_observacion_responsabilidad_9')

    def get_texto_registro13(self):
        return self.get_name_item_catalogo('_selection_text_registro7')

    def get_texto_registro14(self):
        return self.get_name_item_catalogo('_selection_text_registro8')

    def get_texto_registro15(self):
        return self.get_name_item_catalogo('_selection_text_registro9')

    def get_texto_registro16(self):
        return self.get_name_item_catalogo('_selection_text_registro10')

    def get_texto_otro_infraestructura1(self):
        return self.get_name_item_catalogo('_selection_otros')

    def get_valor_infraestructura29(self):
        return self.get_name_item_catalogo('_selection_infraestructura29')

    def get_valor_pregunta_registro5(self):
        return self.get_name_item_catalogo('_selection_pregunta_seguridad_4')

    def get_valor_observacion_registro5(self):
        return self.get_name_item_catalogo('_selection_observacion_seguridad_4')

    def infraestructura_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_infraestructura{}_chbs2'.format(key))

    def pregunta_biologica_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_pregunta_biologica{}_chbs2'.format(key))

    def observacion_biologica_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_observacion_biologica{}_chbs2'.format(key))

    def pregunta_calidad_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_pregunta_calidad{}_chbs2'.format(key))

    def observacion_calidad_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_observacion_calidad{}_chbs2'.format(key))

    def pregunta_almacenamiento_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_pregunta_almacenamiento{}_chbs2'.format(key))

    def observacion_almacenamiento_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_observacion_almacenamiento{}_chbs2'.format(key))

    def pregunta_equipamiento_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_pregunta_equipamiento{}_chbs2'.format(key))

    def texto_equipamiento_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_texto_equipamiento{}_chbs2'.format(key))

    def texto_proceso_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_texto_proceso{}_chbs2'.format(key))

    def observacion_proceso_chbs2(self, key):
        return self.get_name_item_catalogo('_selection_observacion_proceso{}_chbs2'.format(key))

    def get_valor_observacion_proceso_37_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_proceso_17')

    def get_valor_pregunta_proceso31_chbs2(self):
        return self.get_name_item_catalogo('_selection_pregunta_proceso_31')

    def get_seguridad_pregunta1_chbs2(self):
        return self.get_name_item_catalogo('_selection_pregunta_seguridad_1_chbs2')

    def get_seguridad_observacion1_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_seguridad_1_chbs2')

    def get_responsabilidad_pregunta5(self):
        return self.get_name_item_catalogo('_selection_pregunta_responsabilidad_1_chbs2')

    def get_responsabilidad_pregunta2_chbs2(self):
        return self.get_name_item_catalogo('_selection_pregunta_responsabilidad_2_chbs2')

    def get_texto_registro4_chbs2(self):
        return self.get_name_item_catalogo('_selection_text_registro1_chbs2')

    def get_observacion_registro4(self):
        return self.get_name_item_catalogo('_selection_observacion_registro1_chbs2')

    def get_texto_observacion_infraestructura10_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_infraestructura10_chbs2')

    def get_pregunta_proceso_43(self):
        return self.get_name_item_catalogo('_selection_pregunta_proceso_43')

    def get_texto_biologico1_chbs2(self):
        return self.get_name_item_catalogo('_selection_pregunta_biologica1_chbs2')

    def get_texto_observacion_biologico2_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_proceso_32')

    def get_texto_observacion_biologico10_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_biologica10_chbs2')

    def get_texto_observacion_calidad1_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_calidad1_chbs2')

    def get_texto_almacenamiento1_chbs2(self):
        return self.get_name_item_catalogo('_selection_pregunta_almacenamiento1_chbs2')

    def get_texto_observacion_almacenamiento1_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_almacenamiento1_chbs2')

    def get_texto_almacenamiento2_chbs2(self):
        return self.get_name_item_catalogo('_selection_pregunta_proceso_25')

    def get_texto_observacion_almacenamiento2_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_proceso_25')

    def get_texto_almacenamiento3_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_calidad3_chbs2')

    def get_proceso_observacion27_chbs2(self):
        return self.get_name_item_catalogo('_selection__selection_observacion_proceso26_chbs2')

    def get_proceso_observacion58_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_proceso58_chbs2')

    def get_proceso_observacion81_chbs2(self):
        return self.get_name_item_catalogo('_selection_observacion_proceso81_chbs2')

    def action_supervision(self):
        self.ensure_one()
        values = {}
        for i in range(1, 43 + 1):
            values.update({
                'default_proceso_pregunta{}'.format(i): self.get_name_catalogo_proceso(i),
                'default_proceso_observacion{}'.format(i): self.get_name_catalogo_proceso_pregunta(i),
            })
        for i in range(1, 17 + 1):
            values.update({
                'default_texto_equipamiento{}'.format(i): self.get_texto_equipamiento(i),
            })
        for i in range(1, 37 + 1):
            values.update({
                'default_texto_infraestructura{}'.format(i): self.get_texto_infraestructura(i),
            })
        for i in range(1, 12 + 1):
            values.update({
                'default_texto_rrhh{}'.format(i): self.get_texto_rrhh(i),
            })
        for i in range(1, 12 + 1):
            values.update({
                'default_texto_registro{}'.format(i): self.get_texto_registro(i),
            })
        for i in range(1, 6 + 1):
            values.update({
                'default_observacion_registro{}'.format(i): self.get_observacion_registro(i),
            })
        for i in range(1, 22 + 1):
            values.update({
                'default_responsabilidad_pregunta{}'.format(i): self.get_responsabilidad_pregunta(i),
                'default_responsabilidad_observacion{}'.format(i): self.get_responsabilidad_observacion(i),
            })
        for i in range(1, 5 + 1):
            values.update({
                'default_informatico_pregunta{}'.format(i): self.get_informatico_pregunta(i),
            })
        for i in range(1, 5 + 1):
            values.update({
                'default_seguirdad_pregunta{}'.format(i): self.get_seguirdad_pregunta(i),
                'default_seguirdad_observacion{}'.format(i): self.get_seguirdad_observacion(i),
            })
        for i in range(1, 10 + 1):
            values.update({
                'default_texto_infraestructura{}_chbs2'.format(i): self.infraestructura_chbs2(i)
            })
        for i in range(4, 8 + 1):
            values.update({
                'default_texto_biologico{}_chbs2'.format(i): self.pregunta_biologica_chbs2(i)
            })
        for i in range(3, 8 + 1):
            values.update({
                'default_texto_observacion_biologico{}_chbs2'.format(i): self.observacion_biologica_chbs2(i)
            })
        for i in range(1, 5 + 1):
            values.update({
                'default_texto_calidad{}_chbs2'.format(i): self.pregunta_calidad_chbs2(i)
            })
        for i in range(3, 5 + 1):
            values.update({
                'default_texto_observacion_calidad{}_chbs2'.format(i): self.observacion_calidad_chbs2(i)
            })
        for i in range(4, 8 + 1):
            values.update({
                'default_texto_almacenamiento{}_chbs2'.format(i): self.pregunta_almacenamiento_chbs2(i)
            })
        for i in range(3, 4 + 1):
            values.update({
                'default_texto_observacion_almacenamiento{}_chbs2'.format(i): self.observacion_almacenamiento_chbs2(i)
            })
        for i in range(1, 3 + 1):
            values.update({
                'default_texto_equipamiento{}_chbs2'.format(i): self.pregunta_equipamiento_chbs2(i)
            })
        for i in range(1, 2 + 1):
            values.update({
                'default_texto_equipamiento_{}_chbs2'.format(i): self.texto_equipamiento_chbs2(i)
            })
        for i in range(4, 14 + 1):
            values.update({
                'default_texto_equipamiento_{}_chbs2'.format(i): self.texto_equipamiento_chbs2(i)
            })
        for i in range(1, 101 + 1):
            values.update({
                'default_proceso_pregunta{}_chbs2'.format(i): self.texto_proceso_chbs2(i)
            })
        for i in range(1, 5 + 1):
            values.update({
                'default_proceso_observacion{}_chbs2'.format(i): self.observacion_proceso_chbs2(i)
            })
        for i in range(11, 19 + 1):
            values.update({
                'default_proceso_observacion{}_chbs2'.format(i): self.observacion_proceso_chbs2(i)
            })
        for i in range(25, 26 + 1):
            values.update({
                'default_proceso_observacion{}_chbs2'.format(i): self.observacion_proceso_chbs2(i)
            })
        for i in range(28, 33 + 1):
            values.update({
                'default_proceso_observacion{}_chbs2'.format(i): self.observacion_proceso_chbs2(i)
            })
        for i in range(36, 37 + 1):
            values.update({
                'default_proceso_observacion{}_chbs2'.format(i): self.observacion_proceso_chbs2(i)
            })
        for i in range(39, 50 + 1):
            values.update({
                'default_proceso_observacion{}_chbs2'.format(i): self.observacion_proceso_chbs2(i)
            })
        for i in range(60, 67 + 1):
            values.update({
                'default_proceso_observacion{}_chbs2'.format(i): self.observacion_proceso_chbs2(i)
            })
        for i in range(70, 71 + 1):
            values.update({
                'default_proceso_observacion{}_chbs2'.format(i): self.observacion_proceso_chbs2(i)
            })
        for i in range(86, 90 + 1):
            values.update({
                'default_proceso_observacion{}_chbs2'.format(i): self.observacion_proceso_chbs2(i)
            })
        for i in range(94, 101 + 1):
            values.update({
                'default_proceso_observacion{}_chbs2'.format(i): self.observacion_proceso_chbs2(i)
            })
        values.update({
            'default_banco_id': self.id,
            'default_institucion': self.institucion,
            'default_tipo_guia': constants.GUIAI,
            'default_jefe_responsable': self.medico_coordinador_responsable,
            'default_email_responsable': self.email,
            'default_telefono_jefe': self.telefono,
            'default_plaquetas': self.get_plaquetas(),
            'default_globular': self.get_globular(),
            'default_plasma': self.get_plasma(),
            'default_crioprecipitado': self.get_crioprecipitado(),
            'default_reactivo': self.get_reactivo(),
            'default_tubo': self.get_tubo(),
            'default_gel': self.get_gel(),
            'default_otros': self.get_otros(),
            'default_texto_otro_infraestructura1': self.get_texto_otro_infraestructura1(),
            'default_infraestructura_observacion23': self.get_valor_infraestructura29(),
            'default_infraestructura_observacion24': self.get_valor_infraestructura29(),
            'default_text_respuesta_rrh2': self.get_valor_pregunta_rrhh36(),
            'default_observacion_rrh2': self.get_valor_observacion_rrhh36(),
            'default_text_respuesta_rrh3': self.get_valor_pregunta_rrhh36(),
            'default_observacion_rrh3': self.get_valor_observacion_rrhh36(),
            'default_text_respuesta_rrh4': self.get_valor_pregunta_rrhh36(),
            'default_observacion_rrh4': self.get_valor_observacion_rrhh36(),
            'default_text_respuesta_rrh5': self.get_valor_pregunta_rrhh36(),
            'default_observacion_rrh5': self.get_valor_observacion_rrhh39(),
            'default_text_respuesta_rrh6': self.get_valor_pregunta_rrhh36(),
            'default_observacion_rrh6': self.get_valor_observacion_rrhh39(),
            'default_text_respuesta_rrh7': self.get_valor_pregunta_rrhh36(),
            'default_observacion_rrh7': self.get_valor_observacion_rrhh39(),
            'default_text_respuesta_rrh8': self.get_valor_pregunta_rrhh36(),
            'default_observacion_rrh8': self.get_valor_observacion_rrhh39(),
            'default_text_respuesta_rrh9': self.get_valor_pregunta_rrhh36(),
            'default_observacion_rrh9': self.get_valor_observacion_rrhh39(),
            'default_text_respuesta_rrh10': self.get_valor_pregunta_rrhh36(),
            'default_observacion_rrh10': self.get_valor_observacion_rrhh39(),
            'default_observacion_rrh11': self.get_observacion_rrh11(),
            'default_observacion_rrh12': self.get_valor_observacion_proceso37(),
            'default_texto_registro13': self.get_texto_registro13(),
            'default_texto_registro14': self.get_texto_registro14(),
            'default_texto_registro15': self.get_texto_registro15(),
            'default_texto_registro16': self.get_texto_registro16(),
            'default_responsabilidad_observacion6': self.get_valor_observacion_proceso37(),
            'default_observacion_responsabilidad_9': self.get_observacion_responsabilidad_9(),
            'default_responsabilidad_observacion12': self.get_valor_observacion_proceso37(),
            'default_informatico_observacion1': self.get_informatico_observacion1(),
            'default_informatico_observacion5': self.get_informatico_observacion5(),
            'default_texto_registro5': self.get_valor_pregunta_registro5(),
            'default_observacion_registro5': self.get_valor_observacion_registro5(),
            'default_texto_observacion_biologico1_chbs2': self.get_valor_observacion_proceso_37_chbs2(),
            'default_texto_observacion_biologico9_chbs2': self.get_valor_observacion_proceso_37_chbs2(),
            'default_texto_biologico2_chbs2': self.get_valor_pregunta_proceso31_chbs2(),
            'default_texto_biologico3_chbs2': self.get_valor_pregunta_proceso31_chbs2(),
            'default_texto_biologico9_chbs2': self.get_valor_pregunta_proceso31_chbs2(),
            'default_seguridad_pregunta1_chbs2': self.get_seguridad_pregunta1_chbs2(),
            'default_seguridad_observacion1_chbs2': self.get_seguridad_observacion1_chbs2(),
            'default_responsabilidad_pregunta5': self.get_responsabilidad_pregunta5(),
            'default_responsabilidad_pregunta2_chbs2': self.get_responsabilidad_pregunta2_chbs2(),
            'default_texto_registro4_chbs2': self.get_texto_registro4_chbs2(),
            'default_observacion_registro4': self.get_observacion_registro4(),
            'default_texto_observacion_infraestructura10_chbs2': self.get_texto_observacion_infraestructura10_chbs2(),
            'default_texto_infraestructura11_chbs2': self.get_pregunta_proceso_43(),
            'default_texto_observacion_infraestructura11_chbs2': self.get_pregunta_proceso_43(),
            'default_texto_biologico1_chbs2': self.get_texto_biologico1_chbs2(),
            'default_texto_observacion_biologico2_chbs2': self.get_texto_observacion_biologico2_chbs2(),
            'default_texto_observacion_biologico10_chbs2': self.get_texto_observacion_biologico10_chbs2(),
            'default_texto_observacion_calidad1_chbs2': self.get_texto_observacion_calidad1_chbs2(),
            'default_texto_almacenamiento1_chbs2': self.get_texto_almacenamiento1_chbs2(),
            'default_texto_observacion_almacenamiento1_chbs2': self.get_texto_observacion_almacenamiento1_chbs2(),
            'default_texto_almacenamiento2_chbs2': self.get_texto_almacenamiento2_chbs2(),
            'default_texto_observacion_almacenamiento2_chbs2': self.get_texto_observacion_almacenamiento2_chbs2(),
            'default_texto_almacenamiento3_chbs2': self.get_texto_almacenamiento3_chbs2(),
            'default_proceso_observacion27_chbs2': self.get_proceso_observacion27_chbs2(),
            'default_proceso_observacion58_chbs2': self.get_proceso_observacion58_chbs2(),
            'default_proceso_observacion81_chbs2': self.get_proceso_observacion81_chbs2(),
        })
        if self.tipo_banco == '1':
            action = self.env.ref('hemored.hemored_supervision_action').read()[0]
            action['domain'] = [('banco_id', '=', self.id), ('tipo_guia', '=', constants.GUIAI)]
            action['context'] = values
            return action
        elif self.tipo_banco == '2':
            values.update({
                'default_tipo_guia': constants.GUIAII,
            })
            action = self.env.ref('hemored.hemored_supervision2_action').read()[0]
            action['domain'] = [('banco_id', '=', self.id), ('tipo_guia', '=', constants.GUIAII)]
            action['context'] = values
            return action

    def get_seguridad_pregunta(self, key):
        return self.get_name_item_catalogo('sd_seg_{}'.format(key))

    def get_oportunidad_pregunta(self, key):
        return self.get_name_item_catalogo('sd_op_{}'.format(key))

    def get_otros_pregunta(self):
        return self.get_name_item_catalogo('sd_o_1')

    def action_supervision_dif(self):
        self.ensure_one()
        values = {}
        for i in range(1, 27 + 1):
            values.update({
                'default_seguridad_pregunta_{}'.format(i): self.get_seguridad_pregunta(i)
            })
        for i in range(1, 3 + 1):
            values.update({
                'default_oportunidad_pregunta_{}'.format(i): self.get_oportunidad_pregunta(i)
            })
        values.update({
            'default_banco_id': self.id,
            'default_institucion': self.institucion,
            'default_diresa_id': self.diresa_id.id,
            'default_tipo_guia': constants.GUIAI,
            'default_otros_pregunta_1': self.get_otros_pregunta()
        })
        if self.tipo_banco == '1':
            action = self.env.ref('hemored.hemored_supervision_dif_action').read()[0]
            action['domain'] = [('banco_id', '=', self.id), ('tipo_guia', '=', constants.GUIAI)]
            action['context'] = values
            return action
        elif self.tipo_banco == '2':
            values.update({
                'default_tipo_guia': constants.GUIAII,
            })
            action = self.env.ref('hemored.hemored_supervision_dif_action').read()[0]
            action['domain'] = [('banco_id', '=', self.id), ('tipo_guia', '=', constants.GUIAII)]
            action['context'] = values
            return action
