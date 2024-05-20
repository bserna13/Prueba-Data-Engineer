# Prueba técnica talento B - 2024 

Este proyecto tiene como objetivo desarrollar una herramienta analítica que facilite a los gerentes comerciales de inversión la visualización y el análisis de los portafolios de sus clientes. Dicha herramienta permitirá extraer conocimiento de la información disponible y generar nuevos negocios de inversión de manera más automatizada.

## Índice

- [Introducción](#introducción)
- [Instalación](#instalación)
- [Pipeline del proyecto](#características)
- [Uso](#uso)
- [Conclusiones técnicas e insights de negocio  ](#tecnologías)

## Introducción

Los gerentes comerciales de inversión manejan una gran cantidad de clientes, cuya información se encuentra dispersa en diversas fuentes y con códigos poco convencionales. Esto dificulta la extracción de conocimiento y la generación de nuevos negocios de inversión de manera automatizada. 

Para abordar este problema, se ha desarrollado una herramienta analítica que permite visualizar:

- El portafolio de cada cliente y el porcentaje que representa cada macroactivo y activo en el total del portafolio.
- El portafolio por banca y el porcentaje que representa cada macroactivo.
- El portafolio por perfil de riesgo y el porcentaje que representa cada macroactivo.
- La evolución mes a mes del promedio de Activos Bajo Administración (ABA) del total del portafolio, con la opción de seleccionar periodos específicos para el análisis.

## Instalación

Se clona el repositorio y se ejecuta la siguiente sentencia de docker para montar los contenedores que albergan el proyecto con las respectivas dependencias ya cargadas.

```bash
# Monta los contenedores que ejecutan el proyecto
docker-compose up -d
```
## Pipeline del proyecto

Este es el bosquejo del sistema o pipeline que diseñe para el sistema analítico

!['Diagrama del Sistema'](Diagrama y Video/diagrama.png)

