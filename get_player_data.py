#Imma try getting my data from futbin
import requests
from bs4 import BeautifulSoup
import sys
import time
import js2xml
import re


'''
r = requests.get('https://www.futwiz.com/en/fifa23/players')


soup = BeautifulSoup(r.content, 'html.parser')
'''
'''
This code writes the website data to a text file
with open('futwiz_data.txt', 'w') as f:
    f.write(soup.prettify())
f.close()
'''
'''
lis = soup.find_all("div", class_="col-2")
print(lis[1])
'''




#Code aboves does all the work in making the database of player: Now code below will work on extracting graphs from each player





soup = BeautifulSoup(requests.get("https://www.futbin.com/23/sales/26384/antonio-rudiger?platform=ps").content, "html.parser")
script = soup.find("script", text=re.compile("Highcharts.chart")).text
# script = soup.find("script", text=re.compile("precipchartcontainer")).text if you want precipitation data
parsed = js2xml.parse(script)
print(js2xml.pretty_print(parsed))



