import bs4
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime
from datetime import timedelta
from datetime import datetime

import json
import pymongo
from pymongo import MongoClient
import urllib.parse


def Scraper():
    global dataframe #zodat we over heel het programma onze dataframe hebben met de variabelen erin
    global current 

    website = requests.get(url) #we roepen de website aan
    soup = BeautifulSoup(website.content, 'html.parser') #we willen de htmlcode

    classes=soup.find_all('div',class_='sc-1g6z4xm-0 hXyplo') # stukje waarin al de variabelen staan

    for clas in classes: #voor elk stukje
        #print(clas)
        hashes=clas.find('a') #gaan we de hash zoeken, <a>
        #print(hashes.text)
        informatie=clas.find_all('span',class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC') #al de informatie heeft dezelfde class

        tijd=informatie[0].text #de tijd staat op plaats nul
        if tijd<current: #als de tijd kleiner is dan de current tijd dan gaan we naar de volgende hash kijken omdat we al bij de volgende minuut zitten (11:11<11:12 en we zitten bij 11:12)
            break
        else:
            if tijd==current: #als de tijd hetzelfde is
                
                waardeBTC=informatie[1].text #we halen de amount BTC eruit deze staat op plaats 1
                getal=re.sub('BTC','',waardeBTC) #we doen BTC weg
                value=float(getal) #we zetten het om naar een getal
                
                waardeUSD=informatie[2].text
                getalUSD=re.sub('[$,]','',waardeUSD)
                #print(getalUSD)
                valueUSD=float(getalUSD)

                # we voegen de variabelen toe aan een dictionary
                data['info'].append({"Hash" : hashes.text, "Time" : tijd,"Amount (BTC)" : value, "Amount (USD)": valueUSD})
               
               
                
            else: #als de tijd niet hetzelfde is als current
                # we schrijven de data weg naar een json file.
                with open('information.json', 'w') as json_file:
                    json.dump(data, json_file)

                with open('information.json','r') as file: 
                    file_data = json.load(file)
                x = mycol.insert_one(file_data)

                # for y in mycol.find():
                #     print(y) 
                data.clear()
                data['info']=[]
                current=tijd #current is de tijd dus de volgende minuut
                
                #we voegen de informatie toe aan de dataframe, dit doen we hier aangezien we anders deze hash overslagen
                waardeBTC=informatie[1].text
                getal=re.sub('BTC','',waardeBTC)
                value=float(getal)
            
                waardeUSD=informatie[2].text
                getalUSD=re.sub('[$,]','',waardeUSD)
                #print(getalUSD)
                valueUSD=float(getalUSD)

                data['info'].append({"Hash" : hashes.text, "Time" : tijd,"Amount (BTC)" : value, "Amount (USD)": valueUSD})
               

                
               

           

#variabelen
data={}
data['info']=[]

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["Bitcoin"]
mycol = mydb["Transaction_info"]  



url="https://www.blockchain.com/btc/unconfirmed-transactions" # url declareren

currenttest=(datetime.now()) #current is de tijd dat het nu is
test= currenttest-timedelta(hours=1) #de gegevens die we krijgen zijn 1 uur vroeger dus we doen de tijd van nu min 1 uur (11:08-1 = 10:08)
current=test.strftime('%H:%M') #we zetten het om naar een string in de vorm uur:minuten

while True: #zodat ons programma altijd blijft draaien
    Scraper()
    
