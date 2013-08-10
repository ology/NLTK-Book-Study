#!/usr/local/bin/python
# -- coding: utf-8 --

#
# Work through the http://nltk.org/book/
# -- gene + github at ology dot net not dot com
#
# Handy links: http://nltk.org/
# http://stackoverflow.com/questions/4092994/unable-to-install-matplotlib-on-mac-os-x
#

# Use floating point division.
from __future__ import division
from nltk.book import *

# Basics:
words = ["monstrous", "very", "citizens", "democracy", "freedom", "duties", "America"]
text1
text2
text1.concordance(words[0])
text1.similar(words[0])
text2.similar(words[0])
text2.common_contexts([words[:1]])
text4.dispersion_plot(words[2:])
#vocab1 = set(text1)

# All / Unique words:
def lexical_diversity(text):
    return len(text) / len(set(text))

# Density of token in text.
def token_percent(token, text):
    return 100 * text.count(token) / len(text)

lexical_diversity(text5)
lexical_diversity(sent1)
text_percent('a', text4)

# Frequency distributions:
fdist1 = FreqDist(text1)
vocab1 = fdist1.keys()
vocab1[:50]
fdist1.plot(50, cumulative=True)
fdist5 = FreqDist(text5)
sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])

# Distribution of word lengths in a text
fdist = FreqDist([len(w) for w in text1])
fdist.keys()
fdist.items()
fdist[3]
fdist.freq(3)
# From this we see that the most frequent word length is 3, and that words of
# length 3 account for roughly 50,000 (or 20%) of the words making up the book.

# List operations:
sorted([w for w in set(text6) if w.isalpha()])
len(set([word.lower() for word in text1 if word.isalpha()]))
tricky = sorted([w for w in set(text2) if 'cie' in w or 'cei' in w])
for word in tricky:
    print word,

