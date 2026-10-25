ENCUESTA

CREATE TABLE encuesta (
encuestaID integer PRIMARY KEY AUTOINCREMENT,
Encuestatexto text NOT NULL UNIQUE 
);

INSERT INTO encuesta (
encuestaID,
encuestatexto)
SELECT 
SurveyID,
Description 
FROM Survey;

PREGUNTAS

CREATE TABLE diccionario_pregunta (
preguntaID integer PRIMARY KEY,
pregunta_texto text NOT NULL UNIQUE
);

INSERT INTO diccionario_pregunta (
preguntaID,
pregunta_texto
)
SELECT  
q.questionid,
q.questiontext
FROM Question q;

GENERO

CREATE TABLE genero (
generoID integer PRIMARY KEY AUTOINCREMENT,
generotexto varchar);

INSERT INTO genero (
generotexto)
SELECT DISTINCT 
a.AnswerText 
FROM Answer a 
WHERE a.QuestionID = 2;

PAIS

CREATE TABLE pais (
paisID integer PRIMARY KEY AUTOINCREMENT,
paistexto varchar(100) NOT NULL UNIQUE);

INSERT INTO pais (
paistexto)
SELECT DISTINCT 
a.AnswerText 
FROM Answer a 
WHERE a.QuestionID IN (3, 50);

PUESTO TRABAJO

CREATE TABLE puesto_trabajo (
puesto_trabajoID integer PRIMARY KEY AUTOINCREMENT,
puestotexto text NOT NULL UNIQUE);

INSERT INTO puesto_trabajo (
puestotexto)
SELECT DISTINCT a.AnswerText 
FROM Answer a 
WHERE a.QuestionID = 117;

CONDICION TRASTORNO

CREATE TABLE condicion_trastorno (
condicion_trastornoID integer PRIMARY KEY AUTOINCREMENT,
condicion_trastornotexto text NOT NULL UNIQUE);

INSERT INTO condicion_trastorno (
condicion_trastornotexto)
SELECT DISTINCT a.AnswerText 
FROM Answer a 
WHERE a.QuestionID = 115;

ESTADO EEUU

CREATE TABLE estado_EEUU (
estado_EEUUID integer PRIMARY KEY AUTOINCREMENT,
Estadotexto varchar (100) NOT NULL UNIQUE);

INSERT INTO estado_EEUU (
estadotexto)
SELECT DISTINCT a.AnswerText 
FROM Answer a 
WHERE a.QuestionID IN (51, 4);

PARTICIPANTE

CREATE TABLE participante (
participanteID integer PRIMARY KEY,
edad 		   int,
generoID 	   integer,
paisID 		   integer,
estado_EEUUID  integer,
raza 		   text,
FOREIGN KEY (generoID) 		REFERENCES genero(generoID),
FOREIGN KEY (paisID)        REFERENCES pais(paisID),
FOREIGN KEY (estado_EEUUID) REFERENCES estado_EEUU(estado_EEUUID)
);

WITH edad AS (
	SELECT a.answertext,a.UserID 
	FROM answer a
	WHERE questionID = 1
),
	 ge AS (
	SELECT a.userID,g.generoID  
	FROM Answer a 
	JOIN genero g ON g.generotexto = a.AnswerText 
	WHERE a.QuestionID = 2
),
	 pa AS (
	SELECT a.userID,p.paisID
	FROM Answer a 
	JOIN pais p ON p.paistexto = a.AnswerText
	WHERE a.questionID = 3
),
	 es AS (
	SELECT a.userID,ee.estado_EEUUID 
	FROM Answer a 
	JOIN estado_EEUU ee ON ee.Estadotexto = a.AnswerText
	WHERE a.QuestionID = 4
),
	 raza AS (
	SELECT a.userID,a.answertext
	FROM Answer a 
	WHERE a.QuestionID = 89
)
SELECT DISTINCT 
a.userID,
edad.answertext,
ge.generoID,
pa.paisID,
es.estado_EEUUID,
raza.answertext
FROM answer a 
JOIN edad ON edad.UserID = a.userID
JOIN ge ON ge.userID = a.userID
JOIN pa ON pa.userID = a.userID
JOIN es ON es.userID = a.userID
LEFT JOIN raza ON a.userID = raza.userID;

INSERT INTO participante (
participanteID,
edad,
generoID,
paisID,
estado_EEUUID,
raza)
SELECT DISTINCT 
a.userID,
edad.answertext,
ge.generoID,
pa.paisID,
es.estado_EEUUID,
raza.answertext
FROM answer a 
JOIN (
	SELECT a.answertext,a.UserID 
	FROM answer a
	WHERE questionID = 1
) AS edad ON edad.UserID = a.userID
JOIN (
	SELECT a.userID,g.generoID  
	FROM Answer a 
	JOIN genero g ON g.generotexto = a.AnswerText 
	WHERE a.QuestionID = 2
) AS ge ON ge.userID = a.userID
JOIN (
	SELECT a.userID,p.paisID
	FROM Answer a 
	JOIN pais p ON p.paistexto = a.AnswerText
	WHERE a.questionID = 3
) AS pa ON pa.userID = a.userID
JOIN (
	SELECT a.userID,ee.estado_EEUUID 
	FROM Answer a 
	JOIN estado_EEUU ee ON ee.Estadotexto = a.AnswerText
	WHERE a.QuestionID = 4
) AS es ON es.userID = a.userID
LEFT JOIN (
	SELECT a.userID,a.answertext
	FROM Answer a 
	WHERE a.QuestionID = 89
) as raza ON a.userID = raza.userID;

ESTADO_MENTAL

CREATE TABLE estado_mental (
participanteID             integer NOT NULL UNIQUE,
encuestaID    		       integer NOT NULL,
diagnostico_oficial        varchar (10),
busco_tratamiento          integer,
condiciones_diagnosticadas text,
PRIMARY KEY (participanteID , encuestaID),
FOREIGN KEY (participanteID) REFERENCES participantes(participanteID),
FOREIGN KEY (encuestaID)     REFERENCES encuesta(encuestaID)
);

WITH base AS (
    SELECT DISTINCT
           a.UserID,
           a.SurveyID,
           a.QuestionID,
           TRIM(a.AnswerText) AS respuesta
    FROM Answer a
    WHERE a.QuestionID IN (7, 34, 115)
)
SELECT
    UserID                                              AS usuario_id,
    MIN(SurveyID)                                       AS encuesta_id,
    MAX(CASE WHEN QuestionID =  34 THEN respuesta END)  AS diagnostico_oficial,
    MAX(CASE WHEN QuestionID =   7 THEN respuesta END)  AS busco_tratamiento,
    GROUP_CONCAT(CASE WHEN QuestionID = 115 THEN respuesta END, ' | ')
                                                        AS condiciones_diagnosticadas,
    COUNT(CASE WHEN QuestionID = 115 THEN 1 END)        AS cant_condiciones
FROM base
GROUP BY UserID;

INSERT INTO estado_mental (
    participanteID,
    encuestaID,
    diagnostico_oficial,
    busco_tratamiento,
    condiciones_diagnosticadas 
)
SELECT
    UserID                                             	AS usuario_id,
    MIN(SurveyID)                                       AS encuesta_id,
    MAX(CASE WHEN QuestionID =  34 THEN respuesta END)  AS diagnostico_oficial,
    MAX(CASE WHEN QuestionID =   7 THEN respuesta END)  AS busco_tratamiento,
    GROUP_CONCAT(CASE WHEN QuestionID = 115 THEN respuesta END, ' | ')
                                                        AS condiciones_diagnosticadas
FROM (
    SELECT DISTINCT
           a.UserID,
           a.SurveyID,
           a.QuestionID,
           TRIM(a.AnswerText) AS respuesta
    FROM Answer a
    WHERE a.QuestionID IN (7, 34, 115)
) AS base
GROUP BY UserID;

CATEGORIA LABORAL

CREATE TABLE categoria_laboral (
participanteID        integer NOT NULL UNIQUE,
encuestaID            integer NOT null, 
puesto_trabajoID      integer,
trabajo_remoto        varchar(100),
paisID                integer,
estado_eeuuID         integer,
independiente_trabajo integer,
compania_estech       integer,
PRIMARY KEY (participanteID , encuestaID),
FOREIGN KEY (puesto_trabajoID) REFERENCES puesto_trabajo(puesto_trabajoID),
FOREIGN KEY (participanteID)   REFERENCES participantes(participanteID),
FOREIGN KEY (encuestaID)       REFERENCES encuesta(EncuestaID),
FOREIGN KEY (paisID)           REFERENCES pais(paisID),
FOREIGN KEY (estado_eeuuID)    REFERENCES estado_eeuu(estado_eeuuID)
);

WITH base AS (
    SELECT DISTINCT
           a.UserID,
           a.SurveyID,
           a.QuestionID,
           TRIM(a.AnswerText) AS respuesta
    FROM Answer a
    WHERE a.QuestionID IN (118, 50, 51, 5, 13, 68, 117)
)
SELECT 
	UserID												        AS usuarioID,
	MIN(SurveyID)										     	AS encuestaID,
	MAX(CASE WHEN QuestionID =  118 THEN respuesta        END ) AS trabajo_remoto,
	MAX(CASE WHEN QuestionID =  117 THEN puesto_trabajoID END ) AS puesto_trabajo,
	MAX(CASE WHEN QuestionID =   50 THEN paisID           END ) AS PaisID,
	MAX(CASE WHEN QuestionID =   51 THEN estado_EEUUID    END ) AS estado_eeuuID,
	MAX(CASE WHEN QuestionID =    5 THEN respuesta        END ) AS independiente_trabajo,
	MAX(CASE WHEN QuestionID =   13 THEN respuesta        END ) AS rol_trabajo_estech,
	MAX(CASE WHEN QuestionID =   68 THEN respuesta        END ) AS primer_trabajo
FROM base b
LEFT JOIN pais p ON p.paistexto = b.respuesta
LEFT JOIN estado_EEUU ee ON ee.Estadotexto = b.respuesta
LEFT JOIN puesto_trabajo pt ON pt.puestotexto = b.respuesta 
GROUP BY UserID;

INSERT INTO categoria_laboral (
    participanteID,
    encuestaID,
    puesto_trabajoID,
    paisID,
    estado_eeuuID,
    independiente_trabajo,
    rol_trabajo_estech,
    trabajo_remoto,
    primer_trabajo
)
SELECT 
    b.UserID 													   AS participanteID,
    MIN(b.SurveyID) 											   AS encuestaID,
    MAX(CASE WHEN b.QuestionID = 117 THEN pt.puesto_trabajoID END) AS puesto_trabajoID,
    MAX(CASE WHEN b.QuestionID =  50 THEN p.paisID 		      END) AS paisID,
    MAX(CASE WHEN b.QuestionID =  51 THEN ee.estado_EEUUID    END) AS estado_eeuuID,
    MAX(CASE WHEN b.QuestionID =   5 THEN b.respuesta         END) AS independiente_trabajo,
    MAX(CASE WHEN b.QuestionID =  13 THEN b.respuesta         END) AS rol_trabajo_estech,
    MAX(CASE WHEN b.QuestionID = 118 THEN b.respuesta         END) AS trabajo_remoto,
    MAX(CASE WHEN b.QuestionID =  68 THEN b.respuesta 	      END) AS primer_trabajo
FROM (
    SELECT DISTINCT
           a.UserID,
           a.SurveyID,
           a.QuestionID,
           TRIM(a.AnswerText) AS respuesta
    FROM Answer a
    WHERE a.QuestionID IN (118, 50, 51, 5, 13, 68, 117)
) AS b
LEFT JOIN pais p ON p.paistexto = b.respuesta
LEFT JOIN estado_EEUU ee ON ee.Estadotexto = b.respuesta
LEFT JOIN puesto_trabajo pt ON pt.puestotexto = b.respuesta 
GROUP BY b.UserID;

IMPACTO PROFESIONAL

CREATE TABLE impacto_profesional (
    participanteID                  integer NOT NULL unique,
    encuestaID                      integer NOT NULL,
    afecta_carrera                  integer,
    interfiere_trabajo              varchar(50),
    PRIMARY KEY (participanteID , encuestaID)
    FOREIGN KEY (participanteID) REFERENCES participantes(participanteID),
	FOREIGN KEY (encuestaID)     REFERENCES encuesta(EncuestaID)
);

WITH base AS (
    SELECT DISTINCT
           a.UserID,
           a.SurveyID,
           a.QuestionID,
           TRIM(a.AnswerText) AS respuesta
    FROM Answer a
    WHERE a.QuestionID IN (113, 49)
)
SELECT 
	b.UserID 											AS participanteID,
    MIN(b.SurveyID) 									AS encuestaID,
    MAX(CASE WHEN b.QuestionID = 113 THEN respuesta END) AS afecta_carrera,
    MAX(CASE WHEN b.QuestionID = 49 THEN respuesta END) AS interfiere_trabajo
FROM base b
GROUP BY userID;

INSERT INTO impacto_profesional (
    participanteID,
    encuestaID,
    afecta_carrera,
    interfiere_trabajo
)
SELECT 
    b.UserID 											AS participanteID,
    MIN(b.SurveyID)  									AS encuestaID,
    MAX(CASE WHEN b.QuestionID = 113 THEN respuesta END) AS afecta_carrera,
    MAX(CASE WHEN b.QuestionID = 49 THEN respuesta END) AS interfiere_trabajo
FROM (
    SELECT DISTINCT
           a.UserID,
           a.SurveyID,
           a.QuestionID,
           TRIM(a.AnswerText) AS respuesta
    FROM Answer a
    WHERE a.QuestionID IN (113, 49)
) AS b
GROUP BY b.UserID;

PERJUICIO SALUD MENTAL

create table prejuicio_salud_mental(
	participanteID           integer NOT NULL unique,
    encuestaID               integer NOT NULL,
	crees_te_verian_mal      varchar(10),
	comentarios_malos        varchar(10),
	consecuencias_negativas  varchar(50),
	PRIMARY KEY (participanteID , encuestaID),
	FOREIGN KEY (participanteID)  REFERENCES participantes(participanteID),
	FOREIGN KEY (encuestaID)      REFERENCES encuesta(EncuestaID)
);

WITH base AS (
    SELECT DISTINCT
           a.UserID,
           a.SurveyID,
           a.QuestionID,
           TRIM(a.AnswerText) AS respuesta
    FROM Answer a
    WHERE a.QuestionID IN (114, 31, 105)
)
SELECT 
	UserID 											    AS participanteID,
    MIN(SurveyID) 									    AS encuestaID,
    MAX(CASE WHEN QuestionID = 114 THEN respuesta END ) AS crees_te_verian_mal,
    MAX(CASE WHEN QuestionID =  31 THEN respuesta END ) AS comentarios_malos,
    MAX(CASE WHEN QuestionID = 105 THEN respuesta END ) AS consecuencias_negativas
FROM base  
GROUP BY UserID;

INSERT INTO prejuicio_salud_mental (
    participanteID,
    encuestaID,
    crees_te_verian_mal,
    comentarios_malos,
    consecuencias_negativas
)
SELECT 
    b.UserID 											   AS participanteID,
    MIN(b.SurveyID) 									   AS encuestaID,
    MAX(CASE WHEN b.QuestionID = 114 THEN b.respuesta END) AS crees_te_verian_mal,
    MAX(CASE WHEN b.QuestionID =  31 THEN b.respuesta END) AS comentarios_malos,
    MAX(CASE WHEN b.QuestionID = 105 THEN b.respuesta END) AS consecuencias_negativas
FROM (
    SELECT DISTINCT
           a.UserID,
           a.SurveyID,
           a.QuestionID,
           TRIM(a.AnswerText) AS respuesta
    FROM Answer a
    WHERE a.QuestionID IN (114, 31, 105)
) AS b
GROUP BY b.UserID;

AYUDA LABORAL

create table ayuda_laboral (
participanteID  		      integer NOT NULL UNIQUE,
encuestaID 					  integer NOT NULL ,
recursos_empresa_ayuda_mental varchar(50),
discucion_formal_salud_mental varchar(50),
conoces_opciones_ayuda 		  varchar(50),
beneficios_salud_mental 	  varchar(50),
anonimato_protegido			  varchar(50),
PRIMARY KEY (participanteID , encuestaID),
FOREIGN KEY (participanteID) REFERENCES participantes(participanteID),
FOREIGN KEY (encuestaID)     REFERENCES encuesta(encuestaID)
);

WITH base AS (
    SELECT DISTINCT
           a.UserID,
           a.SurveyID,
           a.QuestionID,
           TRIM(a.AnswerText) AS respuesta
    FROM Answer a
    WHERE a.QuestionID IN (16,15,14,10,11)
)
SELECT 
	UserID 								 AS participanteID,
    MIN(SurveyID) 					     AS encuestaID,
    MAX(CASE WHEN QuestionID = 16 THEN respuesta END ) AS recursos_empresa_ayuda_mental,
    MAX(CASE WHEN QuestionID = 15 THEN respuesta END ) AS discucion_formal_salud_mental,
    MAX(CASE WHEN QuestionID = 14 THEN respuesta END ) AS conoces_opciones_ayuda,
    MAX(CASE WHEN QuestionID = 10 THEN respuesta END ) AS beneficios_salud_mental,
    MAX(CASE WHEN QuestionID = 11 THEN respuesta END ) AS anonimato_protegido
FROM base
GROUP BY userID;

INSERT INTO  ayuda_laboral (
    participanteID,
    encuestaID,
    recursos_empresa_ayuda_mental,
    discucion_formal_salud_mental,
    conoces_opciones_ayuda,
    beneficios_salud_mental,
    anonimato_protegido
)
SELECT 
    b.UserID AS participanteID,
    MIN(b.SurveyID) AS encuestaID,
    MAX(CASE WHEN b.QuestionID = 16 THEN b.respuesta END) AS recursos_empresa_ayuda_mental,
    MAX(CASE WHEN b.QuestionID = 15 THEN b.respuesta END) AS discucion_formal_salud_mental,
    MAX(CASE WHEN b.QuestionID = 14 THEN b.respuesta END) AS conoces_opciones_ayuda,
    MAX(CASE WHEN b.QuestionID = 10 THEN b.respuesta END) AS beneficios_salud_mental,
    MAX(CASE WHEN b.QuestionID = 11 THEN b.respuesta END) AS anonimato_protegido
FROM (
    SELECT DISTINCT
           a.UserID,
           a.SurveyID,
           a.QuestionID,
           TRIM(a.AnswerText) AS respuesta
    FROM Answer a
    WHERE a.QuestionID IN (16, 15, 14, 10, 11)
) AS b
GROUP BY b.UserID;






