import streamlit as st
import base64
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="Conclusiones", page_icon="✅", layout="wide")

if "seccion_conclusiones" not in st.session_state:
    st.session_state.seccion_conclusiones = "📌 Conclusiones"
if st.session_state.seccion_conclusiones == "📌 Conclusiones":
    st.image("assets/Conclusiones.png", use_container_width=True) 
elif st.session_state.seccion_conclusiones == "💡 Recomendaciones":
    st.image("assets/Recomendaciones.png", use_container_width=True)

st.write("") 

st.selectbox(
    "**Explora por los resultados finales:**",
    ["📌 Conclusiones", "💡 Recomendaciones"],
    key="seccion_conclusiones"
)

st.divider()


@st.cache_data
def a_base64(ruta: str, mime: str) -> str:
    try:
        data = Path(ruta).read_bytes()
        return f"data:{mime};base64," + base64.b64encode(data).decode()
    except FileNotFoundError:
        return ""

if st.session_state.seccion_conclusiones == "📌 Conclusiones":
    
    st.markdown("### Resumen de los resultados")
    st.write("Basados en el análisis descriptivo y el modelo ANOVA factorial de dos vías sobre la muestra de 1.311 trabajadores (OSMI 2016), llegamos a las siguientes conclusiones:")
    st.markdown("""
    <div style="background-color: rgba(132, 179, 206, 0.15); border-left: 8px solid #17597C; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #17597C; margin-top: 0;"> El hallazgo principal: La Jerarquía importa</h3>
        <p style="font-size: 1.1rem; margin-bottom: 0;">
            Rechazamos la Hipótesis Nula (<b>p = 0,0168</b>). El nivel jerárquico sí influye en cómo se percibe el estigma. 
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("""
    **¿Qué significa esto?** 
    Se valida empíricamente la **Teoría de Demandas-Control de Karasek (1979)**. Los trabajadores en niveles operativos, al tener menos autonomía y control sobre su trabajo, se sienten más vulnerables a las consecuencias negativas (represalias o estigma) de hablar sobre su salud mental.
    """)

    st.write("")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("#### El factor Edad")
            st.info("**No significativo (p = 0,4658)**")
            st.write("""
            La edad por sí sola no determina el miedo al estigma. Los jóvenes de 18-24 años y los adultos de 55+ perciben el perjuicio de manera muy similar. 
            *El estigma es transversal a las generaciones.*
            """)
            
    with col2:
        with st.container(border=True):
            st.markdown("#### La Interacción")
            st.info("**No significativa (p = 0,9679)**")
            st.write("""
            No existe un efecto combinado entre jerarquía y edad. Ser joven y operativo no genera un "doble castigo". Los factores actúan de forma independiente en la organización.
            """)

    st.divider()
    
    st.markdown("### El panorama general")
    st.markdown("""
    *   **El estigma es estructural:** El miedo al perjuicio profesional no es un problema individual o generacional, sino una consecuencia directa de cómo están diseñadas las jerarquías en la industria tecnológica.
    *   **Una cultura de alta exigencia:** La muestra analizada refleja una industria joven (25-34 años), mayoritariamente masculina y operativa, que siente una presión constante que afecta su percepción de seguridad laboral.
    """)

elif st.session_state.seccion_conclusiones == "💡 Recomendaciones":
    
    st.markdown("### Propuestas de acción")
    st.write("A partir de los hallazgos obtenidos, se plantean dos líneas de acción concretas:")
    
    st.write("")
    
    col_emp, col_acad = st.columns(2)
    
    with col_emp:
        with st.container(border=True):
            st.markdown("### 🏢 Para las Empresas Tech")
            st.markdown("""
            1. **Políticas focalizadas en lo operativo:** Dado que este grupo es el más vulnerable, los programas de bienestar y las campañas de salud mental deben diseñarse pensando en las demandas específicas de los desarrolladores, diseñadores y soporte técnico.
            
            2. **Canales de ayuda anónimos:** Para combatir el miedo al perjuicio, las empresas deben implementar líneas de apoyo psicológico externas, donde el trabajador no tenga que rendir cuentas ante su jefe directo ni arriesgar su carrera.
            
            3. **Formación de líderes:** Capacitar a los mandos medios para que ejerzan un *liderazgo transformacional*. Un líder que genera confianza reduce significativamente el estrés y la percepción de estigma en su equipo.
            """)
            
    with col_acad:
        with st.container(border=True):
            st.markdown("### 🎓 Para Futuras Investigaciones")
            st.markdown("""
            1. **Expandir la muestra a Latinoamérica:** La base OSMI tiene un fuerte sesgo hacia Estados Unidos. Replicar este modelo con datos de nuestra región es crucial para entender si los factores culturales cambian los resultados.
            
            2. **Estudios longitudinales:** Al ser un estudio transversal, solo vemos una foto del momento. Un estudio que siga a los trabajadores en el tiempo podría revelar si el miedo al estigma cambia cuando un trabajador asciende de puesto.
            
            3. **Enfoque cualitativo:** Complementar el análisis numérico con entrevistas a profundidad. ¿Qué palabras exactas usan los operativos cuando temen hablar? El dato duro ya está, ahora toca conocer las historias.
            """)

    st.write("")
    st.success("**Conclusión Final:** La salud mental en el sector IT no es un tema de jóvenes, es un tema de poder y estructura organizacional. Humanizar el trabajo es el primer paso para retener el talento.")