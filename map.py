import folium
import pandas

data = pandas.read_json("Volcanoes.json")
lat = list(data["lat"])
lon = list(data["lon"])
elev = list(data["elevation"])
Map = "Stamen Terrain"

def colorofmark(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 2000:
        return 'orange'
    elif elevation > 2000:
        return 'red'
    else:
        return 'black' 

map = folium.Map(location=[39.0,-99.9],zoom_start=6.0,tiles = Map)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=str(el)+" meters",fill_color=colorofmark(el),color = 'grey',fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=(open("world.json", 'r', encoding='utf-8-sig').read()),

style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000
else 'red','fillOpacity':0.5}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")

