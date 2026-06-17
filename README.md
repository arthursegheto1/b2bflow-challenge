# b2bflow-challenge

Script Python que lê contatos cadastrados no Supabase e envia mensagens personalizadas via WhatsApp usando a Z-API.

## Pré-requisitos

- Python 3.x
- Conta no [Supabase](https://supabase.com)
- Conta na [Z-API](https://z-api.io) com um número conectado

## Setup da tabela

No painel do Supabase, crie uma tabela chamada `contatos` com as seguintes colunas:

| Coluna | Tipo |
|---|---|
| id | int8 (primary key, autoincrement) |
| nome | text |
| telefone | text |

Insira os contatos manualmente pelo Table Editor. O telefone deve estar no formato internacional sem símbolos, por exemplo: `5531999999999`.

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_KEY=sua_anon_key_aqui

ZAPI_INSTANCE=sua_instance_aqui
ZAPI_TOKEN=seu_token_aqui
ZAPI_CLIENT_TOKEN=seu_client_token_aqui
```

## Como rodar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o script:

```bash
python main.py
```

O script busca até 3 contatos no banco e envia para cada um a mensagem:

```
Olá, <nome_contato> tudo bem com você?
```