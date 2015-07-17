**Basic Introduction to the Natural Language Toolkit**
------------------------------------------------------

 

This lesson is intended to introduce some of the basic features of the [Natural
Language Toolkit (NLTK)](<http://www.nltk.org/>), which is "a leading platform
for building Python programs to work with human language data”. The NLTK is a
Python package that adds a wide range of functions and tools that can be used
for text mining historical soruces. It also includes a wide range of data, from
stopword lists to large test corpus, some of which are particularly useful for
testing digital history methods (such as the Inaugural Address corpus). This
lesson is relatively brief, as there is an excellent open access book\* written
by the NLTK developers that introduces computational linguistics and programming
in Python and this lesson will end off by encouraging digital historians to work
through this fantastic resource.

-   <http://www.nltk.org/>

-   Steven Bird, Ewan Klein, and Edward Loper, *Natural Language Processing with
    Pythoy*, <http://www.nltk.org/book>

\*NLTK has been updated to Version 3 and the publish book uses Version 2. The
authors are currently updating the book and plan to publish a second edition in
early 2016. The online version includes many of the updates and flags the
chapters that are still works in progress.

### Installing Python:

Python 2.7 and 3.x:

There are two versions of Python 2.7 and 3.x. Version 2.7 is no longer
developed, but a lot of older code still relies on it. The most recent version
of the NLTK has been adapted for Python 3, so this lesson will use version 3.
You may need to install the new version if you’ve done the other Python lessons
on this website. You can install both versions on your computer and use them
both. The most noticeable change is that the print command requrieds brackets in
version 3: print(“Hello World”).

1.  Installing Python 3 on Windows:
    <http://www.howtogeek.com/197947/how-to-install-python-on-windows/>

2.  Windows users might also consider installing Cygwin, which makes it easy to
    work with a range of opensource software (Get that Linux feeling - on
    Windows):< http://cygwin.com/>

3.  Installling Python 3 on Mac OSX (Mac comes with 2.7 installed, but it is
    easy to add the latest release of version 3):
    <https://docs.python.org/3/using/mac.html>

4.  Both versions of Python normally come preinstalled on Linux:
    <https://docs.python.org/3/using/unix.html>

 

### Installing NLTK and BeautifulSoup:

Python has a core language and then packages that extent the language for other
uses. This tutorial uses the Natural Language Toolkit or NLTK for text mining
and we need to get it and Beautiful Soup installed.

1.   

2.  The NLTK website provides instructions on installing their package and Numpy
    on Mac/Linux or Windows machines: <http://www.nltk.org/install.html>

3.  to check that it all worked, launch your terminal and start by launching
    Python3 and try to import nltk and hit enter. If you don’t get an error it
    worked:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>python3
import nltk 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Next, check to see if you have Beautiful Soup already installed from a
    pervious lesson.

2.  From the Python consoul, try ‘import bs4’ and hit enter to check Beautiful
    Soup is installed.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import bs4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  If you get an error, visit the "[Intro to Beautiful
    Soup](<http://programminghistorian.org/lessons/intro-to-beautiful-soup>)"
    lesson for instructions on installing beautifulsoup4

NLTK Data:

NLTK also provides some data that we’ll use in the workshop. Use the Python
Console again and follow these instructions (from
<http://www.nltk.org/data.html>):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> import nltk
>>> nltk.download()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

>   A new window should open, showing the NLTK Downloader. Click on the File
>   menu and select Change Download Directory. For central installation, set
>   this to C:\\nltk\_data (Windows), or/usr/share/nltk\_data (Mac, Unix). Next,
>   select the packages or collections you want to download: **[Everything Used
>   in the NLTK book].**

>   If you did not install the data to one of the above central locations, you
>   will need to set theNLTK\_DATA environment variable to specify the location
>   of the data. (On a Windows machine, right click on “My Computer” then select
>   Properties \> Advanced \> Environment Variables \> UserVariables \> New...)

>   Test that the data has been installed as follows. (This assumes you
>   downloaded the Brown Corpus):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> from nltk.corpus import brown
>>> brown.words()
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

 

**The Internet Archive:**

The internet is a massive and growing archive for humanities research. The
Internet Archive (Archive.org) is the largest archive in the world and it is
easy to search and bulk download thousands of historical documents from this
website. In October 2012, its collection topped 10 petabytes. In this workshop
we’ll be looking at Karl Marx’s
[Capital](<https://archive.org/details/capitalcritiqueo00marx>) and Adam Smith’s
[Wealth of Nations](<https://archive.org/details/WealthOfNationsAdamSmith>):

-   Plain Text
    versions:<http://archive.org/stream/capitalcritiqueo00marx/capitalcritiqueo00marx_djvu.txthttp://archive.org/stream/capitalcritiqueo00marx/capitalcritiqueo00marx_djvu.txt>

-   <https://archive.org/stream/WealthOfNationsAdamSmith/Wealth%20of%20Nations_Adam%20Smith_djvu.txt>

 

 

 

### Python Code explained:

 

You can use the link above and cut and past the whole code and run it on your
machine, but it is a better learning experience if you work step by step, either
in the Python Console or by creating a new .py file in PyCharm (*File - New -
Python File*) and running the program each time you add a step.

 

Each time we start working with Python we need to import the packages we will
use. Here we import urllib2 so Python can read websites, Beautifulsoup to
download and convert the webpage to raw text and nltk to process the raw text.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import urllib2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from bs4 import BeautifulSoup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import nltk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from nltk.corpus import stopwords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Next we can establish any code that we'll use a number of times below. When we
use an equal sign the Python interpreter assigns the data or code to that value.

 

I've also chosen to strip punctuation when removing stopwords. I add this list
of punctuation to the end of a list of stopwords provided by the NLTK:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
punk = [".", ",", ";", "\"", "\'", "?", "(", ")", ":", "-", "_", "`","''","``","—","...","&"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
stopword = stopwords.words('english')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
stopword.extend(punk)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

 

**With those basics prepared, the script starts here:**

 

This print command simply prints "Karl Marx Capital" to let us know the program
is starting with this book:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Karl Marx Capital")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This opens and reads the website, returning the HTML code

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
soup = BeautifulSoup(urllib2.urlopen("http://archive.org/stream/capitalcritiqueo00marx/capitalcritiqueo00marx_djvu.txt").read())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   *You can cut and past the address to a different Internet Archive text here
    and explore the results.*

I checked the source HTML code and found that the \<pre\> tag comes after all of
the website preamble that we don't want to include. This command searches
through the string of HTML data and finds the location of the \<pre\> tag and
returns the [text
string](<http://en.wikipedia.org/wiki/String_%28computer_science%29>) from that
point forward. We now have the long raw text of Marx's Capital.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
raw = soup.pre.string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can measure the number of characters in the book:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(len(raw))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tokenizer breaks the text in too a list of word tokens.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tokens = nltk.word_tokenize(raw)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can measure the number of characters in the book:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(len(tokens))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This next steps does two things. It creates a NLTK "Text" from the tokens, which
allows us to preform other NLTK functions.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
text = nltk.Text(tokens)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can also it normalizes all the words to lowercase, which makes it possible to
count word frequencies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
words = [w.lower() for w in text]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(words[100:200])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is not particularly useful, but now that we have a list of all of the words
in the book, we can quickly list the most frequent words to see it they provide
any useful information.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fdist0 = nltk.FreqDist(words)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print fdist0.most_common(20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our word list, however, still contains common English worlds "the", "of", "a",
"to" and punctuation. This next stepuses our stopword list created above to
strip the list of words. I've also only returned words larger than 1 characters
as this reduces some of the noise showing up in the word frequencies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
filtered_words = [w for w in words if not w in stopword]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#filtered_words = [w for w in filtered_words if not w in punk]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
filtered_words = [w for w in filtered_words if len(w) > 1]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(filtered_words[500:600])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can now uses the Frequency Distribution function again to determine the most
frequent words in the filtered list:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print "WORD FREQUENCY of Filtered Words:"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fdist1 = nltk.FreqDist(filtered_words)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(fdist1.most_common(20))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Next we canproduce a vocabulary of words used in the text by discarding all
duplicates and sorting the results.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vocab = sorted(set(filtered_words))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(vocab[500:600])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The Collocations command is really helpful, as it finds the most common word
pairs in the text, which can provide some insight into the topics covered in the
book. You'll notice, however, we still have some issues with end of line
hyphonations from the OCR process as a few split words show up in the
collocations results:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(text.collocations())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Concordance is another really powerful function that displays keywords in
context. It give us a quick way to check the context of key terms like freedom
or nature. Feel free to add a third or fourth concordance:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(text.concordance('freedom'))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(text.concordance('nature'))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(text.concordance('**add your own word here**'))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This function adds part of speech tags to 801 word tokens. This is a slow,
computationally intensive, task, so we can limited to a small sample. This is an
important step in an NLP pipeline, as more complicated tasks, such as Named
Entity Recognition reply on part of speech tags. We could also explore the most
frequently used verbs or nouns in this text with a little more coding.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(nltk.pos_tag(tokens[200:1000]))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This regular expression searches through the text and provides us with the words
found before the word man in the text:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(text.findall(r" (<.*>) <man>"))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This final function creates a text dispersion graph that shows us where
different words appear in the text:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
text.dispersion_plot(["labour", "democracy", "freedom", "capital", "nature"])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   *Try changing the search terms, but make sure you keep the syntax the same
    with quotation marks and commas.*

 

### Same again for Adam Smith:

You can now explore a second classic economic text and decide whether the
resutls are notably different from Marx’s *Capital*.

 

Download the book using BeautifulSoup:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
soup = BeautifulSoup(urllib2.urlopen("https://archive.org/stream/WealthOfNationsAdamSmith/Wealth%20of%20Nations_Adam%20Smith_djvu.txt").read())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Identify the raw text:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
raw = soup.pre.string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Raw text length:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(len(raw))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Tokenize:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tokens = nltk.word_tokenize(raw)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Number of tokens:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(len(tokens))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Text:

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
text = nltk.Text(tokens)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Lower case words:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
words = [w.lower() for w in text]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Filtered words:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
filtered_words = [w for w in words if not w in stopword]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#filtered_words = [w for w in filtered_words if not w in punk]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
filtered_words = [w for w in filtered_words if len(w) > 1]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(filtered_words[500:600])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Frequency Distribution (filtered):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fdist1 = nltk.FreqDist(filtered_words)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(fdist1.most_common(20))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Vocabulary:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vocab = sorted(set(filtered_words))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(vocab[500:600])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Collocations:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(text.collocations())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Concordances::

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(text.concordance('freedom'))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(text.concordance('nature'))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(text.concordance('**add your own word here**'))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Part of Speech Tagging.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(nltk.pos_tag(tokens[200:1000]))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Words before man:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(text.findall(r" (<.*>) <man>"))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Disperson Plot:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
text.dispersion_plot(["labour", "democracy", "freedom", "capital", "nature"])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   *Try changing the search terms, but make sure you keep the syntax the same
    with quotation marks and commas.*

 

### **Final Challange:​**

Can you use the Word Frequency, Collocations and/or Concordance tools from this
lesson with the bulk downloading lessons
([Wget](<http://programminghistorian.org/lessons/automated-downloading-with-wget>)
or [Internet
Archive](<http://programminghistorian.org/lessons/data-mining-the-internet-archive>))
to quickly explore more than a thousand Internet Archive texts?

 

### **The NLTK Book:**

Once again, this lesson only touched the surface of the power of the NLTK
package and did not introduce you to the field of computational linguistics**​**.
The NLTK book is avalible for [free online](<http://www.nltk.org/book/>) or
through major online books stores (wait until the revised second edition comes
out in early 2016 if you’d like to buy a paper copy). It provides a great crash
course in natural language processing and provides an opertunity to further
develop your Python skills.
