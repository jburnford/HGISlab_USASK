__author__ = 'jimclifford'
import urllib2
from bs4 import BeautifulSoup
#This script requires the Natural Language Tool Kit installed and the book data downloaded.
#You can install NLTK using pip: http://www.nltk.org/install.html
#Test the install from a python command line by entering >> import nltk
# Next enter >> nltk.download()
#a graphical interface downloader will pop up and you can choose to download everything included in the book.
#with NLTK installed on your machine, the following two imports should work.
import nltk
from nltk.corpus import stopwords

# This is a regular expression pattern used lower down in the tokenizer.
# It results in a more nuanced split of the raw text into a list of tokens than simply splitting at white spaces.
pattern = r'''(?x)    # set flag to allow verbose regexps
    ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
    | \w+(-\w+)*        # words with optional internal hyphens
    | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
    | \.\.\.            # ellipsis
    | [][.,;"'?():-_`]  # these are separate tokens
    '''
#This defines which sentense tokenizer I've choosen to use.
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

#I've also chossen to strip punctuation when removing stopwords. I add this list of punctuation to the end of a list of
#stopwords provided by the NLTK:
punk = [".", ",", ";", "\"", "\'", "?", "(", ")", ":", "-", "_", "`"]
stopword = stopwords.words('english')
stopword.extend(punk)

#With those basics prepared, the script starts here:

#This print command simply prints "Karl Marx Capital"
print "Karl Marx Capital"
raw_input("Press Enter to continue...")
#This opens and reads the website, returning the HTML code
html = urllib2.urlopen("http://archive.org/stream/capitalcritiqueo00marx/capitalcritiqueo00marx_djvu.txt").read()

#I checked the source HTML code and found that the <pre> tag comes after all of the website preamble that we don't
#want to analysis. This command searches through the string of HTML data and finds the location of the <pre> tag and
#returns the string from that point forward.
be = html.find("<pre>")
html2 = html[be:]

#This is a crucial step if we were working with a page with a lot of HTML coding. It strips out the HTLM and returns
#raw plaintext.
raw = nltk.clean_html(html2).replace("-    ","").replace("\xe2", "")

#This tokenizer using the regular expressions above to break the text in too a list of word tokens.
tokens = nltk.regexp_tokenize(raw, pattern)

#This next steps does two things. It creates a "Text" from the tokens, which allows us to preform other NLTK fucntions.
#And it normalizes all the words to lowercase, which makes it possible to count word frequencies.
print "WORDS:"
text = nltk.Text(tokens)
words = [w.lower() for w in text]
print words[100:200]
raw_input("Press Enter to continue...")
#Our word list, however, still contains common English worlds "the", "of", "a", "to" and punctuation. This next step
#uses our stopword list created above to strip the list of words. I've also only returned words larger than 1 characters
#as I noticed some OCR noise showing up in the word frequencies. The final step prints a random selection of filtered
#words from the 500th to the 600th in the list.
print "FILTERED WORDS"
filtered_words = [w for w in words if not w in stopword]
#filtered_words = [w for w in filtered_words if not w in punk]
filtered_words = [w for w in filtered_words if len(w) > 1]
print filtered_words[500:600]
raw_input("Press Enter to continue...")
#This step uses an NLTK function to determine the most frequent words in the filtered list:
print "WORD FREQUENCY:"
print nltk.FreqDist(filtered_words)

#It is also possible to tokenize the sentences and this step is useful for further natural language analysis. The third
#step prints ten sentences from the middle of the text.
print "SENTENCES:"
sents = sent_tokenizer.tokenize(raw)
print sents[171:181]
raw_input("Press Enter to continue...")
#This step produces a vocabulary of words used in the text by discarding all duplicates and sorting the results.
print "VOCAB:"
vocab = sorted(set(filtered_words))
print vocab[500:600]
raw_input("Press Enter to continue...")
#The Collocations command finds the most common word pairs in the text. You'll notice we still have some OCR issues
#as a few split words show up in the collocations results "commod ities":
print "COLLOCATIONS:"
print text.collocations()
raw_input("Press Enter to continue...")
#Concordance is a really powerful function that displays keywords in context. It give us a quick way to check how the
#text uses words like freedom or nature. Feel free to add a third concordance:
print "CONCORDANCE:"
print text.concordance('freedom')
print text.concordance('nature')
raw_input("Press Enter to continue...")
#This function adds part of speech tags to 801 word tokens. This is a slow, computationally intensive, task, so
#I limited to a small sample for this workshop. This is an important step in an NLP pipeline, as more complicated
#tasks, such as Named Entity Recognition reply on part of speech tags. We could also explore the most frequently used
#verbs or nouns in this text with a little more coding.
print "PART OF SPEECH TAGGED:"
tagged = nltk.pos_tag(tokens[200:1000])
print tagged
raw_input("Press Enter to continue...")
#This searches through the text and provides us with the words found before the word man in the textL
print "WORDS FOUND BEFORE _MAN_"
print text.findall(r" (<.*>) <man>")
raw_input("Press Enter to continue...")
#This final function creates a text dispersion graph that shows us where different words appear in the text:
text.dispersion_plot(["labour", "democracy", "freedom", "capital", "nature"])

#Same again for Adam Smith
print "Adam Smith Wealth of Nations"
html = urllib2.urlopen("https://archive.org/stream/WealthOfNationsAdamSmith/Wealth%20of%20Nations_Adam%20Smith_djvu.txt").read()
raw_input("Press Enter to continue...")
#I checked the source HTML code and found that the <pre> tag comes after all of the website preamble that we don't
#want to analysis. This command searches through the string of HTML data and finds the location of the <pre> tag and
#returns the string from that point forward.
be = html.find("<pre>")
html2 = html[be:]

#This is a crucial step if we were working with a page with a lot of HTML coding. It strips out the HTLM and returns
#raw plaintext.
raw = nltk.clean_html(html2).replace("-    ","").replace("\xe2", "")

#This tokenizer using the regular expressions above to break the text in too a list of word tokens.
tokens = nltk.regexp_tokenize(raw, pattern)

#This next steps does two things. It creates a "Text" from the tokens, which allows us to preform other NLTK fucntions.
#And it normalizes all the words to lowercase, which makes it possible to count word frequencies.
print "WORDS:"
text = nltk.Text(tokens)
words = [w.lower() for w in text]
print words[100:200]
raw_input("Press Enter to continue...")
#Our word list, however, still contains common English worlds "the", "of", "a", "to" and punctuation. This next step
#uses our stopword list created above to strip the list of words. I've also only returned words larger than 1 characters
#as I noticed some OCR noise showing up in the word frequencies. The final step prints a random selection of filtered
#words from the 500th to the 600th in the list.
print "FILTERED WORDS"
filtered_words = [w for w in words if not w in stopword]
#filtered_words = [w for w in filtered_words if not w in punk]
filtered_words = [w for w in filtered_words if len(w) > 1]
print filtered_words[500:600]
raw_input("Press Enter to continue...")
#This step uses an NLTK function to determine the most frequent words in the filtered list:
print "WORD FREQUENCY:"
print nltk.FreqDist(filtered_words)
raw_input("Press Enter to continue...")
#It is also possible to tokenize the sentences and this step is useful for further natural language analysis. The third
#step prints ten sentences from the middle of the text.
print "SENTENCES:"
sents = sent_tokenizer.tokenize(raw)
print sents[171:181]
raw_input("Press Enter to continue...")
#This step produces a vocabulary of words used in the text by discarding all duplicates and sorting the results.
print "VOCAB:"
vocab = sorted(set(filtered_words))
print vocab[500:600]
raw_input("Press Enter to continue...")
#The Collocations command finds the most common word pairs in the text. You'll notice we still have some OCR issues
#as a few split words show up in the collocations results "commod ities":
print "COLLOCATIONS:"
print text.collocations()
raw_input("Press Enter to continue...")
#Concordance is a really powerful function that displays keywords in context. It give us a quick way to check how the
#text uses words like freedom or nature. Feel free to add a third concordance:
print "CONCORDANCE:"
print text.concordance('freedom')
print text.concordance('nature')
raw_input("Press Enter to continue...")
#This function adds part of speech tags to 801 word tokens. This is a slow, computationally intensive, task, so
#I limited to a small sample for this workshop. This is an important step in an NLP pipeline, as more complicated
#tasks, such as Named Entity Recognition reply on part of speech tags. We could also explore the most frequently used
#verbs or nouns in this text with a little more coding.
print "PART OF SPEECH TAGGED:"
tagged = nltk.pos_tag(tokens[200:1000])
print tagged
raw_input("Press Enter to continue...")
#This searches through the text and provides us with the words found before the word man in the textL
print "WORDS FOUND BEFORE _MAN_"
print text.findall(r" (<.*>) <man>")
raw_input("Press Enter to continue...")
#This final function creates a text dispersion graph that shows us where different words appear in the text:
text.dispersion_plot(["labour", "democracy", "freedom", "capital", "nature"])