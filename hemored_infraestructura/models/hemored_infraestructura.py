# -*- coding: utf-8 -*-
from lxml import etree

from odoo import fields, models, api

from ..models import constants


class Infraestructura(models.Model):
    _inherit = 'mail.thread'
    _name = 'hemored_infraestructura.infraestructura'
    _description = 'Infraestructura'
    _rec_name = 'banco_id'

    diresa_id = fields.Many2one(
        comodel_name='renipress.diresa',
        string='Diresa',
        default=lambda self: self.env.user.diresa_id,
        readonly=True
    )
    banco_id = fields.Many2one(
        comodel_name='hemored.banco_sangre',
        string='CHBS',
        default=lambda self: self.env.user.banco_id
    )
    tipo_banco = fields.Selection(
        '_selection_tipo_banco',
        'Tipo de CHBS',
        related='banco_id.tipo_banco',
        store=True
    )
    estado = fields.Selection(
        constants.SELECTION_ESTADO_INFRAESTRUCTURA,
        default=constants.BORRADOR,
        string='Estado'
    )
    area_total = fields.Float(
        string='Área total (m2) del CHBS',
        track_visibility='onchange',
        default=0
    )
    numero_pisos = fields.Integer(
        string='Número de pisos',
        track_visibility='onchange',
        default=1
    )
    ubicacion_piso = fields.Char(
        string='Referencia donde se ubica',
        track_visibility='onchange'
    )
    directo = fields.Boolean(
        string='Directo',
        track_visibility='onchange'
    )
    escalera = fields.Boolean(
        string='Escaleras',
        track_visibility='onchange'
    )
    rampa = fields.Boolean(
        string='Rampa',
        track_visibility='onchange'
    )
    ascensor = fields.Boolean(
        string='Ascensor',
        track_visibility='onchange'
    )

    a_1_total = fields.Float(
        string='Metros cuadrados del área funcional',
        track_visibility='onchange',
        default=0
    )
    a_1_recepcion_donantes = fields.Boolean(
        string='Recepción de donantes y sala de espera',
        track_visibility='onchange'
    )
    a_1_entrevista_medica = fields.Boolean(
        string='Consultorio / área para entrevista médica',
        track_visibility='onchange'
    )
    num_consultorios = fields.Integer(
        string='# de consultorios',
        track_visibility='onchange'
    )
    a_1_extraccion = fields.Boolean(
        string='Área de extracción de sangre y de reposo',
        track_visibility='onchange'
    )
    a_1_aferesis = fields.Boolean(
        string='Área de aféresis',
        track_visibility='onchange'
    )
    a_1_sshh = fields.Boolean(
        string='Servicios higiénicos para donantes',
        track_visibility='onchange'
    )
    a_2_total = fields.Float(
        string='Metros cuadrados del área funcional',
        track_visibility='onchange',
        default=0
    )
    a_2_toma_muestra = fields.Boolean(
        string='Área de análisis de muestras de donantes',
        track_visibility='onchange'
    )
    a_2_inmunohematologia = fields.Boolean(
        string='Área de inmunohematología',
        track_visibility='onchange'
    )
    a_2_inmunoserologia = fields.Boolean(
        string='Área de inmunoserología',
        track_visibility='onchange'
    )
    a_2_recepcion_muestra = fields.Boolean(
        string='Área de recepción de muestras y unidades de sangre',
        track_visibility='onchange'
    )
    a_3_total = fields.Float(
        string='Metros cuadrados del área funcional',
        track_visibility='onchange',
        default=0
    )
    a_3_recepcion_muestras = fields.Boolean(
        string='Área de recepción de muestras y unidades de sangre',
        track_visibility='onchange'
    )
    a_3_fraccionamiento = fields.Boolean(
        string='Área de fraccionamiento',
        track_visibility='onchange'
    )
    a_3_cuarentena = fields.Boolean(
        string='Área de cuarentena',
        track_visibility='onchange'
    )
    a_4_total = fields.Float(
        string='Metros cuadrados del área funcional',
        track_visibility='onchange',
        default=0
    )
    a_4_conservadora_sangre = fields.Boolean(
        string='Área para conservadora(s) de sangre de +/-2 °C a +6 °C',
        track_visibility='onchange'
    )
    a_4_congeladora = fields.Boolean(
        string='Área para congeladora(s) de -20 o menos °C',
        track_visibility='onchange'
    )
    a_4_almacenamiento_plaqueta = fields.Boolean(
        string='Área de almacenamiento de plaquetas de 20 a 24 °C',
        track_visibility='onchange'
    )
    a_4_seroteca = fields.Boolean(
        string='Área para seroteca',
        track_visibility='onchange'
    )
    a_4_distribucion = fields.Boolean(
        string='Área de distribución',
        track_visibility='onchange'
    )
    a_5_total = fields.Float(
        string='Metros cuadrados del área funcional',
        track_visibility='onchange',
        default=0
    )
    a_5_recepcion = fields.Boolean(
        string='Área de recepción y atención de solicitudes transfusionales y entrega de resultados',
        track_visibility='onchange'
    )
    a_6_total = fields.Float(
        string='Metros cuadrados del área funcional',
        track_visibility='onchange',
        default=0
    )
    a_6_administrativo = fields.Boolean(
        string='área funcional administrativo',
        track_visibility='onchange'
    )
    a_7_total = fields.Float(
        string='Metros cuadrados del área funcional',
        track_visibility='onchange',
        default=0
    )
    a_7_lavado = fields.Boolean(
        string='área funcional de lavado, autoclavado y descontaminación',
        track_visibility='onchange'
    )
    a_8_total = fields.Float(
        string='Metros cuadrados del área funcional',
        track_visibility='onchange',
        default=0
    )
    a_8_sshh = fields.Boolean(
        string='Área de servicios higiénicos para el personal',
        track_visibility='onchange'
    )
    a_9_total = fields.Float(
        string='Metros cuadrados del área funcional',
        track_visibility='onchange',
        default=0
    )
    a_9_otro = fields.Boolean(
        string='Área de servicios higiénicos para el personal',
        track_visibility='onchange'
    )
    a_9_almacen = fields.Boolean(
        string='Almacén',
        track_visibility='onchange'
    )
    a_9_sala_reuniones = fields.Boolean(
        string='Sala de reuniones',
        track_visibility='onchange'
    )
    a_9_vestuario = fields.Boolean(
        string='Vestuario del personal',
        track_visibility='onchange'
    )
    a_9_otro_texto = fields.Char(
        string='Otros',
        track_visibility='onchange'
    )
    a_10_total = fields.Float(
        string='Metros cuadrados del área funcional',
        track_visibility='onchange',
        default=0
    )
    a_10_control_calidad = fields.Boolean(
        string='Área de control de calidad de hemocomponentes',
        track_visibility='onchange'
    )
    a_11_total = fields.Float(
        string='Metros cuadrados del área',
        track_visibility='onchange',
        default=0
    )
    a_11_transfusion = fields.Boolean(
        string='área para transfusión',
        track_visibility='onchange'
    )
    a_12_total = fields.Float(
        string='Metros cuadrados del área',
        track_visibility='onchange',
        default=0
    )
    a_12_promocion = fields.Boolean(
        string='área de promoción de la donación voluntaria de sangre',
        track_visibility='onchange'
    )
    suma_total = fields.Float(
        string='Suma total de áreas',
        compute='_compute_anual_mensual',
        store=True
    )
    archivo = fields.Binary(
        string='Plano de distribución de área funcionals y áreas del CHBS*',
        attachment=True,
        track_visibility='onchange'
    )
    archivo_nombre = fields.Char(
        string='Nombre plano de distribución de área funcionales y áreas del CHBS',
        track_visibility='onchange'
    )
    special = fields.Boolean(default=True)

    _sql_constraints = [
        ('codigo_name', 'unique(banco_id)',
         'El registro debe ser único!'),
    ]

    @api.model
    def _selection_tipo_banco(self):
        return self.env['basecatalogo.catalogo'].get_catalogo('_selection_tipo_banco')

    @api.one
    @api.depends('area_total', 'a_1_total', 'a_2_total', 'a_3_total', 'a_4_total', 'a_5_total', 'a_6_total', 'a_7_total', 'a_8_total', 'a_9_total', 'a_10_total', 'a_11_total', 'a_12_total')
    def _compute_anual_mensual(self):
        self.suma_total = self.a_1_total + self.a_2_total + self.a_3_total + self.a_4_total + self.a_5_total + self.a_6_total + self.a_7_total + self.a_8_total + self.a_9_total + self.a_10_total + self.a_11_total + self.a_12_total
        if self.suma_total == self.area_total:
            self.special = True
        else:
            self.special = False

    map_field_campo = constants.MAP_FIELD_CAMPO

    @api.onchange(*map_field_campo)
    def _onchange_tuple_attrs(self):
        def message_error(valor, name):
            return {
                'warning': {'message': u'El valor ingresado de {}, deben ser valor positivo o igual a 0 '.format(valor)},
                'value': {name: 0},
            }

        for name, valor in self.map_field_campo.items():
            if getattr(self, name) < 0:
                return message_error(valor, name)

    @api.one
    def action_send(self):
        self.estado = constants.ENVIADO

    @api.one
    def action_validate(self):
        self.estado = constants.VALIDADO

    @api.one
    def action_draft(self):
        self.estado = constants.BORRADOR

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(Infraestructura, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        es_coordinador_establecimiento = self.env.user.has_group('hemored.group_coordinador_establecimiento_hemored')
        if view_type == 'form':
            doc_input_infraestructura = etree.XML(res['arch'])
            my_attrs1 = '{"readonly": true}'
            if es_coordinador_establecimiento:
                for node in doc_input_infraestructura.xpath("//field[@name='banco_id']"):
                    node.set('modifiers', my_attrs1)
            res['arch'] = etree.tostring(doc_input_infraestructura)
        return res
