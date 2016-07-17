#!/usr/bin/env python2
import requests
from bs4 import BeautifulSoup
import json
from Page import Page
from Application import Application
from NLP import NLP

from pprint import pprint

class CharacterPage(Page):
    """Handles data scrpaing of characters"""


    def getCharactersList(self):
        """Returns a list of characters

        Returns:
            list: list of characters
        """
        self.setParams('page', 'List_of_characters').setParams('prop', 'links')
        self.fetchPage()
        _request = self.getRequest()
        _data = json.loads(_request.content)
        _links_list = _data['parse']['links']
        return _links_list

    def fetchCharacterText(self, character_name):
        """Downloads character page in raw text format

        Args:
            character_name (string): name of character (spaces allowed)

        Returns:
            string: entire text of page
        """
        self.setParams('page', character_name)
        self.setParams('prop', 'text')
        self.fetchPage()
        _request = self.getRequest()
        _data = json.loads(_request.content)

        try:
            _data = _data['parse']['text']['*']
            # pprint (_data)
            soup = BeautifulSoup(_data)
            text = soup.getText()
        except Exception:
            raise Exception("Was not able to parse. Sure you entered the right Character name?")
        else:
            return text


    def getCharacterInfo(self, character_name):
        """Returns JSON formatted data structure for character_name

        Args:
            character_name (string): name of character (spaces allowed)

        Returns:
            dict: JSON formatted data for character. empty if chacrachter not found
        """
        self.setParams('page', character_name)
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
            dict: JSON formatted character data
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
        _data[unicode('Summary')] = _paragraph
        return _data

    def nlpCharacterInfo(self, text):
        return NLP().pipeline(text)

