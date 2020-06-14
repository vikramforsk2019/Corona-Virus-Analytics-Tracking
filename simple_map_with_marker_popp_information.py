#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 08:24:27 2020

@author: jagveer
"""

import folium
map = folium.Map([20.5937,78.9629], zoom_start=5)
tile = folium.TileLayer('Mapbox Bright').add_to(map)

from folium.plugins import MarkerCluster
#adding marker to map
marker_cluster = MarkerCluster().add_to(map)

data_lat=[78.01,75.7873,75.8648]
data_lon=[27.18,26.9124,25.2138]
#adding marker and popup of city and crime-name
for i in range(0,3):
    folium.Marker([float(data_lon[i]),float(data_lat[i])],popup="hare krishna hare krishna hare hare hare ram").add_to(marker_cluster)

#saving map to a html file
map.save('corona_data.html')

#creating a html iframe
from IPython.display import HTML
HTML('<iframe src=plot_corona.html width=300 height=200></iframe>')
