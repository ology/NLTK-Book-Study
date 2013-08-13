#!/usr/local/bin/python
# -- coding: utf-8 --

# ------------------------------------------------------------------------------
# Work through the http://nltk.org/book/
# -- gene + github at ology dot net not dot com
#
# Handy links:
# http://nltk.org/
# http://stackoverflow.com/questions/4092994/unable-to-install-matplotlib-on-mac-os-x
# ------------------------------------------------------------------------------

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

# All / Unique words.
def lexical_diversity(text):
    return len(text) / len(set(text))

# Density of tokens in text.
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

# 1.8 Exercises:
# 6.
text2.dispersion_plot(['Elinor','Marianne','Edward','Willoughby'])
# 6 & 23. Monty Python speakers:
text6.dispersion_plot([w for w in vocab6 if w.isupper() and len(w) > 2][:21]) 

# 14. Locating all instances of a word in a text:
[i for i, w in enumerate(sent3) if w == "the"]

# 15. List of words with 3 or more repeated letters.
import re
[w for w in set(text5) if re.findall(r'((\w)\2{2,})', w)]

# 17. First sentence in "The Man Who Was Thursday" containing the word, sunset.
word_positions = [i for i, w in enumerate(text9) if w == 'sunset']
pre_period_positions = [i for i, w in enumerate(text9) if w == '.' and i < word_positions[0]]
post_period_positions = [i for i, w in enumerate(text9) if w == '.' and i > word_positions[0]]
head = pre_period_positions[-1] + 1
tail = post_period_positions[0] + 1
text9[head:tail]

# 18. Vocab of initial sentences.
sorted(set(sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8))

# 19.
sorted(set([w.lower() for w in text1])) # "set of lc"
sorted([w.lower() for w in set(text1)]) # "lc of set" <- May have dups.

# 20.
# >>> '1'.isupper()
#False
#>>> not '1'.islower()
#True
#>>> 'a'.isupper()
#False
#>>> not 'a'.islower()
#False
#>>> 'A'.isupper()
#True
#>>> not 'A'.islower()
#True

# 21.
text2[-2:]

# 22.
fdist5 = FreqDist(set([w for w in text5 if w.isalpha() and len(w) == 4]))
vocab5 = fdist5.keys()
vocab5[:50]

# 26.
def avg_word_len(text):
    v = set([w.lower() for w in text if w.isalpha()])
    t = sum([len(w) for w in v])
    return t / len(v)

avg_word_len(text1) # 7.43 chars

