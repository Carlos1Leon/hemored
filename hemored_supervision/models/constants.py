# -*- coding: utf-8 -*-

MODULO = 'hemored_supervision'
BORRADOR = 'borrador'
PROPUESTO = 'propuesto'
POSTERGADO = 'postergado'
CONFIRMADO = 'confirmado'
SUPERVISION = 'supervision'
MONITOREO = 'monitoreo'
OBSERVADO = 'observado'
TERMINADO = 'terminado'
SI = 'S'
NO = 'N'
SERVICIO = 'servicio'
DEPARTAMENTO = 'departamento'
AREA = 'area'
NOMBRADO = 'nombrado'
CAS = 'cas'
TERCERO = 'tercero'
CERO = '0'
UNO = '1'
DOS = '2'
TRES = '3'
CUATRO = '4'
CINCO = '5'
SEIS = '6'
NULO = 'N'
LEVE = 'L'
MODERADO = 'M'
GRAVE = 'G'
ENTREVISTA = 'entrevista'
AUTOAPLICADO = 'autoaplicado'
MEDICO = 'medico'
TECNOLOGO = 'tecnologo_medico'
BIOLOGO = 'biologo'
OTRA_PROFESION = 'otra_profesion'
OTRO = 'otro'
COMPLETO = 'completo'
INCOMPLETO = 'incompleto'
EMAIL = 'email'
PRESENCIAL = 'presencial'
PRE_DONACION = 'pre_donacion'
POST_DONACION = 'post_donacion'
AMBOS = 'ambos'
MANUAL = 'manual'
SELLADOR_ELECTRONICO = 'sellador_electronico'
DOBLE = 'doble'
TRIPLE = 'triple'
CUADRUPLE = 'cuadruple'
DIGITAL = 'digital'
ELISA = 'elisa'
QUIMIOLUMINISCENCIA = 'quimioluminiscencia'
ELECTROQUIMIOLUMINISCENCIA = 'electroquimioluminiscencia'
DIARIO = 'diario'
INTERDIARIO = 'interdiario'
MAYOR_A_UNA_SEMANA = 'mayor_a_una_semana'
NUEVA_MUESTRA = 'nueva_muestra'
CON_MUESTRA_ALMACENADA = 'con_muestra_almacenada'
PLASMA_DE_LA_UNIDAD_EXTRAIDA = 'plasma_de_la_unidad_extraida'
SEMIAUTOMATICO = 'semiautomatico'
AUTOMATICO = 'automatico'
PRODUCTOS_IRRADIADOS = 'productos_irradiados'
PRODUCTO_LEUCORREDUCIDO = 'producto_leucorreducido'
COMPONENTES_EN_POOL = 'componentes_en_pool'
METODO = 'metodo'
EQUIPO = 'equipo'
PROPIO = 'propio'
CESION_DE_USO = 'entregado_calidad_cesion_de_uso'
CESION_DE_USO_1 = 'cesion_de_uso'
BUENO = 'bueno'
REGULAR = 'regular'
MALO = 'malo'
MENOR_UN_ANO = 'menor_un_ano'
DE_UNO_A_DOS = 'de_uno_a_dos'
DE_DOS_A_TRES = 'de_dos_a_tres'
DE_TRES_A_CUATRO = 'de_tres_a_cuatro'
DE_CINCO_A_MAS = 'de_cinco_a_mas'
PRIMER_PISO = 'primer_piso'
SEGUNDO_PISO = 'segundo_piso'
SOTANO = 'sotano'
COMPARTIDO = 'compartido'
TERCERIZADO = 'tercerizado'
SO = 'segunda_opcion'
TO = 'tercera_opcion'
SELECTION_C_OPT = [
    (SO, u'Segunda opción'),
    (TO, u'Tercera Opción'),
    (OTRO, u'Otros'),
]
SELECTION_PROFESION = [
    (TECNOLOGO, u'Tecnólogo Médico'),
    (BIOLOGO, u'Biólogo'),
    (OTRA_PROFESION, u'Otra Profesión'),
]
SELECTION_RANGO_EDAD = [
    (MENOR_UN_ANO, u'Menor a un año'),
    (DE_UNO_A_DOS, u'De 1 a 2'),
    (DE_DOS_A_TRES, u'De 2 a 3'),
    (DE_TRES_A_CUATRO, u'De 3 a 4'),
    (DE_CINCO_A_MAS, u'De 5 a más'),
]
SELECTION_ESTADO = [
    (BUENO, u'Bueno'),
    (REGULAR, u'Regular'),
    (MALO, u'Malo'),
]
SELECTION_SGI = [
    (PROPIO, u'Propio'),
    (CESION_DE_USO, u'Entregado en calidad de cesión de uso'),
]
SELECTION_REL_EQUIP = [
    (PROPIO, u'Propio'),
    (CESION_DE_USO_1, u'cesión de uso'),
]
SELECTION_TIPO_SELLADO_TABULADURA = [
    (MANUAL, u'Manual'),
    (SELLADOR_ELECTRONICO, u'Sellador Electronico'),
]
SELECTION_TIPO_BOLSA_COLECTORA = [
    (DOBLE, u'Doble'),
    (TRIPLE, u'Triple'),
    (CUADRUPLE, u'Cuadruple'),
]
SELECTION_TIPO_TRAZABILIDAD_COMPONENTES = [
    (MANUAL, u'Manual'),
    (DIGITAL, u'digital'),
]
SELECTION_TIPO_REACTIVO_MARCADOR = [
    (ELISA, u'Elisa'),
    (QUIMIOLUMINISCENCIA, u'Quimioluminiscencia'),
    (ELECTROQUIMIOLUMINISCENCIA, u'Electroquimioluminiscencia'),
]
SELECTION_TIPO_FREC_TAMIZAJE_SEROLOGICO = [
    (DIARIO, u'Diario'),
    (INTERDIARIO, u'Interdiario'),
    (MAYOR_A_UNA_SEMANA, u'Mayor a una semana'),
]
SELECTION_TIPO_MUESTRAS_REACTIVAS = [
    (NUEVA_MUESTRA, u'Nueva muestra'),
    (CON_MUESTRA_ALMACENADA, u'Con Muestra Almacenada'),
    (PLASMA_DE_LA_UNIDAD_EXTRAIDA, u'Plasma de la Unidad Extraida'),
]
SELECTION_TIPO_MANUAL_SEMI_AUTO = [
    (MANUAL, u'Manual'),
    (SEMIAUTOMATICO, u'Semiautomatizado'),
    (AUTOMATICO, u'Automatizado'),
]
SELECTION_TIPO_PROC_ETIQ_ESPECIALES = [
    (PRODUCTOS_IRRADIADOS, u'Productos Irradiados'),
    (PRODUCTO_LEUCORREDUCIDO, u'Producto Leucorreducido'),
    (COMPONENTES_EN_POOL, u'Componentes en pool'),
]
SELECTION_TIPO_PROCED_COLECT_CELULAR = [
    (METODO, u'Método'),
    (EQUIPO, u'Equipo'),
]
SELECTION_TIPO_ENVIO = [
    (EMAIL, u'Email'),
    (PRESENCIAL, u'Presencial'),
]
SELECTION_TIPO_EXAM = [
    (COMPLETO, u'Completo'),
    (INCOMPLETO, u'Incompleto'),
]
SELECTION_TIPO_TAMIZAJE = [
    (PRE_DONACION, u'Pre Donacion'),
    (POST_DONACION, u'Post Donacion'),
    (AMBOS, u'Ambos'),
]
SELECTION_TIPO_METODOLOGIA = [
    (ENTREVISTA, u'Entrevista'),
    (AUTOAPLICADO, u'Autoaplicado'),
]
SELECTION_PESO = [
    (CERO, u'0'),
    (UNO, u'1'),
    (DOS, u'2'),
    (TRES, u'3'),
    (CUATRO, u'4'),
    (CINCO, u'5'),
]
SELECTION_GRAVEDAD = [
    (NULO, u'Nulo'),
    (LEVE, u'Leve'),
    (MODERADO, u'Moderado'),
    (GRAVE, u'Grave'),
]
SELECTION_TIPO_CONDICION = [
    (NOMBRADO, u'Nombrado'),
    (CAS, u'CAS'),
    (OTRO, u'Otros'),
]
SELECTION_CANT_CONVENIO = [
    (UNO, u'1'),
    (DOS, u'2'),
    (TRES, u'3'),
    (CUATRO, u'4'),
    (CINCO, u'5'),
    (SEIS, u'6'),
]
SELECTION_SERVICIO_DEPARTAMENTO = [
    (SERVICIO, u'Servicio'),
    (DEPARTAMENTO, u'Departamento'),
    (AREA, u'Área'),
]
SELECTION_ESTADO_SUPERVISION_BANCO = [
    (BORRADOR, u'Borrador'),
    (PROPUESTO, u'Propuesto'),
    (CONFIRMADO, u'Confirmado'),
    (POSTERGADO, u'Postergado'),
]
SELECTION_ESTADO_FORMULARIO_SUPERVISION_BANCO = [
    (BORRADOR, u'Borrador'),
    (SUPERVISION, u'Supervisión'),
    (OBSERVADO, u'Observado'),
    (TERMINADO, u'Terminado'),
]
SELECTION_RESPUESTA = [
    (SI, u'Sí'),
    (NO, u'No'),
]
SELECTION_TIPO_FORMULARIO = [
    (SUPERVISION, u'Supervisión'),
    (MONITOREO, u'Monitoreo'),
]
SELECTION_PISO = [
    (SOTANO, u'Sotano'),
    (PRIMER_PISO, u'1er Piso'),
    (SEGUNDO_PISO, u'2do Piso'),
    (OTRO, u'Otro'),
]
SELECTION_INFRA_INSTAL = [
    (PROPIO, u'Propio'),
    (COMPARTIDO, u'Compartido'),
    (TERCERIZADO, u'Tercerizado'),
]
