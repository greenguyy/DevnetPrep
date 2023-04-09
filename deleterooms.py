import requests
from rich import print
import json


# Define your Webex bot access token and room ID
ACCESS_TOKEN = 'MDI0MzYxYzktNTI2NC00OTQyLWFmMzgtMzZkYTEyZjhjOWM1MjZkN2Q3YWUtYWNm_P0A1_ca0eddbe-7060-445d-9128-1246a8ac7a49'


# Define the Webex API URL and headers
API_URL = 'https://webexapis.com/v1/rooms'
HEADERS = {
    'Authorization': f"Bearer {ACCESS_TOKEN}"
}
get_response = requests.get(API_URL,headers=HEADERS).json()
items = get_response["items"]
for item in items:
    title = item["title"]
    if title != "Hello" and title != "TestDevnet":
        roomId = item["id"]
        roomId_url = f"https://webexapis.com/v1/rooms/{roomId}"
        HEADERS = {'Authorization': f"Bearer {ACCESS_TOKEN}"}
        del_response = requests.delete(roomId_url, headers=HEADERS)
        del_response.raise_for_status()
        if del_response.status_code == 204:
            print(f"Room {title}: [red] DELETED [/red]")
            