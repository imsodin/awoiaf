import io
import requests
import traceback
import nltk
from pprint import pprint
from bs4 import BeautifulSoup
import json


class NLP(object):
  """docstring for NLP"""
  def __init__(self, arg):
    super(NLP, self).__init__()
    self.arg = arg
    self.res = dict()

  def pipeline(self):
    mined_data = dict()
    pos_tag = ''
    url = self.arg['url_to_fetch']
    r=requests.get(url)
    d = json.loads(r.content)
    try:
      html_to_parse =  d['parse']['text']['*']
      parsed_html = BeautifulSoup(html_to_parse)
      parsed_html = parsed_html.get_text()
      sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
      sents = sent_tokenizer.tokenize(parsed_html)
      tokens = nltk.word_tokenize(sents[0])
      text = nltk.Text(tokens)
      words = [w.lower() for w in tokens]
      self.res['vocab'] = sorted(set(words))
      self.res['pos_tag'] =  nltk.pos_tag(text)
      self.res['text'] = parsed_html
    except Exception, e:
      traceback.print_exc()
