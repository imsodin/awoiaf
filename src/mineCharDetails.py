"""Summary: driver script to handle charchter pages.
1. downloads input character page as raw text
2. parses the page's info box
3. analyzes the part of speech of the page

Example:
    python mineCharDetails.py -v -c Bran_Stark

Attributes:
    app (Application): The main application class
    args (dict): input arguments
    chars (CharacterPage): access the characterpage module
    content (string): extracted content from the wiki
    parser (argpasre): access the argparse module
"""
import argparse
import urllib
import os
import sys

import traceback
from pprint import pprint
from Characters import CharacterPage
from Application import Application


# Command line options
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-c", "--character", type=str, help="character name to fetch details")
parser.add_argument("-l", "--list_of_characters", help="get list of characters", action="store_true")


args = parser.parse_args()
app = Application()

# app begins
chars = CharacterPage()

if args.list_of_characters:
    list_of_characters = [str(x['*']) for x in chars.getCharactersList()]
    pprint (list_of_characters)
    sys.exit(0)

if args.character:
    char_name = urllib.quote(args.character)
    file_name_text = '/'.join([app.settings['storage_folder']['Characters_text'],char_name])
    file_name_info = '/'.join([app.settings['storage_folder']['Characters_info'],char_name])
    file_name_nlp = '/'.join([app.settings['storage_folder']['Characters_nlp'],char_name])
    if not os.path.exists(file_name_text):
        text_content = chars.fetchCharacterText(char_name)
        app.storeFile(file_name_text, text_content)
        info_content = chars.getCharacterInfo(args.character)
        app.storeFile(file_name_info, info_content)
        nlp_content = chars.nlpCharacterInfo(text_content)
        app.storeFile(file_name_nlp, nlp_content)
    else:
        with open(file_name_text, 'r') as myfile:
            data=myfile.read().replace('\n', '')
        content = chars.nlpCharacterInfo(data)
        app.storeFile(file_name_nlp, content)
