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
    """
    Inicializa la conexión con la base de datos Supabase.

    Obtiene la URL y la clave de Supabase desde las variables de entorno
    y crea un cliente con opciones específicas.

    Returns:
        Client: Objeto de cliente Supabase configurado.

    Raises:
        ValueError: Si las credenciales no están definidas en las variables de entorno.
    """
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    return create_client(url, key,
      options=ClientOptions(
        postgrest_client_timeout=10,
        storage_client_timeout=10,
        schema="public",
      ))

def select_datos(name_bd):
    """
    Realiza una consulta a la base de datos Supabase y obtiene todos los datos de una tabla.

    Args:
        name_bd (str): Nombre de la tabla de la base de datos a consultar.

    Returns:
        pd.DataFrame: Un DataFrame de Pandas con los datos obtenidos de la tabla.

    Raises:
        RuntimeError: Si hay un error en la consulta a la base de datos.
    """
    supabase = init_conection_bd()
    response_select = supabase.table(name_bd).select("*").order("index").execute()
    datos_select = pd.DataFrame(response_select.data).reset_index(drop=True)
    datos_select = datos_select.drop('index', axis=1)
    return datos_select
 

