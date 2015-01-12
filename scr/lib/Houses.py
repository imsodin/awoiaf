import requests
from bs4 import BeautifulSoup
import json
import urllib
import io
from pprint import pprint
from mongodb import MongoDB
import sys


class Houses(object):
  """docstring for Houses"""
  def __init__(self, arg):
    super(Houses, self).__init__()
    self.arg = arg
    self.arg['houses_list_file'] = '../Data/list_of_IAF_houses'
    self.arg['houses_details_file']  = '../Data/houses_details'

  def get_house_info(self,house_name):

    awoif_url = 'http://awoiaf.westeros.org/api.php?action=parse&page='+urllib.quote(house_name)+
                '&format=json&section=0&prop=text'
    r=requests.get(awoif_url)
    d = json.loads(r.content)
    html_to_parse =  d['parse']['text']['*']
    html_to_parse = html_to_parse.replace('<br>', '\n')
    parsed_html = BeautifulSoup(html_to_parse)

    info = dict()
    data = []

    rows = parsed_html.findAll('tr')
    for row in rows:
      tKey = tVal = ''
      cols_head = row.find('th')
      if cols_head:
        tKey =  cols_head.get_text()
      cols_data = row.find('td')
      if cols_data:
        tVal =  cols_data.get_text()
      if tKey and not tVal:
        info[u'Name']  =  [unicode(house_name)]
      elif tKey:
        info[tKey] = tVal.split('\n')
    return info

  def get_houses_loyalty(self):
    cur=mong.arg['collection_ref'].find({},{"Name":1,"Overlord":1})
    for c in cur:
      try:
        s =  c['Name'][0].rstrip().lstrip()
        o = c['Overlord'][0].rstrip().lstrip()
        seq = (s,o)
        print "\t\t\t".join(seq)
      except KeyError:
        continue

mong = MongoDB(dict({'collection':'Houses'}))
houses = Houses(dict())

# with open(houses.arg['houses_list_file']) as f:
#       houses_list = f.read().splitlines()

# for house in houses_list:
#   print ("Processing house:  " + house)
#   info = houses.get_house_info (house)
#   mong.arg['collection_ref'].insert(info)


houses.get_houses_loyalty()





