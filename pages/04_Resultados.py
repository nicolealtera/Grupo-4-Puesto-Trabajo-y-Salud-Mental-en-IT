import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from styles import PALETA_GRAFICOS

st.image("assets/resultados.png", use_container_width=True)

conn = st.session_state.get("conn")

if conn is None:
    st.error("No hay conexión a la base de datos.")
    st.stop()

def cargar_datos(conexion):
    query = "SELECT * FROM salud_mental"
    df = conexion.execute(query).df()
    
    df = df.rename(columns={
        'generotexto': 'genero',
        'paistexto': 'pais',
        'escala_perjuicio': 'nivel_percepcion_perjuicio',
        'grupo_edad': 'Grupo_Edad'
    })
    return df

try:
    df = cargar_datos(conn)
    df_2016 = df[(df['encuestaID'] == 2016) & (df['nivel_percepcion_perjuicio'].notna())].copy()

except Exception as e:
    st.error(f"Error al consultar la base de datos: {e}")
    st.stop()

if "seccion_resultados" not in st.session_state:
    st.session_state.seccion_resultados = "Resultados Generales"

st.write("") 
st.selectbox("**Explora los resultados de la investigación:**", ["Resultados Generales", "Análisis ANOVA"], key="seccion_resultados")

if st.session_state.seccion_resultados == "Resultados Generales":
    
    # Obj 1
    st.header("1. Caracterización de la muestra")
    st.markdown("Se presenta el perfil sociodemográfico de los trabajadores que conforman la muestra de estudio.")
    total_personas = len(df)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de encuestados", f"{total_personas:,}")
    col2.metric("Nivel Jerárquico más común", df['nivel_jerarquico'].mode()[0])
    col3.metric("Género predominante", df['genero'].mode()[0])
    col4.metric("Edad predominante", df['Grupo_Edad'].mode()[0])

    st.write("")

    col_izq, col_der = st.columns(2)

    with col_izq:
        df_genero = df['genero'].value_counts().reset_index()
        df_genero.columns = ['genero', 'count']
    
        fig_genero = px.pie(
            df_genero, names="genero", values='count', title="Distribución por Género", hole=0.4,
            color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white")
        
        fig_genero.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_genero, use_container_width=True)

    with col_der:
        df_jerarquia = df['nivel_jerarquico'].value_counts().reset_index()
        df_jerarquia.columns = ['nivel_jerarquico', 'count']
    
        fig_jerarquia = px.bar(
            df_jerarquia, x="nivel_jerarquico", y='count', title="Distribución por Nivel Jerárquico",
            labels={'count': "Cantidad", "nivel_jerarquico": "Nivel"},
            color="nivel_jerarquico", color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white")
        
        fig_jerarquia.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis={'categoryorder':'total descending'})
        st.plotly_chart(fig_jerarquia, use_container_width=True)

    st.write("")

    top_paises = df['pais'].value_counts().reset_index().nlargest(5, 'count')
    top_paises.columns = ['pais', 'count']

    fig_pais = px.bar(
        top_paises, x="count", y="pais", orientation='h',title="Top 5 Países de Residencia", labels={"count": "Cantidad de personas", "pais": "País"}, 
        color="pais", color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white")

    fig_pais.update_layout(yaxis={'categoryorder':'total ascending'}, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_pais, use_container_width=True)
    
    # Obj 2
    st.header("2. Distribución de la percepción de perjuicio (Año 2016)")
    st.markdown("Describir la distribución de la percepción de perjuicio profesional por nivel jerárquico y grupo de edad, utilizando la escala compuesta del 2016.")

    col_g1, col_g2 = st.columns(2)

    with col_g1:
        df_perj_jer = df_2016.groupby("nivel_jerarquico", observed=False)["nivel_percepcion_perjuicio"].mean().reset_index()
    
        fig_p_jer = px.bar(
            df_perj_jer, x="nivel_jerarquico", y="nivel_percepcion_perjuicio", title="Nivel Promedio por Jerarquía", 
            labels={"nivel_percepcion_perjuicio": "Nivel Promedio", "nivel_jerarquico": "Nivel"},
            color="nivel_jerarquico", color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white")
    
        fig_p_jer.update_yaxes(range=[1, 4])
        fig_p_jer.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_p_jer, use_container_width=True)

        with st.popover("❓ ¿Qué significa esto?"):
            st.markdown("""
            **Percepción por Jerarquía:**
            *   Los promedios de percepción de perjuicio son muy similares entre los tres niveles (rondando el 2.1 en la escala).
            *   **Interpretación:** Visualmente, no se observan diferencias drásticas, lo que anticipa que el ANOVA podría no encontrar diferencias significativas si la varianza es alta.
            """)

    with col_g2:
        df_perj_edad = df_2016.groupby("Grupo_Edad", observed=False)["nivel_percepcion_perjuicio"].mean().reset_index()
        fig_p_edad = px.line(
            df_perj_edad, x="Grupo_Edad", y="nivel_percepcion_perjuicio", markers=True, title="Nivel Promedio por Edad", 
            labels={"nivel_percepcion_perjuicio": "Nivel Promedio", "Grupo_Edad": "Edad"}, 
            color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white")
    
        fig_p_edad.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_p_edad, use_container_width=True)

        with st.popover("❓ ¿Qué significa esto?"):
            st.markdown("""
            **Tendencia por Edad:**
            *   Se observa cómo varía el promedio de percepción a lo largo de los distintos rangos etarios.
            *   **Interpretación:** Si la línea sube o baja abruptamente, indica que los grupos generacionales (ej. jóvenes vs mayores) experimentan el estigma de manera diferente en el sector tech.
            """)

elif st.session_state.seccion_resultados == "Análisis ANOVA":
    
    #Obj 3
    st.header("3. Relación entre Edad y Jerarquía")
    st.markdown("Analizar visualmente cómo varía la percepción con la edad dentro de cada nivel jerárquico.")

    df_perj_edad_jer = df_2016.groupby(['Grupo_Edad', 'nivel_jerarquico'], observed=False)["nivel_percepcion_perjuicio"].mean().reset_index()
    fig_obj3 = px.line(
        df_perj_edad_jer, x='Grupo_Edad', y='nivel_percepcion_perjuicio', color='nivel_jerarquico',
        markers=True, title='Evolución de la Percepción por Edad y Jerarquía',
        labels={'nivel_percepcion_perjuicio': 'Nivel Promedio', 'Grupo_Edad': 'Edad', 'nivel_jerarquico': 'Jerarquía'},
        color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white"
    )
    fig_obj3.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_obj3, use_container_width=True)

    with st.popover("❓ ¿Qué significa esto?"):
        st.markdown("""
        **Gráfico de Interacción (Edad vs Jerarquía):**
        *   Este gráfico muestra el comportamiento de las tres jerarquías a través de las edades.
        *   **Interpretación:** Si las líneas se mantienen paralelas, la edad afecta por igual a todos. Si se cruzan o van en direcciones opuestas, significa que el efecto de envejecer es distinto dependiendo del puesto de trabajo (Interacción).
        """)