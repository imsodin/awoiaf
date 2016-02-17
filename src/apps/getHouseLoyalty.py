import requests
import json
import sys
import io
from pprint import pprint
from Houses import Houses
from pymongo import MongoClient


#   def get_houses_loyalty(self):
#       cur=mong.arg['collection_ref'].find({},{"Name":1,"Overlord":1})
#       for c in cur:
#         try:
#           s =  c['Name'][0].rstrip().lstrip()
#           o = c['Overlord'][0].rstrip().lstrip()
#           seq = (s,o)
#           print "\t\t\t".join(seq)
#         except KeyError:
#           continue

# mong = MongoDB(dict({'collection':'HousesPage'}))
# houses = HousesPage(dict())

# with open(houses.arg['houses_list_file']) as f:
#       houses_list = f.read().splitlines()

# for house in houses_list:
#   print ("Processing house:  " + house)
#   info = houses.get_house_info (house)
#   mong.arg['collection_ref'].insert(info)


# houses.get_houses_loyalty()
