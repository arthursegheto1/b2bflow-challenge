from db import buscarContatos
from whatsapp import enviarMensagem

print("Buscando contatos no Supabase...")
contatos = buscarContatos()

if not contatos:
    print("Nenhum contato encontrado no banco.")
else:
    print(f"{len(contatos)} contato(s) encontrado(s). Iniciando envio...\n")
    for contato in contatos:
        enviarMensagem(contato["telefone"], contato["nome"])