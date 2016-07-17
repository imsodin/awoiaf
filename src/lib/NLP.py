#!/usr/bin/env python2
import traceback
import nltk
from pprint import pprint


class NLP():
    """Processes raw text"""
    def __init__(self):
        # super(NLP, self).__init__()
        # self.arg = arg
        self.res = dict()

    def pipeline(self, text):
          text = unicode(text)
          try:
            tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
            sents = tokenizer.tokenize(text)
            tokens = nltk.word_tokenize(sents[0])
            text = nltk.Text(tokens)
            words = [w.lower() for w in tokens]
            self.res['vocab'] = sorted(set(words))
            self.res['pos_tag'] = nltk.pos_tag(text)
          except Exception, e:
            traceback.print_exc()
          return self.res
