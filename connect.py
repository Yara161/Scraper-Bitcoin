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
        test=r.get('test_json')
        testdic=json.loads(test)

        dictionary= dict(sorted(testdic.items(),key=lambda r:r[1][2],reverse=True))

        hash=next(iter(dictionary))
        hoogstewaarde=str(next(iter(dictionary.values())))

        eind={hash:hoogstewaarde}


        x = mycol.insert_one(eind)

        r.delete('test_json')

        # testdic={}
        # eind={}
        # hash=''
        # dictionary={}

    except:
        print()