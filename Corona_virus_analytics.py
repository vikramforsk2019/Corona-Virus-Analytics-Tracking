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



#visualize data using matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

#df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])

df['Active Cases*'].plot.bar();
df['Cured/Discharged/Migrated*'].plot.bar();
df['Deaths**'].plot.bar();
df['Total Confirmed cases*'].plot.bar();

df['Deaths**'].iloc[:5].plot.barh();
df['Deaths**'].iloc[:5].plot.pie();
df['Deaths**'].iloc[:5].plot.line();
df['Deaths**'].iloc[:5].plot.hist();
df['Deaths**'].iloc[:5].plot.box();
df['Deaths**'].iloc[:5].plot.kde();

df['Deaths**'].iloc[:5].plot.scatter();


plt.bar(df['Name of State / UT'].iloc[:5].values,df['Deaths**'].iloc[:5].values,color = "red")



plt.barh(df['Name of State / UT'].iloc[:10].values, df['Deaths**'].iloc[:10].values,color='red')
plt.barh(df['Name of State / UT'].iloc[15:20].values, df['Deaths**'].iloc[15:20].values,color='yellow')
plt.xlabel('States', fontsize=15)
plt.ylabel('NO of Deaths', fontsize=15)
plt.xticks(df['Name of State / UT'].iloc[:5].values, fontsize=10, rotation=45)
plt.title('Corona-Virus Analytics')
plt.show()

#import numpy as np
#df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])

df.iloc[:10,1:5].plot.bar();

df.iloc[:10,1:5].plot.bar(stacked=True);

df.iloc[:10,1:5].plot.barh(stacked=True);


df.iloc[:10,1:5].plot.hist(alpha=0.5);

df.iloc[:10,1:5].plot.hist(stacked=True, bins=20)


df.iloc[:10,1:5].hist(figsize=(6, 4))


