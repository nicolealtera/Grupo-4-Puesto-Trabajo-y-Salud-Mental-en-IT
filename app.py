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

