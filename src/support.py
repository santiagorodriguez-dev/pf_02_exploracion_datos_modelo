
import sys
sys.path.append("../")

import os
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
        print(f"Registro Actualizado {data.get("email")}")
    else:
        print("Registro no actualizado")

def get_data_update(datos, openai_client, my_assistant, thread):

    reg = -1

    i = 0
    for index, row in datos.iterrows():
        df1 = pd.DataFrame(row).transpose().to_markdown()
        message =f"calcula el score de: {df1}"
        assistant_response = sp.process_data(openai_client, my_assistant.id, thread.id, message)
        data = extract_json(assistant_response)
        update_data(data)
        reg = index
        i = i + 1
        if i == 3:
            break
    
    return reg + 1