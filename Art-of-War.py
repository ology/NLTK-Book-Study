#!/usr/local/bin/python
# -- coding: utf-8 -- 
import nltk
from __future__ import division

# ------------------------------------------------------------------------------
# Art of War analysis based on http://nltk.org/book/
# -- gene + github at ology dot net not dot com
# ------------------------------------------------------------------------------

from nltk.corpus import PlaintextCorpusReader

corpus_root = '/Users/gene/Backed/Documents'
taow = PlaintextCorpusReader(corpus_root, 'artofwar.txt')
taow.fileids()
#['artofwar.txt']
taow.words()
#['THE', 'ART', 'OF', 'WAR', 'BY', 'SUN', 'TZU', ...]
len(taow.words())
#13038
len(taow.sents())
#943
len([s for s in taow.sents() if 'enemy' in s])
#111
len([s for s in taow.sents() if 'ally' in s])
#2
len([s for s in taow.sents() if 'allies' in s])
#3
len([s for s in taow.sents() if 'spy' in s])
#8
len([s for s in taow.sents() if 'spies' in s])
#11

corpus_root = '/Users/gene/Backed/Documents'
taow = PlaintextCorpusReader(corpus_root, 'artofwar.txt')
b = nltk.bigrams(taow.words())
len(b)
#13037
cfd = nltk.ConditionalFreqDist(b)
generate_model(cfd, 'enemy')
# enemy ' s own men , and the enemy ' s own men , and

# Functions
f = open('/Users/gene/Backed/Documents/artofwar.txt')
raw = f.read()
def lexical_diversity(text):
    word_count = len(text)
    vocab_size = len(set(text))
    lexical_diversity = word_count / vocab_size
    return lexical_diversity
lexical_diversity(raw)

# More AoW fiddling.
f = open('/Users/gene/Backed/Documents/artofwar.txt')
raw = f.read()
stopwords = nltk.corpus.stopwords.words('english')
tokens = nltk.word_tokenize(raw)
content = [w for w in tokens if w.isalpha() and w.lower() not in stopwords]
len(stopwords)
#127
len(tokens)
#11976
len(content)
#4616
content_fraction(tokens)
#0.385437541750167
