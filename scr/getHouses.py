import requests
from xml.dom import minidom

# Move this to the Houses class

max_houses=460 #

def get_house(offset):
  awoif_url='http://awoiaf.westeros.org/api.php?action=query&list=search&srsearch=house&format=xml&sroffset='+str(offset)
  r=requests.get(awoif_url)

  xmldoc = minidom.parseString(r.content)
  itemlist = xmldoc.getElementsByTagName('p')

  for s in itemlist :
    print s.attributes['title'].value


offset=0
while offset <= max_houses:
    get_house (offset)
    offset+=10
