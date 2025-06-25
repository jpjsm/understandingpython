from pymongo import MongoClient
import datetime
import uuid
import random

#client = MongoClient("mongodb://10.227.242.242:27017/")
client = MongoClient("mongodb://localhost:27017/")

print(f"{client.server_info()=}")

dbs = client.list_database_names()
print("Databases:")
for db_name in dbs:
    print(f"-\t{db_name}")
    db = client[db_name]
    collections = db.list_collection_names()
    for collection_name in collections:
        print(f"\t-\t{collection_name}")

print("done!")

client.close()

