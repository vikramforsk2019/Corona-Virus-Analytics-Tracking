import pandas as pd
from selenium import webdriver
from collections import OrderedDict
#from bs4 import BeautifulSoup as BS
url="https://www.mohfw.gov.in/"
#driver path
browser = webdriver.Firefox(executable_path="/home/vikram/anaconda3/geckodriver")
browser.get(url)
right_table=browser.find_element_by_class_name('table')

get_corona = browser.find_element_by_xpath('/html/body/div/div/div/section[3]/div/div/div/h2/a')
get_corona.click()
get_data=browser.find_element_by_xpath('/html/body/div/div/div/section[3]/div/div/div/div/table/tbody')
#column_name=browser.find_elements_by_xpath('/html/body/div/div/div/section[3]/div/div/div/div/table/thead') #Give column name
col_name=['Name of State','Active Cases*','Active Cases* yesterday','Cured/Discharged/Migrated*','Recover since yesterday','Deaths**','Deaths** since yesterday']
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
col=[]
for row in get_data.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    
    if len(cells) == 8:
       # col.append(column_name[0].text.strip)
       # A.append(cells[0].text.strip())  #no need serial no.
        B.append(cells[1].text.strip())#cells[0] remove bcoz it is se no. it take automaticly
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        G.append(cells[6].text.strip())
        H.append(cells[7].text.strip())        
col_data = OrderedDict(zip(col_name,[B,C,D,E,F,G,H]))
df = pd.DataFrame(col_data) 
df.to_csv("covid19_data.csv",index= False)  #scrapped covid 19 data from live website in india.
browser.quit()

#find the coordinate of the states in india using state name in covid19.csv
import pandas as pd
from selenium import webdriver
import requests
import json
data_lon=[]
data_lat=[]
url1 = "http://api.openweathermap.org/data/2.5/weather?q="
url2 = ""
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

df=pd.read_csv('covid19_data.csv')
#df=df.drop(["Unnamed: 0"],axis=1)
df=df.iloc[:35,:]
df.info()

url2=df.iloc[:,0]
url = url1 + url2 + url3

data_lon=[]
data_lat=[]

for i in range(0,len(url)):
    #print(url[i])
    response = requests.get(url[i])
    data= response.content
    new_data=json.loads(data)
    if new_data['cod']=='404':
        print('coordinate not:',url2[i])
        if(url2[i]=="Andaman and Nicobar Islands"):
            data_lon.insert(i,"92.6586")
            data_lat.insert(i,"11.7401")
        elif(url2[i]=="Dadra and Nagar Haveli and Daman and Diu"):
            data_lon.insert(i,"72.8397")
            data_lat.insert(i,"20.4283")
        elif(url2[i]=="Jammu and Kashmir"):
            data_lon.insert(i,"76.5762")
            data_lat.insert(i,"33.7782")
        elif(url2[i]=="Ladakh"):
            data_lon.insert(i,"77.577049")
            data_lat.insert(i,"34.152588")
        elif(url2[i]=="Telengana"):
            data_lon.insert(i,"79.0193")
            data_lat.insert(i,"18.1124")
        else:
            print('not found')
    else:
        print(url2[i])
        data_lon.insert(i,new_data["coord"]["lon"])
        data_lat.insert(i,new_data["coord"]["lat"])
df['log']=data_lon
df['lat']=data_lat

df.to_csv("covid19_data_map.csv",index = False)









