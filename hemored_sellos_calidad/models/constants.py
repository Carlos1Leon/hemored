# -*- coding: utf-8 -*-

GLOBULOS_ROJOS = 'globulos_rojos'
PLASMA = 'plasma'
PLAQUETAS = 'plaquetas'
CRIOPRECIPITADO = 'crioprecipitado'
BORRADOR = 'borrador'
ENVIADO = 'enviado'
ACTIVO = 'activo'
ELIMINADO = 'eliminado'
O_POSITIVO = 'o+'
A_POSITIVO = 'a+'
B_POSITIVO = 'b+'
AB_POSITIVO = 'ab+'
O_NEGATIVO = 'o-'
A_NEGATIVO = 'a-'
B_NEGATIVO = 'b-'
AB_NEGATIVO = 'ab-'


MONTH = {
    '01': 'Enero',
    '02': 'Febrero',
    '03': 'Marzo',
    '04': 'Abril',
    '05': 'Mayo',
    '06': 'Junio',
    '07': 'Julio',
    '08': 'Agosto',
    '09': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre',
}

SELECTION_GRUPOSANGUINEO = [
    (O_POSITIVO, u'O+'),
    (A_POSITIVO, u'A+'),
    (B_POSITIVO, u'B+'),
    (AB_POSITIVO, u'AB+'),
    (O_NEGATIVO, u'O-'),
    (A_NEGATIVO, u'A-'),
    (B_NEGATIVO, u'B-'),
    (AB_NEGATIVO, u'AB-'),
]

SELECTION_STATE = [
    (BORRADOR, u'Borrador'),
    (ENVIADO, u'Enviado'),
]

SELECTION_STATE_REGISTRO = [
    (ACTIVO, u'Activo'),
    (ELIMINADO, u'Eliminado'),
]

SELECTION_COMPONENTES_SELLOS = [
    (GLOBULOS_ROJOS, 'Globulos rojos'),
    (PLASMA, 'Plasma'),
    (PLAQUETAS, 'Plaquetas'),
    (CRIOPRECIPITADO, 'Crioprecipitado'),
]
