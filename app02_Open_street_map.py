#https://github.com/python-visualization/folium

import folium

map = folium.Map(location=[45.372, -121.697], zoom_start=12, tiles="Stamen Terrain") #latitude and longitude
folium.Marker(location=[45.372, -121.697], popup = "Mt. Hood Meadow").add_to(map)
folium.Marker(location=[45.322, -121.627], popup = "Timberlake").add_to(map)




map.save("test_map.html")