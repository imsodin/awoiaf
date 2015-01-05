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

    awoif_url = 'http://awoiaf.westeros.org/api.php?action=parse&page='+urllib.quote(house_name)+'&format=json&section=0&prop=text'
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
    rel_table = ''
    node_table = ''

    for c in cur:
      try:
        s =  c['Name'][0].rstrip().lstrip()
        o = c['Overlord'][0].rstrip().lstrip()
        col = '#'
        if o == 'House Greyjoy':
          col += '000000'
        elif o == 'House Arryn':
          col += '5D91EB'
        elif o == 'House Bolton':
          col += 'FE93CA'
        elif o == 'House Baratheon of Dragonstone':
          col += 'D8BD25'
        elif o == 'House Lannister':
          col += '8A1919'
        elif o == 'House Stark':
          col += '9E9E9E'
        elif o == 'House Martell':
          col += 'F97A10'
        elif o == "House Baratheon of King's Landing":
          col += 'F9B43F'
        elif o == "House Tyrell":
          col += '006400'
        elif o == "House Baelish of Harrenhal":
          col += '009700'
        elif o == "House Targaryen":
          col += 'D1361C'
        elif o == "House Baratheon":
          col += 'FDD518'
        elif o == "House Tully":
          col += '174B82'
        else:
          col = ''

        seq = (s,o)
        rel_table += "\t\t\t".join(seq) + '\n'
        seq = (s,col)
        node_table += "\t\t\t".join(seq)+ '\n'


      except KeyError:
        continue
    out_file = '../Data/weateros_aliances'
    f = io.open(out_file, 'w', encoding='utf8')
    f.write(rel_table)
    f.close()

    out_file = '../Data/weateros_aliances_node_attrs'
    f = io.open(out_file, 'w', encoding='utf8')
    f.write(node_table)
    f.close()


mong = MongoDB(dict({'collection':'Houses'}))
houses = Houses(dict())

# with open(houses.arg['houses_list_file']) as f:
#       houses_list = f.read().splitlines()

# for house in houses_list:
#   print ("Processing house:  " + house)
#   info = houses.get_house_info (house)
#   mong.arg['collection_ref'].insert(info)


houses.get_houses_loyalty()





