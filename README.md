# Scraper-Bitcoin

## Hoe gebruik je deze code:
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

## Hoe werkt de code:
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

    
