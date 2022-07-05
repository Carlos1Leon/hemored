# -*- coding: utf-8 -*-

MODULO = 'hemored'
TIPO_BANCO = 'tipo_banco'
CATEGORIA = 'categoria'
TIPO_DONANTE = 'tipo_donante'
TIPO_POSTULANTE = 'tipo_postulante'
MOTIVO_DIFERIDO_EXCLUIDO = 'motivo_diferido_excluido'
MARCADOR = 'marcador'
CLASE = 'clase'
REACTIVIDAD = 'reactividad'
TIPO_HEMOCOMPONENTE = 'tipo_hemocomponente'
HEMOCOMPONENTE = 'hemocomponente'
TIPO_UNIDAD_SANGRE = 'tipo_unidad_sangre'
SUB_TIPO_UNIDAD_SANGRE = 'sub_tipo_unidad_sangre'
GRUPO_EDAD = 'grupo_edad'
GRUPO_EDAD_DONANTE = 'grupo_edad_donante'
TIPO_DEMANDA_HEMOCOMPONENTE = 'tipo_demanda_hemocomponente'
TRANSFERENCIA_HEMOCOMPONENTE = 'transferencia_hemocomponente'
TIPO_REACCION_ADVERSA = 'tipo_reaccion_adversa'
CAUSA_ELIMINACION_SANGRE = 'causa_eliminacion_sangre'

BORRADOR = 'borrador'
ENVIADO = 'enviado'
VALIDADO = 'validado'
APROBADO = 'aprobado'
OBSERVADO = 'observado'
REVISION = 'revision'
PRE_INSCRIPCION = 'pre_inscripcion'
REGISTRADO = 'registrado'
SUSPENDIDO = 'suspendido'
ANULADO = 'anulado'
GENERADO = 'generado'

FICHA_MENSUAL = 'ficha_mensual'
FICHA_ANUAL = 'ficha_anual'

SI = 'S'
NO = 'N'

SEXO_MASCULINO = 'M'
SEXO_FEMENINO = 'F'

HABILITA = 'habilitado'
INHABILITA = 'inhabilitado'
CADUCADO = 'caducado'

ALMACENABLE = 'product'
CONSUMIBLE = 'consu'

JEFE = 'jefe_responsable_de_chbs'
RESPONSABLE = 'responsable_del_sistema_calidad'
PERSONAL_ASISTENCIAL = 'personal_asistencial'
PERSONAL_ADMINISTRATIVO = 'personal_administrativo'

BUENO = 'bueno'
REGULAR = 'regular'
MALO = 'malo'

LABORATORIO = 'laboratorio_clinico'
BANCO_SANGRE = 'banco_de_sangre'

PROPIO = 'propio'
COMPARTIDO = 'compartido'
SESION_USO = 'sesión_de_uso'

DEPARTAMENTO = 'departamento'
SERVICIO = 'servicio'
AREA = 'area'

CUMPLE = 'cumple'
NO_CUMPLE = 'no_cumple'
CUMPLE_PARCIALMENTE = 'cumple_parcialmente'

VIGENTE = 'vigente'
VENCIDO = 'vencido'
POR_VENCER = 'por_vencer'
RENOVADO = 'renovado'
CESADO = 'cesado'

DIRECTO = 'directo'
ESCALERAS = 'escaleras'
RAMPA = 'rampa'
ASCENSOR = 'ascensor'

CRITICO_A = 'critico_a'
CRITICO_B = 'critico_b'
OTROS = 'otros'

NO_TIENE = 'no_tiene'
HEMATOLOGO_CLINICO = 'hematologo_clinico'
PATOLOGO_CLINICO = 'patologo_clinico'
GENERALES = 'generales'

OPERATIVO = 'operativo'
IN_OPERATIVO = 'in_operativo'

COSTO_HEMOTERAPIA = 'costo_hemoterapia'
PRUEBA_INMUNOHEMATOLOGIA = 'pruebas_inmunohematologia'

MENSUAL = 'mensual'
BIMESTRAL = 'bimestral'
TRIMESTRAL = 'trimestral'
SEMESTRAL = 'semestral'
ANUAL = 'anual'

ELISA = 'elisa'
CLIA = 'clia'
ECLIA = 'eclia'
ELFA = 'elfa'

QUIMIOLUMNICENCIA = 'quimiolumnicensia'

EN_TUBO = 'en_tubo'
TARJETA_GEL = 'tarjeta_gel'
MICROPLACA = 'microplaca'

CAS = 'cas'
CONTRATADO = 'contratado'
NOMBRADO = 'nombrado'
OTRO = 'otro'

GUIAI = 'i'
GUIAII = 'ii'

MANUAL = 'manual'
ELECTRICO = 'sellador_electronico'

SELECTION_ESTADO_FICHA = [
    (BORRADOR, 'Borrador'),
    (ENVIADO, 'Enviado'),
    (VALIDADO, 'Validado'),
]

SELECTION_DONANTE = [
    (ELISA, 'ELISA'),
    (QUIMIOLUMNICENCIA, 'QUIMIOLUMNICENCIA'),
]

SELECTION_EXTRACCION = [
    (MANUAL, 'Manual'),
    (ELECTRICO, 'Sellador Electrónico'),
]

SELECTION_GUIA = [
    (GUIAI, 'I'),
    (GUIAII, 'II'),
]

SELECTION_LABORAL = [
    (CAS, 'CAS'),
    (CONTRATADO, 'Contratado'),
    (NOMBRADO, 'Nombrado'),
    (OTRO, 'Otro'),
]

SELECTION_CATEGORIA = [
    ('1', 'I-1'),
    ('2', 'I-2'),
    ('3', 'I-3'),
    ('4', 'I-4'),
    ('5', 'II-1'),
    ('6', 'II-2'),
    ('7', 'II-E'),
    ('8', 'III-1'),
    ('9', 'III-2'),
    ('10', 'III-E'),
    ('99', 'Sin Categoría'),
]

SELECTION_METODOLOGIA_INMUNOHEMATOLOGIA = [
    (EN_TUBO, u'En tubo'),
    (TARJETA_GEL, u'Tarjeta gel'),
    (MICROPLACA, u'Microplaca'),
    (OTROS, u'Otro')
]

SELECTION_METODOLOGIA_INMUNOSEROLOGIA = [
    (ELISA, u'ELISA'),
    (CLIA, u'CLIA'),
    (ECLIA, u'ECLIA'),
    (ELFA, u'ELFA'),
    (OTROS, u'Otro')
]

SELECTION_PERIODICIDAD = [
    (MENSUAL, u'Mensual'),
    (BIMESTRAL, u'Bimestral'),
    (TRIMESTRAL, u'Trimestral'),
    (SEMESTRAL, u'Semestral'),
    (ANUAL, u'Anual'),
    (OTROS, u'Otra')
]

SELECTION_COSTO = [
    (COSTO_HEMOTERAPIA, u'Costo de producción de hemocomponentes'),
    (PRUEBA_INMUNOHEMATOLOGIA, u'Pruebas de inmunohematología')
]

SELECTION_TIPO_ESPECIALIDAD_MEDICO = [
    (PATOLOGO_CLINICO, u'Patología Clínica'),
    (HEMATOLOGO_CLINICO, u'Hematología Clínica'),
    (OTROS, u'Otra especialidad'),
    (NO_TIENE, u'Sin especialidad')
]

SELECTION_TIPO_ESPECIALIDAD_TECNOLOGO = [
    (GENERALES, u'Banco de Sangre / Hemoterapia / Medicina Transfusional'),
    (OTROS, u'Otra especialidad'),
    (NO_TIENE, u'Sin especialidad')
]

SELECTION_TIPO_OPERATIVIDAD = [
    (OPERATIVO, u'Operativo'),
    (IN_OPERATIVO, u'Inoperativo')
]

SELECTION_TIPO_EQUIPAMIENTO = [
    (CRITICO_A, u'Equipos críticos categoría A'),
    (CRITICO_B, u'Equipos críticos categoría B'),
    (OTROS, u'Otros equipos indispensables, servicios e instalaciones')
]

SELECTION_TIPO_ACCESO = [
    (DIRECTO, u'Directo'),
    (ESCALERAS, u'Escaleras'),
    (RAMPA, u'Rampa'),
    (ASCENSOR, u'Ascensor')
]

SELECTION_ESTADO_CONVENIO = [
    (VIGENTE, u'Vigente'),
    (VENCIDO, u'Vencido'),
    (POR_VENCER, u'Por vencer'),
    (RENOVADO, u'Renovado'),
    (CESADO, u'Cesado'),
]

SELECTION_REQUISITOS = [
    (CUMPLE, u'Cumple'),
    (NO_CUMPLE, u'No cumple'),
    (CUMPLE_PARCIALMENTE, u'Cumple parcialmente'),
]

SELECTION_ESTRUCTURA = [
    (DEPARTAMENTO, u'Departamento'),
    (SERVICIO, u'Servicio'),
    (AREA, u'Área'),
]

SELECTION_CONDICION = [
    (PROPIO, u'Propio'),
    (SESION_USO, u'Cesión de uso'),
]

SELECTION_CONDICION_OPCIONAL = [
    (PROPIO, u'Propio'),
    (COMPARTIDO, u'Compartido'),
]

SELECTION_CONSERVACION = [
    (BUENO, u'Bueno'),
    (REGULAR, u'Regular'),
    (MALO, u'Malo'),
]

SELECTION_UBICACION = [
    (LABORATORIO, u'Laboratorio clínico'),
    (BANCO_SANGRE, u'CHBS'),
]

SELECTION_PUESTO = [
    (JEFE, u'Jefe / Responsable de CHBS'),
    (RESPONSABLE, u'Responsable del Sistema de Gestión de Calidad'),
    (PERSONAL_ASISTENCIAL, u'Personal Asistencial'),
    (PERSONAL_ADMINISTRATIVO, u'Personal Administrativo'),
]

SELECTION_TIPO_CATG = [
    (ALMACENABLE, u'Almacenable'),
    (CONSUMIBLE, u'Consumible'),
]

SELECTION_ESTADO_BANCO = [
    (PRE_INSCRIPCION, u'Pre-inscripción'),
    (REVISION, u'Revisión'),
    (OBSERVADO, u'Observado'),
    (REGISTRADO, u'Registrado'),
    (SUSPENDIDO, u'Suspendido'),
    (ANULADO, u'Anulado'),
]

SELECTION_ESTADO_REPORTE = [
    (BORRADOR, u'Borrador'),
    (REGISTRADO, u'Registrado'),
    (GENERADO, u'Generado'),
]

SELECTION_SEXO = [
    (SEXO_MASCULINO, u'Masculino'),
    (SEXO_FEMENINO, u'Femenino'),
]

SELECTION_FICHA = [
    (FICHA_MENSUAL, u'Ficha mensual'),
    (FICHA_ANUAL, u'Ficha anual'),
]

SELECTION_RESPUESTA = [
    (SI, u'Sí'),
    (NO, u'No'),
]

SELECTION_MES = [
    ('01', u'Enero'),
    ('02', u'Febrero'),
    ('03', u'Marzo'),
    ('04', u'Abril'),
    ('05', u'Mayo'),
    ('06', u'Junio'),
    ('07', u'Julio'),
    ('08', u'Agosto'),
    ('09', u'Setiembre'),
    ('10', u'Octubre'),
    ('11', u'Noviembre'),
    ('12', u'Diciembre'),
]

SELECTION_STATE = [
    (BORRADOR, u'Borrador'),
    (ENVIADO, u'Enviado'),
    (VALIDADO, u'Validado')
]

SELECTION_INSTITUCION = [
    ('1', 'MINSA'),
    ('2', 'ESSALUD'),
    ('3', 'SANIDAD DEL EJERCITO DEL PERU'),
    ('4', 'SANIDAD DE LA FUERZA AEREA DEL PERU'),
    ('5', 'SANIDAD DE LA POLICIA NACIONAL DEL PERU'),
    ('6', 'SANIDAD DE LA MARINA DE GUERRA DEL PERU'),
    ('7', 'GOBIERNO REGIONAL'),
    ('8', 'MUNICIPALIDAD PROVINCIAL'),
    ('9', 'MUNICIPALIDAD DISTRITAL'),
    ('10', 'PRIVADO'),
    ('13', 'INPE'),
    ('11', 'OTRO'),
]

SELECTION_INSTITUCION_1 = 'MINSA'
SELECTION_INSTITUCION_2 = 'ESSALUD'
SELECTION_INSTITUCION_3 = 'SANIDAD DEL EJERCITO DEL PERU'
SELECTION_INSTITUCION_4 = 'SANIDAD DE LA FUERZA AEREA DEL PERU'
SELECTION_INSTITUCION_5 = 'SANIDAD DE LA POLICIA NACIONAL DEL PERU'
SELECTION_INSTITUCION_6 = 'SANIDAD DE LA MARINA DE GUERRA DEL PERU'
SELECTION_INSTITUCION_7 = 'GOBIERNO REGIONAL'
SELECTION_INSTITUCION_8 = 'MUNICIPALIDAD PROVINCIAL'
SELECTION_INSTITUCION_9 = 'MUNICIPALIDAD DISTRITAL'
SELECTION_INSTITUCION_10 = 'PRIVADO'
SELECTION_INSTITUCION_13 = 'INPE'
SELECTION_INSTITUCION_11 = 'OTRO'

TIPO_BANCO_1 = 'tipo I'
TIPO_BANCO_2 = 'tipo II'

MAP_FIELD_CELDA = {
    # Donacion Sangre
    'cantidad_pe_x_ca': 'C15',
    'cantidad_pe_x_cvim': 'C16',
    'cantidad_pe_x_cvem': 'C17',
    'cantidad_pe_x_cr': 'C18',
    'cantidad_pe_x_cpr': 'C19',
    'cantidad_pd_x_ca': 'D15',
    'cantidad_pd_x_cvim': 'D16',
    'cantidad_pd_x_cvem': 'D17',
    'cantidad_pd_x_cr': 'D18',
    'cantidad_pd_x_cpr': 'D19',
    'cantidad_padi_x_ca': 'E15',
    'cantidad_padi_x_cvim': 'E16',
    'cantidad_padi_x_cvem': 'E17',
    'cantidad_padi_x_cr': 'E18',
    'cantidad_padi_x_cpr': 'E19',
    'cantidad_padc_x_ca': 'F15',
    'cantidad_padc_x_cvim': 'F16',
    'cantidad_padc_x_cvem': 'F17',
    'cantidad_padc_x_cr': 'F18',
    'cantidad_padc_x_cpr': 'F19',
    # Donaciones por sexo
    'cantidad_donacion_h': 'B31',
    'cantidad_donacion_m': 'C31',
    # Tamizaje unidades
    'cantidad_mvih_clt_cv': 'C43',
    'cantidad_mvih_clt_cr': 'C44',
    'cantidad_mvih_clt_cpr': 'C45',
    'cantidad_mvih_clt_ca': 'C46',
    'cantidad_mvih_clr_cv': 'D43',
    'cantidad_mvih_clr_cr': 'D44',
    'cantidad_mvih_clr_cpr': 'D45',
    'cantidad_mvih_clr_ca': 'D46',
    'cantidad_mvih_clzg_cv': 'E43',
    'cantidad_mvih_clzg_cr': 'E44',
    'cantidad_mvih_clzg_cpr': 'E45',
    'cantidad_mvih_clzg_ca': 'E46',
    'cantidad_mhbsag_clt_cv': 'F43',
    'cantidad_mhbsag_clt_cr': 'F44',
    'cantidad_mhbsag_clt_cpr': 'F45',
    'cantidad_mhbsag_clt_ca': 'F46',
    'cantidad_mhbsag_clr_cv': 'G43',
    'cantidad_mhbsag_clr_cr': 'G44',
    'cantidad_mhbsag_clr_cpr': 'G45',
    'cantidad_mhbsag_clr_ca': 'G46',
    'cantidad_mhbsag_clzg_cv': 'H43',
    'cantidad_mhbsag_clzg_cr': 'H44',
    'cantidad_mhbsag_clzg_cpr': 'H45',
    'cantidad_mhbsag_clzg_ca': 'H46',
    'cantidad_mhepc_clt_cv': 'I43',
    'cantidad_mhepc_clt_cr': 'I44',
    'cantidad_mhepc_clt_cpr': 'I45',
    'cantidad_mhepc_clt_ca': 'I46',
    'cantidad_mhepc_clr_cv': 'J43',
    'cantidad_mhepc_clr_cr': 'J44',
    'cantidad_mhepc_clr_cpr': 'J45',
    'cantidad_mhepc_clr_ca': 'J46',
    'cantidad_mhepc_clzg_cv': 'K43',
    'cantidad_mhepc_clzg_cr': 'K44',
    'cantidad_mhepc_clzg_cpr': 'K45',
    'cantidad_mhepc_clzg_ca': 'K46',
    'cantidad_mantihbc_clt_cv': 'L43',
    'cantidad_mantihbc_clt_cr': 'L44',
    'cantidad_mantihbc_clt_cpr': 'L45',
    'cantidad_mantihbc_clt_ca': 'L46',
    'cantidad_mantihbc_clr_cv': 'M43',
    'cantidad_mantihbc_clr_cr': 'M44',
    'cantidad_mantihbc_clr_cpr': 'M45',
    'cantidad_mantihbc_clr_ca': 'M46',
    'cantidad_mantihbc_clzg_cv': 'N43',
    'cantidad_mantihbc_clzg_cr': 'N44',
    'cantidad_mantihbc_clzg_cpr': 'N45',
    'cantidad_mantihbc_clzg_ca': 'N46',
    'cantidad_mhtlv_clt_cv': 'C51',
    'cantidad_mhtlv_clt_cr': 'C52',
    'cantidad_mhtlv_clt_cpr': 'C53',
    'cantidad_mhtlv_clt_ca': 'C54',
    'cantidad_mhtlv_clr_cv': 'D51',
    'cantidad_mhtlv_clr_cr': 'D52',
    'cantidad_mhtlv_clr_cpr': 'D53',
    'cantidad_mhtlv_clr_ca': 'D54',
    'cantidad_mhtlv_clzg_cv': 'E51',
    'cantidad_mhtlv_clzg_cr': 'E52',
    'cantidad_mhtlv_clzg_cpr': 'E53',
    'cantidad_mhtlv_clzg_ca': 'E54',
    'cantidad_msifilis_clt_cv': 'F51',
    'cantidad_msifilis_clt_cr': 'F52',
    'cantidad_msifilis_clt_cpr': 'F53',
    'cantidad_msifilis_clt_ca': 'F54',
    'cantidad_msifilis_clr_cv': 'G51',
    'cantidad_msifilis_clr_cr': 'G52',
    'cantidad_msifilis_clr_cpr': 'G53',
    'cantidad_msifilis_clr_ca': 'G54',
    'cantidad_msifilis_clzg_cv': 'H51',
    'cantidad_msifilis_clzg_cr': 'H52',
    'cantidad_msifilis_clzg_cpr': 'H53',
    'cantidad_msifilis_clzg_ca': 'H54',
    'cantidad_mchagas_clt_cv': 'I51',
    'cantidad_mchagas_clt_cr': 'I52',
    'cantidad_mchagas_clt_cpr': 'I53',
    'cantidad_mchagas_clt_ca': 'I54',
    'cantidad_mchagas_clr_cv': 'J51',
    'cantidad_mchagas_clr_cr': 'J52',
    'cantidad_mchagas_clr_cpr': 'J53',
    'cantidad_mchagas_clr_ca': 'J54',
    'cantidad_mchagas_clzg_cv': 'K51',
    'cantidad_mchagas_clzg_cr': 'K52',
    'cantidad_mchagas_clzg_cpr': 'K53',
    'cantidad_mchagas_clzg_ca': 'K54',
    'cantidad_motros_clt_cv': 'L51',
    'cantidad_motros_clt_cr': 'L52',
    'cantidad_motros_clt_cpr': 'L53',
    'cantidad_motros_clt_ca': 'L54',
    'cantidad_motros_clr_cv': 'M51',
    'cantidad_motros_clr_cr': 'M52',
    'cantidad_motros_clr_cpr': 'M53',
    'cantidad_motros_clr_ca': 'M54',
    'cantidad_motros_clzg_cv': 'N51',
    'cantidad_motros_clzg_cr': 'N52',
    'cantidad_motros_clzg_cpr': 'N53',
    'cantidad_motros_clzg_ca': 'N54',
    # Reactividad
    'cantidad_unr_cv': 'C60',
    'cantidad_unr_cr': 'C61',
    'cantidad_unr_cpr': 'C62',
    'cantidad_unr_ca': 'C63',
    'cantidad_ur_cv': 'D60',
    'cantidad_ur_cr': 'D61',
    'cantidad_ur_cpr': 'D62',
    'cantidad_ur_ca': 'D63',
    'cantidad_uzg_cv': 'E60',
    'cantidad_uzg_cr': 'E61',
    'cantidad_uzg_cpr': 'E62',
    'cantidad_uzg_ca': 'E63',
    # USO DE HEMOCOMPONENTE
    'cantidad_gh1_pact': 'C82',
    'cantidad_gh1_hst': 'D82',
    'cantidad_gh1_hgr': 'E82',
    'cantidad_gh1_hpfc': 'F82',
    'cantidad_gh1_hc': 'G82',
    'cantidad_gh1_hp': 'H82',
    'cantidad_gh1_hap': 'I82',
    'cantidad_gh1_hagr': 'J82',
    'cantidad_gh1_haplasma': 'K82',
    'cantidad_gh2_pact': 'C83',
    'cantidad_gh2_hst': 'D83',
    'cantidad_gh2_hgr': 'E83',
    'cantidad_gh2_hpfc': 'F83',
    'cantidad_gh2_hc': 'G83',
    'cantidad_gh2_hp': 'H83',
    'cantidad_gh2_hap': 'I83',
    'cantidad_gh2_hagr': 'J83',
    'cantidad_gh2_haplasma': 'K83',
    'cantidad_gh3_pact': 'C84',
    'cantidad_gh3_hst': 'D84',
    'cantidad_gh3_hgr': 'E84',
    'cantidad_gh3_hpfc': 'F84',
    'cantidad_gh3_hc': 'G84',
    'cantidad_gh3_hp': 'H84',
    'cantidad_gh3_hap': 'I84',
    'cantidad_gh3_hagr': 'J84',
    'cantidad_gh3_haplasma': 'K84',
    'cantidad_gh4_pact': 'C85',
    'cantidad_gh4_hst': 'D85',
    'cantidad_gh4_hgr': 'E85',
    'cantidad_gh4_hpfc': 'F85',
    'cantidad_gh4_hc': 'G85',
    'cantidad_gh4_hp': 'H85',
    'cantidad_gh4_hap': 'I85',
    'cantidad_gh4_hagr': 'J85',
    'cantidad_gh4_haplasma': 'K85',
    'cantidad_gh5_pact': 'C86',
    'cantidad_gh5_hst': 'D86',
    'cantidad_gh5_hgr': 'E86',
    'cantidad_gh5_hpfc': 'F86',
    'cantidad_gh5_hc': 'G86',
    'cantidad_gh5_hp': 'H86',
    'cantidad_gh5_hap': 'I86',
    'cantidad_gh5_hagr': 'J86',
    'cantidad_gh5_haplasma': 'K86',
    'cantidad_gh6_pact': 'C87',
    'cantidad_gh6_hst': 'D87',
    'cantidad_gh6_hgr': 'E87',
    'cantidad_gh6_hpfc': 'F87',
    'cantidad_gh6_hc': 'G87',
    'cantidad_gh6_hp': 'H87',
    'cantidad_gh6_hap': 'I87',
    'cantidad_gh6_hagr': 'J87',
    'cantidad_gh6_haplasma': 'K87',
    'cantidad_gh7_pact': 'C88',
    'cantidad_gh7_hst': 'D88',
    'cantidad_gh7_hgr': 'E88',
    'cantidad_gh7_hpfc': 'F88',
    'cantidad_gh7_hc': 'G88',
    'cantidad_gh7_hp': 'H88',
    'cantidad_gh7_hap': 'I88',
    'cantidad_gh7_hagr': 'J88',
    'cantidad_gh7_haplasma': 'K88',
    # DEMANDA DE HEMOCOMPONENTE
    'cantidad_ds_hgr': 'D94',
    'cantidad_ds_hpfc': 'E94',
    'cantidad_ds_hp': 'F94',
    'cantidad_ds_hap': 'G94',
    'cantidad_da_hgr': 'D95',
    'cantidad_da_hpfc': 'E95',
    'cantidad_da_hp': 'F95',
    'cantidad_da_hap': 'G95',
    # TRANSFERENCIA DE HEMOCOMPONENTE
    'cantidad_tur_hst': 'D100',
    'cantidad_tur_hgr': 'E100',
    'cantidad_tur_hpfc': 'F100',
    'cantidad_tur_hc': 'G100',
    'cantidad_tur_hp': 'H100',
    'cantidad_tur_hap': 'I100',
    'cantidad_tur_hagr': 'J100',
    'cantidad_tut_hst': 'D101',
    'cantidad_tut_hgr': 'E101',
    'cantidad_tut_hpfc': 'F101',
    'cantidad_tut_hc': 'G101',
    'cantidad_tut_hp': 'H101',
    'cantidad_tut_hap': 'I101',
    'cantidad_tut_hagr': 'J101',
    # ELIMINACIÓN DE SANGRE Y HEMOCOMPONENTES
    'cantidad_cv_hst': 'C129',
    'cantidad_cv_hgr': 'D129',
    'cantidad_cv_hpfc': 'E129',
    'cantidad_cv_hc': 'F129',
    'cantidad_cv_hp': 'G129',
    'cantidad_cv_hap': 'H129',
    'cantidad_cv_hagr': 'I129',
    'cantidad_cv_haplasma': 'J129',
    'cantidad_cmitt_hst': 'C130',
    'cantidad_cmitt_hgr': 'D130',
    'cantidad_cmitt_hpfc': 'E130',
    'cantidad_cmitt_hc': 'F130',
    'cantidad_cmitt_hp': 'G130',
    'cantidad_cmitt_hap': 'H130',
    'cantidad_cmitt_hagr': 'I130',
    'cantidad_cmitt_haplasma': 'J130',
    'cantidad_ca_hst': 'C131',
    'cantidad_ca_hgr': 'D131',
    'cantidad_ca_hpfc': 'E131',
    'cantidad_ca_hc': 'F131',
    'cantidad_ca_hp': 'G131',
    'cantidad_ca_hap': 'H131',
    'cantidad_ca_hagr': 'I131',
    'cantidad_ca_haplasma': 'J131',
    'cantidad_ct_hst': 'C132',
    'cantidad_ct_hgr': 'D132',
    'cantidad_ct_hpfc': 'E132',
    'cantidad_ct_hc': 'F132',
    'cantidad_ct_hp': 'G132',
    'cantidad_ct_hap': 'H132',
    'cantidad_ct_hagr': 'I132',
    'cantidad_ct_haplasma': 'J132',
    'cantidad_cp_hst': 'C133',
    'cantidad_cp_hgr': 'D133',
    'cantidad_cp_hpfc': 'E133',
    'cantidad_cp_hc': 'F133',
    'cantidad_cp_hp': 'G133',
    'cantidad_cp_hap': 'H133',
    'cantidad_cp_hagr': 'I133',
    'cantidad_cp_haplasma': 'J133',
    'cantidad_co_hst': 'C134',
    'cantidad_co_hgr': 'D134',
    'cantidad_co_hpfc': 'E134',
    'cantidad_co_hc': 'F134',
    'cantidad_co_hp': 'G134',
    'cantidad_co_hap': 'H134',
    'cantidad_co_hagr': 'I134',
    'cantidad_co_haplasma': 'J134',
}
