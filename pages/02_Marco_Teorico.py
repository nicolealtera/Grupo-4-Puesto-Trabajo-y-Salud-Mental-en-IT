import streamlit as st

st.set_page_config(
    page_title="Marco Teórico",
    page_icon="📚",
    layout="wide",
)

st.image("assets/marco teorico.png", use_container_width=True)
if "seccion_teorica" not in st.session_state:
    st.session_state.seccion_teorica = "Antecedentes"

st.write("Selecciona una categoría a continuación para comenzar a navegar por el contenido:")

col_btn1, col_btn2, col_btn3 = st.columns(3)
with col_btn1:
    if st.button("**1. Antecedentes**", use_container_width=True,):st.session_state.seccion_teorica = "Antecedentes"

with col_btn2:
    if st.button("**2. Bases Conceptuales**", use_container_width=True,): st.session_state.seccion_teorica = "Bases"

with col_btn3:
    if st.button("**3. Fundamentos del ANOVA**",use_container_width=True,):st.session_state.seccion_teorica = "ANOVA"


if st.session_state.seccion_teorica == "Antecedentes":
    st.header("1. Antecedentes de la investigación")
    st.subheader("1.1. La base OSMI como fuente científica")
    st.markdown("""
    La **Open Sourcing Mental Illness (OSMI) Mental Health in Tech Survey** es una de las principales
    fuentes de datos de autorreporte sobre salud mental en el sector tecnológico. Creada por la organización
    sin fines de lucro **OSMI**, su objetivo es evaluar la prevalencia de problemas de salud mental entre
    los profesionales de la tecnología y sus actitudes hacia estos en el lugar de trabajo.

    La base se estructura en torno a preguntas sobre: diagnóstico, tratamiento, estigma percibido,
    apoyo del empleador, confianza en la alta dirección y miedo a consecuencias profesionales. Su naturaleza
    estructurada y de acceso abierto se ha convertido en un recurso ampliamente utilizado en la literatura académica.
    Para que un registro sea incluido, el encuestado debe pertenecer al sector tecnológico o desempeñar un rol
    técnico, lo que garantiza la homogeneidad de la población objetivo. El producto resultante, miles de registros
    que abarcan múltiples ediciones, es hoy una de las fuentes de referencia para el estudio cuantitativo de la
    salud mental en el sector tecnológico.
    """)


    st.subheader("1.2. Antecedente directo: estudios que emplean la base OSMI")
    st.markdown("""
       Diversos trabajos han utilizado la encuesta **OSMI** para el análisis cuantitativo de la salud mental
    en el sector tecnológico. **Rado y Neagu (2019)** emplearon la encuesta para predecir la probabilidad
    de que un individuo buscara tratamiento de salud mental, utilizando modelos que iban desde árboles de
    decisión hasta redes neuronales. **Sharma et al. (2018)** aplicaron técnicas de clasificación en el ámbito
    sanitario, demostrando la utilidad del conjunto de datos para la investigación predictiva. **Reddy, Thota y Dharun (2018)**
    usaron los datos para predecir si un empleado había recibido tratamiento por trastornos de salud mental.


    Estos trabajos comparten un enfoque predictivo y se centran en la variable de búsqueda de tratamiento.
    La presente investigación se diferencia en dos aspectos: primero, adopta un enfoque descriptivo-inferencial
    en lugar de predictivo; segundo, se centra en la percepción de perjuicio profesional como variable dependiente,
    y en el nivel jerárquico y el grupo de edad como factores independientes, una combinación que no ha sido
    examinada sistemáticamente en la literatura existente.
    """)


elif st.session_state.seccion_teorica == "Bases": 
    st.header("2. Bases conceptuales")
    st.subheader("2.1. Estrés laboral y salud mental")
    st.markdown("""
        El **estrés laboral** es un factor de riesgo crónico de carácter psicosocial que afecta la 
        salud de los trabajadores a través de reacciones emocionales, cognitivas y fisiológicas
        intensas (Gongil, s/a). La **salud mental**, por su parte, va más allá de la ausencia de
        trastornos; implica la capacidad de aprender, trabajar eficazmente y contribuir en las
        organizaciones. Cuando el estrés laboral se vuelve patológico, puede derivar en
        presentismo, absentismo, rotación de personal y un deterioro significativo de la calidad
        de vida (NIH, s/a).

        De acuerdo con López, Solano, Arias et al. (2012), el trabajo es un **determinante social**
        de la salud mental. Un trabajo significativo protege y favorece la recuperación, mientras
        que las condiciones laborales deficientes, los entornos peligrosos y las relaciones
        laborales negativas contribuyen al deterioro de la salud mental o exacerban afecciones
        preexistentes.
        """)

    st.subheader("2.2. Categorías de riesgos psicosociales en el sector IT")
    st.markdown("""
    Con base en las *Directrices de la Organización Mundial de la Salud* (en adelante OMS)
    sobre salud mental en el trabajo, se identifican varias categorías de riesgos psicosociales
    especialmente relevantes para el sector tecnológico (IT). Entre las más comunes destacan:


   - **Carga de trabajo y ritmo:** altos niveles de presión de tiempo y sujeción continua a plazos de entrega.
   - **Control:** baja participación en la toma de decisiones y falta de control sobre la carga y el ritmo de trabajo.
   - **Cultura y funcionamiento organizacional:** mala comunicación, bajos niveles de apoyo para la resolución de problemas y burocracias complejas.
   - **Relaciones interpersonales:** aislamiento social, malas relaciones con los superiores y falta de apoyo social.
   - **Desarrollo profesional:** estancamiento, incertidumbre profesional e inseguridad laboral.
   - **Interfaz hogar–trabajo:** exigencias contradictorias entre el trabajo y el hogar, poco apoyo en las responsabilidades de cuidado.
    """)

    st.subheader("2.3. Modelos teóricos del estrés laboral")
    st.markdown("""
    Los modelos teóricos que explican el estrés laboral consideran factores psicosociales
    como las exigencias psicológicas, el control sobre el contenido del trabajo y el apoyo
    social dentro de la organización. A continuación, se presentan los principales modelos
    que sustentan esta investigación.
    """)


    with st.expander("**a. Modelo de la Valoración de Lazarus**", expanded=False):
        st.markdown("""
            Propuesto por Richard S. Lazarus, este modelo **cognitivo-praxiológico** sostiene que
            las emociones no son causadas directamente por las situaciones, sino por la
            interpretación cognitiva (evaluación) que hace el individuo de ellas. El modelo
            distingue dos etapas:


           - **Evaluación primaria:** el individuo determina si el evento es irrelevante, benigno
            o potencialmente perjudicial (amenaza, desafío o pérdida).
           - **Evaluación secundaria:** la persona valora si dispone de recursos (apoyo social,
            experiencia, competencias) para enfrentar la situación.


            Aplicado al sector IT, un programador o analista de datos no reacciona ante un plazo
            de entrega por la fecha límite en sí, sino por cómo interpreta esa exigencia en función
            de sus objetivos, experiencias previas y recursos disponibles.
            """)


    with st.expander("**b. Modelo Demandas-Control de Karasek (1979)**", expanded=True):
        st.markdown("""
        Este es el **modelo más apropiado para el análisis de la base de datos de esta
        investigación**. Explica el estrés laboral a partir de la relación entre las
        **demandas laborales** (lo que se requiere del trabajador) y el **control** que este
        puede ejercer sobre su trabajo (autonomía y desarrollo de habilidades).

        El modelo es **subjetivo**, ya que se basa en la percepción o autodiagnóstico de los
        trabajadores, y ha sido ampliamente utilizado para explicar depresión, ansiedad,
        percepción de estrés, accidentes laborales y bajas por enfermedad. Los puestos con
        altas demandas y bajo control (*trabajos de alta tensión*) presentan el mayor riesgo
        para la salud del trabajador, lo que conecta directamente con la vulnerabilidad de
        los niveles jerárquicos inferiores.
        """)
    with st.expander("**c. Modelo Demandas-Control-Apoyo (JDC-S) de Johnson y Hall (1988)**"):
        st.markdown("""
        Es una ampliación del modelo de Karasek que incorpora el **apoyo social** como una
        tercera dimensión. Según este modelo, el apoyo social (de superiores y colegas) puede
        amortiguar los efectos negativos de las altas demandas y el bajo control, reduciendo
        el riesgo de enfermedad.
        """)

    with st.expander("**d. Modelo del Desequilibrio Esfuerzo-Recompensa de Siegrist**"):
        st.markdown("""
        Este modelo supone que el esfuerzo en el trabajo es parte de un **contrato fundamentado
        en el principio de reciprocidad**. El trabajador recibe un pago por sus esfuerzos
        laborales en forma de dinero, estima y/o seguridad social y laboral. Dicho intercambio
        representa una relación asimétrica de poder donde el trabajador es la parte más débil.


        Cuando existe un desequilibrio entre el alto esfuerzo y las bajas recompensas, se
        genera estrés ocupacional, lo que permite interpretar la percepción de perjuicio
        profesional como una forma de **recompensa negativa** (estima y oportunidades de
        promoción).
        """)

elif st.session_state.seccion_teorica == "ANOVA":
    st.header("2.4. Fundamentos técnicos del ANOVA")
    st.write(
        "El Análisis de Varianza (ANOVA) es una herramienta estadística de modelado lineal "
        "que permite evaluar si los valores esperados de dos o más grupos son estadísticamente iguales."
    )

    tab_anova_1, tab_anova_2, tab_anova_3 = st.tabs([
        "📊 Lógica y Estadístico F", 
        "📖 Terminología y Variantes", 
        "🔍 Supuestos del Modelo"
    ])

    with tab_anova_1:
        st.markdown("### ¿Cómo funciona el ANOVA?")
        st.markdown(
            "El ANOVA estima la proporción de la variación observada atribuible al factor en estudio y la compara con la variación "
            "no explicada o residual. Aunque se suele aplicar para tres o más grupos, también es posible utilizarlo para dos."
        )

        st.markdown("Para contrastar las medias, compara dos estimaciones de variabilidad:")

        col_var1, col_var2 = st.columns(2)
        with col_var1:
            st.info("**Variación entre grupos**\n\nRefleja la variabilidad asociada a las diferencias entre las medias de cada grupo.")
        with col_var2:
            st.info("**Variación dentro de los grupos**\n\nMide la dispersión entre las observaciones respecto a la media de su propio grupo.")

        st.markdown("### Interpretación del Estadístico F")
        st.markdown(
            "- **Si las medias son iguales:** Los cuadrados medios entre y dentro de los grupos estiman "
            "aproximadamente la misma varianza de error, produciendo un **estadístico F cercano al valor de 1**.\n"
            "- **Si las medias difieren:** La estimación entre grupos aumenta, generando un **estadístico F mayor**, "
            "lo que aporta evidencia sólida para rechazar la hipótesis nula de medias iguales."
        )

    with tab_anova_2:
        st.markdown("### Terminología esencial de ANOVA")

        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown(
                "- **Factor:** Variable explicativa categórica.\n"
                "- **Nivel de factor:** Cada categoría que compone un factor.\n"
                "- **Variable de respuesta:** Medida cuantitativa analizada (dependiente).\n"
                "- **Efecto principal:** Asociación media entre un factor y la respuesta."
            )
        with col_t2:
            st.markdown(
                "- **Efecto de interacción:** Ocurre cuando la relación depende del nivel de otro factor.\n"
                "- **Residual:** Diferencia entre un valor observado y el valor predicho.\n"
                "- **Prueba ómnibus:** Evalúa si existen diferencias globales significativas entre múltiples grupos."
            )

        st.markdown("### Variantes principales del ANOVA")
        st.markdown(
            "- **ANOVA Unidireccional:** Examina un único factor categórico y un resultado cuantitativo.\n"
            "- **ANOVA Bidireccional y Factorial:** Incorpora dos o más factores de manera simultánea para revelar interacciones.\n"
            "- **Otras variantes:** El ANOVA de medidas repetidas, el ANOVA mixto o el ANOVA de Welch."
        )

    with tab_anova_3:
        st.markdown("### Supuestos para la validez del ANOVA")
        st.write("Para que los resultados sean válidos, deben cumplirse rigurosamente los siguientes supuestos:")

        with st.expander("📌 1. Independencia de observaciones"):
            st.write(
                "Las mediciones deben ser independientes entre sí, a menos que el modelo represente "
                "explícitamente datos repetidos, emparejados o jerárquicos. La independencia está determinada "
                "por el diseño de la investigación y el proceso de recopilación de datos."
            )

        with st.expander("📌 2. Normalidad de los residuos (Prueba de Shapiro-Wilk)"):
            st.write(
                "Los residuos del modelo deben seguir una distribución aproximadamente normal. "
                "Para su verificación formal se aplica la **prueba de Shapiro-Wilk (1965)**:"
            )
            
            col_h1, col_h2 = st.columns(2)
            with col_h1:
                st.error("**Hipótesis Nula (H0):**\n\n Los datos provienen de una población con distribución normal.")
            with col_h2:
                st.success("**Hipótesis Alternativa (H1):**\n\n Los datos no provienen de una población normal.")

            st.warning(
                "⚠️ **Nota práctica:** No debe usarse como un pase directo automático; en muestras pequeñas "
                "tiene poca potencia, y con muestras muy grandes puede detectar desviaciones sin consecuencias prácticas."
            )

        with st.expander("📌 3. Homogeneidad de varianzas (Prueba de Levene)"):
            st.write(
                "El ANOVA clásico asume que la varianza del error es constante e igual entre los grupos. "
                "Se evalúa formalmente mediante la **prueba de Levene**:"
            )
            
            col_l1, col_l2 = st.columns(2)
            with col_l1:
                st.error("**Hipótesis Nula (H0):**\n\n Los grupos tienen varianzas iguales.")
            with col_l2:
                st.success("**Hipótesis Alternativa (H1):**\n\n Los grupos tienen varianzas diferentes.")

        with st.expander("📌 4. Ausencia de observaciones altamente influyentes"):
            st.write(
                "El ANOVA se basa en desviaciones al cuadrado, por lo que se debe comprobar que el modelo "
                "no esté sesgado por valores extremos (*outliers*), ya que pueden alterar fuertemente las medias, las sumas de cuadrados y "
                "la estadística F. Cualquier exclusión debe documentarse de forma transparente."
            )