# "Planteamiento del problema"
""" La salud mental se ha consolidado como una de las principales preocupaciones de la salud publica a nivel mundial. La Organización Mundial de la Salud estima que los trastornos mentales generan pérdidas económicas globales cercanas al billón de dólares anuales por concepto de productividad no realizada, y advierte que aproximadamente el 15% de los trabajadores presenta algún trastorno  de este tipo. Dado que cerca del 60% de la población mundial desarrolla su actividad en un entorno laboral, la salud mental en el trabajo ha dejado de ser un asunto privado hasta el punto de que hoy ocupa un eje central tanto en las organizaciones como en las políticas públicas de empleo a nivel mundial. Desde una perspectiva más específica hacia el sector tecnológico los estudios disponibles documentan una prevalencia de malestar psicológico superior a las otras industrias, asociada a una cultura que normaliza las jornadas prolongadas.

Ahora bien, en este contexto el estigma da lugar a lo que la literatura denomina percepción de perjuicio profesional: la creencia de que divulgar una condición de salud mental tendrá consecuencias negativas en el desarrollo de la carrera.Desde una perspectiva más específica hacia el sector tecnológico los estudios disponibles documentan una prevalencia de malestar psicológico superior a las otras industrias, asociada a una cultura que normaliza las jornadas prolongadas, y con el avance exponencial de la tecnología en los últimos años la constante presión por innovar,  y la exigencia constante de actualización de habilidades. A ello se suma que una amplia mayoría de los empleados percibe estigma en su entorno laboral lo que constituye una barrera formidable para buscar ayuda y agrava el problema de fondo según Rado & Neagu, 2019; Sharma et al., 2018. Esta combinación de alta exigencia y estigma convierte al sector tecnológico en un caso especialmente relevante para el estudio de la salud mental. 

   Ahora bien, en este contexto el estigma da lugar a lo que la literatura denomina percepción de perjuicio profesional: la creencia de que divulgar una condición de salud mental tendrá consecuencias negativas en el desarrollo de la carrera, las oportunidades de ascenso o el estatus dentro de la organización. No obstante, persisten vacíos significativos sobre cómo esta percepción varía según el nivel jerárquico del puesto y el grupo de edad del trabajador. Respecto a la jerarquía, la teoría de demandas-control de Karasek (1979) sugiere que los puestos inferiores, con menor autonomía y control, deberían presentar mayor vulnerabilidad al estrés laboral. Sin embargo, no se ha examinado empíricamente si esa vulnerabilidad se traduce en una mayor percepción de perjuicio profesional por motivos de salud mental, ni si el nivel jerárquico modula esa percepción. 

 En cuanto a la edad, existen indicios de diferencias generacionales y de limitaciones de carrera asociadas a la edad en el sector tecnológico (CWJobs, 2019; Mental Health at Work Report, 2019), pero no se ha examinado si la percepción de perjuicio difiere entre grupos etarios ni cómo interactúa con la jerarquía. Por consiguiente, aunque se sabe que la salud mental es crítica en el sector tecnológico, no se ha establecido empíricamente si la percepción de perjuicio varía según la combinación de ambos factores. De ahí surge la siguiente pregunta: ¿Difiere la percepción de perjuicio profesional por motivos de salud mental según el nivel jerárquico y el grupo de edad en el sector tecnológico? Responderla permitirá identificar los segmentos más vulnerables y diseñar políticas basadas en evidencia. """

# "Objetivo general" 
"Determinar si la percepción de perjuicio profesional por motivos de salud mental difiere según el nivel jerárquico del puesto de trabajo y el grupo de edad del trabajador en el sector tecnológico. 

# "Objetivos específicos"
● "Caracterizar socio-demográficamente a la muestra de trabajadores del sector tecnológico (edad, género, nivel jerárquico y país). 
● "Describir la distribución de la percepción de perjuicio profesional por nivel jerárquico y grupo de edad. 
● "Analizar la relación entre la edad y la percepción de perjuicio dentro de cada nivel jerárquico. 
● "Determinar si existen diferencias significativas en la percepción de perjuicio según el nivel jerárquico y el grupo de edad, y si existe interacción entre ambos factores. "

t.subheader("Limitaciones del Estudio")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 🚨 1. Sesgo de autoselección y representatividad")
        st.markdown("""La recolección de datos se basó en encuestas de participación voluntaria (2016-2019) sin un muestreo probabilístico. 
        Esto genera un sesgo de autoselección, ya que es probable que la muestra sobrerrepresente a individuos con mayor interés o sensibilización hacia la salud mental. 
        Además, la predominancia de participantes de Estados Unidos limita la generalización de los hallazgos al resto de los trabajadores del sector tecnológico a nivel global.""")

with col2:
    with st.container(border=True):
        st.markdown("### 📂 2. Uso de datos secundarios")
        st.markdown("""La investigación emplea la encuesta *OSMI Mental Health in Tech Survey*, diseñada por una organización externa.
        Esto implica que el equipo investigador no tuvo control sobre el diseño del cuestionario, la redacción de las preguntas ni la disponibilidad de las variables (algunas, como el puesto de trabajo, solo se aplicaron en años específicos, como 2016). 
        Asimismo, al tratarse de datos autorreportados, no es posible verificar la veracidad absoluta de las respuestas.""")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.markdown("### ⏳ 3. Diseño transversal")
        st.markdown("""Al tratarse de encuestas transversales, cada medición capta a los individuos en un único momento. " 
        Dado que los participantes varían de un año a otro (no hay un seguimiento longitudinal de los mismos sujetos entre 2016 y 2019), no es posible analizar cambios individuales a lo largo del tiempo ni establecer relaciones de causalidad, 
        limitando los resultados a la identificación de asociaciones estadísticas.""")

with col4:
    with st.container(border=True):
        st.markdown("### 📊 4. Limitaciones de la técnica estadística (ANOVA)")
        st.markdown("""La variable dependiente mide la *percepción* subjetiva de perjuicio, no el perjuicio objetivo o real. 
        "Por otro lado, el ANOVA exige el cumplimiento de supuestos estrictos (normalidad, homogeneidad de varianzas e independencia de las observaciones) 
        "y requiere tratar como numéricas variables que, en algunos casos, son de naturaleza ordinal. Finalmente, el tamaño reducido de la muestra en ciertas combinaciones de nivel jerárquico y grupo de edad limita la potencia estadística del análisis.""")

