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

get_url = "https://10.10.20.65/api/fdm/v6/object/networks?limit=5"

get_headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

get_response = requests.get(get_url, headers=get_headers, verify=False).json()
print(get_response)