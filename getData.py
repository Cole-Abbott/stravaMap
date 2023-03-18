#get data of each activity
import requests
import json

access_token = "APIKEY"
headers = {"Authorization": f"Bearer {access_token}"}

file = open("activityIds.txt", 'r')
file.close()

activity_ids = file.readlines()

activities = []

for activity_id in activity_ids:
    response = requests.get(
        f"https://www.strava.com/api/v3/activities/{activity_id}",
        headers=headers
    )
    activities.append(json.loads(response.text))


file = open("activities.txt", 'w')
file.write(json.dumps(activities))
file.close()
