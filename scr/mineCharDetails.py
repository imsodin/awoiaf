import argparse
import urllib
import os
import io
import ConfigParser
import traceback
from pprint import pprint
from Charachters import CharachterPage

class RootDirException(Exception):
    pass

# Command line options
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-c", "--charachter", type=str, help="charachter name to fetch details")
args = parser.parse_args()

# Config options
try:
  config = ConfigParser.ConfigParser()
  config.read(os.path.expanduser('~/.awoiafrc'))
  rootdir = config.get('Folders', 'rootdir')
  datadir =  config.get('Folders', 'datadir')
  if not rootdir or not os.path.isdir(rootdir):
    raise RootDirException()
except Exception, e:
  traceback.print_exc()

# app begins

chars = CharachterPage()

if args.charachter:
  char_name = urllib.quote(args.charachter)
  res = chars.getCharachtersDetails(char_name)

  infodir =  "/".join([datadir,'info'])
  if not os.path.isdir(infodir):
    os.mkdir(infodir)

  out_file = "/".join([infodir,char_name])
  print (out_file)
  f = io.open(out_file, 'w', encoding='utf8')
  f.write(unicode(res))
  f.close()

  if args.verbose:
    pprint (res)





