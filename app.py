import streamlit as st   
import os
import duckdb
from dotenv import load_dotenv
from styles import load_css

st.set_page_config(page_title="Salud mental en IT", page_icon="🧠", layout="wide")
load_css()

inicio        = st.Page("pages/00_Inicio.py",             title="Inicio",             icon="🏠", default=True)
planteamiento = st.Page("pages/01_Planteamiento.py",      title="Planteamiento",      icon="🔍")                
marco_teorico = st.Page("pages/02_Marco_Teorico.py",      title="Marco Teórico",      icon="📚")
marco_metodo  = st.Page("pages/03_Marco_Metodologico.py", title="Marco Metodológico", icon="🧪")
resultados    = st.Page("pages/04_Resultados.py",         title="Resultados",         icon="📊")
cuestionario  = st.Page("pages/05_Cuestionario_SQL.py",   title="Cuestionario SQL",   icon="🗄️")
conclusiones  = st.Page("pages/06_Conclusiones.py",       title="Conclusiones",       icon="✅")

pg = st.navigation(
    [inicio, planteamiento, marco_teorico, marco_metodo, resultados, cuestionario, conclusiones],
    position="hidden",
)

def boton(pagina, n):
    activo = "-activo" if pagina.title == pg.title else ""
    with st.container(key=f"btn-{n}{activo}"):
        st.page_link(pagina)

with st.sidebar:
    st.markdown("## 🧠 Salud mental en IT")
    st.caption("Percepción de perjuicio profesional · Sector tecnológico")
    st.write("")

    boton(inicio, 0)                     
    st.write("")

    st.caption("**INVESTIGACIÓN**")
    boton(planteamiento, 1)
    boton(marco_teorico, 2)
    boton(marco_metodo,  3)

    st.write("")
    st.caption("**ANÁLISIS**")
    boton(resultados, 4)
    boton(cuestionario, 5)
    boton(conclusiones, 6)

    st.write("")
    with st.expander("📎 Equipo", expanded=False):
        st.write("")
        for n in ["Nicole Altera", "Danmara Dos Ramos",
                "Camila Santiago", "Sebastian Soto"]:
            st.write(n)

load_dotenv()

token = os.getenv("motherduck_token")

conn = duckdb.connect("md:puesto de trabajo y salud mental")