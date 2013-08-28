#!/usr/local/bin/python
# -- coding: utf-8 --
from __future__ import division
import nltk, re, pprint

# ------------------------------------------------------------------------------
# Work through http://nltk.org/book/ch03.html
# -- gene + github at ology dot net not dot com
# ------------------------------------------------------------------------------

def inspect(it):
    print 'type=%s, len=%d' % (type(it).__name__, len(it)),
    if isinstance(it, str):
        print 'chars'
    elif isinstance(it, list):
        print 'elements'

from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()
# Or this:
#proxies = {'http': 'http://www.someproxy.com:3128'}
#raw = urlopen(url, proxies=proxies).read()
inspect(raw) #type=str, len=1176893 chars
raw[31:73] #'Crime and Punishment, by Fyodor Dostoevsky'

tokens = nltk.word_tokenize(raw)
inspect(tokens) #type=list, len=244484 elements
tokens[5:12] #['Crime', 'and', 'Punishment', ',', 'by', 'Fyodor', 'Dostoevsky']
