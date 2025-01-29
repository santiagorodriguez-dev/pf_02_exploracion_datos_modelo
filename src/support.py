

import sys
sys.path.append("../")

import dotenv  # type: ignore
dotenv.load_dotenv()

import os
import pandas as pd  # type: ignore
from supabase import create_client, Client # type: ignore
from supabase.client import ClientOptions # type: ignore

from src import support_open_ai as sp
from src import support_bd as bd

import re
import json
import time

def extract_json(input_text):
    """
    Extrae y convierte un bloque de texto JSON formateado en un diccionario de Python.

    Args:
        input_text (str): Texto de entrada que puede contener un bloque JSON.

    Returns:
        dict: Diccionario con los datos extraídos del JSON o un diccionario vacío en caso de error.
    """
    try:   
        match = re.search(r"```json\n(.*?)```", input_text, re.DOTALL)
        if match:
            return json.loads(match.group(1))
        else:
            return json.loads("{}")
    except:
        return json.loads("{}")
    
def update_data(data):
    """
    Actualiza el campo 'score' en la base de datos 'leads' si se proporciona un email válido.

    Args:
        data (dict): Diccionario que debe contener al menos la clave 'email' y opcionalmente 'score'.

    Returns:
        None
    """

    if (data.get("email") != None):
        if (data.get("score")) != None:
            score = data.get("score")
        else:
            score = 0

        supabase = bd.init_conection_bd()

        response = (
            supabase.table("leads")
            .update({"score": score})
            .eq("email", data.get("email"))
            .execute())
        print(f"Registro Actualizado {response}")
    else:
        print("Registro no actualizado")

def get_data_update(datos, openai_client, my_assistant):
    """
    Procesa los registros de un DataFrame para calcular un score usando OpenAI y actualiza la base de datos.

    Para cada fila del DataFrame:
    - Se convierte en una tabla Markdown.
    - Se envía a un modelo de OpenAI para calcular el 'score'.
    - Se actualiza la base de datos con el score obtenido.

    Args:
        datos (pd.DataFrame): Datos a procesar.
        openai_client (OpenAI): Cliente de OpenAI.
        my_assistant (Assistant): Asistente de OpenAI para procesamiento.

    Returns:
        int: Número total de registros procesados.
    """
    reg = -1

    for index, row in datos.iterrows():
        start = time.perf_counter()
        df1 = pd.DataFrame(row).transpose().to_markdown()
        print(f"registro a calcular score numero: {index + 1}")
        message =f"calcula el score de: {df1}"
        thread = sp.create_thread(openai_client)
        data = sp.process_data(openai_client, my_assistant.id, thread.id, message)
        elapsed = time.perf_counter() - start
        print(f"Tiempo de procesamiento: {elapsed:0.2f} seconds")
        update_data(extract_json(data))
        reg = index
    
    return reg + 1