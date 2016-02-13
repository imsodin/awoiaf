"""Summary: driver script to handle data related to houses information in the wiki. The script can be used for

* download a list of great houses

OR

* for each house;
    1. downloads input house_name page as raw text
    2. parses the page's info box
    3. analyzes the part of speech of the page

Example:
    python mineHousesDetails.py -v -s 'House Egen'

Attributes:
    app (Application): The main application class
    args (dict): input arguments
    houses (TYPE): access the HousesPage module
    list_of_houses (list): list of houses extracted from the wiki
    content (string): extracted content from the wiki
    parser (argpasre): access the argparse module
"""
import os
import argparse
import urllib
from pprint import pprint
from Houses import HousesPage
from Application import Application


# Command line options
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-s", "--house", type=str, help="house name to fetch details")
parser.add_argument("-l", "--list_of_houses", help="get list of houses", action="store_true")

args = parser.parse_args()
app = Application()
list_of_houses = []

# app begins
houses = HousesPage(dict())
if args.list_of_houses:
  list_of_houses = houses.getListOfHouses()
  pprint (list_of_houses)

if args.house:
    house_name = urllib.quote(args.house)

    # setup persistent storage locations
    file_name_text = '/'.join([app.settings['storage_folder']['Houses_text'],house_name])
    file_name_info = '/'.join([app.settings['storage_folder']['Houses_info'],house_name])
    file_name_nlp = '/'.join([app.settings['storage_folder']['Houses_nlp'],house_name])
    # store data onto disk
    if not os.path.exists(file_name_text):
        content = houses.fetchHouseText(house_name)
        app.storeFile(file_name_text, content)
        content = houses.getHouseInfo(house_name)
        app.storeFile(file_name_info, content)
    else:
      with open(file_name_text, 'r') as myfile:
        content=myfile.read().replace('\n', '')
    content = houses.nlpHouseInfo(content)
    app.storeFile(file_name_nlp, content)
