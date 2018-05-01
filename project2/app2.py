# Second app from python udemy couse

import json
import folium as fl
import pandas as pd

data = pd.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = fl.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg = fl.FeatureGroup(name="Elevation")

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(fl.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m", fill=True,
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7)) 
    # print '{} {}'.format(el, color_producer(el))

fg2 = fl.FeatureGroup(name='Population')
fg2.add_child(fl.GeoJson(data=open('world.json', 'r').read()))

# print str(fl.GeoJson(open('world.json', 'r').read()))

map.add_child(fg)
# map.add_child(fg2)
map.add_child(fl.LayerControl())

map.save("elevation_population_map.html")
