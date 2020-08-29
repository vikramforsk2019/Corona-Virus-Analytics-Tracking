#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:07:34 2020

@author: jagveer
"""

import pandas as pd
from selenium import webdriver
from datetime import datetime
#from collections import OrderedDict
#from bs4 import BeautifulSoup as BS
url="https://www.worldometers.info/coronavirus/"
#driver path
browser = webdriver.Firefox(executable_path="/home/jagveer/anaconda3/geckodriver")
browser.get(url)
right_table=browser.find_element_by_class_name('table')

column_name=right_table.find_elements_by_tag_name('th') #Give column name
col_name=[]
for i in range(1,len(column_name)-1):
    col_name.append(column_name[i].text)
    
get_corona = browser.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]')
right_table=get_corona.find_elements_by_tag_name('tr')

data_list=[]
data_list2=[]
for row in right_table:
  cells = row.find_elements_by_tag_name('td')
  for i in  cells:    
     data_list.append(i.text)
  data_list2.append(data_list)
  data_list=[]
df=pd.DataFrame(data_list2)  
df=df.iloc[:,1:14]
df.columns=col_name

dir_csv='covid19_daily'
filename = datetime.now().strftime('Date-%Y-%m-%d.csv')
df.to_csv(dir_csv+'/'+filename,index= False)
browser.quit()

df=pd.read_csv('covid19_world_data.csv')
new_df = df.dropna(axis=0,how='all')

new_df = new_df.dropna(axis=1,thresh=30)
