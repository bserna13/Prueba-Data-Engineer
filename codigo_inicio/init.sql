CREATE TABLE IF NOT EXISTS public.historico_aba_macroactivos
(
    ingestion_year varchar(50),
    ingestion_month varchar(50),
    ingestion_day varchar(50),
    id_sistema_cliente varchar(50) ,
    macroactivo varchar(50) ,
    cod_activo varchar(50) ,
    aba varchar(50),
    cod_perfil_riesgo varchar(50),
    cod_banca varchar(50),
    year varchar(50),
    month varchar(50)
);


CREATE TABLE IF NOT EXISTS public.cat_perfil_riesgo
(
    cod_perfil_riesgo varchar(50) ,
    perfil_riesgo varchar(50) 
);

CREATE TABLE IF NOT EXISTS public.catalogo_activos
(
    activo varchar(50),
    cod_activo varchar(50)
);

CREATE TABLE IF NOT EXISTS public.catalogo_banca
(
    cod_banca varchar(50) ,
    banca varchar(50) 
);