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
        access_token = "MDI0MzYxYzktNTI2NC00OTQyLWFmMzgtMzZkYTEyZjhjOWM1MjZkN2Q3YWUtYWNm_P0A1_ca0eddbe-7060-445d-9128-1246a8ac7a49"
        membership_url = "https://webexapis.com/v1/memberships"
        HEADERS = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }
        body = {
            "roomId": f"{roomId}",
            "personEmail": "devnetCBTbot@webex.bot",
            "isModerator": False,
        }
        post_response = requests.post(
            membership_url,headers=HEADERS, data=json.dumps(body) # dump the body from on top into the put request
        )
        print(post_response)

        post_response.raise_for_status()
        if post_response.status_code == 200:
            print(f"[green]Success![/green] user:devnetCBTbot@webex.bot added to {title}")
        # print(f"Room {HEADERS} has an ID of {body}")