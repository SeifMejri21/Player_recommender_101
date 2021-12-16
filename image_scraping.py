# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 11:02:54 2021

@author: Administrator
"""


import urllib.request
import requests
from bs4 import BeautifulSoup
import shutil
import re
import os

url1 = "https://fbref.com/en/comps/Big5/2020-2021/possession/players/2020-2021-Big-5-European-Leagues-Stats"

def player_url(url):
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')
    table = soup.find_all('table')
    r=[]
    print(len(table))
    for row in table:
        print("lenth row:  " +str(len(row)))
        col = row.find_all('td')
        print(len(col))
        for c in col[0]:
            print("lenth one column:  " +str(len(c)))
            b = row.find_all('a')
            print(len(b))
            for m in b:
                r.append(m.get('href'))
    w = [a for a in r if re.search('players', a) ]
    lenght = int((len(w)-1)/2)
    x = [w[2*i] for i in range(lenght)]
    return list(set(x))


players_urld = player_url(url1)


def image_scraper(players_urls):
    existing_data = [re.sub('.jpg','',f) for f in os.listdir("C:/Users/Administrator/Desktop/Systeme de recommendation/photo 2")]
    players_urls_2 = [re.sub('-',' ' , a[21:])for a in players_urls]
    for a in  players_urls_2:
        if a in existing_data:
            pass
        else:                    
            for url in players_urls:
                url2 = "https://fbref.com"+url
                html_page = requests.get(url2)
                soup = BeautifulSoup(html_page.content, 'html.parser')
                table = soup.find_all('img')
                print(table[1]['src'])
                player_name = re.sub('-',' ' , url[21:]) 
                resource = urllib.request.urlopen(table[1]['src'])
                output = open("C:/Users/Administrator/Desktop/Systeme de recommendation/photo 2/"+player_name+".jpg","wb")
                output.write(resource.read())
                output.close()



image_scraper(players_urld)








    



