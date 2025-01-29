# Exploración de Datos y Selección del Modelo
  Objetivo: Analizar los datos y elegir el modelo más adecuado para tu caso.
-  1. Explorar los dato
  Realiza un análisis exploratorio de datos (EDA) para entender patrones
  relaciones.
  Genera visualizaciones relevantes (e.g., histogramas, correlaciones,
  diagramas de dispersión).
-  2. Seleccionar el model
  Decide qué tipo de modelo necesitas (regresión, clasificación o
  clustering).
  Justifica tu elección con base en el objetivo del proyecto.
-  3. Probar el modelo inicia
  Entrena el modelo usando una parte de los datos.
  Evalúa el desempeño inicial utilizando métricas apropiadas.
-  4. Entregabl
  Informe del EDA con visualizaciones.
  Selección del modelo y métrica de evaluación elegida.
  
  python.exe modelo_predictivo.py > logs\modelo_predictivo.txt


  pip install -r requirements.txt


  # Exploración de Datos y Selección del Modelo

## 🌟 Objetivo

Este proyecto tiene como objetivo analizar un conjunto de datos y seleccionar el modelo predictivo más adecuado para el caso de estudio. Se abordan las siguientes etapas:

1. **Exploración de Datos (EDA):** Realizar un análisis exploratorio para identificar patrones y relaciones en los datos, apoyado en visualizaciones relevantes.
2. **Selección del Modelo:** Determinar el tipo de modelo necesario (regresión, clasificación o clustering) y justificar la elección según el objetivo del proyecto.
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

## 🔧 Requisitos del Entorno

Para asegurar la correcta ejecución del proyecto, es necesario instalar las siguientes dependencias en un entorno virtual de Python:

- **pandas**: Para manipulación y análisis de datos.
- **numpy**: Para operaciones numéricas.
- **matplotlib**: Para generación de gráficos y visualizaciones.
- **seaborn**: Para visualizaciones estadísticas.
- **scikit-learn**: Para algoritmos de machine learning y herramientas de modelado.
- **tensorflow**: Para algoritmos de machine learning y herramientas de modelado.
- **openai-python**: Cliente oficial conexion con openai.

---

## 💻 Configuración del Entorno

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

## 🎨 Ejecución del Script Principal

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
python modelo_predictivo.py
```
```bash
cd modelos
python modelo_predictivo.py
```

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia Apache 2.0. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

💡 **Nota:** Si tienes algún problema o sugerencia, siéntete libre de abrir un *issue* en el repositorio. ✅
