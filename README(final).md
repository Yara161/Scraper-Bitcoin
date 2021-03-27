# Hoe gebruik je deze code?
Als je wilt zien dat je containers runnen, kun je docker desktop installeren via volgende link. Dit is optioneel.

https://docs.docker.com/get-docker/ 

Om te kijken dat de data in de mongodb databases komt, kun je mongodb compass installeren.

https://www.mongodb.com/try/download/compass?tck=docs_compass

## Images aanmaken
We maken eerste de Redis image aan. Dit doe je door hetvolgende in de terminal te typen:
  - docker pull redis
  - 
De image van Mongo gaan we opdezelfde manier aanmaken:
  - docker pull mongo

Nu gaan we onze eigen images aanmaken, voor de 'Scraper' en de 'ToMongo'. Zorg dat je in dezelfde map zit als waar je dockerfile staat.
Mijn beide dockerfiles noemen 'Dockerfile', maar staan in een aparte map. In de terminal typ je:
  - docker build -t scraper_main ./Scraper
  - docker build -t scraper_tomongo ./ToMongo
  
In docker desktop kun je zien dat er nu vier images zijn aangemaakt:
  - redis
  - mongo
  - scraper_main
  - scraper_tomongo

## Containers aanmaken en docker-compose runnen
De containers worden aangemaakt door de docker-compose file. Ook starten onze containers door deze file en zullen de codes draaien.
Zorg dat je in dezelfde map zit als je docker-compose file. Je typt hetvolgende:
  - docker-compose up
  
In de docker desktop zal je zien dat er een nieuw netwerk is aangemaakt met vier containers en dat deze allemaal aan het draaien zijn. 
Als je wilt kijken ofdat de data wordt opgeslagen in Mongodb ga je naar 'Fill in connection fields individually'.
Bij Hostname typ je 'localhost' en bij Port typ je '8001'.
KLik op connect.
Nu kun je zien dat er een nieuwe database 'Bitcoin' is aangemaakt met een collectie 'Transaction_info', hierin komen de hoogste waarden per minuut.


