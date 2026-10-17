# ARQUITECTURA DE LA BASE DE DATOS

## 1. METODOLOGÍA

### 1.1 ESTADÍSTICA
La base de datos Salud mental en la industria tecnológica de Open Sourcing Mental Illness (OSMI) (osmihelp.org), disponible en Kaggle, recoge datos entre los años 2014 al 2019, a excepción del año 2015, distribuidos de la siguiente manera:
- **2014:** 1.259 filas (encuestados) y 27 columnas (variables).
- **2016:** 1.433 filas (encuestados) y 63 columnas (variables).
- **2017:** 756 filas (encuestados) y 122 columnas (variables).
- **2018:** 417 filas (encuestados) y 123 columnas (variables).
- **2018:** 352 filas (encuestados) y 82 columnas (variables).

Para el logro de los objetivos desde el punto de vista del diseño experimental estadístico y siguiendo Martin (s/a) en referencia a Walter Federer (1973), tenemos que la investigación por su concepción de la estadística como ciencia, caracterización e inferencia, la investigación se tiene como un estudio observacional, transversal y correlacional de fuente secundaria. Así, se va a sintetizar descriptivamente una muestra de los encuestados para evaluar la distribución de las variables que será completado con un modelo inferencial basado en el ANOVA factorial de dos vías con interacción para contrastar el impacto simultáneo del nivel jerárquico y el grupo de edad sobre la percepción de perjuicio profesional; por lo que los hallazgos se circunscriben analíticamente a lo observado. A saber: Año 2014.

### 1.2 DE PROGRAMACIÓN
Ahora bien, el diseño de la investigación por lo que corresponde a la programación, se basa en cuanto a arquitectura al enfoque Bottom-Up de Kimball “para el diseño de sistemas de almacenamiento y análisis de datos, basado en la construcción incremental de Data Marts dimensionales orientados a procesos de negocio específicos, los cuales posteriormente se integran para formar un Data Warehouse corporativo.” Específicamente, en el modelo dimensional simple de estrella en virtud de ser un “simple, intuitivo y de alto rendimiento para el análisis de datos.” (Ochoa y Triveno 2026)

Por lo que se verificarán los siguientes pasos para cumplir ese modelo:

#### 1.2.1 Selección del Proceso Organizacional (Año 2014): 
Para alcanzar el modelo estrella de Kimball se creará una Tabla de Hechos (`Fact_Percepcion_Salud_Mental`), seleccioándose las variables (preguntas) que de seguidas se indican: 

##### 1.2.1.1 (Variable Dependiente: Variable respuesta):
"Do you think that discussing a mental health issue with your employer would have negative consequences?" (¿Crees que hablar de un problema de salud mental con tu empleador tendría consecuencias negativas?).: `obs_consequence`. Valores: `Yes` (Si)/ `No` (No)/ `Maybe` (Quizas)

##### 1.2.1.2 (Variables Independientes Simples. Dimensión Persona) 
- *“How old are you?”* (¿Qué edad tienes?): `Age` (Edad).
- *“What is your gender?”* (¿Cuál es tu género?): `Gender` (Género). Se estandarizará en la limpieza de los datos.
- *“What country do you live in?”* (¿En qué país vives?): `Country` (País).
- *"Do you have a family history of mental illness?"* (¿Tienes antecedentes familiares de enfermedad mental?): `family_history` (historia familiar) Valores: `Yes` (Si), `No` (No)  

##### 1.2.1.3 (Variables Independientes Compuestas. Dimensión Organizacional)
**Nivel Jerárquico del Puesto de Trabajo (`Nivel_Jerarquico`):**
- *"Are you self-employed?"* (¿Trabaja independiente?): `self_employed`. Valores: `Yes`, `No`, `NA`.
- *"Is your employer primarily a tech company/organization?"* (¿Es su empleador principalmente una empresa u organización tecnológica?). Valores: `Yes` (Si), `No` (No)  
- *"How many employees does your company or organization have?"* (¿Cuántos empleados tiene su empresa u organización?): `no_employees`. Valores: Intervalos en `1-5`, `6-25`, `26-100`, `100-500`, `500-1000`, `More than` (más de) `1000`.
- *"Would you be willing to discuss a mental health issue with your direct supervisor(s)?"* (¿Estaría dispuesto a hablar sobre un problema de salud mental con su(s) supervisor(es) directo(s)?): `supervisor`. Valores: `Yes`, `No`, `Some of them`.

#### 1.2.2 Declaración de la Granularidad: 
Una (1) fila por cada encuestado para el año 2014. La tabla de hechos (`Fact_Percepcion_Salud_Mental`) asentará para cada individuo la variable dependiente transformada que se vinculará mediante *Foreign Keys* (FK) a la Dimensión Persona (agrupación de las variables sociodemográficas y de control: `age`, `gender`, `country`, `family_history`) y a la Dimensión Organizacional (variables independientes compuestas: `Nivel_Jerarquico` del puesto de trabajo).

#### 1.2.3 Identificación de las dimensiones que se aplican a cada fila en la tabla de hechos: 
- `id_persona_fk`: Conexión con el perfil demográfico, el rango de edad y los antecedentes del encuestado en la Dimensión Persona.
- `id_organizacional_fk`: Conexión con las características de la empresa y el puesto ocupado en la Dimensión Organizacional.

#### 1.2.4 Identificación de los hechos 
(“Campos numéricos que completaran cada fila de la tabla de hechos. Que se está respondiendo. Métricas verdades al nivel de detalle seleccionado.” (Ochoa y Triveno, 2026). En consecuencia, los hechos serán transformación cuantitativa de la respuesta analítica evaluada como de seguidas se explica:

##### 1.2.4.1 `obs_consequence_score`:
- `0 = No` (No). Interpretación: No cree que hablar de un problema de salud mental con el empleador tendrá consecuencias negativas.
- `1 = Maybe` (Quizás). Interpretación: Cree que quizás hablar de un problema de salud mental con el empleador tendrá consecuencias negativas.
- `2 = Yes` (Si): Interpretación: Si cree que hablar de un problema de salud mental con el empleador tendrá consecuencias negativas.
Es decir, el dato cualitativo se transformará en una escala continua de intervalo ordinal.

##### 1.2.4.2 `Cantidad_encuestados`: 
Suma de la constante que será igual a 1 para cada fila. (COUNT/SUM) para calcular la distribución descriptiva y el tamaño de la muestra ($n$) por cada celda dentro de la entidad según registro y atributo. Es decir, la celda es la medida que habita dentro de la entidad (Tabla de hechos (`Fact_Percepcion_Salud_Mental`)) según el registro (fila) y el atributo (columna) que viene dado por la granularidad.

#### 1.2.5 Definición de los Factores y sus Niveles

##### 1.2.5.1 Factor Edad. Niveles:
- `E1`: Joven (Menos de 30 años)
- `E2`: Adulto Intermedio (De 30 a 45 años) — El grupo mayoritario en el sector tecnológico.
- `E3`: Adulto Sénior (Más de 45 años)

##### 1.2.5.2 Factor Jerárquico. Niveles: 
- `J1`: Operativo (Junior): encuestados en empresas grandes, no independientes, sin personal a cargo.
- `J2`: Supervisor (Semi-senior): encuestados con funciones de coordinación/supervisión en empresas medianas con supervisores, estructuras corporativas medianas.
- `J3`: Directivo / Independiente (encuestados independientes).

##### 1.2.5.3 Matriz de Datos: 
3x3 (Por elaborar)

---

## 2. BASE DE DATOS EN DBEAVER 
`C:\Users\User\Desktop\mental_health.sqlite\mental_health.sqlite`

---

## 3. TIPOS DE DATOS

### 3.1 Numérico(s)
- `3.1.1` `Age`: `Int`
- `3.1.2` `mental_health_consequence`: `Int`

### 3.2 Texto
- `3.2.1` `Grupo_edad`: `Varchar`
- `3.2.2` `Nivel_jerárquico`: `Varchar`
- `3.2.3` `mental_health_consequence`: `Varchar`
- `3.2.4` `Country`: `varchar`
- `3.2.5` `Gender`: `Varchar`

### 3.3 Fecha
- `3.3.1` `Datetime`: `Datetime`

---

## 4. LIBRERIAS E INSTALACIONES
```python
import duckdb
import pandas as pd
import numpy as np
import sqlite3

## 5.	BLOQUES DE CÓDIGO: Por definir

