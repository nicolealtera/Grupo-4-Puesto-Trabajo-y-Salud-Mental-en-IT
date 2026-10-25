import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from styles import PALETA_GRAFICOS

st.image("assets/resultados.png", use_container_width=True)

conn = st.session_state.get("conn")

if conn is None:
    st.error("No hay conexión a la base de datos.")
    st.stop()

def cargar_datos(conexion):
    query = """
        SELECT 
            p.edad, 
            p.generotexto AS genero, 
            t.nivel_jerarquico, 
            u.paistexto AS pais, 
            h.crees_te_verian_mal AS percepcion_perjuicio,
            COUNT(*) as cantidad
        FROM HECHOS h
        JOIN DIM_PARTICIPANTE p ON h.participanteID = p.participanteID
        JOIN DIM_TRABAJO t ON h.puesto_trabajoID = t.puesto_trabajoID
        JOIN DIM_UBICACION u ON h.ubicacionID = u.ubicacionID
        WHERE h.crees_te_verian_mal IS NOT NULL
        GROUP BY 1, 2, 3, 4, 5
    """
    df = conexion.execute(query).df()
    
    df['Grupo_Edad'] = pd.cut(
        df['edad'], 
        bins=[17, 24, 34, 44, 54, 100], 
        labels=['18-24', '25-34', '35-44', '45-54', '55+']
    )

    escala_percepcion_perjuicio = {
        "Yes, I think they would": 1.0,
        "Yes, they do": 1.0,
        "Maybe": 0.5,
        "No, I don't think they would": 0.0,
        "No, they do not": 0.0
    }
    
    df["nivel_percepcion_perjuicio"] = df["percepcion_perjuicio"].map(escala_percepcion_perjuicio)
    
    return df

try:
    df = cargar_datos(conn)
except Exception as e:
    st.error(f"Error al consultar la base de datos: {e}")
    st.stop()

st.markdown("---")

# Obj 1
st.header("1. Caracterización de la muestra")
st.markdown("se presenta el perfil sociodemográfico de los trabajadores que conforman la muestra de estudio.")

total_personas = df["cantidad"].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de encuestados", f"{total_personas:,}")
col2.metric("Nivel Jerárquico más común", df['nivel_jerarquico'].mode()[0])
col3.metric("Género predominante", df['genero'].mode()[0])
col4.metric("Grupo de edad predominante", df['Grupo_Edad'].mode()[0])

st.write("")

col_izq, col_der = st.columns(2)

with col_izq:
    df_genero = df.groupby("genero")["cantidad"].sum().reset_index()
    fig_genero = px.pie(
        df_genero, names="genero", values="cantidad", title="Distribución por Género", hole=0.4,
        color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white"
    )
    fig_genero.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_genero, use_container_width=True)

with col_der:
    df_jerarquia = df.groupby("nivel_jerarquico")["cantidad"].sum().reset_index()
    fig_jerarquia = px.bar(
        df_jerarquia, x="nivel_jerarquico", y="cantidad", title="Distribución por Nivel Jerárquico",
        labels={"cantidad": "Cantidad", "nivel_jerarquico": "Nivel"},
        color="nivel_jerarquico", color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white"
    )
    fig_jerarquia.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_jerarquia, use_container_width=True)

col_izq2, col_der2 = st.columns(2)

with col_izq2:
    df_edad = df.groupby("Grupo_Edad", observed=False)["cantidad"].sum().reset_index()
    fig_edad = px.bar(
        df_edad, x="Grupo_Edad", y="cantidad", title="Distribución por Grupo de Edad",
        labels={"cantidad": "Cantidad", "Grupo_Edad": "Edad"},
        color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white"
    )
    fig_edad.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_edad, use_container_width=True)

with col_der2:
    top_paises = df.groupby("pais")["cantidad"].sum().reset_index().nlargest(5, "cantidad")
    fig_pais = px.bar(
        top_paises, x="pais", y="cantidad", title="Top 5 Países de Residencia",
        labels={"cantidad": "Cantidad", "pais": "País"},
        color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white"
    )
    fig_pais.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_pais, use_container_width=True)

# Obj 2

st.header("2. Distribución de la percepción de perjuicio")
st.markdown("Describir la distribución de la percepción de perjuicio profesional por nivel jerárquico y grupo de edad.")

col_g1, col_g2 = st.columns(2)

with col_g1:
    df_perj_jer = df.groupby("nivel_jerarquico").apply(
        lambda x: (x["nivel_percepcion_perjuicio"] * x["cantidad"]).sum() / x["cantidad"].sum()
    ).reset_index(name="promedio")
    
    fig_p_jer = px.bar(
        df_perj_jer, x="nivel_jerarquico", y="promedio", 
        title="Nivel Promedio por Jerarquía",
        labels={"promedio": "Nivel Promedio (0 a 1)", "nivel_jerarquico": "Nivel"},
        color="nivel_jerarquico", color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white"
    )
    fig_p_jer.update_yaxes(range=[0, 1])
    fig_p_jer.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_p_jer, use_container_width=True)

with col_g2:
    df_perj_edad = df.groupby("Grupo_Edad", observed=False).apply(
        lambda x: (x["nivel_percepcion_perjuicio"] * x["cantidad"]).sum() / x["cantidad"].sum()
    ).reset_index(name="promedio")
    
    fig_p_edad = px.line(
        df_perj_edad, x="Grupo_Edad", y="promedio", markers=True,
        title="Nivel Promedio por Edad",
        labels={"promedio": "Nivel Promedio (0 a 1)", "Grupo_Edad": "Edad"},
        color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white"
    )
    fig_p_edad.update_yaxes(range=[0, 1])
    fig_p_edad.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_p_edad, use_container_width=True)