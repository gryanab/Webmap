import folium
import pandas

# importing data from data file
data = pandas.read_csv('Volcanoes.txt')

# Env variables
lat = list(data['LAT'])
lon = list(data['LON'])
elevation = list(data['ELEV'])
name = list(data['NAME'])


def elevation_gradient(elevation):
    """
    Simply returns a color gradient according to volcanoes height.
    """

    if elevation < 2000:
        return 'green'
    elif 2000 <= elevation <= 4000:
        return 'orange'
    else:
        return 'red'


# Creating the base map and centering it on the centroid of all lands  (Romania ? )
my_map = folium.Map(location=[lat[0], lon[0]], tiles='Mapbox Bright', zoom_start=5)

# Styling popup information
html = '''
    <h4> Volcano information <h4>
    Name: %s
    Height: %s m
    '''

fg = folium.FeatureGroup(name='My Map')


# Printing all volcanoes location from txt file
for lat, lon, elevation, name in zip(lat, lon, elevation, name):
    iframe = folium.IFrame(html=html % (name, elevation), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(iframe), radius=5, fill=True, # Set fill to True
                                     fill_color=elevation_gradient(elevation),
                                     color=None,
                                     fill_opacity=0.7))

my_map.add_child(fg)
my_map.save('map.html')
