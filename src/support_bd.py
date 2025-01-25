import sys
sys.path.append("../")

import os
import dotenv  # type: ignore
dotenv.load_dotenv()

import os
import pandas as pd  # type: ignore
from supabase import create_client, Client # type: ignore
from supabase.client import ClientOptions # type: ignore


def init_conection_bd():
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    return create_client(url, key,
      options=ClientOptions(
        postgrest_client_timeout=10,
        storage_client_timeout=10,
        schema="public",
      ))

def select_datos(name_bd):
    supabase = init_conection_bd()
    response_select = supabase.table(name_bd).select("*").order("index").execute()
    datos_select = pd.DataFrame(response_select.data).reset_index(drop=True)
    datos_select = datos_select.drop('index', axis=1)
    return datos_select
 

