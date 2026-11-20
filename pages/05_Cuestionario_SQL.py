import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

st.set_page_config(page_title="Consultas SQL", page_icon="🗄️", layout="wide")
st.image("assets/Cuestionario.png", use_container_width=True)

@st.cache_resource
def get_db_engine():
    try:
        DB_URL = st.secrets["connections"]["supabase"]["SUPABASE_DB_URL"]
        return create_engine(DB_URL, pool_pre_ping=True)
    except Exception as e:
        st.error(f"Error exacto de conexión: {e}")
        return None
    

engine = get_db_engine()

tab1, tab2, tab3, tab4 = st.tabs([
    "Pregunta 1: Mapa de Cobertura", 
    "Pregunta 2: Perfil Etario", 
    "Pregunta 3: Brecha Política", 
    "Pregunta 6: Respuestas Abiertas"
])

with tab1:
    st.header("Pregunta 1")
    st.subheader("Mapa de Cobertura del Instrumento")
    st.markdown("""
    **Enunciado:** No existe documentación de qué preguntas se aplicaron en cada edición. 
    Construí ese mapa a partir de los datos, determinando en qué ediciones fue formulada cada pregunta, 
    cuántas respuestas válidas recibió (descartando el centinela -1 y cadenas vacías) y la proporción de centinelas.
    """)
    st.markdown("---")

    query_1 = """
WITH resp AS (
    SELECT "AnswerText" AS answertext, "SurveyID" AS surveyid, "UserID" AS userid, "QuestionID" AS questionid
    FROM answer
),
base AS (
    SELECT q.questionid, q.questiontext, a.surveyid,
           CASE WHEN TRIM(a.answertext) IN ('', '-1') THEN NULL
                ELSE TRIM(a.answertext) END AS resp_limpia
    FROM resp a
    JOIN question q ON q.questionid = a.questionid
    WHERE a.questionid IN (10, 11, 14, 15, 16, 31, 49, 105, 113, 114)
      AND a.answertext IS NOT NULL
),
por_anio AS (
    SELECT questionid, questiontext, surveyid,
           COUNT(1) AS total_registros,
           COUNT(resp_limpia) AS respuestas_validas,
           COUNT(1) - COUNT(resp_limpia) AS respuestas_nulas
    FROM base
    GROUP BY questionid, questiontext, surveyid
),
multi AS (
    SELECT questionid
    FROM por_anio
    GROUP BY questionid
    HAVING COUNT(DISTINCT surveyid) > 1
),
tasas AS (
    SELECT p.questionid, p.questiontext, p.surveyid, p.respuestas_validas,
           1.0 * p.respuestas_nulas / p.total_registros AS prop_nulos,
           1.0 * p.respuestas_validas / p.total_registros AS tasa_valida
    FROM por_anio p
    JOIN multi m ON m.questionid = p.questionid
),
calculos AS (
    SELECT questiontext, surveyid, respuestas_validas, prop_nulos,
           tasa_valida - LAG(tasa_valida) OVER (PARTITION BY questionid ORDER BY surveyid) AS variacion_tasa_anterior,
           RANK() OVER (PARTITION BY surveyid ORDER BY tasa_valida DESC) AS ranking_cobertura
    FROM tasas
)
SELECT questiontext AS pregunta, surveyid AS encuesta, respuestas_validas,
       ROUND(prop_nulos, 3) AS proporcion_nulos,
       ROUND(variacion_tasa_anterior, 3) AS variacion_tasa_anterior,
       ranking_cobertura
FROM calculos
ORDER BY questiontext, surveyid
"""
    
    sql_input_1 = st.text_area("Escribe tu primera consulta:", value=query_1, height=250, key="sql_1")
    
    if st.button("Ejecutar Consulta 1", key="btn_1", type="primary"):
        if engine:
            with st.spinner("Ejecutando..."):
                try:
                    query_limitado = f"SELECT * FROM ({sql_input_1}) AS subquery LIMIT 50"
                    with engine.connect() as conn:
                        df = pd.read_sql(text(query_limitado), conn)
                        st.success("Consulta ejecutada con éxito.")
                        st.dataframe(df, use_container_width=True)
                except Exception as e:
                    st.error(f"Error al ejecutar el SQL: {e}")
        else:
            st.warning("⚠️ No hay conexión a la base de datos.")

with tab2:
    st.header("Pregunta 2")
    st.subheader("Perfil Etario por Nivel Jerárquico")
    st.markdown("""
    **Enunciado:** Asigná a cada encuestado un único nivel jerárquico (el más alto). 
    Depurá la edad descartando valores no numéricos y fuera del rango 15-80. 
    Para cada edición y nivel mostrá cantidad de encuestados, edad mediana (sin percentiles), mediana general y diferencia.
    """)
    st.markdown("---")

    query_2 = """
SELECT * FROM answer LIMIT 5;
"""
    
    sql_input_2 = st.text_area("Escribe tu segunda consulta:", value=query_2, height=250, key="sql_2")
    
    if st.button("Ejecutar Consulta 2", key="btn_2", type="primary"):
        if engine:
            with st.spinner("Ejecutando..."):
                try:
                    query_limitado = f"SELECT * FROM ({sql_input_2}) AS subquery LIMIT 50"
                    with engine.connect() as conn:
                        df = pd.read_sql(text(query_limitado), conn)
                        st.success("Consulta ejecutada con éxito.")
                        st.dataframe(df, use_container_width=True)
                except Exception as e:
                    st.error(f"Error al ejecutar el SQL: {e}")

with tab3:
    st.header("Pregunta 3")
    st.subheader("Brecha entre Política y Confianza")
    st.markdown("""
    **Enunciado:** Para cada edición y tramo de tamaño de empresa, calculá dos proporciones: 
    la de quienes declaran beneficios de salud mental y la de quienes se sienten cómodos hablando con su supervisor. 
    Mostrá la brecha, el ranking y el porcentaje acumulado.
    """)
    st.markdown("---")

    query_3 = """
WITH tamano AS (
    SELECT a."SurveyID", a."UserID", MAX(TRIM(a."AnswerText")) AS tramo
    FROM answer a
    JOIN question q ON q.questionid = a."QuestionID"
    WHERE LOWER(q.questiontext) LIKE '%how many employees%'
    AND TRIM(a."AnswerText") NOT IN ('-1', '')
    GROUP BY a."SurveyID", a."UserID"
),
beneficios AS (
    SELECT a."SurveyID", a."UserID",
        MAX(CASE WHEN LOWER(TRIM(a."AnswerText")) = 'yes' THEN 1 ELSE 0 END) AS ofrece
    FROM answer a
    JOIN question q ON q.questionid = a."QuestionID"
    WHERE LOWER(q.questiontext) LIKE '%your employer provide mental health benefits%'
    AND TRIM(a."AnswerText") NOT IN ('-1', '')
    GROUP BY a."SurveyID", a."UserID"
),
confianza AS (
    SELECT a."SurveyID", a."UserID",
        MAX(CASE WHEN LOWER(TRIM(a."AnswerText")) = 'yes' THEN 1 ELSE 0 END) AS comodo
    FROM answer a
    JOIN question q ON q.questionid = a."QuestionID"
    WHERE LOWER(q.questiontext) LIKE '%direct supervisor%'
    AND (LOWER(q.questiontext) LIKE '%comfortable%' OR LOWER(q.questiontext) LIKE '%willing%')
    AND LOWER(q.questiontext) NOT LIKE '%have been%'
    AND LOWER(q.questiontext) NOT LIKE '%previous%'
    AND TRIM(a."AnswerText") NOT IN ('-1', '')
    GROUP BY a."SurveyID", a."UserID"
),
poblacion AS (
    SELECT t."SurveyID", t.tramo, b.ofrece, c.comodo,
        CASE t.tramo WHEN '1-5' THEN 1 WHEN '6-25' THEN 2 WHEN '26-100' THEN 3
                        WHEN '100-500' THEN 4 WHEN '500-1000' THEN 5
                        WHEN 'More than 1000' THEN 6 ELSE 99 END AS orden
    FROM tamano t
    JOIN beneficios b ON b."SurveyID" = t."SurveyID" AND b."UserID" = t."UserID"
    JOIN confianza c ON c."SurveyID" = t."SurveyID" AND c."UserID" = t."UserID"
),
tramos AS (
    SELECT "SurveyID", tramo, orden,
        COUNT(*) AS encuestados,
           1.0 * SUM(ofrece) / COUNT(*) AS prop_beneficios,
           1.0 * SUM(comodo) / COUNT(*) AS prop_comodos,
           1.0 * SUM(ofrece) / COUNT(*) - 1.0 * SUM(comodo) / COUNT(*) AS brecha
    FROM poblacion
    GROUP BY "SurveyID", tramo, orden
)
SELECT "SurveyID" AS edicion, tramo AS tamano_empresa, encuestados,
       ROUND(100 * prop_beneficios, 1) AS pct_ofrece_beneficios,
       ROUND(100 * prop_comodos, 1) AS pct_comodo_con_supervisor,
       ROUND(100 * brecha, 1) AS brecha_pp, 
       RANK() OVER (PARTITION BY "SurveyID" ORDER BY brecha DESC) AS puesto_brecha,
       ROUND(100.0 * SUM(encuestados) OVER (PARTITION BY "SurveyID" ORDER BY orden)
            / SUM(encuestados) OVER (PARTITION BY "SurveyID"), 1) AS pct_acumulado
FROM tramos
ORDER BY "SurveyID", orden
"""
    
    sql_input_3 = st.text_area("Escribe tu tercera consulta:", value=query_3, height=250, key="sql_3")
    
    if st.button("Ejecutar Consulta 3", key="btn_3", type="primary"):
        if engine:
            with st.spinner("Ejecutando..."):
                try:
                    query_limitado = f"SELECT * FROM ({sql_input_3}) AS subquery LIMIT 50"
                    with engine.connect() as conn:
                        df = pd.read_sql(text(query_limitado), conn)
                        st.success("Consulta ejecutada con éxito.")
                        st.dataframe(df, use_container_width=True)
                except Exception as e:
                    st.error(f"Error al ejecutar el SQL: {e}")

with tab4:
    st.header("Pregunta 6")
    st.subheader("Calidad de las Respuestas Abiertas")
    st.markdown("""
    **Enunciado:** Clasificá cada respuesta abierta como sustantiva o descartable (cadenas vacías, un carácter, signos, números). 
    Para cada edición y pregunta abierta, calculá la cantidad de respuestas, proporción de sustantivas, longitud mediana y decil de calidad. 
    Solo preguntas con al menos 50 respuestas.
    """)
    st.markdown("---")

    query_6 = """
WITH preguntas_abiertas AS (
    SELECT q.questionid, q.questiontext
    FROM question q
    WHERE q.questiontext LIKE 'Describe%' OR
          q.questiontext LIKE 'Briefly Describe%' OR
          q.questiontext LIKE 'If there is anything else you would like to tell us%' OR
          q.questiontext LIKE 'Any additional notes or comments%'
),
respuestas AS (
    SELECT
        a."QuestionID",
        a."SurveyID",
        LOWER(REGEXP_REPLACE(a."AnswerText", '^[[:space:][:punct:]]+|[[:space:][:punct:]]+$', '', 'g')) AS respuesta
    FROM preguntas_abiertas p
    JOIN answer a ON a."QuestionID" = p.questionid
),
clasificacion AS (
    SELECT r.*,
        CASE WHEN LENGTH(r.respuesta) < 3
               OR r.respuesta !~ '[a-zA-Z]'
               OR r.respuesta !~ '[aeiouáéíóúAEIOUÁÉÍÓÚ]'
             THEN 'desechable'
             ELSE 'sustantiva' END AS clasificacion
    FROM respuestas r
),
ordenamiento AS (
    SELECT
        c."SurveyID",
        c."QuestionID",
        LENGTH(c.respuesta) AS longitud,
        ROW_NUMBER() OVER (PARTITION BY c."SurveyID", c."QuestionID" ORDER BY LENGTH(c.respuesta)) AS orden,
        COUNT(*) OVER (PARTITION BY c."SurveyID", c."QuestionID") AS n
    FROM clasificacion c
    WHERE c.clasificacion = 'sustantiva'
),
mediana AS (
    SELECT
        o."SurveyID",
        o."QuestionID",
        AVG(o.longitud) AS mediana_longitud
    FROM ordenamiento o
    WHERE o.orden IN ((o.n + 1) / 2, (o.n + 2) / 2)
    GROUP BY o."SurveyID", o."QuestionID"
),
todo AS (
    SELECT
        c."SurveyID",
        c."QuestionID",
        COUNT(*) AS respuestas,
        SUM(CASE WHEN c.clasificacion = 'sustantiva' THEN 1 ELSE 0 END) AS sustantivas,
        SUM(CASE WHEN c.clasificacion = 'desechable' THEN 1 ELSE 0 END) AS desechables,
        ROUND(1.0 * SUM(CASE WHEN c.clasificacion = 'sustantiva' THEN 1 ELSE 0 END) / COUNT(*), 4) AS prop_sustantivas,
        ROUND(m.mediana_longitud, 2) AS mediana_longitud_sustantivas
    FROM clasificacion c
    LEFT JOIN mediana m ON m."SurveyID" = c."SurveyID" AND m."QuestionID" = c."QuestionID"
    GROUP BY c."SurveyID", c."QuestionID", m.mediana_longitud
),
deciles AS (
    SELECT t.*,
        NTILE(10) OVER (PARTITION BY t."SurveyID" ORDER BY t.prop_sustantivas, t."QuestionID") AS decil
    FROM todo t
)
SELECT
    d."SurveyID",
    d."QuestionID",
    pa.questiontext,
    d.respuestas,
    d.sustantivas,
    d.desechables,
    d.prop_sustantivas,
    d.mediana_longitud_sustantivas,
    d.decil
FROM deciles d
JOIN preguntas_abiertas pa ON pa.questionid = d."QuestionID"
WHERE d.respuestas >= 50
ORDER BY d."SurveyID", d.decil DESC, d.prop_sustantivas DESC
"""
    
    sql_input_6 = st.text_area("Escribe tu cuarta consulta:", value=query_6, height=250, key="sql_6")
    
    if st.button("Ejecutar Consulta 6", key="btn_6", type="primary"):
        if engine:
            with st.spinner("Ejecutando..."):
                try:
                    query_limitado = f"SELECT * FROM ({sql_input_6}) AS subquery LIMIT 50"
                    with engine.connect() as conn:
                        df = pd.read_sql(text(query_limitado), conn)
                        st.success("Consulta ejecutada con éxito.")
                        st.dataframe(df, use_container_width=True)
                except Exception as e:
                    st.error(f"Error al ejecutar el SQL: {e}")