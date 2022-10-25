#from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import requests
import pandas as pd
START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

req = requests.get(START_URL)
print(req)

soup = bs(req.text,'html.parser')

startable = soup.find('table')

templist= []
tablerows = startable.find_all('tr')
for tr in tablerows:
    th = tr.find_all('th')
    row = [i.text.rstrip() for i in th]
    templist.append(row)

Propernames = []
Dist =[]
Mass = []
Radi =[]
Lumi = []

for i in range(1,len(templist)):
    Propernames.append(templist[i][2])
    Dist.append(templist[i][4])
    Mass.append(templist[i][6])
    Radi.append(templist[i][7])
    Lumi.append(templist[i][8])
    
df = pd.DataFrame(list(zip(Propernames,Dist,Mass,Radi,Lumi)),columns=['Proper name','Distance','Mass','Radius','Luminosity'])
print(df)
df.to_csv('brightstars.csv')