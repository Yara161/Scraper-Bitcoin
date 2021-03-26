import json
import pymongo
from pymongo import MongoClient
import pandas as pd
data={}
import redis
import time

from sshtunnel import SSHTunnelForwarder

r= redis.Redis(host= 'redis', port=6379, db=0)
MONGO_HOST= "109.130.60.209"
MONGO_USER = "USERNAME"
MONGO_PASS = "PASSWORD"
MONGO_DB = "DATABASE_NAME"
MONGO_COLLECTION = "COLLECTION_NAME"

server = SSHTunnelForwarder(MONGO_HOST,ssh_username=MONGO_USER,ssh_password=MONGO_PASS,remote_bind_address=('127.0.0.1', 27017))

server.start()
connection=pymongo.MongoClient('127.0.0.1', server.local_bind_port)
connection.close()
server.stop()




# client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
# mydb = client["Bitcoin"]
# mycol = mydb["Transaction_info"] 
print("Connected")
# while True: #nog per minuut
#     try:
#         print("yes")

       
#         test=r.get('test_json')
#         testdic=json.loads(test)
#         # print(type(testdic))
#        # print("wtf")

#         dictionary= dict(sorted(testdic.items(),key=lambda r:r[1][2],reverse=True))
#         # print(dictionary)

#         hash=next(iter(dictionary))
#         hoogstewaarde=str(next(iter(dictionary.values())))
#         #print(type(hoogstewaarde))

#         eind={hash:hoogstewaarde}
#         print(eind)


#         x = mycol.insert_one(eind)
#         print(x)
#         r.delete('test_json')
#         print("deleted")
#     except:
#         print()