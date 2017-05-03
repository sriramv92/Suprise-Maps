import folium
import pandas as pd

pitt_hoods = r'data/pitt-hoods.json'
pitt_photos = r'data/Pitt-Photos.csv'

pitt_data = pd.read_csv(pitt_photos)

#Let Folium determine the scale

tileset = r'https://api.mapbox.com/styles/v1/sriramv92/cj0ikild9006a2sqpu11nobjm/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoic3JpcmFtdjkyIiwiYSI6ImNpemVsMmdvMzI3cTQycW84dHA1c2V0emQifQ.p3fjmEqOn5MzF9N07t5PUg'

map = folium.Map(location=[40.4406, -79.9959], zoom_start=12, 
                 tiles=tileset, attr='My Data Attribution')
                 
map.choropleth(geo_path=pitt_hoods, data=pitt_data,
             columns=['Neighborhood', 'Photos'],
             threshold_scale=[10, 100, 1000, 10000, 11000, 12000],
             key_on='feature.properties.hood',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Photo Density')
map.save('pittPhotos.html') 