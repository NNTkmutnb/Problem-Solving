import folium
from folium.plugins import AntPath

# create a map object
mapObj = folium.Map(location=[18.906286495910905, 79.40917968750001],
                    zoom_start=5)

# latitude longitude coordinates of the lines
pathLatLngs = [(19.082502,72.7163773), (12.9541467,77.3191065), (23.199546,77.3234906), (19.0860154,82.0145882), (22.5355649,88.2649519)]
pathLatLngs2 = [(13.0478078,80.0442025), (17.6615468,75.8774177), (24.6083586,73.6636725), (26.8488213,80.860112)]

# create antpaths and add to map
AntPath(pathLatLngs, delay=400, dash_array=[30,15], color="red", weight=5).add_to(mapObj)

AntPath(pathLatLngs2, delay=200, dash_array=[10,50], color="blue", pulse_color="orange", weight=5, opacity=1).add_to(mapObj)

# save the map object as a html
mapObj.save('output.html')