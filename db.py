from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabaseClient = create_client(url, key)

def buscarContatos():
    resposta = supabaseClient.table("contatos").select("nome, telefone").limit(3).execute()
    return resposta.data