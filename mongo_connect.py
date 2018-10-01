import pymongo
from pymongo import MongoClient
import json
config = json.load(open('configuration.json'))
setup = config[config["current_state"]]
mongo_connection = setup["mongo"]

client = MongoClient(mongo_connection)
db = client.hd15pd38

result_cursor = db.songs.find()
results = []

for i in result_cursor:
    results.append(i)
