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
    if st.button("**Antecedentes y Contexto**", use_container_width=True,):st.session_state.seccion_teorica = "Antecedentes"

with col_btn2:
    if st.button("**Bases y Terminos**", use_container_width=True,): st.session_state.seccion_teorica = "Bases"

with col_btn3:
    if st.button("**Fundamentos del ANOVA**",use_container_width=True,):st.session_state.seccion_teorica = "ANOVA"


if st.session_state.seccion_teorica == "Antecedentes":
    st.header("Antecedentes de la investigación")
    st.subheader("La base OSMI como fuente científica")
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


    st.subheader("Antecedente directo: estudios que emplean la base OSMI")
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

    st.header("Contexto histórico e internacional de la salud mental")
    st.write("A continuación, se presenta la evolución de los derechos laborales, los modelos de estrés y el reconocimiento de la salud mental en el ámbito organizacional.")
    
    st.write("")
    
    tab_c1, tab_c2, tab_c3, tab_c4 = st.tabs([
            "1872 - 1948 ➔", 
            "1979 - 1984 ➔", 
            "1990 - 2006 ➔", 
            "2014 - Hoy"
        ])
        
    with tab_c1:
        with st.container(border=True):
            st.write(
                "La creación de la OMS es un hecho anterior a su constitución el 7 de abril de 1948. "
                "Los programas de seguridad social Von Bismarck sirven de precedente al sistema de bienestar social de Estados Unidos y como antecedente a la constitución "
                "de la Organización Internacional del Trabajo (OIT) en 1919, para reflejar que la justicia social es esencial para alcanzar la paz universal. Esto se complementa "
                "con el Informe de Massachusetts de 1872 y la Ley Williams-Steiger de Seguridad y Salud Ocupacional en 1970.")
    
    with tab_c2:
        with st.container(border=True):
            st.write(
                "Las agencias de la ONU actúan en colaboración en asuntos de interés común, como la salud mental en el trabajo. Para 1979 surge el Modelo Demandas-Control de Karasek, "
                "que describe las demandas psicológicas y el control, dando lugar a estados laborales como la alta tensión (alta demanda + bajo control), trabajo activo, baja tensión y trabajo pasivo. "
                "Este modelo se constituye como fundamento teórico de la OIT y la OMS durante 1984 para definir los factores psicosociales de las enfermedades ocupacionales.")
    
    with tab_c3:
        with st.container(border=True):
            st.write(
                "En paralelo, durante 1990 se aprueba la Ley de Estadounidenses con Discapacidades (ADA), asimilada posteriormente en la Convención sobre los Derechos de las Personas con Discapacidad (CRPD) de 2006. "
                "Para 1996 surge el Modelo Esfuerzo-Recompensa de Siegrist, el cual diferencia dos tipos de esfuerzo: extrínseco (demandas del trabajo) e intrínseco (motivación y sobre-compromiso). Las recompensas que obtienen los trabajadores "
                "pueden ser monetarias, respeto y apoyo, o seguridad en el puesto y promoción.")
    
    with tab_c4:
        with st.container(border=True):
            st.write(
                "Para el año 2014 se registra la iniciativa de la corporación sin fines de lucro Open Sourcing Mental Health (OSMI), creada por Ed Finkler, cuyas encuestas desde 2014 a 2019 sirvieron de base de datos bruta a esta investigación. "
                "Finalmente, la 11.ª revisión de la Clasificación Internacional de Enfermedades (CIE-11) define el agotamiento laboral como un fenómeno ocupacional. De tal manera que queda en evidencia que la salud mental no es una tendencia sino un tema "
                "de interés legítimo y de vanguardia.")

elif st.session_state.seccion_teorica == "Bases": 
    st.header("Bases conceptuales")
    st.subheader("Estrés laboral y salud mental")
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

    st.subheader("Categorías de riesgos psicosociales en el sector IT")
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

    st.subheader("Modelos teóricos del estrés laboral")
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

    st.subheader("Jerarquía organizacional")
    st.markdown("""
    > **La jerarquía organizacional** es la estructura ordenada en la que se distribuyen responsabilidades y el poder dentro de una empresa, facilitando asi la comunicación y la toma de decisiones.
    
    Según Karasek y sus modelos de estres, los puestos de niveles inferiores suelen caracterizarse por una mayor dependencia jerárquica y una supervisión más estrecha. Esta configuración se traduce en una menor latitud de decisión, que se refiere al margen de maniobra que tiene un trabajador para organizar sus tareas y tomar decisiones. Y una mayor exposición a las demandas, lo que hace a los trabajadores operativos potencialmente más vulnerables al estrés y a percibir consecuencias negativas para su carrera.
    """)
    st.divider()

    st.subheader("Confianza hacia el liderazgo")
    st.markdown("""
    > La confianza en el liderazgo actúa como un **mediador crucial** entre el estilo de mandato y el bienestar de los empleados.
    
    El liderazgo transformacional inspira, motiva y desarrolla a los seguidores, fomentando relaciones de confianza. Gracias a Perilla-Toro y Gómez-Ortiz, 2017, podemos decir que este estilo de liderazgo se relaciona positivamente con el bienestar psicológico, teniendo a la confianza en el líder como su principal efecto mediador. Un entorno de seguridad psicológica reduce el miedo a ser estigmatizado.
    """)

    st.divider()

    st.subheader("Percepción del perjuicio profesional")
    st.markdown("""
    > Se cree que es la **creencia de que divulgar una condición de salud mental** tendrá consecuencias negativas en el desarrollo de la carrera, las oportunidades laborales o su estatus dentro de la organización.
    
    Esto se relaciona directamente con el estigma percibido y el miedo a la discriminación. Y su importancia en el sector tecnologico radica en la cultura de alto rendimiento, la competitividad y la presion constante por la innovación. Todos estos factores aumenta el temor a ser percibido como vulnerable, poco productivo o incapaz de soportar la carga. Esto lleva a los trabajadores a ocultar sus condiciones, agravando el como los empleados perciben colectivamente su entorno de trabajo, las políticas de la empresa y las relaciones humanas en el día a día.
    """)
    
    st.divider()
    
    st.header("Definición de términos básicos")
    
    tab_t1, tab_t2, tab_t3, tab_t4 = st.tabs([
        "🧠 Salud y Prejuicio", 
        "🚫 Estigma", 
        "🏢 Jerarquía y Liderazgo", 
        "💻 Edad y Sector"
    ])

    with tab_t1:
        st.markdown("### Salud mental")
        st.write("Se define como el \"estado de bienestar mental que permite a las personas hacer frente a los momentos de estrés de la vida, desarrollar todas sus habilidades, aprender y trabalhar adecuadamente e integrarse en su entorno\". Constituye un valor intrínseco y fundamental de las personas, formando parte esencial del bienestar general.")
        
        st.markdown("### Percepción de prejuicio profesional")
        st.write("Se refiere a los estereotipos sociales sobre las enfermedades mentales que generan actitudes y comportamientos negativos, en ocasiones inconscientes. Incluye el pesimismo terapéutico y el estigma en el entorno laboral (De Angelis, 2024).")

    with tab_t2:
        st.markdown("### Estigma")
        st.write("Suele surgir de una falta de conocimiento o de miedo. En el ámbito de la salud mental, se identifican estos tipos de estigma:")
        st.markdown("- **Estigma público:** Actitudes negativas o discriminatorias que otras personas tienen sobre la enfermedad mental.""- **Autoestigma:** Actitudes negativas que tienen las personas sobre su propia enfermedad mental, incluyendo sentir vergüenza.")
        st.markdown("- **Estigma institucional:** Es sistémico e implica políticas del gobierno y organizaciones que limitan las oportunidades de las personas con enfermedad mental.")
        st.markdown("- **Factores subyacentes:** Miedo/evitación, malevolencia, autoritarismo e imprevisibilidad.")

    with tab_t3:
        st.markdown("### Jerarquía laboral")
        st.write("De acuerdo con la Escuela de Negocios de Madrid, es \"el sistema formal que establece el orden, la subordinación y las líneas de reporte entre los diferentes niveles de autoridad dentro de una organización\". Para efectos de la investigación, se operacionaliza en tres niveles: Directivo, Coordinación y Operativo.")
        
        st.markdown("### Confianza en el liderazgo")
        st.write("Se fundamenta en la premisa de que \"la confianza es el ingrediente más importante para construir un equipo\" (Covey). Nace de dos dimensiones: el carácter y la competencia.")

    with tab_t4:
        st.markdown("### Edad")
        st.write("Se refiere a la edad en años cumplidos, es decir, al número de aniversarios del nacimiento transcurridos hasta la fecha de referencia.")
        
        st.markdown("### Sector tecnológico")
        st.write("""Es el conjunto de actividades económicas y organizaciones dedicadas a la investigación, desarrollo, fabricación, comercialización y prestación de servicios relacionados con la tecnología. 
        Abarca áreas como el desarrollo de software, la infraestructura de hardware, las telecomunicaciones, los servicios de TI (Tecnologías de la Información), la computación en la nube y el análisis de datos. 
        Este sector se caracteriza por su rápido ritmo de innovación, la alta exigencia de actualización técnica, una cultura orientada a resultados y entornos de trabajo altamente competitivos.""")

elif st.session_state.seccion_teorica == "ANOVA":
    st.header("Fundamentos técnicos del ANOVA")
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