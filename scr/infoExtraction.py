from os import listdir
from os.path import isfile, join
import nltk
mypath = '../Data/nlp'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]


for f in onlyfiles[:10]:
    try:
        s = open(mypath+"/"+f, 'r').read()
        dict = eval(s)
        sent = dict['pos_tag']
        t = nltk.ne_chunk(sent)
        print t
#        for (tag, name) in t[0]:
#            print tag

    except Exception, e:
        continue


#f = open ('')
