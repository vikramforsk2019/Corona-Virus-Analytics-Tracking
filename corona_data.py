import pandas as pd
from selenium import webdriver
from collections import OrderedDict
#from bs4 import BeautifulSoup as BS
url="https://www.mohfw.gov.in/"
#driver path
browser = webdriver.Firefox(executable_path="/home/jagveer/anaconda3/geckodriver")
browser.get(url)
right_table=browser.find_element_by_class_name('table')

get_school_result = browser.find_element_by_xpath('/html/body/div/div/div/section[3]/div/div/div/h2/a')
get_school_result.click()
get_col=browser.find_element_by_xpath('/html/body/div/div/div/section[3]/div/div/div/div/table/thead/tr')
column_name=get_col.find_elements_by_tag_name('th') #Give column name
col_name=[]
for i in range(len(1,column_name)):
    col_name.append(column_name[i].text)
#A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
col=[]
for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    
    if len(cells) == 6:
       # col.append(column_name[0].text.strip)
       # A.append(cells[0].text.strip())  #no need serial no.
        B.append(cells[1].text.strip())#cells[0] remove bcoz it is se no. it take automaticly
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))
df = pd.DataFrame(col_data) 
df.to_csv("corona.csv")
browser.quit()

