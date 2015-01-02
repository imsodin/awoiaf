import requests
from BeautifulSoup import BeautifulSoup
import json
import io
from pprint import pprint
from pymongo import MongoClient

class Charachters(object):
  """docstring for Charachters"""


  def __init__(self, arg):
    super(Charachters, self).__init__()
    self.args = arg
    self.args['charachters'] = []

  def getCharachtersList(self):
    charachters = []
    list_of_charchters_url = 'http://awoiaf.westeros.org/api.php?action=parse&page=List_of_characters&format=json&prop=links&redicrects'
    r=requests.get(list_of_charchters_url)
    d = json.loads(r.content)
    links_list = d['parse']['links']
    for l in links_list:
     self.args['charachters'].append(l['*'])

  def getCharachterDetails(self):
    char_list = []
    for charachter in self.args['charachters']:
      print "Now Processing: "+charachter
      # fetching individual pages
      currents_url = 'http://awoiaf.westeros.org/api.php?action=parse&page='+charachter+'&format=json&section=0&prop=text'
      r=requests.get(currents_url)
      d = json.loads(r.content)
      try:
        html_to_parse =  d['parse']['text']['*']
        parsed_html = BeautifulSoup(html_to_parse)

        char_data = dict()
        char_data["name"]=charachter
        table = parsed_html.find('table')
        rows = parsed_html.findAll('tr')
        for row in rows:
          tKey = tVal = ''
          cols_head = row.find('th')
          if cols_head:
            tKey = cols_head.text.strip()
          cols_data = row.find('td')
          if cols_data:
            tVal = cols_data.text.strip()
          if tKey and tVal:
            char_data[tKey] = tVal
        char_list.append(char_data)
      except Exception, e:
        continue
    self.args['charachters_data'] = json.dumps(char_list)

  def stroreHouseDetails(self):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['local']
    collection = db['Charachters']

    input_filename = '../Data/charachters_details'
    json_data=open(input_filename)
    data = json.load(json_data)
    json_data.close

    for l in data:
      pprint(l)
      collection.insert(l)



chars = Charachters(dict())
# chars.getCharachtersList()
# print "Will process {} {}".format(len(chars.args['charachters']), "charachters")
# chars.getCharachterDetails()
# print chars.args['charachters_data']

# out_file = '../Data/charachters_details'

# f = io.open(out_file, 'w', encoding='utf8')
# f.write(unicode(chars.args['charachters_data']))
# f.close()

# chars.stroreHouseDetails()



