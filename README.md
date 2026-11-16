# Puesto de Trabajo y su Relación con la Salud Mental en el Ámbito Tecnológico

![Puesto de Trabajo y su Relación con la Salud Mental en el Ámbito Tecnológico: Un Análisis Estadístico del Impacto en el Desarrollo Profesional](assets/banner.png)

## Descripción del Proyecto

Este proyecto analiza cómo difieren las percepciones de perjuicio profesional por motivos de salud mental según el nivel jerárquico del puesto de trabajo y el grupo de edad en trabajadores del sector tecnológico, utilizando datos de la encuesta OSMI Mental Health in Tech Survey. El estudio emplea un ANOVA factorial de dos vías con interacción como técnica inferencial principal, complementado con análisis descriptivo y visualización de datos para explorar las diferencias entre los grupos e identificar los segmentos más vulnerables.

---

## 🔬 Metodología Estadística

Investigación de nivel descriptivo-correlacional, con diseño no experimental, transversal y documental sobre fuente secundaria. Al trabajar con una muestra no probabilística y de participación voluntaria, los resultados no permiten generalizaciones estrictas a toda la población del sector tecnológico global. En consecuencia, la inferencia estadística se aborda mediante un ANOVA factorial de dos vías con interacción como única técnica inferencial. Los hallazgos se complementan con análisis descriptivo y visualización de datos para explorar las diferencias entre los grupos, y se interpretan dentro de las limitaciones del sesgo de autoselección.

### Pregunta de la Investigación

> ¿Difiere la percepción de perjuicio profesional por motivos de salud mental según el nivel jerárquico y el grupo de edad en el sector tecnológico?

### Objetivos específicos

1. Caracterizar socio-demográficamente a la muestra de trabajadores del sector tecnológico (edad, género, nivel jerárquico y país).
2. Describir la distribución de la percepción de perjuicio profesional por nivel jerárquico y grupo de edad.
3. Analizar la relación entre la edad y la percepción de perjuicio dentro de cada nivel jerárquico.
4. Determinar si existen diferencias significativas en la percepción de perjuicio según el nivel jerárquico y el grupo de edad, y si existe interacción entre ambos factores.

## 🛠️ Arquitectura del Proyecto

```text
Kaggle: OSMI Mental Health in Tech Survey (Datos crudos en formato EAV)
│
▼
[Limpieza y Normalización] → Python + Pandas + DBeaver
│  (Unificación de esquemas, tratamiento de nulos, creación de variables)
▼
Base de Datos Normalizada (3FN) → SQLite / Supabase (PostgreSQL)
│  (Modelo en estrella: Tablas de hechos y dimensiones)
▼
[Exportación / Conexión] → DuckDB / SQLAlchemy
│
┌─────────────┴─────────────┐
▼                           ▼
Aplicativo en Streamlit     Consultas SQL Avanzadas
(Análisis interactivo)      (Evaluación de SQL con Supabase)
```

### ¿Por qué este conjunto de herramientas?

| Herramienta | Papel en el proyecto | Razón de la elección |
| :--- | :--- | :--- |
| **Python + Pandas** | Limpieza y transformación de datos | Manejo eficiente de datos nulos y normalización de variables. |
| **DBeaver / SQLite** | Modelado y normalización relacional | Permite construir y verificar el esquema en 3FN antes de subirlo a la nube. |
| **Supabase** | Base de datos en la nube (PostgreSQL) | Alojamiento de la base normalizada, acceso remoto y soporte para SQL avanzado. |
| **SQLAlchemy** | Conexión desde Python a Supabase | Permite ejecutar consultas SQL puras y manejar la conexión de forma segura. |
| **DuckDB** | Motor analítico para el dashboard | Procesamiento rápido de datos locales y consultas a archivos Parquet. |
| **Streamlit** | Interfaz del aplicativo | Publica el análisis completo (marco teórico, resultados, ANOVA y editor SQL) en una web interactiva. |

### Base de datos

### 📌 [**Mental Health in the Tech Industry**](https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry)

### Fase de normalización

El sistema original utilizaba un esquema EAV (Entidad-Atributo-Valor) que, aunque flexible para recolectar datos dispersos, presentaba problemas de rendimiento y carecía de integridad de tipos, por lo que se rediseñó la información hacia un modelo relacional normalizado en Tercera Forma Normal (3FN). Para lograrlo, se filtraron únicamente las variables clave de la investigación y se establecieron dos entidades principales independientes (Participantes y Encuestas) que eliminan las dependencias parciales de la 2FN y sirven de anclaje para todo el sistema.

A partir de estas bases, la información útil se organizó en entidades categóricas dependientes que agrupan los datos por dominios temáticos —como situación laboral, estado mental, impacto profesional, apoyo corporativo y prejuicios— vinculados de forma uno a uno con los participantes y uno a muchos con las encuestas. Asimismo, se separaron las dependencias transitivas en catálogos independientes de referencia para los puestos, géneros, países y estados, logrando una estructura consistente, sin duplicidades y altamente optimizada para consultas analíticas.

![Visualización](./assets/DER_normalizacion.png)

---

## Guía de instalación y uso:

### 1. Clonar el repositorio

```bash
git clone https://github.com
cd Grupo-4-Puesto-Trabajo-y-Salud-Mental-en-IT
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar las credenciales (Secrets)

Crea una carpeta llamada `.streamlit` en la raíz del proyecto y dentro un archivo `secrets.toml` con las credenciales de MotherDuck y Supabase (usa el archivo `.env.ejemplo` como guía).

```toml
MOTHERDUCK_TOKEN = "tu_token_de_motherduck"

[connections.supabase]
SUPABASE_DB_URL = "postgresql+psycopg2://postgres:tu_contraseña@db.tu_proyecto.supabase.co:5432/postgres"
```

### 4. Ejecutar el aplicativo

```bash
streamlit run app.py
```

---

## 📁 Estructura del Repositorio

```text

├── app.py                    # Código principal de la App de Streamlit
├── requirements.txt          # Librerias de Python
├── README.md.                # Documentación del repositorio
├── .streamlit
│   └──config.toml            # Tema visual de la app
│ 
├── pages/
│   ├── 01_Inicio.py                # Página de inicio
│   ├── 02_Marco_Metodologico.py    # Operacionalización y metodología
│   ├── 03_Marco_Teorico.py         # Fundamentos conceptuales
│   ├── 05_Conclusiones.py          # Hallazgos y recomendaciones
│   └── 06_Bibliografia.py          # Referencias bibliográficas
│
```

---

## 🔍 Equipo de investigación

- **Nicole Altera**
- **Danmara Dos Ramos**
- **Arianna Oliveros**
- **Camila Santiago**
- **Sebastian Soto**
