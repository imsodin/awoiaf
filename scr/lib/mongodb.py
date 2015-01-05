from pymongo import MongoClient

class MongoDB(object):
  """docstring for MongoDB"""
  def __init__(self, arg):
    super(MongoDB, self).__init__()
    self.arg = arg
    client = MongoClient('mongodb://localhost:27017/')
    db = client['local']
    self.arg['collection_ref'] = db[arg['collection']]
