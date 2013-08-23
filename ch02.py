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
#religion = brown.words(categories=genres[1])
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
sents[0] #[u'Universal', u'Declaration', u'of', u'Human', u'Rights'...

# Loading your own Corpus
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
wordlists.words('connectives')

# 2.2 Conditional Frequency Distributions
from nltk.corpus import brown
cats = ['religion', 'science_fiction']
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
cfd[cats[1]] #<FreqDist with 3233 samples and 14470 outcomes>
len(list(cfd[cats[1]])) #3233
cfd[cats[1]]['could'] #49

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
cfd['rabbit'] #<FreqDist with 3 samples and 5 outcomes>
cfd['Rabbit'] #<FreqDist with 30 samples and 45 outcomes>
print cfd['Rabbit'] #<FreqDist: ',': 8, "'": 4, 'blew': 2, 'came': 2...>
generate_model(cfd, 'Rabbit')

from nltk.corpus import PlaintextCorpusReader
corpus_root = '/Users/gene/Backed/Documents'
taow = PlaintextCorpusReader(corpus_root, 'artofwar.txt')
b = nltk.bigrams(taow.words())
len(b) #13037
cfd = nltk.ConditionalFreqDist(b)
generate_model(cfd, 'enemy') # enemy ' s own men , and the enemy ' s own men , and

# Functions
f = open('/Users/gene/Backed/Documents/artofwar.txt')
raw = f.read()
def lexical_diversity(text):
    word_count = len(text)
    vocab_size = len(set(text))
    lexical_diversity = word_count / vocab_size
    return lexical_diversity

lexical_diversity(raw)

# XXX Lame:
def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

plural('boy') #'boies'
plural('fan') #'fen'

# Modules
# local import:
from textproc import plural
plural('boy') #'boies'
plural('fan') #'fen'

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

# Personal names.
names = nltk.corpus.names
names.fileids() #['female.txt', 'male.txt']
male_names = names.words('male.txt')
female_names = names.words('female.txt')
androgenous = [w for w in male_names if w in female_names]
len(androgenous) #365

cfd = nltk.ConditionalFreqDist(
    (fileid, name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid)
)
cfd.plot()

# Pronounciation database entries.
# word x phonetic code list ("phones")
# Where phone digits represent primary stress (1), secondary stress (2) & no
# stress (0).
entries = nltk.corpus.cmudict.entries()
len(entries) #133737
entries[133736] #('zywicki', ['Z', 'IH0', 'W', 'IH1', 'K', 'IY0'])
i = 39943
j = 9
for entry in entries[ i : i + j ]:
    print entry

[e for e in entries if e[0] == 'gene'] # [('gene', ['JH', 'IY1', 'N'])]
[e for e in entries if e[0].startswith('gene')] # [('gene', ['JH', 'IY1', 'N'])]

syllable = ['N', 'IH0', 'K', 'S']
[word for word, pron in entries if pron[-4:] == syllable]
syllable = ['IY1', 'N']
[word for word, pron in entries if pron[-2:] == syllable]

# Show words that end with a "silent n."
[w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n']
# Show the sorted set of initial letters of words that sound like they start
# with an 'N' but actually don't.
sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n'))
#['gn', 'kn', 'mn', 'pn']

# Return the syllable stress list.
def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]

[w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']]
[w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']]
[w for w, pron in entries if stress(pron) == ['0', '0']]

# Pronunciation dictionary.
prondict = nltk.corpus.cmudict.dict()
prondict['fire'] #[['F', 'AY1', 'ER0'], ['F', 'AY1', 'R']]

prondict['foo'] #[['F', 'UW1']]
prondict['foobar'] #[['F', 'UW1', 'B', 'AA1', 'R']]
prondict['foobarbaz']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'foobarbaz'

prondict['jazz'] # [['JH', 'AE1', 'Z']]
prondict['foobarbaz'] = [['F', 'UW1', 'B', 'AA1', 'R', 'B', 'AE1', 'Z']]

# Kraftwerk ftw.
text = ['bowing', 'boom', 'chalk']
[ph for w in text for ph in prondict[w][0]]
#['B', 'OW1', 'IH0', 'NG', 'B', 'UW1', 'M', 'CH', 'AA1', 'K']
prondict['boing'] = [['B', 'OY1', 'N']]
text = ['boing', 'boom', 'chuck']
[ph for w in text for ph in prondict[w][0]]
#['B', 'OY1', 'N', 'B', 'UW1', 'M', 'CH', 'AH1', 'K']

# Comparative Wordlists
from nltk.corpus import swadesh
len(swadesh.words('en')) #207
en2fr = swadesh.entries(['en', 'fr'])
translate = dict(en2fr)
translate['one'] #'un'
translate['two'] #'deux'
translate['three'] #'trois'
# Swap wordlists.
en2es = swadesh.entries(['en', 'es'])
translate.update(dict(en2es))
translate['dog'] #'perro'
translate.update(dict(en2fr))
translate['dog'] #'chien'

# Show common entries.
languages = ['en', 'de', 'nl', 'es', 'fr', 'pt', 'la']
entry = range(139, 143)
for i in entry:
    print swadesh.entries(languages)[i]

# Toolbox Lexicon
# http://www.sil.org/computing/toolbox/
from nltk.corpus import toolbox
toolbox.entries('rotokas.dic')
# TODO Find/build useful toolbox.dic files.

# WordNet
from nltk.corpus import wordnet as wn
# synset, synsets: synonym set
# lemma: collection of synonymous words
syn = 'car.n.01'
wn.synsets('motorcar')
wn.synset(syn).lemma_names #['car', 'auto', 'automobile', 'machine', 'motorcar']
wn.synset(syn).definition #'a motor vehicle with four wheels;...
wn.synset(syn).examples #['he needs a car to get to work']
wn.synset(syn).lemmas #[Lemma('car.n.01.car'), Lemma('car.n.01.auto'), ...
wn.lemma(syn + '.automobile') #Lemma('car.n.01.automobile')
wn.lemma(syn + '.automobile').synset #Synset('car.n.01')
wn.lemma(syn + '.automobile').name #'automobile'
wn.synsets('car') #[Synset('car.n.01'), Synset('car.n.02'),...
for synset in wn.synsets('car'):
    print synset.lemma_names

#['car', 'auto', 'automobile', 'machine', 'motorcar']
#['car', 'railcar', 'railway_car', 'railroad_car']
#['car', 'gondola']
#['car', 'elevator_car']
#['cable_car', 'car']

wn.lemmas('car') #[Lemma('car.n.01.car'), Lemma('car.n.02.car'),...

# The WordNet Hierarchy
#
# Hypernyms and hyponyms are lexical relations that relate synsets. These
# relations navigate up and down the "is-a" path hierarchy.
# Hyponym: conceptually "more specific"
# Hypernym: conceptually "more general"
# Hypernym paths lead to more general terms.
cars = wn.synset('car.n.01')
car_types = cars.hyponyms()
car_types[26] #Synset('ambulance.n.01')
sorted([lemma.name for synset in car_types for lemma in synset.lemmas])
#['Model_T', 'S.U.V.', 'SUV'...'used-car', 'waggon', 'wagon']
cars.hypernyms()
paths = cars.hypernym_paths()
len(paths) #2
# wheeled_vehicle.n.01 is classed as both vehicle & container.
[synset.name for synset in paths[0]]
[synset.name for synset in paths[1]]
cars.root_hypernyms()

# Brose WN.
nltk.app.wordnet() # W00! Very cool!

# More Lexical Relations
# meronyms: Parts, kinds of
wn.synset('tree.n.01').part_meronyms()
wn.synset('tree.n.01').substance_meronyms()
# holonyms: Groups of
wn.synset('tree.n.01').member_holonyms()

# Inspect the relations of the word "mint."
for synset in wn.synsets('mint', wn.NOUN):
    print synset.name + ':', synset.definition

# The leaves are a part of the plant.
wn.synset('mint.n.04').part_holonyms() #[Synset('mint.n.02')]
# A derived candy from the plant.
wn.synset('mint.n.04').substance_holonyms() #[Synset('mint.n.05')]

# Verb entailments.
wn.synset('walk.v.01').entailments() #[Synset('step.v.01')]
wn.synset('eat.v.01').entailments()
#[Synset('swallow.v.01'), Synset('chew.v.01')]
wn.synset('tease.v.03').entailments()
#[Synset('arouse.v.07'), Synset('disappoint.v.01')]
# Lemma relations.
wn.lemma('supply.n.02.supply').antonyms()
#[Lemma('demand.n.02.demand')]
wn.lemma('rush.v.01.rush').antonyms()
#[Lemma('linger.v.04.linger')]
wn.lemma('horizontal.a.01.horizontal').antonyms()
#[Lemma('vertical.a.01.vertical'), Lemma('inclined.a.02.inclined')]
wn.lemma('staccato.r.01.staccato').antonyms()
#[Lemma('legato.r.01.legato')]

# Methods defined on a synset.
dir(wn.synset('harmony.n.02'))
# ['__class__', '__delattr__' ... 'verb_groups', 'wup_similarity']
help(wn) # Also handy.

# Semantic Similarity.
right = wn.synset('right_whale.n.01')
things = ['orca', 'minke_whale', 'tortoise', 'novel']
i = 0
# Show common conceptual ancestors and respective metrics.
for thing in things:
    i += 1
    syns = wn.synset(thing + '.n.01')
    print '%d path. %s %s = %.4f similarity' % (i, right, syns, right.path_similarity(syns))
    for hyp in right.lowest_common_hypernyms(syns):
        min = hyp.min_depth()
        print '\t%s = %d synset depth' % (hyp, min)

# Verbs!
from nltk.corpus import verbnet as vn
vn
<VerbnetCorpusReader in '.../corpora/verbnet' (not loaded yet)>
# XXX Can't make this work, even after reading the source (with no docs).

# 2.8 Exercises
# 2.
austen = nltk.corpus.gutenberg.words('austen-sense.txt')
len(austen) #141576
len(set(austen)) #6833

# 4.
from nltk.corpus import state_union
state_union.fileids()
def cond_freq_dist(text, targets):
    cfd = nltk.ConditionalFreqDist(
        (target, fileid[:4])             # word target, file name year
        for fileid in text.fileids()     # text file name
        for w in text.words(fileid)      # all words in the address
        for target in targets            # all targets
        if w.lower().startswith(target)) # ...that is lower, etc.
    cfd.plot()

targets = ['people','man','woman']
cond_freq_dist(state_union, targets)
targets = ['terror','freedom','secur','priv']
cond_freq_dist(state_union, targets)

# 5.
from nltk.corpus import wordnet as wn
# Meronyms: Parts, kinds of
#{member,part,substance}_meronyms()
# Holonyms: Groups of
#{member,part,substance}_holonyms()
concept = 'think'
for synset in wn.synsets(concept, wn.VERB):
    print synset.name + ':', synset.definition

syn = 'shopfront.n.01'
wn.synset(syn).member_meronyms()
wn.synset(syn).part_meronyms()
wn.synset(syn).substance_meronyms()
wn.synset(syn).member_holonyms()
wn.synset(syn).part_holonyms()
wn.synset(syn).substance_holonyms()

# 7.
text = nltk.Text(state_union.words())
text.concordance('however') # . However , = 25. , however , = 67.

# 8. Already done above
# 9. Words in common (but with different usage-meaning)
nltk.corpus.gutenberg.fileids() # What are the file names again?
austen = nltk.corpus.gutenberg.words('austen-sense.txt')
austen_vocab = set([w.lower() for w in austen if w.isalpha()])
moby = nltk.corpus.gutenberg.words('melville-moby_dick.txt')
moby_vocab = set([w.lower() for w in moby if w.isalpha()])
shared_vocab = [a for a in austen_vocab for m in moby_vocab if a == m]
len(shared_vocab) #4354
# TODO Use WN to puzzle-out "different usage-meaning?"

# 10. "word types?" As in ...stemming?  XXX This was never discussed.
# # Hyponym: conceptually "more specific" ^ Maybe
# 11. Already done above
# 12.
prondict = nltk.corpus.cmudict.dict()
len(prondict) #123455
len(set(prondict)) #123455 - All distinct.
alphas = [w for w in prondict if w.isalpha()]
len(alphas) #115533
multi_pron = [w for w in alphas if len(prondict[w]) > 1]
len(multi_pron) #8492
8492 / 115533 #7.4% of words have muliple pronunciations.

# 13. Noun synsets without hyponyms.
from nltk.corpus import wordnet as wn
for s in wn.all_synsets('n'):
    if len(s.hyponyms()) == 0:
        print s

# 14. Show word: defn & any {hyper,hypo}nyms with defns.
def supergloss(s):
    print "%s: %s" % (wn.synset(syn).lemma_names[0], s.definition)
    if len(s.hypernyms()) > 0:
        print "Hypernyms:"
        for hyp in s.hypernyms():
            print "\t%s: %s" % (hyp.lemma_names[0], hyp.definition)
        print "Hyponyms:"
        for hyp in s.hyponyms():
            print "\t%s: %s" % (hyp.lemma_names[0], hyp.definition)

syn = 'car.n.01'
supergloss(wn.synset(syn))

# 15. All words that occur at least X times in document Y.
from nltk.corpus import brown
adventure = brown.words(categories=brown.categories()[0])
scifi = brown.words(categories=brown.categories()[-1])
len(scifi) #14470
len([w.lower() for w in scifi if w.isalpha()]) #11762
len(set([w.lower() for w in scifi if w.isalpha()])) #2870
# Return a list of pair-lists for "normalized" word occurances.
def occurance(n, text):
    fdist = nltk.FreqDist([w.lower() for w in text if w.isalpha()])
    occurance = []
    i = 0
    for word in fdist.keys():
        if fdist[word] >= n:
            occurance.append([word, fdist[word]])
            i = i + 1
            print '%d. %s: %d' % (i, word, fdist[word])
    return occurance

at_least = occurance(700, scifi) #1. the: 723
at_least = occurance(300, scifi) #1. the: 723 2. of: 329 3. to: 306

# 16. Categorical lexical diversity.
#print 'Genre, Tokens, Types, Lexical diversity'
for genre in brown.categories():
    w = brown.words(categories=genre)
    x = len(w)
    y = len(set(w))
    print '%s, %d, %d, %f' % (genre, x, y, (x / y))

# 17. most frequently occurring words of a text that are not stopwords
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('english')
def freq_occuring_words(n, text, stop):
    content = [w.lower() for w in text if w.isalpha() and w.lower() not in stopwords]
    fd = nltk.FreqDist(content)
    print fd.keys()[:n + 1]

freq_occuring(50, adventure, stopwords)

# 18. print the 50 most frequent non-stopword bigrams
def freq_occuring_bigrams(n, words, stop):
    bigrams = nltk.bigrams(words)
    cfd = nltk.FreqDist(
        (w1, w2)
        for (w1, w2) in bigrams
            if w1.isalpha() and w1 not in stop
           and w2.isalpha() and w2 not in stop
    )
    print cfd.keys()[:n + 1]

freq_occuring_bigrams(20, adventure, stopwords)
freq_occuring_bigrams(20, scifi, stopwords)
freq_occuring_bigrams(20, scifi + adventure, stopwords)

# 19. create a table of word frequencies by genre. find words whose presence (or
# absence) is typical of a genre.
cats = brown.categories()
subj_prons = ['i',  'he',  'she', 'it', 'they', 'we', 'you']
obj_prons  = ['me', 'him', 'her', 'it', 'them', 'us', 'you']
# XXX 'it' and 'you' are ambiguous without grammatical analysis.
cfd = nltk.ConditionalFreqDist(
    (genre, word.lower())
    for genre in cats
    for word in brown.words(categories=genre)
        if word.isalpha()
)
cfd.tabulate(conditions=cats, samples=subj_prons)
cfd.tabulate(conditions=cats, samples=obj_prons)
# Fascinating!

