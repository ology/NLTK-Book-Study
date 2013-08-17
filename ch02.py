#!/usr/local/bin/python
# -- coding: utf-8 --
import nltk
from __future__ import division

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

# List languages.
len([latin for latin in udhr.fileids() if latin.endswith('-Latin1')])
#190
len([utf8 for utf8 in udhr.fileids() if utf8.endswith('-UTF8')])
#93
[latin for latin in udhr.fileids() if 'french' in latin.lower()]
['French_Francais-Latin1']

languages = [
    'English',
    'French',
    'German',
    'Italian',
    'Spanish',
]

# Nested loop to get filenames.
files = []
for file in udhr.fileids():
    for lang in languages:
        if lang in file:
            files.append(file)
# List comprehension of same:
[file for file in udhr.fileids() for lang in languages if lang in file]

# ConditionalFreqDist for words in the given languages.
def udhr_cond_freq_dist(udhr, languages):
    cfd = nltk.ConditionalFreqDist(
        (lang, len(word))
        for file in udhr.fileids()
        for lang in languages if lang in file
        for word in udhr.words(file))
    cfd.plot()
udhr_cond_freq_dist(udhr, languages)

# Parsing methods.
raw = udhr.raw('English-Latin1')
raw[:50]
words = udhr.words('English-Latin1')
words[:10]
sents = udhr.sents('English-Latin1')
sents[0]
#[u'Universal', u'Declaration', u'of', u'Human', u'Rights', u'Preamble', u'Whereas' ...

# Loading your own Corpus
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
wordlists.words('connectives')

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

# 2.2 Conditional Frequency Distributions
from nltk.corpus import brown
cats = ['religion', 'science_fiction']
#cfd = nltk.ConditionalFreqDist(
#    (genre, word)
#    for genre in cats
#    for word in brown.words(categories=genre))
genre_word = [
    (genre, word)
    for genre in cats
    for word in brown.words(categories=genre)
]
len(genre_word)
genre_word[:4]
genre_word[-4:]
cfd = nltk.ConditionalFreqDist(genre_word)
cfd
cfd.conditions()
cfd[cats[0]]
cfd[cats[1]]
#<FreqDist with 3233 samples and 14470 outcomes>
len(list(cfd[cats[1]]))
#3233
cfd[cats[1]]['could']
#49

# Plotting and Tabulating Distributions
from nltk.corpus import udhr
def udhr_cond_freq_dist(udhr, languages):
    return nltk.ConditionalFreqDist(
        (lang, len(word))
        for file in udhr.fileids()
        for lang in languages if lang in file
        for word in udhr.words(file))
languages = [
    'English',
    'French',
    'German',
    'Italian',
    'Spanish',
]
langs = ['English', 'German']
cfd = udhr_cond_freq_dist(udhr, languages)
cfd.tabulate(conditions=langs, samples=range(1,10), cumulative=True)

# Your Turn
from nltk.corpus import brown
cats = brown.categories() #['news', 'religion', 'science_fiction']
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in cats
    for word in brown.words(categories=genre)
)
days = [day + 'day' for day in ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']]
cfd.tabulate(samples=days)
cfd.plot(samples=days)

# Generating Bigram Text
f = 'english-kjv.txt'
w = nltk.corpus.genesis.words(f)
b = nltk.bigrams(w)
cfd = nltk.ConditionalFreqDist(b)

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word = cfdist[word].max() # XXX max() renders loops

generate_model(cfd, 'living')

f = 'carroll-alice.txt'
w = nltk.corpus.gutenberg.words(f)
b = nltk.bigrams(w)
cfd = nltk.ConditionalFreqDist(b)
cfd['rabbit']
#<FreqDist with 3 samples and 5 outcomes>
cfd['Rabbit']
#<FreqDist with 30 samples and 45 outcomes>
print cfd['Rabbit']
#<FreqDist: ',': 8, "'": 4, 'blew': 2, 'came': 2, 'read': 2, 'say': 2, 'was': 2, '-': 1, '.': 1, ':': 1, ...>
generate_model(cfd, 'Rabbit')

from nltk.corpus import PlaintextCorpusReader
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

def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

plural('boy')
#'boies'
plural('fan')
#'fen'

# Modules
# local import:
from textproc import plural
plural('boy')
#'boies'
plural('fan')
#'fen'

# Wordlist Corpora
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)

unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))

from nltk.corpus import stopwords
stopwords.words('english')

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in tokens if w.isalpha() and w.lower() not in stopwords]
    return len(content) / len(text)

content_fraction(nltk.corpus.reuters.words())

# Word Puzzle
puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
[w for w in wordlist if len(w) >= 6
                     and obligatory in w
                     and nltk.FreqDist(w) <= puzzle_letters]

