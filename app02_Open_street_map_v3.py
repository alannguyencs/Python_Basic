#https://github.com/python-visualization/folium

import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")

map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=6, tiles="Stamen Terrain") #latitude and longitude

def color(elev):
    min_color = int(min(df['ELEV']))
    step = int((max(df['ELEV']) - min_color) / 3)
    if elev in range(min_color, min_color + step):
        return 'green'
    elif elev in range(min_color + step, min_color + 2 * step):
        return 'orange'
    else:
        return 'red'


fg = folium.FeatureGroup(name = "Volcano Locations")

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    fg.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev))))


map.add_child(fg)


# map.add_child(folium.GeoJson(data = open('world_population.json'),
#                              name = 'World population',
#                              style_function=lambda x: {'fillcolor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 <  x['properties']['POP2005'] < 20000000 else 'red'}))
#


map.add_child(folium.GeoJson(data = open('world_population.json'),
                             name = 'World population',
                             style_function=lambda x: {'fillcolor': 'red'}))

map.add_child(folium.LayerControl())

map.save(outfile="test_map_3.html")