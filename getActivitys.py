#gets all of a users activities
import requests
import json

access_token = "APIKEY"
headers = {"Authorization": f"Bearer {access_token}"}
file = open("activityIds.txt", 'w')
page = 1

while True:
    response = requests.get(
        f"https://www.strava.com/api/v3/activities?&per_page=50&page={page}",
        headers=headers
    )

    data = json.loads(response.text)

    if not data:
        break

    for activity in data:
        file.write(f"{activity['id']}\n")

    page += 1
    

file.close()