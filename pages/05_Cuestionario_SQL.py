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
SELECT * FROM answer LIMIT 5;
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
SELECT * FROM answer LIMIT 5;
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
SELECT * FROM answer LIMIT 5;
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