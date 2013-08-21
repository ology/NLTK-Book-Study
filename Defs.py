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

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)

def cond_freq_dist(text, target1, target2):
    cfd = nltk.ConditionalFreqDist(
        (target, fileid[:4])                # word-target, address-year
        for fileid in text.fileids()        # inagural address
        for w in text.words(fileid)         # all words in the address
        for target in [target1, target2]    # for each word
        if w.lower().startswith(target))    # ...that is lower, etc.
    cfd.plot()

# ConditionalFreqDist for words in the given languages.
def udhr_cond_freq_dist(udhr, languages):
    cfd = nltk.ConditionalFreqDist(
        (lang, len(word))
        for file in udhr.fileids()
        for lang in languages if lang in file
        for word in udhr.words(file))
    cfd.plot()

# Return the syllable stress list.
def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]

