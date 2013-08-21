#!/usr/local/bin/python
# -- coding: utf-8 -- 
#
# Subroutine defs inspired by http://nltk.org/book/
# -- gene + github at ology dot net not dot com
#

# Import functionality.
from __future__ import division
import nltk

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word = cfdist[word].max() # XXX max() renders loops

def lexical_diversity(text):
    word_count = len(text)
    vocab_size = len(set(text))
    lexical_diversity = word_count / vocab_size
    return lexical_diversity

def content_fraction(text, stop):
    content = [w for w in text if w.isalpha() and w.lower() not in stop]
    return len(content) / len(text)

def token_percent(token, text):
    return 100 * text.count(token) / len(text)

def avg_word_len(text):
    v = set([w.lower() for w in text if w.isalpha()])
    t = sum([len(w) for w in v])
    return t / len(v)

