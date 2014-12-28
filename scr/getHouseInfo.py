import requests
from BeautifulSoup import BeautifulSoup
import json
import urllib
import io

data_file = '../Data/list_of_IAF_houses'
filename = '../Data/houses_details'


def get_house_info(house_name, outfile):
  seperator = ("=" * 100)+"\n"
  print seperator
  outfile.write(unicode(seperator))

  awoif_url = 'http://awoiaf.westeros.org/api.php?action=parse&page='+house_name+'&format=json&section=0&prop=text'
  r=requests.get(awoif_url)
  d = json.loads(r.content)
  html_to_parse =  d['parse']['text']['*']
  parsed_html = BeautifulSoup(html_to_parse)

  data = []
  table = parsed_html.find('table')
  rows = parsed_html.findAll('tr')
  for row in rows:
    cols_head = row.find('th')
    if cols_head:
      print cols_head.text.strip()
      outfile.write(cols_head.text.strip()+"\n")
    cols_data = row.find('td')
    if cols_data:
      print cols_data.text.strip()
      outfile.write(cols_data.text.strip()+"\n")

with open(data_file) as f:
      houses = f.read().splitlines()

f = io.open(filename, 'w', encoding='utf8')
for house in houses:
  house  = urllib.quote(house)
  get_house_info (house, f)
f.close()
