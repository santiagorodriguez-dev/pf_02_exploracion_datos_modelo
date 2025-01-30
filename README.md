
# 2 - Agente asistente de ventas - Exploración de Datos y Selección del Modelo

## Objetivo

Este proyecto tiene como objetivo analizar un conjunto de datos y seleccionar el modelo predictivo más adecuado para el caso de estudio. Se abordan las siguientes etapas:

1. **Exploración de Datos (EDA):** 
Visualizacion de los datos sinteticos generados en: [pf_01_etl_preprocesamiento](https://github.com/santiagorodriguez-dev/pf_01_etl_preprocesamiento).
  <br>
   <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/images/Figure_1.png" alt="logo" />
   </div>
  <br>
  <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/images/Figure_2.png" alt="logo" />
   </div>
   <br>

2. **Modelo:**
  - 1. Modelo 1 agente openai, asistente de informacion sobre un curso especifico, en este caso Full Stack (RDC)

   <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/images/modelo_curso_rdc.PNG" alt="logo" />
   </div>

  - 2. Modelo 1 tiene asignada un base de datos de vectores con toda la informacion disponible del curso.

  <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/images/base_de_datos_rdc.PNG" alt="logo" />
   </div>

  - 3. Modelo 2 agente openai, test de prediccion de score de posible venta a un leads.

   <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/images/modelo_prediccion.PNG" alt="logo" />
   </div>

  - 4. Modelo 2 tiene asignada un base de datos de vectores con toda la informacion de todos los alumnos.

  <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/images/base_de_datos_prediccion.PNG" alt="logo" />
   </div>

  - 5. Modelo 3 agente openai, resume el texto de una conversación entre cliente/vendedor, generando un resumen para mejorar la interaccion con los clientes.
  
   <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/images/modelo_resumen_venta.PNG" alt="logo" />
   </div>

  - 6. Modelo 4 Algoritmo en tensor Flow para predecir el score de posible venta a un leads.
  
3. **Entrenamiento y Evaluación Inicial:** Entrenamiento pruebas de modelos.
  - 1. Modelo 1 agente openai, asistente de informacion sobre un curso especifico, en este caso Full Stack (RDC)
```bash
    D:\workspace\pf_02_exploracion_datos_modelo\modelos>python modelo_asistente_ventas.py
    Introduce un mensaje para interactuar con el chatbot (o escribe 'salir' para terminar): hola
    *****************************************************************************************
    Consulta realizada:
    hola
    *****************************************************************************************
    Respuesta asistente:
    ¡Hola! ¿En qué puedo ayudarte hoy? Si tienes preguntas sobre el curso de Desarrollador Full Stack, estaré encantado de responderte.
    *****************************************************************************************
    Introduce un mensaje para interactuar con el chatbot (o escribe 'salir' para terminar): informacion disponible del curso
    *****************************************************************************************
    Consulta realizada:
    informacion disponible del curso
    *****************************************************************************************
    Respuesta asistente:
    Aquí tienes la información sobre el curso de Desarrollador Full Stack:

    ### Descripción del Curso
    El curso de Desarrollador Full Stack está diseñado para convertirte en un profesional versátil en el desarrollo web, abarcando tanto el frontend como el backend. El programa se compone de más de 900 horas de contenido actualizado, incluyendo 100 horas de video y 800 horas de trabajo personal. La duración del curso es de 4 a 12 meses, dependiendo de tu dedicación diaria, con un compromiso de entre 5 y 7 horas al día【6:0†source】.

    ### Estructura del Curso
    El curso incluye 11 módulos que cubren tópicos fundamentales, entre ellos:
    1. **Fundamentos de la Programación**
    2. **JavaScript**
    3. **NodeJS**
    4. **Desarrollo de APIs REST**
    5. **ReactJS**
    6. **Frontend y Backend**
    7. **Empleabilidad y Preparación para el Mercado Laboral**【6:1†source】【6:2†source】.

    ### Especializaciones
    Al finalizar la parte troncal del curso, tendrás la oportunidad de especializarte en áreas como:
    - IA Developer
    - Advanced Web Technologies
    - UX Engineer【6:10†source】.

    ### Certificaciones
    Al completar el curso, recibirás dos certificados: uno como Desarrollador Full Stack y otro correspondiente a la especialización que elijas【6:0†source】【6:10†source】.

    ### Modalidad y Metodología
    - **Modalidad 100% online**: Puedes avanzar a tu propio ritmo y adaptar el estudio a tu rutina diaria.
    - **Clases en directo**: Interacción directa con instructores y compañeros, facilitando la resolución de problemas y el trabajo en proyectos prácticos【6:3†source】【6:5†source】.

    ### Costo
    El precio del curso es de 3,500 euros, con descuentos disponibles de hasta 750 euros【6:15†source】.

    ### Salidas Profesionales
    Al completar el curso, estarás preparado para roles como:
    - Desarrollador Full Stack
    - Frontend Developer
    - Backend Developer
    - UX Engineer【6:11†source】【6:17†source】.

    Si tienes más preguntas o necesitas información adicional sobre algún aspecto específico del curso, ¡no dudes en preguntar!
    *****************************************************************************************
    Introduce un mensaje para interactuar con el chatbot (o escribe 'salir' para terminar): que es una IA?
    *****************************************************************************************
    Consulta realizada:
    que es una IA?
    *****************************************************************************************
    Respuesta asistente:
    Lo siento, pero no tengo información sobre inteligencia artificial (IA) fuera del contexto del curso de Desarrollador Full Stack. Sin embargo, puedo decirte que dentro del curso, hay una especialización en IA Developer, donde se abordan temas relacionados con el desarrollo de aplicaciones que utilizan inteligencia artificial.

    Si deseas más información sobre esa especialización o cualquier otro aspecto del curso, ¡estaré encantado de ayudarte!
    *****************************************************************************************
    Introduce un mensaje para interactuar con el chatbot (o escribe 'salir' para terminar):
```
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
