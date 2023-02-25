import requests as r
from requests.auth import HTTPBasicAuth
import json

url = "<url_pagina>"

login = "<seu-login-atlassian"
auth = HTTPBasicAuth(
    login,
    "<seu-token>",
)

headers = {"Accept": "application/json", "Content-Type": "application/json"}

payload = json.dumps(
    {
        "version": {
            "number": 5,  # Pegar o numero da versão corrente e +1 (pois toda vez que atualizar precisa )
            "message": "Integração de versionamento: Testando publicação confluence",  # Inicio de mensagem padrão
        },
        "title": "Teste Script",
        "type": "page",
        "status": "current",
        "ancestors": [{"id": 1404534787}],  # Id da pagina pai
        "body": {  # Enviar somente um objeto
            "storage": {"value": "Testando", "representation": "storage"},
        },
    }
)


response = r.request("PUT", url, data=payload, headers=headers, auth=auth)


print(
    json.dumps(
        json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
    )
)
