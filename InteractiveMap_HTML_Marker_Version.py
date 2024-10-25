import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """ Volcano name:<br> <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br> Height: %s m """

def colour_producer(el):
	if el >= 3000:
		return 'red'
	elif el >= 1500:
		return 'orange'
	else:
		return 'green'

map = folium.Map(location=[38.2, -99.1], zoom_start=6, tiles='CartoDB Positron')
	
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(lat, lon, elev, name):
	iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
	fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))
	
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' 
						  if x['properties']['POP2005'] <= 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)


map.add_child(folium.LayerControl())
map.save("InteractiveMap_HTML_Marker_Version.html")
