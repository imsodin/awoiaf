"""
Attributes:
    debug (int): enables debug messages
"""
import sys
import requests
from pprint import pprint

debug = 1

class Page(object):
    """Handles data scraping from awoiaf pages"""
    def __init__(self):
        """Summary"""
        super(Page, self).__init__()
        self.args = {
            'base_api_url' : 'http://awoiaf.westeros.org/api.php',
            'api_arugments' : {
                'action': 'parse',
                'page': '',
                'format': 'json',
                'prop':'',
                'redirects':1
            },
            'request' : None,
            'request_url' : ''
        }

    def getRequest(self):
        """
        Returns:
            Object: gets private member request
        """
        return self.args['request']

    def fetchPage (self):
        """Fetches the contents of a page"""
        self.composeURL()
        self.args['request'] = requests.get(self.args['reqeust_url'])

    def setParams(self, key, value):
        """Accessor to the api_arugments private member"""
        self.args['api_arugments'][key] = value
        return self

    def composeURL(self):
        """Assembles a qualified URI to fetch"""
        _output_string = []
        for key, value in self.args['api_arugments'].iteritems():
            if key == 'redirects' and value == 1:
                _output_string.append('redirects')
            else:
                _output_string.append("{}={}".format(key, value))
        self.args['reqeust_url'] =  self.args['base_api_url'] + '?' + "&".join(_output_string)
        if debug:
            sys.stderr.write (self.args['reqeust_url']+'\n')
