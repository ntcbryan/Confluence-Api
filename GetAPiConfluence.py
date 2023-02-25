import requests as r
from requests.auth import HTTPBasicAuth
import json

url = "<sua-url>"
login = "<seu-email>"
auth = HTTPBasicAuth(
    login,
    "<seu-token>",  # gerado nas configurações do perfil
)

headers = {
    "Accept": "application/json",
}

response = r.request("GET", url, headers=headers, auth=auth)


print(
    json.dumps(
        json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
    )
)
