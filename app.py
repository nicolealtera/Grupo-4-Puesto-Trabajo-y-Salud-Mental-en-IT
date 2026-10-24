import steamlit as st   
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

# 5. Definicion de terminos basicos 

st.header("5. Definición de términos básicos")
st.write("Haz clic en cada término para desplegar su definición:")
st.write("")

mostrar_definicion(
    "Salud mental", 
    "Se define como el \"estado de bienestar mental que permite a las personas hacer frente a los momentos de estrés de la vida, desarrollar todas sus habilidades, aprender y trabajar adecuadamente e integrarse en su entorno\". Constituye un valor intrínseco y fundamental de las personas.",
    "🧠"
)

mostrar_definicion(
    "Percepción de prejuicio profesional", 
    "Se refiere a los estereotipos sociales sobre las enfermedades mentales que generan actitudes y comportamientos negativos. Incluye el pesimismo terapéutico y el estigma en el entorno laboral, que puede llevar a quienes experimentan dificultades a guardar silencio (De Angelis, 2024).",
    "👁️"
)

mostrar_definicion(
    "Estigma", 
    """
    Suele surgir de una falta de conocimiento o de miedo. En el ámbito de la salud mental, se identifican estos tipos:
    *   **Estigma público:** Actitudes negativas o discriminatorias de otras personas.
    *   **Autoestigma:** Actitudes negativas propias, incluyendo sentir vergüenza.
    *   **Estigma institucional:** Políticas sistémicas del gobierno u organizaciones que limitan oportunidades (ej. menos fondos para investigación).
    
    *Factores subyacentes:* miedo/evitación, malevolencia, autoritarismo e imprevisibilidad.
    """,
    "🏷️"
)

mostrar_definicion(
    "Jerarquía laboral", 
    "Según la Business School of Madrid, es \"el sistema formal que establece el orden, la subordinación y las líneas de reporte entre los diferentes niveles de autoridad\". Para esta investigación, se operacionaliza en tres niveles: **Directivo, Coordinación y Operativo**.",
    "🏢"
)

mostrar_definicion(
    "Confianza en el liderazgo", 
    "Se fundamenta en la premisa de que \"la confianza es el ingrediente más importante para construir un equipo\" (Covey). Nace de dos dimensiones fundamentales: el **carácter** y la **competencia**.",
    "🤝"
)

mostrar_definicion(
    "Edad", 
    "Se refiere a la edad en años cumplidos, es decir, al número de aniversarios del nacimiento transcurridos hasta la fecha de referencia.",
    "🎂"
)

mostrar_definicion(
    "Sector tecnológico", 
    "Conjunto de actividades económicas dedicadas a la investigación, desarrollo, fabricación y prestación de servicios relacionados con la tecnología (software, hardware, telecomunicaciones, TI, nube, datos). Se caracteriza por su rápido ritmo de innovación, alta exigencia de actualización y entornos altamente competitivos.",
    "💻"
)

