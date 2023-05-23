import requests
import json
import os
from rich import print

requests.packages.urllib3.disable_warnings()
clear_screen = "clear"
os.system(clear_screen)

url = "https://10.10.20.65/api/fdm/v6/fdm/token"

payload = {"grant_type": "password", "username": "admin", "password": "Sbxftd1234!"}
headers = {"Accept": "application/json", "Content-Type": "application/json"}

token_response = requests.post(
    url, headers=headers, data=json.dumps(payload), verify=False #verify is False here
)
token_response.raise_for_status()
if token_response.status_code == 200:
    print("Token Successfully Received...\n")

token = token_response.json()["access_token"] #to get the token and store it as an object

url = "https://10.10.20.65/api/fdm/v6/object/networks"

payload = {
    "name": "IPvZero1",
    "description": "DEVCOR",
    "subType": "NETWORK",
    "value": "199.99.99.0/24",
    "dnsResolution": "IPV4_ONLY",
    "type": "networkobject",
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}",
}

create_response = requests.post(
    url, headers=headers, data=json.dumps(payload), verify=False
)
create_response.raise_for_status()
if create_response.status_code == 200:
    print("[u]SUCCESS: New Object Created status code")
    print(create_response.text)
