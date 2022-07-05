# HEMORED

Aplicativo web que tiene la finalidad fundamental que la Dirección General de Donaciones, Trasplantes y CHBS verifique 
en tiempo real la producción de hemocomponentes en CHBS.
Además, monitorear los hemocomponentes transferidos.
Por último, generar reportes estadísticos en tiempo real del CHBS.


Adicionalmente se agregara complementos para que Bancos de sangre postulen a registrarse para que puedan realizar el 
registro de las estadísticas y supervisiones que realiza PRONAHEBAS


Sistema HEMORED
==================================================

# 1. Repositorio de [hemored] (https://git.minsa.gob.pe/DIGDOT/hemored.git)

|Módulo | Descripción|
|----|----|
hemored | Módulo Hemored
stock_hemocomponente | Módulo Stock Hemocomponente

# 2. Requisitos/Dependencias del sistema

    ## Requisitos del Sistema Operativo

    - Odoo V12
    - Python 3.0.*
    - [mpi-client] hemored/requirements.txt

# 3. Dependencias


## 3.1 [odoo12-share] (https://git.minsa.gob.pe/oidt/odoo12-share):

- renipress
- toponimos_peru
- basecatalogo
- settings_app
- password_security
- minsa_periodo
- consultadatos


## Instalación de modulos
Instalar el modulo:

    -   renipress
    -   hemored
    -   stock_hemocomponente

El resto de addons se instalarán automáticamente por la dependencia entre ellos.

## Configuración de parámetros

### mpi-client
Ingresar a `Configuración/Técnico/Parámetros/Parámetros del sistema` y configurar los parametros: `mpi_api_host` y `mpi_api_token`.


