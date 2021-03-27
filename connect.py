import json
import pymongo
from pymongo import MongoClient
import pandas as pd
data={}
import redis
import time


r= redis.Redis(host= 'redis', port=6379, db=0)

client = pymongo.MongoClient('mongodb://mongo:27017')
mydb = client["Bitcoin"]
mycol = mydb["Transaction_info"] 
while True: #nog per minuut
    try:
        test=r.get('test_json')
        print(test)
        testdic=json.loads(test)
        print(type(testdic))
        dictionary= dict(sorted(testdic.items(),key=lambda r:r[1][2],reverse=True))
        print(dictionary)

        hash=next(iter(dictionary))
        hoogstewaarde=str(next(iter(dictionary.values())))
        print(type(hoogstewaarde))

        eind={hash:hoogstewaarde}
        print(eind)
        print(type(eind))


        x = mycol.insert_one(eind)
        print(x)
        r.delete('test_json')
        testdic={}
        eind={}
        hash=''
        dictionary={}
        print("deleted")
    except:
        print()