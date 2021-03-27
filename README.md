# Scraper-Bitcoin
## Scraper:

### Hoe gebruik je deze code:
- Installeer Ubuntu op een virtual machine.
- Installeer Python3 op de virtual machine.
  - Ga naar de terminal en typ het volgende:
    - sudo apt install python3
    - python3 --version (zo kan je zien welke versie geïnstalleerd is.
- Installeer onderstaande libraries in de terminal:
  - bs4 en Beautifulsoup:
    - pip3 install bs4
    - pip3 install Beautifulsoup4
  - requests:
    - pip3 install requests
  - Pandas
    - pip3 install pandas
  - Datetime:
    - pip3 install datetime
 - Zorg dat je in de terminal in de map zit, waar je bestand staat.
    - cd 'naam map'
 - Om het bestand uit te voeren, typ je in de terminal:
    - python3 'naam bestand'.py
 - Nu gaat het bestand worden uitgevoerd.
 - Om het bestand te stoppen, typ je:
    -  ctrl + C

### Hoe werkt de code:
Eerst importeer je de juiste libraries:
  - import bs4
  - from bs4 import BeautifulSoup
  - import requests
  - import re
  - import pandas as pd
  - import datetime
  - from datetime import timedelta
  - from datetime import datetime

In de Main code, declareer ik eerst de variabelen. Ik maak een dataframe aan en ik zet de juiste url in 'url'. Ook declareer ik de actuele tijd. Deze doe ik min een uur, aangezien de gegevens die wij binnenkrijgen een uur achter lopen. Deze variabele zet ik om naar een string in de vorm 'uur:minuten'. Dan volgt er een while loop die altijd True is, zodat de code altijd blijft runnen tot we die zelf stoppen.

Nu gaan we naar onze functie Scraper(). Hier zijn twee global variabelen aangemaakt, ozdat we deze variabelen over heel de code kunnen meegeven met dezelfde inhoud. Dan roep ik de website aan en ga ik de html code in een variabele zetten. Nu zoek ik al de div's waarin al de nodige informatie staat. Voor al deze div's ga ik de hash zoeken, deze wordt aangeduid door '<a>'. De rest van de informatie heeft dezelfde class, dit ga ik ook zoeken. De tijd staat op plaats nul. Als deze kleiner is dan onze actuele tijd dan gaan we naar de volgende hash aangezien we al een minuut verder zitten (11:11 < 11:12 en we zitten bij 11:12). Als de tijd gelijk is aan de actuele tijd dan gaan we de rest van informatie uit de website halen. BTC bevindt zich op plaats 1 en USD bevindt zich op plaats 2. We gaan 'BTC','$' ,',' verwijderen zodat we enkel het getal overhebben en deze zetten we om van een string naar een getal. Hierna zetten we de gevonden informatie in de dataframe en nu gaan we naar de volgende hash.

Als de tijd groter is dan de actuele tijd dan gaan we de dataframe sorteren op de waarde van USD zodat de hoogste waarde van boven komt te staan en dan printen we de hoogste waardemet de bijhorende informatie uit. Aangezien we het grootste getal van deze minuut hebben uitgeprint, gaan we de gesorteerde dataframe leegmaken. We stellen de actuele tijd gelijk aan tijd en we maken de dataframe leeg. Hierna voegen we de informatie van de actuele hash aan de dataframe toe anders slagen we deze over. Zo gaat het programma verder tot het handmatig gestopt wordt.

## Mongo:

Je moet eerst de vorige stappen hebben uitgevoerd. Dan moet je mongodb installeren op de ubuntu machine. Dit doe je door 'bash.sh' te laten draaien in de terminal.
  - Om het script te runnen moet je eerst toegang geven tot het script.
    - chmod +x /path/to/bashscript.sh
  - Om het te laten runnen, typ je:
    - /path/to/bashscript.sh
  
Het script 'bash.sh' gaat mongodb installeren, starten en een database aanmaken. Als dit gebeurd is, ga je het script 'scrapermongo.py' runnen. Deze code gaat verbinding maken met mongodb, een collectie aan de database toevoegen en per minuut al de gegevens in een jsonfile steken. Deze jsonfile wordt dan toegevoegd aan de collectie. De naam van de database is Bitcoin en de collectie is Transaction_info. Om te kijken of de database is aangemaakt typ je in de terminal 'Show dbs'. Als 'Bitcoin hier bij staat is het gelukt. Om te informatie te bekijken in de collectie typ je 'Use database_name', 'db.collection_name.find().pretty()', dit gaat al de gegevens uitprinten.

Om te kunnen werken met mongodb in python, moeten we eerst nog libraries importeren.
  - pymongo:
    - pip3 install pymongo

In dit script gaan we terug alle gegevens halen van de website maar ipv ze in een database te steken, gaan we ze opslaan in een dictionary. Deze dictionary gaat per minuut in een jsonfile worden opgeslagen 'information.json'. Deze jsonfile wordt wan opgeslagen in onze Bitcoin database. Dan maken we de dictionary leeg, zodat de informatie van de volgende minuut opgeslagen kan worden. Dit gebeurd de hele tijd opnieuw tot je de code stop zet.

## Redis:
Als je de vorige stappen hebt uitgevoerd, kan je redis.sh downloaden. In deze file gaan we redis installeren en checken of het werkt.
  - Om het script te runnen moet je eerst toegang geven tot het script.
    - chmod +x /path/to/bashscript.sh
  - Om het te laten runnen, typ je:
    - /path/to/bashscript.sh
 
 We beginnen met het script Scraperredis.py uit te voeren. Om dit te laten werken moet je enkel nog redis in python installeren.
  - Pip3 install redis

We zetten alles in een dataframe en elke minuut slagen we deze op in redis. Als deze is opgeslagen verwijderen we de gegevens in de dataframe en gaan we de volgende minuut scrapen.

In het bestand Redis.py, gaan we eerst onze mongo database en collectie aanmaken. Dan gaan we de data die we opgeslagen hebben in redis terughalen. Deze informatie zetten we om naar een dictionary om het goed te kunnen sorteren. We nemen de eerste key en de informatie die bij de key hoort, aangezien dit de hoogste waarde heeft. Dit gaan we in onze mongo database plaatsen en na 1 minuut gaan we redis clearen.

## Docker 01:
Eerst moet je docker installeren op je pc. Dan moet je redis en mongo installeren op docker. Je typt in de terminal het volgende:
  - sudo docker pull mongo
  - sudo docker pull redis
Eens dit gebeurd is moet je zeggen op welke poort deze containters moeten draaien zodat je deze kan aanroepen in je code. Dit typ je in de terminal:
  - sudo docker run --name Redis -d redis #on port 6379 default port
  - sudo docker run --name Mongodb -d mongo #on port 27017 default port
Nu moet je de poorten in de code ook aanpassen zodat ze kunnne communiceren met elkaar. In je code typ je:
    - r=redis.Redis(host='localhost', port=6379, db=0) (voor redis) 
    - client = pymongo.MongoClient("mongodb://localhost:27017/") (voor mongo)
