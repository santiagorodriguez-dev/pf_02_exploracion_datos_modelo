# Importaciones
import pandas as pd
import sys
sys.path.append("../")
from src import support_open_ai as sp
from src import support_bd as bd
from src import support as sp_c
import os
import dotenv # type: ignore
dotenv.load_dotenv()


def modelo_predictivo():
   
   openai_client = sp.init_openai()
   assis_predict = sp.get_assistant(openai_client, os.getenv("OPENAI_API_ASSIS_PREDICCION"))
   thread = sp.create_thread(openai_client)

   datos = bd.select_datos("leads")

   reg = sp_c.get_data_update(datos, openai_client, assis_predict, thread)

   print(f"Se procesaron {reg} registros")


def main():
   modelo_predictivo()
   
if __name__ == "__main__":
   main()
