from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
time.sleep(10)

page=requests.get(START_URL)
soup=BeautifulSoup(page.text,"html.parser")
brown_table=soup.find_all("table")
table_rows=brown_table[7].find_all("tr")

dwarfs=[]
consts=[]
distance=[]
mass=[]
radius=[]
discoyear=[]

temp_list=[]

for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

#print(temp_list)
for i in range(1,len(temp_list)):
    dwarfs.append(temp_list[i][0])
    consts.append(temp_list[i][1])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
    discoyear.append(temp_list[i][9])

df=pd.DataFrame(list(zip(dwarfs,consts,distance,mass,radius,discoyear)),columns=['dwarf name','constellation','distance','mass','radius',"discovery"])
df.to_csv("scraped.csv")