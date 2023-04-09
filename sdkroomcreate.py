from webexteamssdk import WebexTeamsAPI

access_token1 = "MDI0MzYxYzktNTI2NC00OTQyLWFmMzgtMzZkYTEyZjhjOWM1MjZkN2Q3YWUtYWNm_P0A1_ca0eddbe-7060-445d-9128-1246a8ac7a49"

api = WebexTeamsAPI(access_token=access_token1)
rooms = api.rooms.list()
for room in rooms:
    if room.title == "Test2":
        roomId = room.id
        print(roomId)

if 2 == 2:
    api.messages.create(roomId, text ="Test Success!")
