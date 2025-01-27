# Importaciones
import pandas as pd # type: ignore
import time
import sys
sys.path.append("../")

import os
import dotenv # type: ignore
dotenv.load_dotenv()
from openai import OpenAI # type: ignore

def init_openai():
    os.getenv("OPENAI_API_KEY")
    return OpenAI()

def get_assistant(openai_client, assistant_id):
    return openai_client.beta.assistants.retrieve(
        assistant_id=assistant_id
    )

def create_thread(openai_client):
    return openai_client.beta.threads.create()

def process_data(openai_client, assistant_id, thread_id, message):

    openai_client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message,
    )

    run = openai_client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    run_status = openai_client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run.id
    )

    while True:
        run_status = openai_client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        if run_status.status == "completed":
            print("se completó exitosamente.")
            break
        elif run_status.status == "failed":
            print("petó.")
            break
        else:
            print(f"Esperando a que se complete...{run.id}")
            time.sleep(3)

    print(f"Thread ID: {thread_id}")
    print(f"Run ID: {run.id}")
    print(f"Run Status: {run_status.status}")

    response_messages = openai_client.beta.threads.messages.list(thread_id=thread_id)

    assistant_response = None
    for message in response_messages.data:
            assistant_response = "\n".join([block.text.value for block in message.content])
            break

    if assistant_response:
        print(f"respuesta procesada del asistente.")
    else:
        print("No se encontró una respuesta del asistente.")

    return assistant_response

def process_data_sin_mensajes(openai_client, assistant_id, thread_id, message):

    assistant_response = "No se encontró una respuesta del asistente."

    openai_client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message,
    )

    run = openai_client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    run_status = openai_client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run.id
    )

    while True:
        run_status = openai_client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        if run_status.status == "completed":
            break
        elif run_status.status == "failed":
            print("Error, no se encontró una respuesta del asistente. Fallo en llamada a OpenAI.")
            return assistant_response
        else:
            time.sleep(3)

    response_messages = openai_client.beta.threads.messages.list(thread_id=thread_id)

    
    for message in response_messages.data:
            assistant_response = "\n".join([block.text.value for block in message.content])
            break

   
    return assistant_response



