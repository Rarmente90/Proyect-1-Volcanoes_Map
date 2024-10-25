import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data["ELEV"])

def colour_producer(el):
	if el >= 3000:
		return 'red'
	elif el >= 1500:
		return 'orange'
	else:
		return 'green'

map = folium.Map(location=[38.2, -99.1], zoom_start=6, tiles='CartoDB Positron')
	
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
	fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el) + " metres", radius=5,
	fill_color=colour_producer(el), color='grey', fill=True, fill_opacity=0.7))
	
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' 
						  if x['properties']['POP2005'] <= 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)


map.add_child(folium.LayerControl())
map.save("InteractiveMap_Circle_Version.html")
