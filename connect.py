import json
import pymongo
from pymongo import MongoClient
import pandas as pd
data={}
import redis
import time

r= redis.Redis(host= 'redis', port=6379, db=0)

client = pymongo.MongoClient(host='mongo', port=8001)
mydb = client["Bitcoin"]
mycol = mydb["Transaction_info"] 
while True: #nog per minuut
    try:
        print("yes")

       
        test=r.get('test_json')
        testdic=json.loads(test)
        # print(type(testdic))
       # print("wtf")

        dictionary= dict(sorted(testdic.items(),key=lambda r:r[1][2],reverse=True))
        # print(dictionary)

        hash=next(iter(dictionary))
        hoogstewaarde=str(next(iter(dictionary.values())))
        #print(type(hoogstewaarde))

        eind={hash:hoogstewaarde}
        print(eind)


        x = mycol.insert_one(eind)
        print(x)
        r.delete('test_json')
        print("deleted")
    except:
        print()
