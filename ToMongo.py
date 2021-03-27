import json
import pymongo
from pymongo import MongoClient
import pandas as pd
import redis

r= redis.Redis(host= 'redis', port=6379, db=0)

client = pymongo.MongoClient('mongodb://mongo:27017')
mydb = client["Bitcoin"]
mycol = mydb["Transaction_info"] 



def connect():
    try:
        datajson=r.get('json')
        jsondic=json.loads(datajson)

        dictionary= dict(sorted(jsondic.items(),key=lambda r:r[1][2],reverse=True))

        hash=next(iter(dictionary))
        hoogstewaarde=str(next(iter(dictionary.values())))

        maximum={hash:hoogstewaarde}


        x = mycol.insert_one(maximum)

        r.delete('json')

        datajson={}
        maximum={}
        hash=''
        dictionary={}

    except:
        connect()
while True:
    connect()
