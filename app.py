import folium
import pandas

# importing data from data file
data = pandas.read_csv('Volcanoes.txt')

# Env variables
lat = list(data['LAT'])
lon = list(data['LON'])
elevation = list(data['ELEV'])
name = list(data['NAME'])


def elevation_gradient(elev):
    """
    Simply returns a color gradient according to volcanoes height.
    """

    if elev < 2000:
        return 'green'
    elif 2000 <= elev <= 4000:
        return 'orange'
    else:
        return 'red'


# Creating the base map and centering it on Romania (Centroid ?)
my_map = folium.Map(location=[44, 29], tiles='Mapbox Bright', zoom_start=2)

# Styling popup information
html = '''
    <h4> Volcano information <h4>
    Name: %s
    Height: %s m
    '''

fg_volcanoes = folium.FeatureGroup(name='Volcanoes')

# Printing all volcanoes location from txt file
for lat, lon, elevation, name in zip(lat, lon, elevation, name):
    iframe = folium.IFrame(html=html % (name, elevation), width=200, height=100)
    fg_volcanoes.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(iframe), radius=5, fill=True,
                                               fill_color=elevation_gradient(elevation),
                                               color=None,
                                               fill_opacity=0.7))

fg_population = folium.FeatureGroup(name='Population')

# Showing world population from 2005
fg_population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                       style_function=lambda x: {'fillColor':
                                                                     'yellow' if x['properties']['POP2005'] < 10000000
                                                                     else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                                     else 'red'}))


my_map.add_child(fg_volcanoes)
my_map.add_child(fg_population)
my_map.add_child(folium.LayerControl())
my_map.save('map.html')
