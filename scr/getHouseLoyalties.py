import io
import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['local']
collection = db['awoiaf']

cur=collection.find({},{"Overlord":1, "Name":1})
# for c in cur:
  # print c


# cur=collection.find({},{"Name":1,"Overlord":1})
for c in cur:
  try:
    print "\t".join([c['Name'],c['Overlord']])
  except KeyError:
    continue

