#plot activities on map
import json
import polyline
import folium

file = open("activities.txt", 'r')
activities = json.loads(file.read())

# Create a map centered on a specific location
map = folium.Map(location=[42.05227, -87.69426], zoom_start=12)

count = 0

for activity in activities:
    # Define the polyline
    if 'map' in activity.keys():
        if activity['map']['polyline'] == "":
            continue
        count += 1
        print(count)
        locations = polyline.decode(activity['map']['polyline'])

        # Add the polyline to the map
        folium.PolyLine(locations=locations, color='red', weight=2.5, opacity=1).add_to(map)

# Display the map
map.save("Map.html")