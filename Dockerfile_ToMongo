FROM ubuntu:latest
RUN apt-get update

RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip3 install redis

RUN pip3 install pandas

RUN apt-get install -y php-json

RUN pip3 install pymongo

ADD https://raw.githubusercontent.com/Yara161/Scraper-Bitcoin/main/ToMongo.py /usr/src/app/


CMD ["python3","/usr/src/app/ToMongo.py"]
