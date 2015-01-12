import urllib
import urllib2
import requests
import json 
from pprint import pprint 

charachters = []
list_of_charchters_url = 'http://awoiaf.westeros.org/api.php?action=parse&page=List_of_characters&format=json&prop=links&redicrects'
r = requests.get(list_of_charchters_url)
d = json.loads(r.content)
links_list = d['parse']['links']
for l in links_list:
    charachters.append(l['*'])

for char in charachters[:1]:
    current_url = 'http://awoiaf.westeros.org/api.php'
    values = {'action':'parse',
              'page': char.replace(" ","_"),
              'format': 'json',
              'prop':'text'
              }
    data = urllib.urlencode(values)
    full_url = current_url + '?' + data
#    req = urllib2.Request(current_url, data)

    pprint (full_url)
    response = urllib2.urlopen(full_url)
#    page = response.read()
#    raw = page.read().decode('utf8')
    type(raw)
