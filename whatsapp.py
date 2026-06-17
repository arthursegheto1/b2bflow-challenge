import httpx
from dotenv import load_dotenv
import os

load_dotenv()

zapiInstance = os.getenv("ZAPI_INSTANCE")
zapiToken = os.getenv("ZAPI_TOKEN")
zapiClientToken = os.getenv("ZAPI_CLIENT_TOKEN")

url = f"https://api.z-api.io/instances/{zapiInstance}/token/{zapiToken}/send-text"

def enviarMensagem(telefone, nome):
    headers = {
        "Content-Type": "application/json",
        "Client-Token": zapiClientToken
    }

    payload = {
        "phone": telefone,
        "message": f"Olá, {nome} tudo bem com você?"
    }

    try:
        resposta = httpx.post(url, json=payload, headers=headers)
        resposta.raise_for_status()
        print(f"✓ Mensagem enviada para {nome} ({telefone})")
    except httpx.HTTPStatusError as e:
        print(f"✗ Erro ao enviar para {nome}: {e.response.status_code} — {e.response.text}")
    except httpx.RequestError as e:
        print(f"✗ Falha de conexão ao tentar enviar para {nome}: {e}")