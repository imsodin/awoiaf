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
  content = chars.fetchCharachterText(char_name)
  file_name = '/'.join([app.settings['storage_folder']['Charachters_text'],char_name])
  app.storeFile(file_name, content)

  content = chars.getCharachterInfo(args.charachter)
  file_name = '/'.join([app.settings['storage_folder']['Charachters_info'],char_name])
  app.storeFile(file_name, content)

# if args.verbose:
#   pprint (res)
