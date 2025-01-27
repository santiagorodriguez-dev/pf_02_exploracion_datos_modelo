# Importaciones
import pandas as pd # type: ignore
import sys
sys.path.append("../")
from src import support_open_ai as sp
from src import support_bd as bd
from src import support as sp_c
import os
import dotenv # type: ignore
dotenv.load_dotenv()

# Abre y lee un archivo de texto
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:  # Abre el archivo en modo lectura
            contenido = archivo.read()  # Lee el contenido completo del archivo
            print(f"Contenido del archivo '{nombre_archivo}':\n{contenido}")
            return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe. Verifica la ruta.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def main():
    cadena = "*****************************************************************************************"
    openai_client = sp.init_openai()
    my_assistant = sp.get_assistant(openai_client, os.getenv("OPENAI_API_ASSIS_CONVERSACION"))
    thread = sp.create_thread(openai_client)
    print(cadena)
    mensaje= leer_archivo("datos_test/conversacion.txt")
    print(cadena)
    if not mensaje:  # Verifica si el mensaje está vacío
        print("El mensaje no puede estar vacío. Inténtalo de nuevo.")
    else:
        print(cadena)
        print("Respuesta del asistente:")
        print(sp.process_data_sin_mensajes(openai_client, my_assistant.id, thread.id, mensaje))
        print(cadena)

if __name__ == "__main__":
    main()
