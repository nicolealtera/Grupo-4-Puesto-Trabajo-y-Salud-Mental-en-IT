import streamlit as st
st.markdown("""
## 1. Antecedentes de la investigación 

### 1.1. La base OSMI como fuente científica 


La **Open Sourcing Mental Illness (OSMI) Mental Health in Tech Survey** es una de las principales fuentes de datos de autorreporte sobre salud mental en el sector tecnológico. Creada por la organización sin fines de lucro **OSMI**, su objetivo es evaluar la prevalencia de problemas de salud mental entre los profesionales de la tecnología y sus actitudes hacia estos en el lugar de trabajo. 

La base se estructura en torno a preguntas sobre: diagnóstico, tratamiento, estigma percibido, apoyo del empleador, confianza en la alta dirección y miedo a consecuencias profesionales. Su naturaleza estructurada y de acceso abierto la se ha convertido en un recurso ampliamente utilizado en la literatura académica. Para que un registro sea incluido, el encuestado debe pertenecer al sector tecnológico o desempeñar un rol técnico, lo que garantiza la homogeneidad de la poblacion objetivo. El producto resultante, miles de registros que abarcan múltiples ediciones, es hoy una de las fuentes de referencia para el estudio cuantitativo de la salud mental en el sector tecnológico. 

---

### 1.2. Antecedente directo: estudios que emplean la base OSMI

Diversos trabajos han utilizado la encuesta **OSMI** para el análisis cuantitativo de la salud mental en el sector tecnológico. **Rado y Neagu (2019)** emplearon la encuesta  para predecir la probabilidad de que un individuo buscara tratamiento de salud mental, utilizando modelos que iban desde árboles de decisión hasta redes neuronales.  **Sharma et al. (2018)** aplicaron técnicas de clasificación en el ámbito sanitario, demostrando la utilidad del conjunto de datos para la investigación predictiva. **Reddy, Thota y Dharun (2018)** usaron los datos para predecir si un empleado había recibido tratamiento por trastornos de salud mental. 

Estos trabajos comparten un enfoque predictivo y se centran en la variable de búsqueda de tratamiento. La presente investigación se diferencia en dos aspectos: primero, adopta un enfoque descriptivo-inferencial en lugar de predictivo; segundo, se centra en la percepción de perjuicio profesional como variable dependiente, y en el nivel jerárquico y el grupo de edad como factores independientes, una combinación que no ha sido examinada sistemáticamente en la literatura existente. """)

st.header.2. Bases conceptuales
st.subheader("2.1. Estrés laboral y salud mental")
st.markdown("""
El estrés laboral es un factor de riesgo crónico de carácter psicosocial que afecta la salud de
los trabajadores a través de reacciones emocionales, cognitivas y fisiológicas intensas (Gongil,
s/a). La salud mental, por su parte, va más allá de la ausencia de trastornos; implica la
capacidad de aprender, trabajar eficazmente y contribuir en las organizaciones. Cuando el
estrés laboral se vuelve patológico, puede derivar en presentismo, absentismo, rotación de
personal y un deterioro significativo de la calidad de vida (NIH, s/a).
De acuerdo con López, Solano, Arias et al. (2012), el trabajo es un determinante social de la
salud mental. Un trabajo significativo protege y favorece la recuperación, mientras que las
condiciones laborales deficientes, los entornos peligrosos y las relaciones laborales negativas
contribuyen al deterioro de la salud mental o exacerban afecciones preexistentes.
""")
st.subheader("2.2. Categorías de riesgos psicosociales en el sector IT")
st.markdown("""
Con base en las Directrices de la Organización Mundial de la Saludm en adelante OMS, sobre salud mental en el trabajo, se identifican varias
categorías de riesgos psicosociales especialmente relevantes para el sector tecnológico (IT).
Entre las más comunes destacan:
● Carga de trabajo y ritmo: altos niveles de presión de tiempo y sujeción continua a plazos
de entrega.
● Control: baja participación en la toma de decisiones y falta de control sobre la carga y el
ritmo de trabajo.
● Cultura y funcionamiento organizacional: mala comunicación, bajos niveles de apoyo
para la resolución de problemas y burocracias complejas.
● Relaciones interpersonales: aislamiento social, malas relaciones con los superiores y
falta de apoyo social.
● Desarrollo profesional: estancamiento, incertidumbre profesional e inseguridad laboral.
Interfaz hogar-trabajo: exigencias contradictorias entre el trabajo y el hogar, poco apoyo en las
responsabilidades de cuidado.
""")
st.subheader("2.3. Modelos teóricos del estrés laboral")
st.markdown("""
Los modelos teóricos que explican el estrés laboral consideran factores psicosociales como las
exigencias psicológicas, el control sobre el contenido del trabajo y el apoyo social dentro de la
organización. A continuación, se presentan los principales modelos que sustentan esta
investigación.

a. Modelo de la Valoración de Lazarus
Propuesto por Richard S. Lazarus, este modelo cognitivo-praxiológico sostiene que las
emociones no son causadas directamente por las situaciones, sino por la interpretación
cognitiva (evaluación) que hace el individuo de ellas. El modelo distingue dos etapas:
Evaluación primaria: el individuo determina si el evento es irrelevante, benigno o
potencialmente perjudicial (amenaza, desafío o pérdida).
Evaluación secundaria: la persona valora si dispone de recursos (apoyo social,
experiencia, competencias) para enfrentar la situación.
Aplicado al sector IT, un programador o analista de datos no reacciona ante un plazo de
entrega por la fecha límite en sí, sino por cómo interpreta esa exigencia en función de sus
objetivos, experiencias previas y recursos disponibles.

b. Modelo Demandas-Control de Karasek (1979)
Este es el modelo más apropiado para el análisis de la base de datos de esta investigación.
Explica el estrés laboral a partir de la relación entre las demandas laborales (lo que se requiere
del trabajador) y el control que este puede ejercer sobre su trabajo (autonomía y desarrollo de
habilidades).
El modelo es subjetivo, ya que se basa en la percepción o autodiagnóstico de los trabajadores,
y ha sido ampliamente utilizado para explicar depresión, ansiedad, percepción de estrés,
accidentes laborales y bajas por enfermedad. Los puestos con altas demandas y bajo control
(trabajos de alta tensión) presentan el mayor riesgo para la salud del trabajador, lo que conecta
directamente con la vulnerabilidad de los niveles jerárquicos inferiores.

c. Modelo Demandas-Control-Apoyo (JDC-S) de Johnson y Hall (1988)
Es una ampliación del modelo de Karasek que incorpora el apoyo social como una tercera
dimensión. Según este modelo, el apoyo social (de superiores y colegas) puede amortiguar los
efectos negativos de las altas demandas y el bajo control, reduciendo el riesgo de enfermedad.

d. Modelo del Desequilibrio Esfuerzo-Recompensa de Siegrist
Este modelo supone que el esfuerzo en el trabajo es parte de un contrato fundamentado en el
principio de reciprocidad. El trabajador recibe un pago por sus esfuerzos laborales en forma de
dinero, estima o seguridad social y/o laboral. Dicho intercambio representa una relación
asimétrica de poder donde el trabajador es la parte más débil. Cuando existe un desequilibrio
entre el alto esfuerzo y las bajas recompensas, se genera estrés ocupacional, lo que permite
interpretar la percepción de perjuicio profesional como una forma de recompensa negativa
(estima y oportunidades de promoción).

st.subheader("2.4. Jerarquía organizacional")
st.markdown(
    "La jerarquía organizacional es la estructura ordenada en la que se distribuyen las responsabilidades y el poder dentro de una empresa, facilitando la comunicación y la toma de decisiones."
)
st.info(
    "**Conexión con el modelo de Karasek:** Los puestos de niveles inferiores suelen caracterizarse por una mayor dependencia jerárquica y una supervisión más estrecha. Esta configuración se traduce en una menor latitud de decisión y una mayor exposición a las demandas, lo que hace a los trabajadores operativos potencialmente más vulnerables al estrés y a percibir consecuencias negativas para su carrera."
)

st.write("")
st.subheader("2.5. Confianza hacia el liderazgo")
st.markdown(
    "La confianza en el liderazgo actúa como un mediador crucial entre el estilo de mando y el bienestar de los empleados. El liderazgo transformacional inspira, motiva y desarrolla a los seguidores, fomentando relaciones de confianza."
)
st.success(
    "**Hallazgo clave (Perilla-Toro y Gómez-Ortiz, 2017):** Este estilo de liderazgo se relaciona positivamente con el bienestar psicológico, teniendo a la confianza en el líder como su principal efecto mediador. Un entorno de seguridad psicológica reduce el miedo a ser estigmatizado."
)

st.write("")
st.subheader("2.6. Percepción de perjuicio profesional")
st.markdown(
    "Se define como la creencia de que divulgar una condición de salud mental tendrá consecuencias negativas en el desarrollo de la carrera, las oportunidades de ascenso o el estatus dentro de la organización. Se relaciona directamente con el estigma percibido y el miedo a la discriminación."
)
st.warning(
    "**Relevancia en el sector tecnológico:** La cultura de alto rendimiento, competitividad y presión por la innovación amplifica el temor a ser percibido como vulnerable, poco productivo o incapaz de soportar la carga. Esto lleva a los trabajadores a ocultar sus condiciones, agravando el clima organizacional."
)
st.divider()

# Contexto historico: 

st.header("3. Contexto histórico e internacional de la salud mental")
st.write("A continuación, se presentan los hitos más importantes en la evolución de la salud mental laboral a nivel global:")
st.write("")

eventos_historicos = [
    ("1872", "Informe de Massachusetts. Precedente en salud pública y bienestar social."),
    ("1919", "Creación de la OIT. Se establece que la justicia social es esencial para alcanzar la paz universal.”),
    ("1948", "Constitución de la Organización Mundial de la Salud (OMS)."),
    ("1970", "Ley Williams-Steiger de Seguridad y Salud Ocupacional en Estados Unidos.", ),
    ("1979", "Surge el Modelo Demandas-Control de Karasek (alta demanda + bajo control = alta tensión)."),
    ("1984", "La OIT y la OMS usan el modelo de Karasek para definir los factores psicosociales de enfermedades ocupacionales."),
    ("1990", "Se aprueba la Ley de Estadounidenses con Discapacidades (ADA)."),
    ("1996", "Surge el Modelo Esfuerzo-Recompensa de Siegrist (esfuerzo extrínseco e intrínseco vs. recompensas)."),
    ("2006", "Convención sobre los Derechos de las Personas con Discapacidad (CRPD)."),
    ("2014", "Nace la iniciativa OSMI (Open Sourcing Mental Health) por Ed Finkler, base de esta investigación."),
    ("Actualidad", "La CIE-11 define el agotamiento laboral como un fenómeno ocupacional. La salud mental es un tema de vanguardia.")
]

for año, texto in eventos_historicos:
    with st.chat_message(name=str(año)):
        st.markdown(f"**{año}** — {texto}")
