import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb://hd15pd38:hd15pd38@10.1.67.157:27017/hd15pd38")
db = client.hd15pd38

result_cursor = db.game_record.find()
results = []

for i in result_cursor:
    results.append(i)
