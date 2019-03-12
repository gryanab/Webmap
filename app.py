import folium
import pandas


data = pandas.read_csv('Volcanoes.txt')

lat = list(data['LAT'])
lon = list(data['LON'])

my_map = folium.Map(location=[-34, -56], tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='My Map')


for lat, lon in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lat, lon], popup='Marker here', icon=folium.Icon(color='green')))

my_map.add_child(fg)
my_map.save('map.html')
