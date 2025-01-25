

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
    try:   
        match = re.search(r"```json\n(.*?)```", input_text, re.DOTALL)
        if match:
            return json.loads(match.group(1))
        else:
            return json.loads("{}")
    except:
        return json.loads("{}")
    
def update_data(data):

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

def get_data_update(datos, openai_client, my_assistant, thread):

    reg = -1

    for index, row in datos.iterrows():
        start = time.perf_counter()
        df1 = pd.DataFrame(row).transpose().to_markdown()
        message =f"calcula el score de: {df1}"
        data = sp.process_data(openai_client, my_assistant.id, thread.id, message)
        elapsed = time.perf_counter() - start
        print(f"Tiempo de procesamiento: {elapsed:0.2f} seconds")
        update_data(extract_json(data))
        reg = index
    
    return reg + 1