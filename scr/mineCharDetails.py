import argparse
import urllib
import os

import traceback
from pprint import pprint
from Charachters import CharachterPage
from Application import Application


class RootDirException(Exception):
    pass

# Command line options
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-c", "--charachter", type=str, help="charachter name to fetch details")
args = parser.parse_args()
app = Application()

# app begins
chars = CharachterPage()

if args.charachter:
  char_name = urllib.quote(args.charachter)
  file_name_text = '/'.join([app.settings['storage_folder']['Charachters_text'],char_name])
  file_name_info = '/'.join([app.settings['storage_folder']['Charachters_info'],char_name])
  file_name_nlp = '/'.join([app.settings['storage_folder']['Charachters_nlp'],char_name])


if not os.path.exists(file_name_text):
  content = chars.fetchCharachterText(char_name)
  app.storeFile(file_name_text, content)
  content = chars.getCharachterInfo(args.charachter)
  app.storeFile(file_name_info, content)

else:
  with open(file_name_text, 'r') as myfile:
    data=myfile.read().replace('\n', '')
content = chars.nlpCharachterInfo(data)
app.storeFile(file_name_nlp, content)



