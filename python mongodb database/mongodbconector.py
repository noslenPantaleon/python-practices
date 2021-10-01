import pymongo
from pymongo import MongoClient
import json
import datetime
from datetime import timedelta

data ={"_id": 0, "name": "rack1"}

client = pymongo.MongoClient("here replace for your mongodb_address")
database_name = "" 
db = client.database_name 
collection = db.collection1



entry1 = {
      "author": "hello world",
      "text": "My first post!",
      "tags": ["mongodb", "python", "pymongo"],
      "date": datetime.datetime.utcnow() - timedelta(days=1)
      }


entry_inserted_id = db.collection.insert_one(entry1).inserted_id
print( "Inserted entry: " + str(entry_inserted_id) )