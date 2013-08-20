#!/usr/local/bin/python
# -- coding: utf-8 -- 

# -----------------------------------------------------------------------------#
# Art of War analysis based on http://nltk.org/book/
# -- gene + github at ology dot net not dot com
# -----------------------------------------------------------------------------#

import nltk
from __future__ import division
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import wordnet as wn

# PlaintextCorpusReader input.
corpus_root = '/Users/gene/Backed/Documents'
taow = PlaintextCorpusReader(corpus_root, 'artofwar.txt')

taow.fileids() #['artofwar.txt']
taow.words() #['THE', 'ART', 'OF', 'WAR', 'BY', 'SUN', 'TZU', ...]
len(taow.words()) #13038
len(taow.sents()) #943
len([s for s in taow.sents() if 'enemy' in s]) #111
len([s for s in taow.sents() if 'ally' in s]) #2
len([s for s in taow.sents() if 'allies' in s]) #3
len([s for s in taow.sents() if 'spy' in s]) #8
len([s for s in taow.sents() if 'spies' in s]) #11

b = nltk.bigrams(taow.words())
len(b) #13037
cfd = nltk.ConditionalFreqDist(b)

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word = cfdist[word].max() # XXX max() renders loops

generate_model(cfd, 'enemy') # enemy ' s own men , and the enemy ' s own men , and

# Grab stopwords.
stopwords = nltk.corpus.stopwords.words('english')
len(stopwords) #127

# WordNet.
# Senses and Synonyms.
words = ['enemy', 'opponent']
for w in words:
    for synset in wn.synsets(w):
        print synset.lemma_names

#syns = [syn for syn in wn.synsets(w) for w in words] # XXX No worky
# But this does work.
syns = []
for w in words:
    for syn in wn.synsets(w):
        syns.append(syn)

names = []
for syn in syns:
    for name in syn.lemma_names:
        names.append(name)

unique_names = set(names)

#------------------------------------------------------------------------------#
def lexical_diversity(text):
    word_count = len(text)
    vocab_size = len(set(text))
    lexical_diversity = word_count / vocab_size
    return lexical_diversity

# Raw read.
f = open('/Users/gene/Backed/Documents/artofwar.txt')
raw = f.read()
# Raw metrics.
len(raw) #61692
lexical_diversity(raw) #833.6756756756756
text = nltk.Text(raw) # Equivalent to above.
len(text) #61692
lexical_diversity(text) #833.6756756756756
# Token metrics.
tokens = nltk.word_tokenize(raw)
len(tokens) #11976
lexical_diversity(tokens) #4.509036144578313
# Compute restricted mentrics.
content = [w for w in tokens if w.isalpha() and w.lower() not in stopwords]
len(content) #4616

def content_fraction(text, stop):
    content = [w for w in text if w.isalpha() and w.lower() not in stop]
    return len(content) / len(text)

content_fraction(tokens, stopwords) #0.385437541750167
content_fraction(content, stopwords) #1.0
