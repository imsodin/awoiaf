
import requests
from bs4 import BeautifulSoup
import json
from Page import Page
# import io
from pprint import pprint
# from pymongo import MongoClient
# import traceback
# import nltk
# from NLP import NLP
# import sys




class CharachterPage(Page):
    """Handles data scrpaing of charachters"""
    def getCharachtersList(self):
        """Returns a list of charachters

        Returns:
            list: list of charachters
        """
        self.setParams('page', 'List_of_characters').setParams('prop', 'links')
        self.fetchPage()
        _request = self.getRequest()
        _data = json.loads(_request.content)
        _links_list = _data['parse']['links']
        return _links_list

    def getCharachtersDetails(self, charachter_name):
        """Returns JSON formatted data structure for charachter_name

        Args:
            charachter_name (sttring): name of charachter (spaces allowed)

        Returns:
            dict: JSON formatted data for charachter. empty if chacrachter not found
        """
        self.setParams('page', charachter_name)
        self.setParams('prop', 'text')
        self.setParams('section', 0)
        self.fetchPage()
        _request = self.getRequest()
        _data = json.loads(_request.content)
        _data = _data['parse']['text']['*']
         # mine info from text
        _data = self.parseHTML(_data)
        return _data

    def parseHTML (self, html_to_parse):
        """Parses data from info box and summary section

        Args:
            html_to_parse (string): input text

        Returns:
            dict: JSON formatted charachter data
        """
        _parsed_html = BeautifulSoup(html_to_parse)
        _data = dict()
        # fish stuff from data
        table = _parsed_html.find('table')
        rows = _parsed_html.findAll('tr')
        for row in rows:
          tKey = tVal = ''
          cols_head = row.find('th')
          if cols_head:
            tKey = cols_head.text.strip()
          cols_data = row.find('td')
          if cols_data:
            tVal = cols_data.text.strip()
          if tKey and tVal:
            _data[tKey] = tVal
        _paragraph = _parsed_html.find('p').get_text()
        _data['Summary'] = _paragraph
        return _data


cp = CharachterPage()
pprint (cp.getCharachtersDetails('Rhaegar Frey'))




# class Charachters(object):
#   """docstring for Charachters"""


#   def __init__(self, arg):
#     super(Charachters, self).__init__()
#     self.args = arg
#     self.args['charachters'] = []

#   def getCharachtersList(self):
#     charachters = []
#     list_of_charchters_url = 'http://awoiaf.westeros.org/api.php?action=parse&page=List_of_characters&format=json&prop=links&redicrects'
#     r=requests.get(list_of_charchters_url)
#     d = json.loads(r.content)
#     links_list = d['parse']['links']
#     for l in links_list:
#      self.args['charachters'].append(l['*'])

#   def getCharachterDetails(self, charachters=None):
#     char_list = []
#     for charachter in charachters:
#       print "Now Processing: "+charachter
#       # fetching individual pages
#       currents_url = 'http://awoiaf.westeros.org/api.php?action=parse&page='+charachter+'&format=json&section=0&prop=text'
#       r=requests.get(currents_url)
#       d = json.loads(r.content)
#       try:
#         html_to_parse =  d['parse']['text']['*']
#         parsed_html = BeautifulSoup(html_to_parse)

#         char_data = dict()
#         char_data["name"]=charachter

#         # fish stuff from data
#         table = parsed_html.find('table')
#         rows = parsed_html.findAll('tr')
#         for row in rows:
#           tKey = tVal = ''
#           cols_head = row.find('th')
#           if cols_head:
#             tKey = cols_head.text.strip()
#           cols_data = row.find('td')
#           if cols_data:
#             tVal = cols_data.text.strip()
#           if tKey and tVal:
#             char_data[tKey] = tVal
#         char_list.append(char_data)

#         # mine info from text
#         paragraph = parsed_html.find('p').get_text()

#         pprint(paragraph)
#         sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
#         sents = sent_tokenizer.tokenize(paragraph)
#         text = nltk.word_tokenize(sents[0:1][0])
#         nlp_data_file = '../Data/nlp/%s_data' % (charachter.replace(" ", "_"))
#         nlpf = io.open(nlp_data_file, 'w', encoding='utf8')
#         nlpf.write(unicode(nltk.pos_tag(text)))
#         nlpf.close()
#       except Exception, e:
#         traceback.print_exc()
#         continue
#     self.args['charachters_data'] = json.dumps(char_list)

#   def mineCharachterInfo(self,charachter):
#     url = "http://awoiaf.westeros.org/api.php?action=parse&page="+charachter+"&format=json&section=0&prop=text&redicrects"
#     n = NLP({'url_to_fetch': url})
#     n.pipeline()
#     return(n.res)


#   def stroreHouseDetails(self):
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client['local']
#     collection = db['Charachters']

#     input_filename = '../Data/charachters_details'
#     json_data=open(input_filename)
#     data = json.load(json_data)
#     json_data.close

#     for l in data:
#       pprint(l)
#       collection.insert(l)




#chars.getCharachtersList()
# print "Will process {} {}".format(len(chars.args['charachters']), "charachters")
#chars.getCharachterDetails(['balon_Greyjoy'])

#chars.getCharachterDetails(chars.args['charachters'])
# print chars.args['charachters_data']

# out_file = '../Data/charachters_details'

# f = io.open(out_file, 'w', encoding='utf8')
# f.write(unicode(chars.args['charachters_data']))
# f.close()

# chars.stroreHouseDetails()



