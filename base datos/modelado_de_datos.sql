INSTALL sqlite;
LOAD sqlite;
ATTACH IF NOT EXISTS '.\mental_health_limpia3.sqlite' AS MS (TYPE sqlite);
USE main;


CREATE OR REPLACE TABLE tt AS 
SELECT
p.participanteID,
p.edad,
g.generotexto,
pa.paistexto,
pa.paisID,
es.Estadotexto,
al.recursos_empresa_ayuda_mental,
al.discucion_formal_salud_mental,
al.conoces_opciones_ayuda,
al.beneficios_salud_mental,
al.anonimato_protegido,
cl.trabajo_remoto,
cl.independiente_trabajo,
pt.puestotexto,
pt.puesto_trabajoID,
pt.nivel_jerarquico,
e.encuestaID,
e.Encuestatexto,
em.diagnostico_oficial,
em.busco_tratamiento,
em.condiciones_diagnosticadas,
ip.afecta_carrera,
ip.interfiere_trabajo,
psm.crees_te_verian_mal,
psm.comentarios_malos,
psm.consecuencias_negativas

FROM participantes p
LEFT JOIN genero g ON p.generoID = g.generoID
LEFT JOIN pais pa ON p.paisID = pa.paisID
LEFT JOIN estado_EEUU es ON es.estado_EEUUID = p.estado_EEUUID
LEFT JOIN categoria_laboral cl ON p.participanteID = cl.participanteID
LEFT JOIN encuesta e ON e.encuestaID = cl.encuestaID
LEFT JOIN ayuda_laboral al ON p.participanteID = al.participanteID
LEFT JOIN estado_mental em ON p.participanteID = em.participanteID AND e.encuestaID = em.encuestaID
LEFT JOIN impacto_profesional ip ON p.participanteID = ip.participanteID AND e.encuestaID = ip.encuestaID
LEFT JOIN prejuicio_salud_mental psm ON p.participanteID = psm.participanteID AND e.encuestaID = psm.encuestaID
LEFT JOIN puesto_trabajo pt ON cl.puesto_trabajoID = pt.puesto_trabajoID;

CREATE OR REPLACE TABLE DIM_PARTICIPANTE (
    participanteID BIGINT PRIMARY KEY,
    edad BIGINT,
    generotexto VARCHAR,
    condiciones_diagnosticadas VARCHAR,
    busco_tratamiento BIGINT,
    diagnostico_oficial VARCHAR
);

CREATE OR REPLACE TABLE DIM_UBICACION (
	ubicacionID BIGINT PRIMARY KEY,
    paistexto VARCHAR,
    Estadotexto VARCHAR
);

CREATE OR REPLACE TABLE DIM_TRABAJO (
    puesto_trabajoID BIGINT PRIMARY KEY,
    puestotexto VARCHAR,
    nivel_jerarquico VARCHAR,
    independiente_trabajo BIGINT,
    trabajo_remoto VARCHAR
);

CREATE OR REPLACE TABLE HECHOS (
    participanteID BIGINT,
    encuestaID BIGINT,
    encuestatexto VARCHAR,
    puesto_trabajoID BIGINT,
    ubicacionID  BIGINT,
    afecta_carrera VARCHAR,
    interfiere_trabajo VARCHAR,
    crees_te_verian_mal VARCHAR,
    comentarios_malos VARCHAR,
    consecuencias_negativas VARCHAR,
    recursos_empresa_ayuda_mental VARCHAR,
    conoces_opciones_ayuda VARCHAR,
    beneficios_salud_mental VARCHAR,
    anonimato_protegido VARCHAR,
    discucion_formal_salud_mental VARCHAR,
    PRIMARY KEY (participanteID, encuestaID),
    FOREIGN KEY (participanteID) REFERENCES DIM_PARTICIPANTE(participanteID),
    FOREIGN KEY (puesto_trabajoID) REFERENCES DIM_TRABAJO(puesto_trabajoID),
    FOREIGN KEY (ubicacionID) REFERENCES DIM_UBICACION(ubicacionID)
);

INSERT INTO DIM_PARTICIPANTE
SELECT DISTINCT
    participanteID,
    edad,
    generotexto,
    condiciones_diagnosticadas,
    busco_tratamiento,
    diagnostico_oficial
FROM tt;

INSERT INTO DIM_UBICACION
SELECT 
    ROW_NUMBER() OVER (ORDER BY paistexto, Estadotexto) AS ubicacionID,
    paistexto,
    Estadotexto
FROM (
    SELECT DISTINCT paistexto, Estadotexto 
    FROM tt
);

INSERT INTO DIM_TRABAJO
SELECT 
    ROW_NUMBER() OVER (ORDER BY puestotexto, nivel_jerarquico, independiente_trabajo, trabajo_remoto) AS puesto_trabajoID,
    puestotexto,
    nivel_jerarquico,
    independiente_trabajo,
    trabajo_remoto
FROM (
    SELECT DISTINCT 
        puestotexto,
        nivel_jerarquico,
        independiente_trabajo,
        trabajo_remoto
    FROM tt
);
INSERT INTO HECHOS
SELECT 
    t.participanteID,
    t.encuestaID,
    t.Encuestatexto,
    dt.puesto_trabajoID,
    u.ubicacionID,
    t.afecta_carrera,
    t.interfiere_trabajo,
    t.crees_te_verian_mal,
    t.comentarios_malos,
    t.consecuencias_negativas,
    t.recursos_empresa_ayuda_mental,
    t.conoces_opciones_ayuda,
    t.beneficios_salud_mental,
    t.anonimato_protegido,
    t.discucion_formal_salud_mental
FROM tt t
LEFT JOIN DIM_UBICACION u 
    ON t.paistexto = u.paistexto 
    AND t.Estadotexto IS NOT DISTINCT FROM u.Estadotexto
LEFT JOIN DIM_TRABAJO dt
    ON t.puestotexto = dt.puestotexto
    AND t.nivel_jerarquico IS NOT DISTINCT FROM dt.nivel_jerarquico
    AND t.independiente_trabajo IS NOT DISTINCT FROM dt.independiente_trabajo
    AND t.trabajo_remoto IS NOT DISTINCT FROM dt.trabajo_remoto;

DROP TABLE tt;
