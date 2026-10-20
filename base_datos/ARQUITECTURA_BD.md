# ARQUITECTURA DE LA BASE DE DATOS

## 1. METODOLOGÍA

### 1.1 ESTADÍSTICA
Para el logro de los objetivos, y siguiendo a Martín (s/a) en referencia a Walter Federer (1973), se establece que la investigación corresponde a un estudio observacional, transversal y correlacional de fuente secundaria, correspondiente al periodo de años 2016-2019.

### 1.2 DE PROGRAMACIÓN
El diseño de la investigación en lo relativo a la programación se fundamenta, en cuanto a arquitectura, en el enfoque *Bottom-Up* de Kimball "para el diseño de sistemas de almacenamiento y análisis de datos, basado en la construcción incremental de Data Marts dimensionales orientados a procesos de negocio específicos, los cuales posteriormente se integran para formar un Data Warehouse corporativo". Específicamente, se adopta el modelo dimensional simple de estrella por ser "simple, intuitivo y de alto rendimiento para el análisis de datos" (Ochoa y Triveño, 2026).

Para la implementación de este modelo se verificarán los siguientes pasos:

#### 1.2.1 Selección del Proceso Organizacional
Para alcanzar el modelo estrella de Kimball se estructurará la arquitectura en torno a la Tabla de Hechos (`FACT_HECHOS`), relacionando las siguientes variables y preguntas de investigación:

* **1.2.1.1 (Variable Dependiente: Variable respuesta - Tabla de Hechos / Dimensión Percepción):**
  * *"Do you think that discussing a mental health issue with your employer would have negative consequences?"* (¿Crees que hablar de un problema de salud mental con tu empleador tendría consecuencias negativas?): `obs_consequence`. 
  * Valores: `Yes` (Sí) / `No` (No) / `Maybe` (Quizás).

* **1.2.1.2 (Variables Independientes Simples - Dimensión Persona / `DIM_PARTICIPANTE` y `DIM_UBICACION`):**
  * *"How old are you?"* (¿Qué edad tienes?): `Age` (Edad).
  * *"What is your gender?"* (¿Cuál es tu género?): `Gender` (Género). Se estandarizará durante la fase de limpieza de datos.
  * *"What country do you live in?"* (¿En qué país vives?): `Country` (País / alojado en `DIM_UBICACION`).
  * *"Do you have a family history of mental illness?"* (¿Tienes antecedentes familiares de enfermedad mental?): `family_history` (Antecedentes familiares). Valores: `Yes` (Sí), `No` (No).

* **1.2.1.3 (Variables Independientes Compuestas - Dimensión Organizacional / `DIM_TRABAJO`):**
  * Nivel Jerárquico del Puesto de Trabajo (`Nivel_Jerarquico`).
  * *"Are you self-employed?"* (¿Trabaja de forma independiente?): `self_employed`. Valores: `Yes`, `No`, `NA`.
  * *"Is your employer primarily a tech company/organization?"* (¿Es su empleador principalmente una empresa u organización tecnológica?): `tech_company`. Valores: `Yes` (Sí), `No` (No).
  * *"How many employees does your company or organization have?"* (¿Cuántos empleados tiene su empresa u organización?): `no_employees`. Valores: Intervalos `1-5`, `6-25`, `26-100`, `100-500`, `500-1000`, `More than 1000`.
  * *"Would you be willing to discuss a mental health issue with your direct supervisor(s)?"* (¿Estaría dispuesto a hablar sobre un problema de salud mental con su(s) supervisor(es) directo(s)?): `supervisor`. Valores: `Yes`, `No`, `Some of them`.

#### 1.2.2 Declaración de la Granularidad
Una (1) fila por cada respuesta registrada de un encuestado en cada edición anual (años 2016-2019). Así, la tabla de hechos (`FACT_HECHOS`) asentará la variable dependiente transformada, la cual se vinculará mediante Claves Foráneas (`Foreign Keys` - `FK`) a la **Dimensión Persona** (`DIM_PARTICIPANTE`: agrupación de variables sociodemográficas y de control: *age*, *gender*, *family_history*), a la **Dimensión Ubicación** (`DIM_UBICACION`: *country*), a la **Dimensión Organizacional** (`DIM_TRABAJO`: variables independientes compuestas y *Nivel_Jerarquico* del puesto de trabajo), así como a las dimensiones de **Tiempo** (`DIM_TIEMPO`) y **Percepción** (`DIM_PERCEPCION`).

#### 1.2.3 Identificación de las dimensiones que se aplican a cada fila en la tabla de hechos:
* **`participanteSK`:** Conexión con el perfil sociodemográfico, el rango de edad y los antecedentes del encuestado en la Dimensión Persona (`DIM_PARTICIPANTE`).
* **`trabajoSK`:** Conexión con las características de la empresa, el tamaño organizacional y el puesto ocupado en la Dimensión Organizacional (`DIM_TRABAJO`).
* **`encuestaSK`:** Conexión con la edición o año de la encuesta (2016-2019) en la Dimensión Tiempo (`DIM_TIEMPO`).
* **`ubicacionSK`:** Conexión con la procedencia geográfica y el país de residencia en la Dimensión Ubicación (`DIM_UBICACION`).
* **`percepcionSK`:** Conexión con las opiniones y el clima laboral sobre salud mental en la Dimensión Percepción (`DIM_PERCEPCION`).

#### 1.2.4 Identificación de los hechos
"Campos numéricos que completarán cada fila de la tabla de hechos. Qué se está respondiendo. Métricas verdaderas al nivel de detalle seleccionado" (Ochoa y Triveño, 2026). En consecuencia, los hechos serán la transformación cuantitativa de la respuesta analítica evaluada, según se explica a continuación:

* **1.2.4.1 `consecuencias_negativas`:**
  * `0` = No. Interpretación: No cree que hablar de un problema de salud mental con el empleador tendrá consecuencias negativas.
  * `1` = Maybe (Quizás). Interpretación: Cree que quizás hablar de un problema de salud mental con el empleador tendrá consecuencias negativas.
  * `2` = Yes (Sí). Interpretación: Sí cree que hablar de un problema de salud mental con el empleador tendrá consecuencias negativas.
  * *Es decir, el dato cualitativo se transformará en una escala de medida ordinal para el análisis inferencial mediante ANOVA factorial de dos vías.*

* **1.2.4.2 `Cantidad_encuestados`:**
  * Suma de la constante igual a 1 para cada fila (`COUNT`/`SUM`) para calcular la distribución descriptiva y el tamaño de la muestra ($n$) por cada celda dentro de la entidad según registro y atributo. Es decir, la celda es la medida que habita dentro de la entidad (Tabla de hechos: `FACT_HECHOS`) según el registro (fila) y el atributo (columna) determinado por la granularidad.

#### 1.2.5 Definición de los Factores y sus Niveles

* **1.2.5.1 Factor Edad. Niveles:**
  * **E1:** Joven (Menos de 30 años)
  * **E2:** Adulto Intermedio (De 30 a 45 años) — El grupo mayoritario en el sector tecnológico.
  * **E3:** Adulto Sénior (Más de 45 años)

* **1.2.5.2 Factor Jerárquico. Niveles:**
  * **J1:** Operativo / Junior (Encuestados en empresas grandes, no independientes, sin personal a cargo).
  * **J2:** Supervisor / Semi-Senior (Encuestados con funciones de coordinación o supervisión en estructuras corporativas medianas).
  * **J3:** Directivo / Independiente (Encuestados independientes o con cargos directivos).

* **1.2.5.3 Matriz de Datos:** $2 \times 3$ (Por elaborar)

---

## 2. BASE DE DATOS EN DBEAVER
Ruta de conexión local: `C:\Users\User\Desktop\mental_health.sqlite\mental_health.sqlite`

---

## 3. TIPOS DE DATOS

### 3.1 Numéricos
* **3.1.1** `Age`: `INT`
* **3.1.2** `mental_health_consequence` (`consecuencias_negativas` en `FACT_HECHOS`): `INT`

### 3.2 Texto
* **3.2.1** `Grupo_edad`: `VARCHAR`
* **3.2.2** `Nivel_jerarquico`: `VARCHAR`
* **3.2.3** `consecuencias_negativas_texto`: `VARCHAR`
* **3.2.4** `Country`: `VARCHAR`
* **3.2.5** `Gender`: `VARCHAR`

### 3.3 Fecha
* **3.3.1** `Datetime` / `encuestatexto`: `DATETIME` / `VARCHAR`

---

## 4. LIBRERÍAS E INSTALACIONES
```python
import duckdb
import pandas as pd
import numpy as np
import sqlite3
