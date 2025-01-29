
import pandas as pd # type: ignore
import numpy as np # type: ignore
from sklearn.preprocessing import LabelEncoder, StandardScaler # type: ignore
from tensorflow.keras.models import Model # type: ignore
from tensorflow.keras.layers import Input, Dense, Embedding, LSTM, Concatenate # type: ignore
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
import json


import sys
sys.path.append("../")
import dotenv # type: ignore
dotenv.load_dotenv()
from src import support_bd as bd

def crear_modelo():
    """
    Crea y entrena un modelo de aprendizaje profundo para predecir la probabilidad de compra de un alumno.

    - Carga datos de la base de datos.
    - Preprocesa datos categóricos y textuales.
    - Escala los datos numéricos.
    - Divide los datos en conjuntos de entrenamiento y prueba.
    - Construye un modelo de red neuronal con entradas numéricas y de texto.
    - Entrena y evalúa el modelo.
    - Predice y actualiza los datos de los leads con el score calculado.

    Returns:
        None
    """

    df_leads = bd.select_datos("leads")
    df = bd.select_datos("alumnos")
    df = df.drop(columns=["nombre", "apellidos", "email", "telefono"])
      
    # Preparar los codificadores para las columnas categóricas
    le_estudios = LabelEncoder()
    le_especialidad = LabelEncoder()
    le_ciudad = LabelEncoder()
    le_sexo = LabelEncoder()

    # Ajustar los codificadores con los valores únicos de cada columna
    df["estudios"] = le_estudios.fit_transform(df["estudios"])
    df["especialidad"] = le_especialidad.fit_transform(df["especialidad"])
    df["ciudad"] = le_ciudad.fit_transform(df["ciudad"])
    df["sexo"] = le_sexo.fit_transform(df["sexo"])

    # Tokenizar y procesar el campo de texto 'motivo_compra'
    tokenizer = Tokenizer(num_words=5000)  # Limitar a las 5000 palabras más frecuentes
    tokenizer.fit_on_texts(df["motivo_compra"])
    df["motivo_compra"] = tokenizer.texts_to_sequences(df["motivo_compra"])

    # Rellenar las secuencias para que todas tengan la misma longitud
    max_len = 50  # Máxima longitud de las descripciones
    df["motivo_compra"] = pad_sequences(df["motivo_compra"], maxlen=max_len).tolist()

    # Separar características (X) y etiquetas (y)
    X_numerico = df[["edad", "estudios", "especialidad", "sexo", "ciudad"]].values
    X_texto = np.array(df["motivo_compra"].tolist())
    y = df["comprado"].values

    # Escalar los datos numéricos
    scaler = StandardScaler()
    X_numerico = scaler.fit_transform(X_numerico)

    # Dividir en conjunto de entrenamiento y prueba
    X_num_train, X_num_test, X_text_train, X_text_test, y_train, y_test = train_test_split(
        X_numerico, X_texto, y, test_size=0.2, random_state=42
    )

    # Crear el modelo combinado
    # Entrada numérica
    input_numerico = Input(shape=(X_numerico.shape[1],))
    numerico = Dense(16, activation="relu")(input_numerico)

    # Entrada de texto
    input_texto = Input(shape=(max_len,))
    texto = Embedding(input_dim=5000, output_dim=64)(input_texto)
    texto = LSTM(32)(texto)

    # Concatenar entradas
    concatenado = Concatenate()([numerico, texto])
    denso = Dense(16, activation="relu")(concatenado)
    salida = Dense(1, activation="sigmoid")(denso)

    # Modelo final
    model = Model(inputs=[input_numerico, input_texto], outputs=salida)

    # Compilar el modelo
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    # Entrenar el modelo
    history = model.fit(
        [X_num_train, X_text_train], y_train,
        epochs=3, batch_size=128, validation_data=([X_num_test, X_text_test], y_test)
    )

    # Evaluar el modelo
    loss, accuracy = model.evaluate([X_num_test, X_text_test], y_test, verbose=0)
    print(f"Precisión del modelo: {accuracy * 100:.2f}%")

    for index, row in df_leads.iterrows():
        score = predict_modelo(row, le_estudios, le_especialidad, le_ciudad, le_sexo, scaler, tokenizer, max_len, model)
        update_data(row, score)

def predict_modelo(row, le_estudios, le_especialidad, le_ciudad, le_sexo, scaler, tokenizer, max_len, model):
    """
    Predice la probabilidad de compra de un alumno en función de sus características.

    Args:
        row (pd.Series): Datos del alumno a evaluar.
        le_estudios (LabelEncoder): Codificador para la columna "estudios".
        le_especialidad (LabelEncoder): Codificador para la columna "especialidad".
        le_ciudad (LabelEncoder): Codificador para la columna "ciudad".
        le_sexo (LabelEncoder): Codificador para la columna "sexo".
        scaler (StandardScaler): Escalador para los datos numéricos.
        tokenizer (Tokenizer): Tokenizador para el campo de texto "motivo_compra".
        max_len (int): Longitud máxima de la secuencia de texto.
        model (Model): Modelo de red neuronal entrenado.

    Returns:
        float: Probabilidad de compra en porcentaje.
    """
    # Crear un DataFrame con la información del nuevo alumno
    test_lead = pd.DataFrame([row])

    # Transformar los datos categóricos
    test_lead["estudios"] = le_estudios.transform(test_lead["estudios"])
    test_lead["especialidad"] = le_especialidad.transform(test_lead["especialidad"])
    test_lead["ciudad"] = le_ciudad.transform(test_lead["ciudad"])
    test_lead["sexo"] = le_sexo.transform(test_lead["sexo"])

    # Escalar los datos numéricos
    nuevo_test_numerico = scaler.transform(test_lead[["edad", "estudios", "especialidad", "sexo", "ciudad"]])

    # Tokenizar y rellenar la secuencia del texto
    nuevo_test_texto = tokenizer.texts_to_sequences(test_lead["motivo_compra"])
    nuevo_test_texto = pad_sequences(nuevo_test_texto, maxlen=max_len)

    # Predecir la probabilidad de compra
    probabilidad = model.predict([nuevo_test_numerico, nuevo_test_texto])[0][0]
    #print(f"Probabilidad de que el nuevo alumno compre el curso: {probabilidad * 100:.2f}%")

    return  probabilidad * 100

def update_data(row, score):
        """
        Actualiza el puntaje de compra en la base de datos para un lead específico.

        Args:
            row (pd.Series): Datos del lead a actualizar.
            score (float): Puntaje de probabilidad de compra.

        Returns:
            None
        """        
        score_short = np.round(float(score), decimals=2)
        
        data ={ 
            "email" : row['email'], 
            "score" : score_short
        } 
        supabase = bd.init_conection_bd()

        response = (
            supabase.table("leads")
            .update({"score": data['score']})
            .eq("email", data['email'])
            .execute())