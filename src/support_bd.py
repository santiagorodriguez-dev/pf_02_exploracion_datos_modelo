import sys
sys.path.append("../")

import os
import dotenv  # type: ignore
dotenv.load_dotenv()

import os
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

