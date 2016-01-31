#!/usr/local/bin/python
# -- coding: utf-8 --
from __future__ import division
import nltk, re, pprint

# ------------------------------------------------------------------------------
# Work through http://nltk.org/book/ch03.html
# -- gene at ology dot net not dot com
# ------------------------------------------------------------------------------

def inspect(it):
    print 'type=%s, len=%d' % (type(it).__name__, len(it)),
    if isinstance(it, str):
        print 'chars'
    elif isinstance(it, list):
        print 'elements'
    elif isinstance(it, nltk.text.Text):
        print 'nltk tokens'

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

text = nltk.Text(tokens)
inspect(text) #type=Text, len=244484 nltk tokens
text[982:1019] #['CHAPTER', 'I', 'On', 'an', 'exceptionally', 'hot', 'evening', 'early', 'in', 'July', 'a', 'young', 'man', 'came', 'out', 'of', 'the', 'garret', 'in', 'which', 'he', 'lodged', 'in', 'S.', 'Place', 'and', 'walked', 'slowly', ',', 'as', 'though', 'in', 'hesitation', ',', 'towards', 'K.', 'bridge.']

#
text.collocations()

# Find the bounds of the novel.
raw.find("PART I") #5338
raw.find("CHAPTER I") #5352
raw.rfind("End of Project Gutenberg") #1157743
# Slice out the novel content.
raw = raw[raw.find('PART I'):raw.rfind('End of Project Gutenberg')]
inspect(raw) #type=str, len=1152405 chars

# Download a web page.
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
html[:60]
# Purge markup.
raw = nltk.clean_html(html)
tokens = nltk.word_tokenize(raw)
# Find content bounds.
tokens[120:391] #['Scientists', 'believe' ... 'wo', "n't", 'disappear.']
# Reset the tokens to the found content.
tokens = tokens[120:391]
text = nltk.Text(tokens)
inspect(text) #type=Text, len=271 nltk tokens
text.concordance('gene') #Displaying 4 of 4 matches: ...

