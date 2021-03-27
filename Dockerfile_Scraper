FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip3 install bs4
RUN pip3 install Beautifulsoup4

RUN pip3 install requests

RUN pip3 install pandas

RUN pip3 install datetime

RUN apt-get install -y php-json

RUN pip3 install pymongo

RUN pip3 install redis


ADD https://raw.githubusercontent.com/Yara161/Scraper-Bitcoin/main/Scraper.py /usr/src/app/

CMD ["python3","/usr/src/app/Scraper.py"]

