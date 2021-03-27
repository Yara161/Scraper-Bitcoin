import json
import pymongo
from pymongo import MongoClient
import pandas as pd
import redis

r= redis.Redis(host= 'redis', port=6379, db=0)

client = pymongo.MongoClient('mongodb://mongo:27017')
mydb = client["Bitcoin"]
mycol = mydb["Transaction_info"] 

while True:
    try:
        datajson=r.get('json')
        jsondic=json.loads(datajson)

      #  print(jsondic[0])
        hoogstewaarde=jsondic[0]
       # print(hoogstewaarde)

        x = mycol.insert_one(hoogstewaarde)

        r.delete('json')


    except:
        print()