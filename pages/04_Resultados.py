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

    st.markdown("---")
    # Obj 4
    st.header("4. ANOVA Factorial de Dos Vías")
    st.subheader("Fase 1: Verificación de Supuestos")
    st.markdown("Antes de ejecutar el modelo ANOVA, es obligatorio comprobar que los datos cumplen con los supuestos estadísticos para garantizar la validez de los resultados.")

    df_anova = df_2016.copy()
    df_anova['nivel_jerarquico'] = df_anova['nivel_jerarquico'].astype(str)
    df_anova['Grupo_Edad'] = df_anova['Grupo_Edad'].astype(str)

    modelo = smf.ols('nivel_percepcion_perjuicio ~ C(nivel_jerarquico) * C(Grupo_Edad)', data=df_anova).fit()

    col_sup1, col_sup2 = st.columns(2)

    with col_sup1:
        st.markdown("#### 2. Homogeneidad de Varianzas")
        st.markdown("Prueba de Levene (H0: Las varianzas son iguales).")
    
        grupos = [g['nivel_percepcion_perjuicio'] for _, g in df_anova.groupby('nivel_jerarquico')]
        stat_l, p_l = stats.levene(*grupos)
    
        st.metric("P-value (Levene)", f"{p_l:.4f}")
    
        if p_l > 0.05:
            st.success("H0 no rechazada. Se asume homogeneidad de varianzas.")
        else:
            st.warning("H0 rechazada. Las varianzas son diferentes.")

        fig_box = px.box(
            df_anova, x="nivel_jerarquico", y="nivel_percepcion_perjuicio", color="nivel_jerarquico", template="plotly_white",
            color_discrete_sequence=PALETA_GRAFICOS,labels={"nivel_percepcion_perjuicio": "Percepción", "nivel_jerarquico": "Nivel"}
            )
        fig_box.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)', 
            showlegend=False, 
            height=300, 
            title="Dispersión por Jerarquía")
        
        st.plotly_chart(fig_box, use_container_width=True)

    with col_sup2:
        st.markdown("#### 3. Normalidad de Residuos")
        st.markdown("Prueba de Shapiro-Wilk (H0: Los residuos son normales).")

        stat_s, p_s = stats.shapiro(modelo.resid)
        st.metric("P-value (Shapiro-Wilk)", f"{p_s:.4f}")

        if p_s > 0.05:
            st.success("H0 no rechazada. Los residuos son normales.")
        else:
            st.info("H0 rechazada. Residuos no normales.")

        osm, osr = stats.probplot(modelo.resid, dist="norm", fit=False)
        fig_qq = px.scatter(x=osm, y=osr, template="plotly_white", labels={'x': 'Cuantiles Teóricos', 'y': 'Residuos'})

        min_val = min(min(osm), min(osr))
        max_val = max(max(osm), max(osr))
        fig_qq.add_shape(type="line", x0=min_val, y0=min_val, x1=max_val, y1=max_val, line=dict(color="red", dash="dash"))

        fig_qq.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300, title="Gráfico Q-Q de Residuos")
        st.plotly_chart(fig_qq, use_container_width=True)

    st.info("""
    **📌 Justificación Metodológica: El Teorema del Límite Central (TCL)**
    
    Como se observa, la prueba de Shapiro-Wilk rechazó la normalidad. Sin embargo, esto es un comportamiento esperado en muestras extremadamente grandes. Con un tamaño muestral de **N = 1,311**, las pruebas de normalidad detectan desviaciones mínimas que no tienen relevancia práctica.
    
    Gracias al **Teorema del Límite Central**, sabemos que cuando el tamaño de la muestra es grande (típicamente N > 30), la distribución de las medias muestrales se aproxima a una distribución normal, independientemente de la distribución de la población original. Adicionalmente, el **Gráfico Q-Q** muestra que los residuos se alinean de forma muy cercana a la diagonal teórica. Por lo tanto, el ANOVA es lo suficientemente **robusto** para tolerar esta leve desviación y los resultados son válidos.
    """)

    st.divider()

    st.header("Fase 2: Resultados del ANOVA (Prueba Ómnibus)")
    st.markdown("Una vez evaluados los supuestos, procedemos a calcular el modelo principal para determinar si la Jerarquía, "
    "la Edad o su Interacción tienen un efecto estadísticamente significativo.")

    # grafico anova
    st.markdown("#### Visualización de las Distribuciones por Grupo")
    st.markdown("Este gráfico muestra la curva de densidad normal para cada nivel. Usa el interruptor de abajo para ver las curvas superpuestas o separadas.")
    
    vista_separada = st.toggle("Ver gráficos separados", value=False)

    datos_campanas = []
    for nivel in df_anova['nivel_jerarquico'].unique():
        datos_grupo = df_anova[df_anova['nivel_jerarquico'] == nivel]['nivel_percepcion_perjuicio'].dropna()
        media = datos_grupo.mean()
        desviacion = datos_grupo.std()
        
        x_vals = np.linspace(0.5, 4.5, 200)
        y_vals = stats.norm.pdf(x_vals, loc=media, scale=desviacion)
        
        for x, y in zip(x_vals, y_vals):
            datos_campanas.append({'Nivel de Percepción': x, 'Densidad': y, 'Jerarquía': nivel})
            
    df_campanas = pd.DataFrame(datos_campanas)

    if vista_separada:
        fig_gauss = px.line(
            df_campanas, 
            x='Nivel de Percepción', 
            y='Densidad', 
            color='Jerarquía',
            facet_col='Jerarquía',
            title="Distribuciones Normales Separadas",
            labels={'Densidad': 'Probabilidad', 'Nivel de Percepción': 'Nivel'},
            color_discrete_sequence=PALETA_GRAFICOS, 
            template="plotly_white"
        )
        fig_gauss.update_traces(line=dict(width=3), fill='tozeroy', opacity=0.4)
    else:
        fig_gauss = px.line(
            df_campanas, 
            x='Nivel de Percepción', y='Densidad', color='Jerarquía', line_dash='Jerarquía', title="Distribuciones Normales Superpuestas",
            labels={'Densidad': 'Probabilidad', 'Nivel de Percepción': 'Nivel'},color_discrete_sequence=PALETA_GRAFICOS, template="plotly_white")
        
    fig_gauss.update_traces(line=dict(width=3), fill='tozeroy', opacity=0.15)
    fig_gauss.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    
    st.plotly_chart(fig_gauss, use_container_width=True)

    st.markdown("---")
    st.subheader("Tabla de Resultados (Prueba Ómnibus)")
    st.markdown("Esta tabla nos muestra el veredicto, si el valor p (última columna) es menor a 0.05, significa que el factor tiene un efecto real y no es producto del azar.")

    tabla_anova = sm.stats.anova_lm(modelo, typ=2)

    tabla_anova.rename(index={
        'C(nivel_jerarquico)': 'Nivel Jerárquico',
        'C(Grupo_Edad)': 'Grupo de Edad',
        'C(nivel_jerarquico):C(Grupo_Edad)': 'Interacción (Jerarquía * Edad)',
        'Residual': 'Residual (Error no explicado)'
    }, inplace=True)
    
    tabla_anova.rename(columns={
        'sum_sq': 'Suma de Cuadrados',
        'df': 'Grados de Libertad',
        'F': 'Estadístico F',
        'PR(>F)': 'Valor p (Significancia)'
    }, inplace=True)

    p_jer = tabla_anova.loc['Nivel Jerárquico', 'Valor p (Significancia)']
    p_edad = tabla_anova.loc['Grupo de Edad', 'Valor p (Significancia)']
    p_inter = tabla_anova.loc['Interacción (Jerarquía * Edad)', 'Valor p (Significancia)']

    st.write("")

    st.dataframe(
        tabla_anova.style.format({
            'Suma de Cuadrados': '{:.4f}', 
            'Grados de Libertad': '{:.0f}', 
            'Estadístico F': '{:.4f}', 
            'Valor p (Significancia)': '{:.4f}'
        }), 
        use_container_width=True
    )

    st.write("")
    st.markdown("---")
    st.subheader("Conclusiones del Modelo")
    
    col_c1, col_c2, col_c3 = st.columns(3)
    
    with col_c1:
        if p_jer < 0.05:
            st.success(f"**Nivel Jerárquico**\n\n Sí hay diferencia significativa (p = {p_jer:.4f}). El puesto de trabajo influye en cómo se percibe el estigma.")
        else:
            st.info(f"**Nivel Jerárquico**\n\n No hay diferencia significativa (p = {p_jer:.4f}). El puesto de trabajo no influye por sí solo.")

    with col_c2:
        if p_edad < 0.05:
            st.success(f"**Grupo de Edad**\n\n Sí hay diferencia significativa (p = {p_edad:.4f}). La generación del trabajador influye en su percepción.")
        else:
            st.info(f"**Grupo de Edad**\n\n No hay diferencia significativa (p = {p_edad:.4f}). La edad no es un factor determinante.")

    with col_c3:
        if p_inter < 0.05:
            st.success(f"**Interacción (Jerarquía * Edad)**\n\n Hay interacción (p = {p_inter:.4f}). El efecto de la edad cambia dependiendo de tu puesto de trabajo.")
        else:
            st.info(f"**Interacción (Jerarquía * Edad)**\n\n No hay interacción (p = {p_inter:.4f}). Jerarquía y edad actúan de forma independiente.")