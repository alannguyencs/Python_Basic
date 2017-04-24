#https://github.com/python-visualization/folium

import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")

map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=12, tiles="Stamen Terrain") #latitude and longitude

def color(elev):
    min_color = int(min(df['ELEV']))
    step = int((max(df['ELEV']) - min_color) / 3)
    if elev in range(min_color, min_color + step):
        return 'green'
    elif elev in range(min_color + step, min_color + 2 * step):
        return 'orange'
    else:
        return 'red'

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev))).add_to(map)




map.save("test_map_2.html")