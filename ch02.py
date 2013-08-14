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

from nltk.corpus import gutenberg

# Show available texts.
gutenberg.fileids()

alice = gutenberg.words('carroll-alice.txt')
bible = gutenberg.words('bible-kjv.txt')
hamlet = gutenberg.words('shakespeare-hamlet.txt')
macbeth = gutenberg.words('shakespeare-macbeth.txt')

# Average word & sentence length, and the number of times each vocabulary item
# appears in the text on average (lexical diversity).
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

# Fondling sentences.
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
longest_len = max([len(s) for s in macbeth_sentences])
[s for s in macbeth_sentences if len(s) == longest_len]

# Brown!
from nltk.corpus import brown
brown.categories()

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
whords = ['what', 'when', 'where', 'who', 'why']

scifi = brown.words(categories=genres[3])
#scifi = brown.words(fileids=['cm01'])
#religion_scifi = brown.words(categories=[genres[1], genres[3]])
fdist = nltk.FreqDist([w.lower() for w in scifi])
for m in modals:
    print m + ':', fdist[m]
for w in whords:
    print w + ':', fdist[w],

# Conditional frequency distribution
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)
cfd.tabulate(conditions=genres, samples=modals)
cfd.tabulate(conditions=genres, samples=whords)

# Reuters overlapping news test and training texts.
from nltk.corpus import reuters
len(reuters.fileids()) # number of files
reuters.fileids()[3017:3021] # filenames at the test-training transition.
reuters.categories()
metals = ['copper', 'gold', 'iron-steel', 'lead', 'nickel', 'palladium',
    'platinum', 'silver', 'strategic-metal', 'tin', 'zinc']
len(reuters.fileids(metals))
# Show freq.dist. for words in metals.
for m in metals:
    fdistm = nltk.FreqDist(set([w.lower() for w in reuters.words(reuters.fileids(m)) if w.isalpha()]))
    vocabm = fdistm.keys()
    vocabm[:20]

# Inaugural Address Corpus
from nltk.corpus import inaugural
inaugural.fileids()

# TODO What is a "nltk.ConditionalFreqDist" anyway?
def cond_freq_dist(text, target1, target2):
    cfd = nltk.ConditionalFreqDist(
        (target, fileid[:4])                # word-target, address-year
        for fileid in text.fileids()        # inagural address
        for w in text.words(fileid)         # all words in the address
        for target in [target1, target2]    # for each word
        if w.lower().startswith(target))    # ...that is lower, etc.
    cfd.plot()

cond_freq_dist(inaugural, 'america', 'citizen')
cond_freq_dist(inaugural, 'force', 'security')
cond_freq_dist(inaugural, 'freedom', 'security')
cond_freq_dist(inaugural, 'terror', 'safe')

# Corpora in Other Languages
from nltk.corpus import udhr
# TODO How to list all languages?
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut',
    'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1'))
cfd.plot(cumulative=True)

