import streamlit as st

st.set_page_config(
    page_title="Marco Teórico",
    page_icon="📚",
    layout="wide",
)

st.image("assets/marco teorico.png", use_container_width=True)
st.markdown("""
## 1. Antecedentes de la investigación 

### 1.1. La base OSMI como fuente científica 


La **Open Sourcing Mental Illness (OSMI) Mental Health in Tech Survey** es una de las principales fuentes de datos de autorreporte sobre salud mental en el sector tecnológico. Creada por la organización sin fines de lucro **OSMI**, su objetivo es evaluar la prevalencia de problemas de salud mental entre los profesionales de la tecnología y sus actitudes hacia estos en el lugar de trabajo. 

La base se estructura en torno a preguntas sobre: diagnóstico, tratamiento, estigma percibido, apoyo del empleador, confianza en la alta dirección y miedo a consecuencias profesionales. Su naturaleza estructurada y de acceso abierto la se ha convertido en un recurso ampliamente utilizado en la literatura académica. Para que un registro sea incluido, el encuestado debe pertenecer al sector tecnológico o desempeñar un rol técnico, lo que garantiza la homogeneidad de la poblacion objetivo. El producto resultante, miles de registros que abarcan múltiples ediciones, es hoy una de las fuentes de referencia para el estudio cuantitativo de la salud mental en el sector tecnológico. 

---

### 1.2. Antecedente directo: estudios que emplean la base OSMI

Diversos trabajos han utilizado la encuesta **OSMI** para el análisis cuantitativo de la salud mental en el sector tecnológico. **Rado y Neagu (2019)** emplearon la encuesta  para predecir la probabilidad de que un individuo buscara tratamiento de salud mental, utilizando modelos que iban desde árboles de decisión hasta redes neuronales.  **Sharma et al. (2018)** aplicaron técnicas de clasificación en el ámbito sanitario, demostrando la utilidad del conjunto de datos para la investigación predictiva. **Reddy, Thota y Dharun (2018)** usaron los datos para predecir si un empleado había recibido tratamiento por trastornos de salud mental. 

Estos trabajos comparten un enfoque predictivo y se centran en la variable de búsqueda de tratamiento. La presente investigación se diferencia en dos aspectos: primero, adopta un enfoque descriptivo-inferencial en lugar de predictivo; segundo, se centra en la percepción de perjuicio profesional como variable dependiente, y en el nivel jerárquico y el grupo de edad como factores independientes, una combinación que no ha sido examinada sistemáticamente en la literatura existente. """)

st.header("2. Bases conceptuales")
st.subheader("2.1. Estrés laboral y salud mental")
st.markdown(
    """
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
"""
)
st.subheader("2.2. Categorías de riesgos psicosociales en el sector IT")
st.markdown(
    """
Con base en las *Directrices de la Organización Mundial de la Salud* (en adelante OMS)
sobre salud mental en el trabajo, se identifican varias categorías de riesgos psicosociales
especialmente relevantes para el sector tecnológico (IT). Entre las más comunes destacan:

- **Carga de trabajo y ritmo:** altos niveles de presión de tiempo y sujeción continua a plazos de entrega.
- **Control:** baja participación en la toma de decisiones y falta de control sobre la carga y el ritmo de trabajo.
- **Cultura y funcionamiento organizacional:** mala comunicación, bajos niveles de apoyo para la resolución de problemas y burocracias complejas.
- **Relaciones interpersonales:** aislamiento social, malas relaciones con los superiores y falta de apoyo social.
- **Desarrollo profesional:** estancamiento, incertidumbre profesional e inseguridad laboral.
- **Interfaz hogar–trabajo:** exigencias contradictorias entre el trabajo y el hogar, poco apoyo en las responsabilidades de cuidado.
"""
)
st.subheader("2.3. Modelos teóricos del estrés laboral")
st.markdown(
    """
Los modelos teóricos que explican el estrés laboral consideran factores psicosociales
como las exigencias psicológicas, el control sobre el contenido del trabajo y el apoyo
social dentro de la organización. A continuación, se presentan los principales modelos
que sustentan esta investigación.
"""
)
with st.expander("**a. Modelo de la Valoración de Lazarus**", expanded=False):
    st.markdown(
        """
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
    st.markdown(
        """
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
    st.markdown(
        """
Es una ampliación del modelo de Karasek que incorpora el **apoyo social** como una
tercera dimensión. Según este modelo, el apoyo social (de superiores y colegas) puede
amortiguar los efectos negativos de las altas demandas y el bajo control, reduciendo
el riesgo de enfermedad.
"""
    )

with st.expander("**d. Modelo del Desequilibrio Esfuerzo-Recompensa de Siegrist**"):
    st.markdown(
        """
Este modelo supone que el esfuerzo en el trabajo es parte de un **contrato fundamentado
en el principio de reciprocidad**. El trabajador recibe un pago por sus esfuerzos
laborales en forma de dinero, estima y/o seguridad social y laboral. Dicho intercambio
representa una relación asimétrica de poder donde el trabajador es la parte más débil.

Cuando existe un desequilibrio entre el alto esfuerzo y las bajas recompensas, se
genera estrés ocupacional, lo que permite interpretar la percepción de perjuicio
profesional como una forma de **recompensa negativa** (estima y oportunidades de
promoción).
"""
    )
st.markdown(
   """ ## 2.3 Fundamentos técnicos del ANOVA 
El Análisis de Varianza (ANOVA) es una herramienta estadística de modelado  lineal que permite calcular si los valores esperados, usualmente medias, de dos o más grupos o condiciones experimentales son estadísticamente iguales, es decir, define si existen algunas diferencias significativas entre ellos. El ANOVA estima la proporción de la variación observada que se atribuye al factor en estudio  y se compara con la variación no explicada o residual. Aunque este modelo de datos se suele aplicar más como prueba para tres o más grupos, es posible aplicarse a dos grupos.
Como se menciono anteriormente, el ANOVA se utiliza normalmente para probar diferencias de las medias, y esto lo hace comparando dos estimaciones de variabilidad para asi contrastar las medias:
Variación entre grupos: Refleja la variabilidad asociada a las diferencias entre las medias de cada grupo.
Variación dentro de los grupos: Mide la dispersión entre las observaciones respecto a la media de su propio grupo.
Cuando las medias poblacionales son iguales, los cuadrados medios entre grupos y dentro de los grupos deben estimar aproximadamente la misma varianza de error y por lo tanto producir un estadístico F cercano a 1. Opuesto a ello, si las medias de los grupos estan separadas en relación con la variabilidad que existe dentro de los grupos, la estimación entre grupos incrementa, lo que produce un estadístico F mayor,esto aporta evidencia solida para rechazar la hipótesis nula de medias iguales. 
###Terminología esencial de ANOVA
**Factor:** Variable explicativa categórica.
**Nivel de factor:** Cada una de las categorías que componen un factor.
**Variable de respuesta:** O variable dependiente, es la medida cuantitativa que se analiza o de la cual es objeto de analisis.
**Efecto principal:** La asociación media entre un factor y la variable de respuesta, tras considerar los demás términos del modelo.
**Efecto de interacción:** Ocurre cuando la relación entre un factor y la variable de respuesta depende del nivel que tome otro factor.
**Residual:** Es la diferencia entre un valor observado y el valor predicho por el modelo lineal ajustado. Muchas suposiciones acerca del ANOVA se evalúan sobre la distribución de estos residuos, más que del resultado bruto considerado sin su estructura de grupos.
**Prueba ómnibus:** Una prueba general es una prueba estadística que se utiliza para evaluar si existen diferencias significativas entre múltiples grupos o condiciones. Un resultado significativo detecta que existe al menos una diferencia entre las medias, pero no identifica cuáles difieren directamente.

Existen diferentes variantes del modelo ANOVA según el estudio que se va a realizar, siendo las principales:
**ANOVA Unidireccional:** Examina un único factor categórico y un resultado cuantitativo. Es el método estándar para comparar varias medias de grupo independientes bajo un modelo de varianza común.
**ANOVA Bidireccional y Factorial:** Incorpora dos o mas factores de manera simultánea, este modelo puede ser mejor que realizar pruebas unidireccionales separadas porque puede revelar interacciones y estimar los efectos dentro de un modelo unificado. 
**Otras variantes del ANOVA son:** el ANOVA de medidas repetidas, el ANOVA mixto o el ANOVA de Welch, entre otras variantes.

###Supuestos del ANOVA
Para que los resultados sean válidos, deben cumplirse los siguientes supuestos:

**Independencia de observaciones:** Las mediciones deben ser independientes entre sí, a menos que el modelo seleccionado represente explícitamente datos repetidos, emparejados, agrupados o jerárquicos. La independencia está determinada por el diseño de la investigación y el proceso de recopilación de datos.

**Normalidad de los residuos:** Los residuos del modelo deben seguir una distribución aproximadamente normal. Para la verificación formal de este supuesto se aplica la prueba de Shapiro-Wilk (1965):
la prueba se basa en la covarianza entre los valores ordenados de la muestra y los valores esperados bajo la hipótesis de normalidad. De acuerdo con la Universidad Autónoma de Coahuila (s/a), se calcula a partir de los siguientes pasos:

***Hipótesis nula (H0):*** los datos provienen de una población con distribución normal. 
***Hipótesis alternativa (H1):*** los datos no provienen de una población con distribución normal. 

No se debe usar esta prueba de normalidad como un pase directo ya que en las muestras pequeñas el contraste tiene poca potencia, y con muestras muy grandes es posible que detecte desviaciones que no tienen consecuencias prácticas para los contrastes paramétricos.


**Homogeneidad de varianzas:** El ANOVA clásico asume que la varianza del error es constante e igual entre los grupos. Este supuesto se evalúa formalmente mediante la prueba de Levene, la cual contrasta si las varianzas poblacionales de los grupos son equivalentes:
Se utiliza para comprobar si varios grupos tienen la misma varianza en la población. 
***Hipótesis nula (H0):*** Los grupos tienen varianzas iguales.
***Hipótesis alternativa (H1):*** Los grupos tienen varianzas diferentes.

**Ausencia de observaciones altamente influyentes:** El ANOVA se basa en desviaciones al cuadrado, por lo que se tiene que comprobar que el modelo no este sesgado por valores extremos (outliers), ya que observaciones extremas pueden influir fuertemente en medias, suma de cuadrados y estadísticas F. Cualquier exclusión o análisis de sensibilidad debe documentarse de forma transparente.
"""
)