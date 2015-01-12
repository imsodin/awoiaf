import requests
import json
import sys
import io
from pprint import pprint
from Charachters import Charachters

class pageRank(object):
  """docstring for pageRank"""
  def __init__(self, arg):
    super(pageRank, self).__init__()
    self.arg = arg
    self.arg[pageRank] = []

    def getLinks( self, root_page, level = 1  ):
      if level > 2:
        return
        print( '%s %d' % ('Now doing level', level))

        if root_page in self.arg['pages_visited']:
          return
          url = 'http://awoiaf.westeros.org/api.php?action=query&list=backlinks&bltitle='+root_page+'&bllimit=300&format=json&blnamespace=0'
          r=requests.get(url)
          self.arg['pages_visited'].append(root_page)
          d = json.loads(r.content)
          links_list = d['query']['backlinks']

          score = len(links_list)*(1/float(level))
          self.arg[pageRank].append(dict({
            'page_name': root_page,
            'link_count': len(links_list),
            'level': level,
            'score': score
            }))

          if len(links_list)==0:
            return
            level += 1
            for l in links_list:
              if l['title'] == 'List of characters':
                continue
                self.getLinks(l['title'], level)

                chars = Charachters(dict())
                print "Getting charachter list"
                chars.getCharachtersList()

                score_data_file = '../Data/pageRank/score'
                sf = io.open(score_data_file, 'a', encoding='utf8')

                for char_name in chars.args['charachters'][:2]:
                  print "Now processing "+char_name
                  pages_visited = []
                  pr = pageRank(dict({'pages_visited': pages_visited}))
                  pr.getLinks(char_name)
                  total_score = 0
                  for item in pr.arg[pageRank]:
                    total_score += item['score']

                    page_rank_data_file = '../Data/pageRank/%s_data' % (char_name.replace(" ", "_"))
                    prdf = io.open(page_rank_data_file, 'w', encoding='utf8')
                    prdf.write(unicode(pr.arg[pageRank]))
                    prdf.close()

                    print ("Score is %d" % (total_score))
                    sf.write(unicode("%s\t%d \n" %(char_name,total_score)))

                    sf.close()







