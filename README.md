  # Exploración de Datos y Selección del Modelo

## Objetivo

Este proyecto tiene como objetivo analizar un conjunto de datos y seleccionar el modelo predictivo más adecuado para el caso de estudio. Se abordan las siguientes etapas:

1. **Exploración de Datos (EDA):** Visualizacion de los datos sinteticos generados en:
   <div href="https://github.com/santiagorodriguez-dev/pf_01_etl_preprocesamiento">pf_01_etl_preprocesamiento</div>

   <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/images/Figure_1.png" alt="logo" />
   </div>

  <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/images/Figure_2.png" alt="logo" />
   </div>
   
2. **Modelo:** Determinar el tipo de modelo necesario (regresión, clasificación o clustering) y justificar la elección según el objetivo del proyecto.
3. **Entrenamiento y Evaluación Inicial:** Entrenar el modelo utilizando una parte de los datos y evaluar su desempeño inicial con métricas apropiadas.
---

## 🗂 Estructura del Proyecto

El repositorio contiene la siguiente estructura de archivos y carpetas:

- **logs/**: Directorio destinado a almacenar archivos de registro generados durante la ejecución del proyecto.
- **src/**: Directorio que contiene el código fuente del proyecto, incluyendo módulos y scripts auxiliares.
- **.gitignore**: Archivo que especifica qué archivos o directorios deben ser ignorados por Git.
- **LICENSE**: Archivo que define la licencia del proyecto (Apache-2.0).
- **README.md**: Archivo que proporciona información general y documentación del proyecto.
- **modelos/**: Directorio destinado a almacenar archivos principales para generar los distintos modelos.
- **visual/**: Directorio destinado a almacenar archivos principales para generar los distintos informes visuales.

---

## Requisitos del Entorno

Para asegurar la correcta ejecución del proyecto, es necesario instalar las siguientes dependencias en un entorno virtual de Python:

- **pandas**: Para manipulación y análisis de datos.
- **numpy**: Para operaciones numéricas.
- **matplotlib**: Para generación de gráficos y visualizaciones.
- **seaborn**: Para visualizaciones estadísticas.
- **scikit-learn**: Para algoritmos de machine learning y herramientas de modelado.
- **tensorflow**: Para algoritmos de machine learning y herramientas de modelado.
- **openai-python**: Cliente oficial conexion con openai.

---

## Configuración del Entorno

Sigue estos pasos para configurar el entorno de desarrollo:

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo.git
cd pf_02_exploracion_datos_modelo
```

### 2️⃣ Crear y activar un entorno virtual

```bash
python -m venv venv
```

#### En Windows:
```bash
venv\Scripts\activate
```

#### En macOS/Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Instalar las dependencias

```bash
pip install -r requirements.txt
```
---
# Notas
-   Crear fichero .env en el raiz del proyecto.
```bash
SUPABASE_URL='url'
SUPABASE_KEY='key'
OPENAI_API_KEY='open_api_key'
OPENAI_API_ASSIS_PREDICCION='id_asistente_1'
OPENAI_API_ASSIS_VENTA='id_asistente_2'
OPENAI_API_ASSIS_CONVERSACION='id_asistente_3'
TF_ENABLE_ONEDNN_OPTS=0
```

## Ejecución del Proyecto

Para ejecutar los scripts principales y ejecutar los modelos, utiliza los siguientes comandos:

```bash
cd modelos
python modelo_asistente_resumen_conversacion.py
```
```bash
cd modelos
python modelo_asistente_ventas.py
```
```bash
cd modelos
python modelo_predictivo_tsf.py
```
```bash
cd modelos
python modelo_predictivo.py
```
```bash
cd modelos
python modelo_predictivo.py
```

Para ver las visualizaciones
```bash
cd visual
python visualizacion_alumnos.py
```
```bash
cd visual
python visualizacion_leads.py
```

## Licencia

Este proyecto está licenciado bajo la Licencia Apache 2.0. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

## Autores ✒️
* **Santiago Rodriguez** - [santiagorodriguez-dev](https://github.com/santiagorodriguez-dev)
