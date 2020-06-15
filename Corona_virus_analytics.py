#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:11:57 2020

@author: jagveer
"""
import pandas as pd
import folium
df=pd.read_csv("covid19_data_map.csv")
df['log']
map = folium.Map([20.5937,78.9629], zoom_start=5)
tile = folium.TileLayer('Mapbox Bright').add_to(map)
from folium.plugins import MarkerCluster
#adding marker to map
marker_cluster = MarkerCluster().add_to(map)


#importing cluster marker for better look
from folium.plugins import MarkerCluster
#adding marker to map
marker_cluster = MarkerCluster().add_to(map)

#adding marker and popup of city and crime-name
for i in range(0,df.shape[0]):
    folium.Marker([float(df['lat'][i])  ,float(df['log'][i])],popup="city name ="+df['Name of State / UT'][i]).add_to(marker_cluster)

#we can change tiles with help of LayerConrol
folium.LayerControl().add_to(map)

#saving map to a html file
map.save('corona_map.html')

#creating a html iframe
from IPython.display import HTML
HTML('<iframe src=plot_data.html width=300 height=200></iframe>')