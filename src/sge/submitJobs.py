"""creates SGE jobs to fetch details for each characters"""
import argparse
from subprocess import call
import os
import ConfigParser
import traceback
from pprint import pprint
from Characters import CharacterPage


# Command line options
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-n", "--dryrun", help="don't run system calls", action="store_true")
args = parser.parse_args()

# Config options
try:
  config = ConfigParser.ConfigParser()
  config.read(os.path.expanduser('~/.awoiafrc'))
  rootdir = config.get('Folders', 'rootdir')
  if not rootdir or not os.path.isdir(rootdir):
    raise RootDirException()
except Exception, e:
  traceback.print_exc()


_chars = CharacterPage()
_list_of_chars = _chars.getCharactersList()
for l in _list_of_chars:
    l = l['*']
    l = l.replace(" ", "_").replace("'", "").strip().rstrip().lstrip()
    _cmd = " ".join(["/usr/bin/qsub", "-j", "y", "-o", "/dev/null", rootdir+"/scr/sge/awoiaf_miner.sh", l])
    if args.verbose:
        print _cmd
    if not args.dryrun:
        call(["/usr/bin/qsub", "-j", "y", "-o", "/dev/null", rootdir+"/scr/sge/awoiaf_miner.sh", l])
