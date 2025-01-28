
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
import pandas as pd

def predict(row, le_estudios, le_especialidad, le_ciudad, le_sexo, scaler, tokenizer, max_len, model):

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