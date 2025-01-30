
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

  ***Distribución de Edades (Gráfico de Barras y Densidad)***:
  Muestra la cantidad de clientes en diferentes rangos de edad.
  La mayoría de los clientes tienen entre 22 y 38 años, con una distribución relativamente uniforme.
  Hay un leve descenso en la cantidad de clientes alrededor de los 30 años.
  La línea de densidad ayuda a visualizar la tendencia de distribución.

  ***Distribución por Sexo (Gráfico de Barras)***:
  Representa la cantidad de hombres y mujeres que han comprado el curso.
  No hay una diferencia significativa entre ambos géneros, lo que indica que el curso es atractivo tanto para hombres como para mujeres.

  ***Distribución de Estudios (Gráfico de Barras Horizontales)***:
  Muestra los niveles de educación de los clientes.
  Se dividen en tres categorías: "Grado", "Grado Medio" y "Grado Superior".
  La mayoría de los clientes tienen estudios superiores, seguidos de los de grado medio.

  ***Motivos de Compra Más Frecuentes (Gráfico de Barras Horizontales)***:
  Lista los motivos más comunes por los cuales los clientes compran el curso.
  Los motivos más mencionados incluyen el deseo de crear proyectos propios, ser versátiles en el ámbito tecnológico y ganar confianza en el mundo freelance.
  También se observan razones relacionadas con el crecimiento profesional, la mejora salarial y la preparación para roles avanzados como CTO o Tech Lead.

  ***Conclusión***:
  El análisis sugiere que el curso de Full Stack es atractivo para personas jóvenes (22-38 años) con diferentes niveles de educación. No hay una gran brecha de género en la compra del curso, lo que muestra su accesibilidad para ambos sexos. Las motivaciones de compra indican que los clientes buscan tanto oportunidades profesionales como proyectos personales en el mundo de la tecnología.

  <div style="text-align: center;">
     <img src="https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/images/Figure_2.png" alt="logo" />
   </div>
   <br>

*** Score en Función de la Educación (Gráfico de Barras) ***:
Representa el score medio de potenciales clientes según su nivel educativo.
Las personas con "Grado" y "Grado Medio" tienen los scores más altos.
"Grado Superior" y "Licenciatura" también tienen un score considerable, aunque con mayor variabilidad.
Los niveles "ESO" y "Doctorado" tienen scores bajos, indicando menor interés en el curso.

*** Score en Función de la Especialidad (Gráfico de Barras) ***:
Analiza el score según la especialidad académica.
Los clientes con especialidad en "Informática" tienen el score más alto, seguidos de "Ingeniería".
La especialidad en "Letras" tiene un score muy bajo, lo que indica un menor interés en el curso en ese grupo.

*** Score en Función de la Edad (Gráfico de Barras) ***:
Muestra cómo varía el score en función de la edad de los clientes potenciales.
Se observan picos de score en edades como 26, 28 y 31 años, lo que indica que estas edades pueden tener mayor interés en el curso.
Hay una gran variabilidad en ciertos grupos de edad, representada por las barras de error.

*** Top 5 Motivos de Compra con Mayor Score (Gráfico de Barras) ***:
Presenta los principales motivos de compra asociados a los clientes con mayor score.
Los motivos más frecuentes incluyen:
Explorar la satisfacción de construir algo desde cero (mayor score).
Tener más control sobre proyectos creativos.
Hacer realidad ideas locas con código.
Desarrollar videojuegos o apps personales.
Ser un 'todoterreno' en cualquier proyecto tecnológico.

*** Conclusión ***
Los clientes con educación en "Grado" o "Grado Medio" y con especialidad en "Informática" o "Ingeniería" tienden a tener un mayor interés en el curso.
Las edades más propensas a valorar positivamente el curso están en el rango de 26 a 31 años.
Las motivaciones clave están relacionadas con la creatividad, la autonomía y la capacidad de materializar ideas en proyectos tecnológicos.
Este análisis puede ayudar a enfocar estrategias de marketing hacia los grupos con mayor score.

2. **Modelos Previstos:**
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
  - 2. Modelo 2 agente openai, test de prediccion de score de posible venta a un leads.
  logs generados de ejecucion: [modelo_predictivo](https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/logs/modelo_predictivo.txt).

  - 3. Modelo 3 agente openai, resume el texto de una conversación entre cliente/vendedor, generando un resumen para mejorar la interaccion con los clientes.
```bash
  D:\workspace\pf_02_exploracion_datos_modelo\modelos>python modelo_asistente_resumen_conversacion.py
  *****************************************************************************************
  Contenido del archivo '../datos_test/conversacion.txt':
  Cliente: ¡Hola! Estoy interesado en aprender desarrollo web, pero no sé por dónde empezar. ¿Ustedes ofrecen algún curso?

  Vendedor: ¡Hola! Claro que sí. Tenemos un curso Full Stack diseñado para quienes desean aprender desde lo más básico hasta lo avanzado en desarrollo web.

  Cliente: ¿Qué incluye el curso?

  Vendedor: El curso está dividido en dos partes principales:

  Front-End: Aprenderás HTML, CSS, JavaScript, y frameworks como React.
  Back-End: Trabajaremos con Node.js, Express, bases de datos como MongoDB y también veremos conceptos de APIs RESTful.
  Además, incluye ejercicios prácticos y un proyecto final que te servirá como portafolio profesional.

  Cliente: Suena interesante. ¿Necesito conocimientos previos para inscribirme?

  Vendedor: No, está pensado para principiantes. Comenzamos desde cero, así que no necesitas experiencia previa.

  Cliente: Genial. ¿Cuánto dura el curso?

  Vendedor: Tiene una duración de 4 meses, con clases semanales en vivo y acceso ilimitado a una plataforma de aprendizaje.

  Cliente: ¿Y cuánto cuesta?

  Vendedor: El costo total es de $500. Sin embargo, si te inscribes esta semana, tenemos un descuento del 20%, así que pagarías solo $400.

  Cliente: Eso está bastante bien. ¿Incluyen soporte si tengo dudas durante el curso?

  Vendedor: Por supuesto. Contamos con un grupo de soporte en el que puedes consultar dudas, además de sesiones de mentoría personalizadas con los instructores.

  Cliente: Perfecto. Creo que me interesa inscribirme. ¿Qué pasos debo seguir?

  Vendedor: Es muy fácil. Solo necesitas completar un formulario de inscripción y realizar el pago. Si quieres, te puedo enviar el enlace para que lo hagas ahora mismo.

  Cliente: Sí, por favor.

  Vendedor: ¡Excelente! Aquí tienes el enlace. Si necesitas más información, no dudes en contactarnos.

  Cliente: ¡Gracias! Estoy emocionado por empezar.

  Vendedor: ¡Gracias a ti! Nos vemos pronto en el curso. 😊
  *****************************************************************************************
  *****************************************************************************************
  Respuesta del asistente:
  **Observaciones sobre la atención al cliente:**
  El vendedor mostró un tono amigable y servicial a lo largo de la conversación, lo que ayudó a crear un ambiente positivo. Escuchó las preguntas del cliente y proporcionó información clara sobre el curso, sus componentes y beneficios. Sin embargo, podría haber aprovechado más la oportunidad para conectar emocionalmente con el cliente, quizás preguntando sobre sus objetivos personales en el desarrollo web.

  **Recomendaciones de mejora:**
  Para mejorar la atención al cliente, el vendedor podría utilizar preguntas abiertas para indagar más sobre las aspiraciones y necesidades del cliente. Por ejemplo, preguntar "¿Qué te motiva a aprender desarrollo web?" o "¿Tienes algún objetivo específico en mente para tu carrera?" Esto no solo ayuda a personalizar la conversación, sino que también permite mostrar una mayor empatía hacia el cliente.

  **Estrategias de ventas sugeridas:**
  El vendedor hizo un buen trabajo al mencionar el descuento y los beneficios del curso. Sin embargo, podría haber utilizado técnicas adicionales de persuasión, como:
  1. **Testimonios**: Compartir breves historias de éxito de exalumnos podría aumentar la credibilidad y el interés del cliente.
  2. **Urgencia**: Resaltar la duración limitada del descuento podría incentivar una decisión más rápida.
  3. **Cierre más sólido**: Al final, en lugar de solo enviar el enlace, podría haber ofrecido asistencia inmediata para completar el proceso de inscripción, o preguntar si había alguna otra duda que pudiera resolver antes de cerrar la venta.

  **Resumen con recomendaciones prácticas:**
  Para maximizar la efectividad en futuras interacciones, el vendedor debería enfocarse en hacer preguntas abiertas que permitan una mejor comprensión de las necesidades del cliente. Además, incorporar testimonios de alumnos anteriores y crear un sentido de urgencia respecto a las ofertas podría aumentar la tasa de conversión. Finalmente, ofrecer asistencia directa en el proceso de inscripción ayudaría a asegurar el cierre de la venta de manera más efectiva.
  *****************************************************************************************
```
  - 3. Modelo 4 Algoritmo en tensor Flow para predecir el score de posible venta a un leads.
  Logs generados de ejecucion: [modelo_predictivo](https://github.com/santiagorodriguez-dev/pf_02_exploracion_datos_modelo/blob/main/logs/modelo_predictivo_tsf.txt).
```bash
  Epoch 1/3
  [1m185/185[0m [32m====================[0m[37m[0m [1m8s[0m 30ms/step - accuracy: 0.7978 - loss: 0.4677 - val_accuracy: 0.8542 - val_loss: 0.3253
  Epoch 2/3
  [1m185/185[0m [32m====================[0m[37m[0m [1m6s[0m 32ms/step - accuracy: 0.8513 - loss: 0.3058 - val_accuracy: 0.9248 - val_loss: 0.1883
  Epoch 3/3
  [1m185/185[0m [32m====================[0m[37m[0m [1m6s[0m 31ms/step - accuracy: 0.9422 - loss: 0.1611 - val_accuracy: 0.9821 - val_loss: 0.0881
  Precisión del modelo: 98.21%
```
---

## Modelos seleccionados/descartados

Se selecciona los siguientes modelos:

- **Modelo 1 OpenAi Agente**: Interactua correctamente y solo muestra informacion sobre el curso del que tiene informacionn en la base de datos asociada.
- **Modelo 3 OpenAi Agente**: Resume el texto de una conversación entre cliente/vendedor, generando un resumen para mejorar la interaccion con los clientes.
- **Modelo 4 Prediccion TensorFlow**: Algoritmo en tensor Flow para predecir el score de posible venta a un leads.

Se descarta el siguiente modelo:
- **Modelo 2 OpenAi Agente**: Test de prediccion de score de posible venta a un leads, se descarta por tiempo de procesamiento ademas de la imposibilidad de
conseguir siempre el mismo resultado o medianamente parecido.
---

## Estructura del Proyecto

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

## Autores
* **Santiago Rodriguez** - [santiagorodriguez-dev](https://github.com/santiagorodriguez-dev)
