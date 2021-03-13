import redis
import json
import pymongo
from pymongo import MongoClient
import pandas as pd
data={}
r=redis.Redis(host='localhost', port=6379, db=0)


client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["Bitcoin"]
mycol = mydb["Transaction_info"]  
test=r.get('test_json')
testdic=json.loads(test)
# print(type(testdic))


dictionary= dict(sorted(testdic.items(),key=lambda r:r[1][2],reverse=True))
print(dictionary)

hash=next(iter(dictionary))
hoogstewaarde=str(next(iter(dictionary.values())))
print(type(hoogstewaarde))

eind={hash:hoogstewaarde}
print(eind)


x = mycol.insert_one(eind)
print(x)

r.expire('test_json',60)

