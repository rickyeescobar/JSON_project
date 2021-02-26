import json
infile = open("US_fires_9_1.json","r")
fire_data= json.load(infile)

#-------------------------------------------------
lons, lats, brtnss = [],[],[]

for fire in fire_data:
    if fire['brightness'] > 450:
        brtns = fire['brightness']
        lon = fire['longitude']
        lat = fire['latitude']
        brtnss.append(brtns)
        lons.append(lon)
        lats.append(lat)

#-------------------------------------------------
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker':{
        'size':[.03*brtns for brtns in brtnss],
        'color': brtnss,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'Brightness'}

    }
}]

my_layout = Layout(title="US Fires")

fig = {"data":data, 'layout':my_layout}

offline.plot(fig,filename='US_fires_9_1.html')