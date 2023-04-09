import requests
import sys
import json
from rich import print
import os

# Define your Webex bot access token and room ID
ACCESS_TOKEN = 'MDI0MzYxYzktNTI2NC00OTQyLWFmMzgtMzZkYTEyZjhjOWM1MjZkN2Q3YWUtYWNm_P0A1_ca0eddbe-7060-445d-9128-1246a8ac7a49'
ROOM_ID = os.environ.get('ROOM_ID')

# Define the Webex API URL and headers
API_URL = 'https://webexapis.com/v1/rooms'
HEADERS = {
    'Authorization': f"Bearer {ACCESS_TOKEN}",
}
get_request = requests.get(
    API_URL, headers=HEADERS).json()
items = get_request["items"] #this items is from the list that was generated from the GET request
for item in items:
    title = item["title"]
    if title == "Test1":
        roomId = item["id"]
message = sys.argv[1]
def send_message():
    HEADERS1 =  {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }
    data = {"roomId": f"{roomId}", "text": message}
    return requests.post(
        "https://webexapis.com/v1/messages/",
        headers = HEADERS1,
        data = json.dumps(data),
        verify = True,
    )
send_message()
    # print(f"Room {roomName} has an ID of {roomId}")