# Prueba talento B - 2024 

Este proyecto tiene como objetivo desarrollar una herramienta analítica que facilite a los gerentes comerciales de inversión la visualización y el análisis de los portafolios de sus clientes. Dicha herramienta permitirá extraer conocimiento de la información disponible y generar nuevos negocios de inversión de manera más automatizada.

## Índice

- [Introducción](#introducción)
- [Instalación](#instalación)
- [Pipeline del proyecto](#características)
- [Conclusiones técnicas e insights de negocio ](#tecnologías)

## Introducción

Los gerentes comerciales de inversión manejan una gran cantidad de clientes, cuya información se encuentra dispersa en diversas fuentes y con códigos poco convencionales. Esto dificulta la extracción de conocimiento y la generación de nuevos negocios de inversión de manera automatizada. 

Para abordar este problema, se ha desarrollado una herramienta analítica que permite visualizar:

- El portafolio de cada cliente y el porcentaje que representa cada macroactivo y activo en el total del portafolio.
- El portafolio por banca y el porcentaje que representa cada macroactivo.
- El portafolio por perfil de riesgo y el porcentaje que representa cada macroactivo.
- La evolución mes a mes del promedio de Activos Bajo Administración (ABA) del total del portafolio, con la opción de seleccionar periodos específicos para el análisis.

## Instalación

Para la instalación se necesita descargar e instalar Docker y PostgreSQL (tenga en cuenta las variables de entorno del sistema), posteriormente se clona el repositorio y se navega en la teminal hasta donde está el proyecto, se decir en mi caso (C:\Users\Brahi\Documents\GitHub\Prueba-Data-Engineer>) y se ejecuta la siguiente sentencia de docker.

```bash
# Monta los contenedores que ejecutan el proyecto
docker-compose up -d
```

Sé que no mencione esto en el video, se hace una pequeña restauración de la base de datos, por lo tanto, para ejecutar el proyecto adicionalmente se ejecuta el siguiente comando en la consola:

```bash
# Restaurar datos
psql -h localhost -p 5431 -U brahian -f prueba.sql prueba
```
posteriormente pedira la contraseña la cual ponen 'pass' sin comillas

y listo, ve al navegador de su preferenca y pon 'http://localhost:4520/'

## Pipeline del proyecto

Este es el bosquejo del sistema o pipeline que diseñe para el sistema analítico

!['Diagrama del Sistema'](Diagrama%20y%20Video/Diagrama.png)

## Conclusiones técnicas e insights de negocio

### Conclusiones técnicas:

El desarrollo de productos de BI es un proceso en el que se deben considerar diversos factores como la reproducibilidad del producto, para que funcione en cualquier instancia donde se aloje, y diseñarlo de forma sencilla y concisa para que el usuario final pueda hacer uso del producto y generar valor agregado para la toma de decisiones. La escalabilidad del producto es también crucial. Por eso, el desarrollo y la programación para llevar a cabo un ETL o ELT, y posteriormente desarrollar un modelo analítico o dashboard, cobran vital importancia en la creación de estos productos.

### Conclusiones de negocio:

Al hacer un análisis por portafolio de los clientes, a simple vista se observa una variabilidad de portafolios. Esto se debe a que cada cliente es distinto. Por ejemplo, cuando observamos el tipo de banca, se nota que estas tienen diversidad en los activos y macroactivos de sus portafolios, a diferencia de las empresas y pymes que no tienen tan diversificados sus activos y cuyos macroactivos suelen ser de Renta Variable o FICs.

Para disminuir el riesgo en inversiones, una estrategia clásica es diversificar el portafolio de inversión, y eso se ve claramente en las visualizaciones. Cuando el riesgo es moderado, los activos son diversos y los macroactivos suelen ser entre variables y FICs. Cuando el riesgo es conservador, generalmente los macroactivos son FICs. En cambio, cuando el riesgo es agresivo y el portafolio de inversión está sujeto a una compañía en específico como activo, lo que puede aumentar la probabilidad estimada de riesgo, los macroactivos suelen ser Renta Variable o FICs.

!['Portafolio Riesgo Moderado'](Diagrama%20y%20Video/riesgo_moderado.png)

Se observa que durante enero de 2024 el ABA tuvo un incremento en comparación con diciembre de 2023. Este incremento se sostuvo moderadamente hasta marzo, donde se nota una pequeña baja. En los primeros días de abril, sube nuevamente similar al nivel anterior, pero no se mantiene y cae de nuevo a mediados de este mes. Este indicador es importante porque también refleja la confianza que nuestros clientes depositan en el banco para administrar sus activos. Por ende, se recomendaría realizar un estudio en los meses donde hay valles (marzo y finales de abril) con el fin de mejorar la experiencia de los clientes con el banco y aumentar la eficiencia en el manejo de sus activos.

!['Linea de tiempo del ABA promedio'](Diagrama%20y%20Video/linea_tiempo.png)
