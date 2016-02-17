import requests
from bs4 import BeautifulSoup
from xml.dom import minidom
import json
from pprint import pprint
from Page import Page
from NLP import NLP
from pymongo import MongoClient


class HousesPage(Page):
    """docstring for HousesPage

    Attributes:
        arg (TYPE): Description
    """
    def __init__(self, arg):
        """Summary

        Args:
            arg (TYPE): Description
        """
        super(HousesPage, self).__init__()
        self.arg = arg
        # self.arg['houses_list_file'] = '../Data/list_of_IAF_houses'
        # self.arg['houses_details_file']  = '../Data/houses_details'

    def getListOfHouses(self):
        """Returns a list of the great houses of westeros

        Returns:
            list: houses names
        """
        offset = 0
        max_houses = 460
        list_of_houses  = []

        self.setParams('action', 'query')
        self.setParams('list', 'search')
        self.setParams('srsearch', 'house')
        self.setParams('format', 'xml')


        while offset <= max_houses:
            self.setParams('sroffset', str(offset))
            self.fetchPage()
            _request = self.getRequest()
            _xmldoc = minidom.parseString(_request.content)
            _item_list = _xmldoc.getElementsByTagName('p')

            for _item in _item_list:
                list_of_houses.append(_item.attributes['title'].value)
            #offset must stay at 10 due to wiki max_links restriction
            offset += 10
        return list_of_houses

    def getHouseInfo(self, house_name):
        """Returns JSON formatted data structure for house_name

        Args:
            house_name (sttring): name of house (spaces allowed)

        Returns:
            dict: JSON formatted data for house. empty if house not found
        """
        self.setParams('page', house_name)
        self.setParams('prop', 'text')
        self.setParams('section', 0)
        self.fetchPage()
        _request = self.getRequest()
        _data = json.loads(_request.content)
        _data = _data['parse']['text']['*']
         # mine info from text
        _data = self.parseHTML(_data, house_name)
        return _data

    def parseHTML(self, html_to_parse, house_name):
        """Parses data from info box

        Args:
            html_to_parse (string): input text

        Returns:
            dict: JSON formatted house data
        """
        html_to_parse = html_to_parse.replace('<br>', '\n')
        parsed_html = BeautifulSoup(html_to_parse)

        info = dict()

        rows = parsed_html.findAll('tr')
        for row in rows:
            t_key = t_val = ''
            cols_head = row.find('th')
            if cols_head:
                t_key = cols_head.get_text()
            cols_data = row.find('td')
            if cols_data:
                t_val = cols_data.get_text()
            if t_key and not t_val:
                info[u'Name'] = [unicode(house_name)]
            elif t_key:
                info[t_key] = t_val.split('\n')
        return info

    def fetchHouseText(self, house_name):
        """Downloads house page in raw text format

        Args:
            house_name (string): name of house (spaces allowed)

        Returns:
            string: entire text of page
        """
        self.setParams('page', house_name)
        self.setParams('prop', 'text')
        self.fetchPage()
        _request = self.getRequest()
        _data = json.loads(_request.content)
        _data = _data['parse']['text']['*']
        # pprint (_data)
        soup = BeautifulSoup(_data)
        text = soup.getText()
        return text

    def nlpHouseInfo(self, text):
        return NLP().pipeline(text)

    def stroreHouseDetails(self, input_data):
        client = MongoClient('mongodb://pp-dev.informatik.tu-muenchen.de:27017/')
        database = client['awoiaf']
        collection = database['Houses']
        collection.insert(input_data)


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





