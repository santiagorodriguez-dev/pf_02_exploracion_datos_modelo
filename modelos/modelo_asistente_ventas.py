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

def main():
    cadena = "*****************************************************************************************"
    openai_client = sp.init_openai()
    my_assistant = sp.get_assistant(openai_client, os.getenv("OPENAI_API_ASSIS_VENTA"))
    thread = sp.create_thread(openai_client)

    while True:
        mensaje = input("Introduce un mensaje para interactuar con el chatbot (o escribe 'salir' para terminar): ").strip()
        
        if not mensaje:  # Verifica si el mensaje está vacío
            print("El mensaje no puede estar vacío. Inténtalo de nuevo.")
            continue
        
        if mensaje.lower() == 'salir':  # Salir del bucle si el usuario escribe 'salir'
            print("¡Hasta luego!")
            break
        print(cadena)
        print(f"Consulta realizada:")
        print(f"{mensaje}")
        print(cadena)
        print(f"Respuesta asistente:")
        print(sp.process_data_sin_mensajes(openai_client, my_assistant.id, thread.id, mensaje))
        print(cadena)

if __name__ == "__main__":
    main()
