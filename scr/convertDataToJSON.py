import io
import json
from pymongo import MongoClient

input_filename = '../Data/houses_details'
outpust_file = '../Data/houses_details.json'


client = MongoClient('mongodb://localhost:27017/')
db = client['local']
collection = db['awoiaf']


with open(input_filename) as f:
      houses_details = f.read().splitlines()

line_count=0
t_field = t_data =''
t_item={}

for  line in houses_details:
  if line == '====================================================================================================':
    t_field = t_data =''
    line_count = 0
    collection.insert(t_item)
    # a.append(t_item)
    t_item={}
    continue
  if line_count == 0:
    line_count+=2
    t_data = line
    t_field = "Name"
    t_item[t_field] = t_data
    continue

  if line_count % 2 == 1:
    t_field = line
  else:
    t_data = line

  if t_field and t_data:
    t_item[t_field] = t_data
    t_field = t_data =''
  line_count+=1

