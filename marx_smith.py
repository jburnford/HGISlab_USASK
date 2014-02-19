__author__ = 'jimclifford'
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import nltk



from nltk.corpus import stopwords


pattern = r'''(?x)    # set flag to allow verbose regexps
    ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
    | \w+(-\w+)*        # words with optional internal hyphens
    | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
    | \.\.\.            # ellipsis
    | [][.,;"'?():-_`]  # these are separate tokens
    '''
punk = [".", ",", ";", "\"", "\'", "?", "(", ")", ":", "-", "_", "`"]
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

stopword = stopwords.words('english')

stopword.extend(punk)

print "Karl Marx Capital"
html = urllib2.urlopen("http://archive.org/stream/capitalcritiqueo00marx/capitalcritiqueo00marx_djvu.txt").read()

be = html.find("<pre>")
html2 = html[be:]

raw = nltk.clean_html(html2).replace("-    ","").replace("-   ","").replace("-  ","").replace("- ","").replace("\xe2", "")

tokens = nltk.regexp_tokenize(raw, pattern)

print "WORDS:"
text = nltk.Text(tokens)
words = [w.lower() for w in text]
print words[100:200]

print "FILTERED WORDS"
filtered_words = [w for w in words if not w in stopword]
#filtered_words = [w for w in filtered_words if not w in punk]
filtered_words = [w for w in filtered_words if len(w) > 1]
print filtered_words[500:600]
print "WORD FREQUENCY:"
print nltk.FreqDist(filtered_words)
print "SENTENCES:"


sents = sent_tokenizer.tokenize(raw)
print sents[171:181]

print "VOCAB:"
vocab = sorted(set(filtered_words))
print vocab[500:600]

print "COLLOCATIONS:"
print text.collocations()

print "CONCORDANCE:"
print text.concordance('freedom')


print "PART OF SPEECH TAGGED:"
tagged = nltk.pos_tag(tokens[200:1000])
print tagged

#print "Named Entities"
#entities = nltk.ne_chunk(tagged)
#print entities

print "WORDS FOUND BEFORE _MAN_"
print text.findall(r" (<.*>) <man>")

text.dispersion_plot(["labour", "democracy", "freedom", "capital", "America", "India"])

#Same again for Adam Smith
print "Adam Smith Wealth of Nations"
html = urllib2.urlopen("https://archive.org/stream/WealthOfNationsAdamSmith/Wealth%20of%20Nations_Adam%20Smith_djvu.txt").read()

be = html.find("<pre>")
html2 = html[be:]

raw = nltk.clean_html(html2).replace("-    ","").replace("-   ","").replace("-  ","").replace("- ","").replace("\xe2", "")

tokens = nltk.regexp_tokenize(raw, pattern)

print "WORDS:"
text = nltk.Text(tokens)
words = [w.lower() for w in text]
print words[100:200]

print "FILTERED WORDS"
filtered_words = [w for w in words if not w in stopword]
#filtered_words = [w for w in filtered_words if not w in punk]
filtered_words = [w for w in filtered_words if len(w) > 1]
print filtered_words[500:600]
print "WORD FREQUENCY:"
print nltk.FreqDist(filtered_words)
print "SENTENCES:"


sents = sent_tokenizer.tokenize(raw)
print sents[171:181]

print "VOCAB:"
vocab = sorted(set(filtered_words))
print vocab[500:600]

print "COLLOCATIONS:"
print text.collocations()

print "CONCORDANCE:"
print text.concordance('freedom')


print "PART OF SPEECH TAGGED:"
tagged = nltk.pos_tag(tokens[200:1000])
print tagged

#print "Named Entities"
#entities = nltk.ne_chunk(tagged)
#print entities

print "WORDS FOUND BEFORE _MAN_"
print text.findall(r" (<.*>) <man>")

text.dispersion_plot(["labour", "democracy", "freedom", "capital", "America", "India"])