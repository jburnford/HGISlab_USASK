**Basic Introduction to the Natural Language Toolkit**
------------------------------------------------------

**Ian comment: I put my comments in bold throughout. I think a big early one is
to really sell why the NLTK shines? It can do some things that other packages
don't offer, but other things will be familiar to users - i.e. word frequency,
normalizing by lowercasing, etc. Another paragraph really selling the utility of
this might help. Maybe an example from your own research?**

This lesson introduces the [Natural Language Toolkit
(NLTK)](<http://www.nltk.org/>), which is "a leading platform for building
Python programs to work with human language data.” The NLTK is a Python package
that adds a wide range of functions and tools that can be used for text mining
historical sources. This includes basic processes such as breaking a text into
paragraph, sentence and/or word tokens, through to more advanced sentement
analysis or part of speech tagging and named entity recognition. It also
includes a wide range of data, from multilingual stopword lists to large test
corpus, some of which are particularly useful for testing digital history
methods (such as the Inaugural Address corpus). The benefits of the NLTK for an
aspiring digital historian are two fold. First, the package includes a lot of
functions that make basic tasks, from tokenizing, word frequency, or key words
in context (also called concordance) very simple to implement. Secondly, there
is an excellent open access book\* written by the NLTK developers that
introduces natural language processing and programming in Python. The NLTK was
developed as a teaching tool and the book introduces natural language processing
while teaching python and quickly moves beyond basic text analysis to more
advanced chapters on "Learning to Classify Text” or "Analyzing the Meaning of
Sentences”. Throughout the book readers encounter sample code that is easily
adapted to working with historical texts. Given the quality of this resource,
this lesson will simply introduce some of the basic aspects of the NLTK and end
off by encouraging readers to continue their learning by working through the
book.

\*NLTK has been updated to Version 3 and the published book uses Version 2. The
authors are currently updating the book and plan to publish a second edition in
early 2016. The online version has incorporated most of the updates and flags
the chapters that are still works in progress.

### Online Demonstration: 

Before installing the NLTK package on your computer, we can test some of its key
features online. [Text-Processing.com](<http://text-processing.com/demo/>)
allows us to demo a range of tools including: tokenization, sentiment analysis
and named entity chunking. I found a useful sample sentence with lots of people
and place names by searching the British Parliament’s HANSARD 1803–2005 website
for [Saskatoon](<http://hansard.millbanksystems.com/search/Saskatoon>): "Mr.
Pirie asked the Prime Minister whether he has received resolutions from
Vancouver, Winnipeg, New York, St. Louis, Albany, Saskatoon, and other places,
congratulating the Government on their promise to draft a measure of Scottish
Home Rule; and whether he is aware of the disappointment created by the failure
of the Government to implement their pledge?” ([Hansard, July 6,
2014](<http://hansard.millbanksystems.com/commons/1914/jul/06/scottish-home-rule#S5CV0064P0_19140706_HOC_241>))

**Tokenizer:**

Try cutting and pasting the sample sentence into the [Tokenize Text
box](<http://text-processing.com/demo/>) and click tokenize. Scroll down the
results and look at the subtle differences between the different tokenizers.
Some simply break up the words by looking for a space, while others create
tokens out of punctuation, and others still take abbreviations into account and
in this case keep the period connected to “Mr.”. These more sophisticated
tokenizers have significant advantages, as they don’t remove meaningful grammar
from the tokens.

Tokenizing provides some insight into how we get computers to work with
language. Computers do not know the meaning or structure of English and we need
to break the text into component parts before starting further analysis.
Tokenizing alone, however, does not really help historians or digital humanists;
it is a first step in a pipeline or series of text mining steps that build on
each other and make it possible to extract useful information. The website demos
some of these more advanced steps, including part of speech tagging, chunking
and sentiment analysis.

**Tag and Chunk Text:**

We can use the same Hansard sentense to demo some of the Tag and Chunk Text
tools. Cut and past it into the box and click the "Tag & Chunk”. This tool
starts by tagging all of the tokens with different parts of speech and then
extracts [noun phrase](<https://en.wikipedia.org/wiki/Noun_phrase>)s. The
results from the Default Tagger & Named Entity (NE) Chunker are not that
promising. Try some of the other options. The Default Tagger & IEER NE Chunker
is a little more successful with the locations, but still makes some errors. It
would be possible to [train a Named Entity
Chunker](<http://mattshomepage.com/#/blog/feb2013/liftingthehood>) on a sample
of the Hansard corpus to improve results further.

**Sentiment Analysis:**

The NLTK is also capable of analysing wether a text is positive or negative. For
the Sentiment Analysis demo select some reviews of 12 Years a Slave from IMDb:
[Loved It](<http://www.imdb.com/title/tt2024544/reviews?filter=love>) & [Hated
It](<http://www.imdb.com/title/tt2024544/reviews?filter=hate>). Cut a few
positive and negative reviews and past them (one at a time) into the [Sentiment
Analysis demo box](<http://text-processing.com/demo/sentiment/>). The tool
starts by assessing whether the text is natural or polarized and if it finds it
is polarized it estimates whether it is positive or negative. As with just about
all  text mining methods, sentiment analysis does not work as effectively as
close reading, but it still might be a useful tool to identify negative
paragraphs in a large corpus of text, which you could then scrutinize using more
traditional historical methods.

 

### Installing Python:

**Comment from Ian: Could you give a bit more guidance to users here? Do you
think they should dive right ahead and move on to Python 3? Or is 2.7 sufficient
to get through your lessons? I think you want to be upfront.**

Python 2.7 and 3.x:

There are two versions of Python 2.7 and 3.x. Version 2.7 is no longer
developed, but a lot of older code still relies on it and a lot of people
continue to use it. The most recent version of the NLTK has been adapted for
Python 3, so this lesson includes instructions to use both versions. If you’d
like to try Version 3.\# may need to install the new version if you’ve done the
other Python lessons on this website. You can install both versions on your
computer and use them both. The most noticeable change is that the print command
requires brackets in version 3: print(“Hello World”). If you are accustom to
working with 2.7 there is no need to make the switch to use the NLTK.

1.  [Programing Historian instructions on installing Python
    2.7](<http://programminghistorian.org/lessons/introduction-and-installation>):

    -   This lesson works with Python from the command line or a Python Shell
        and does not require Komodo edit.

2.  [Installing Python 3 on
    Windows](<http://www.howtogeek.com/197947/how-to-install-python-on-windows/>):

    -   Choose the 32 bit version.

    -   Windows users might also consider installing
        [Cygwin](<http://cygwin.com/>), which makes it easy to work with a range
        of opensource software. Its tagline: "Get that Linux feeling - on
        Windows."

3.  Installing Python 3 on Mac OSX (Mac comes with 2.7 installed, but it is easy
    to add the latest release of version 3): [Find the documentation
    here](<https://docs.python.org/3/using/mac.html>).

4.  Both versions of Python normally come preinstalled on Linux. For more
    information, [visit this site](<https://docs.python.org/3/using/unix.html>).

 

If you are on a Mac or Linux machine, launch your terminal and start working
with Python through the command line. Mac users can find Terminal in the
Utilities folder in the Applications folder or by searching for Terminal in the
Spotlight Search (top right of your screen). Once you’ve opened the Terminal,
simply type python or python3 and hit enter:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$python
Python 2.7.6 (default, Sep  9 2014, 15:04:36) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 

or 

$python3
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Windows users should use the Python Shell, which provides a similar command line
interface, but adds syntax highlighting and was designed with beginners in mind.
This might be a good option for most Mac users as well. If you’re using the
Python included automatically by the Mac OS you will not have access to the IDLE
Shell, but you can easily update and add this feature by [downloading and
installing the latest 2.7 package](<https://www.python.org/downloads/>). It
should be included already if you installed either 2.7 or 3.\# on Windows. It is
an optional part of Python in most Linux packages.

Search for IDLE in your Mac Search Bar or Python in your Windows Start Menu
search.

 

### Installing NLTK and BeautifulSoup:

Python has a core language and then packages that extend the language. This
tutorial uses the Natural Language Toolkit or NLTK for text mining and we need
to get it and Beautiful Soup installed.

1.  The NLTK website provides instructions on installing their package and Numpy
    on Mac/Linux or Windows machines: <http://www.nltk.org/install.html. >

    -   This might be the most difficult aspect of the whole lesson. There are a
        number of steps and a range of different options.

    -   Mac and Linux have a number of different options to install Python
        packages. Python 3 now includes the most population option called Pip.
        For those running Python 3 you can simply use the Terminal (not Python)
        command line and type in:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$sudo pip install -U nltk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    -   If you’re working with Python 2.7 and have not perviously installed Pip
        then the command above will fail (if you don’t remember, give it a try
        and see if it works).

        -   If you do not have Pip you need to first install Easy Install and
            then install Pip. Use curl on the Terminal command line to install
            Easy Install:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$curl https://bootstrap.pypa.io/ez_setup.py -o - | python
$sudo easy_install pip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    -   Once that is complete, you can use the pip command above to install
        NLTK.

    -   It is a little easier for Windows.

        -   Go to the Windows [download
            page](<https://pypi.python.org/pypi/nltk>) and be sure to choose the
            [nltk-3.0.4.win32.exe
            ](<https://pypi.python.org/packages/2.6/n/nltk/nltk-3.0.4.win32.exe#md5=0a46df1aa62d05b6d5d4bf70f93e4689>)MS
            Windows installer. Double click on the .exe file once it is
            downloaded and follow the instructions.

    -   You can also install Numpy, an important Python package used for a wide
        range of scientific computing, but it is not necessary for this lesson.

1.  To double check that it all worked, launch Python in your terminal or Python
    Shell and try to import nltk and hit enter. If you don’t get an error it
    worked:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>import nltk 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Beautiful Soup:**

1.  Next, check to see if you have Beautiful Soup already installed from a
    pervious lesson.

2.  From the Python command line or Shell, try ‘import bs4’ and hit enter to
    check Beautiful Soup is installed.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>import bs4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  If you get an error, visit the "[Intro to Beautiful
    Soup](<http://programminghistorian.org/lessons/intro-to-beautiful-soup>)"
    lesson for instructions on installing beautifulsoup4

 

**NLTK Data:**

NLTK also provides some data that we’ll use in the workshop. Use the Python
Console again and follow these instructions (from
<http://www.nltk.org/data.html>):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> import nltk
>>> nltk.download()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    -   The NLTK downloader should open in a new window.

    -   Choose Book Everything used in the NLTK Book and click Download.

![](<ProgrammingHistorianNLTKdraft.images/6FPFwW.png>)

To test that it worked try:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> from nltk.corpus import brown
>>> brown.words()
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

 

**The Internet Archive:**

The internet is a massive and growing archive for humanities research. The
Internet Archive (Archive.org) is the largest archive in the world and it is
easy to search and bulk download thousands of historical documents from this
website. In October 2012, its collection topped 10 petabytes. Take a look at
Caleb McDaniel’s Programming Historian lesson titled "[Data Mining the Internet
Archive
Collection](<http://programminghistorian.org/lessons/data-mining-the-internet-archive>)”
for more information.

 

In this workshop we’ll be looking at Karl Marx’s
[Capital](<https://archive.org/details/capitalcritiqueo00marx>) and Adam Smith’s
[Wealth of Nations](<https://archive.org/details/WealthOfNationsAdamSmith>). We
need to find the web addresses for the plain text versions:

<http://archive.org/stream/capitalcritiqueo00marx/capitalcritiqueo00marx_djvu.txthttp://archive.org/stream/capitalcritiqueo00marx/capitalcritiqueo00marx_djvu.txt>

<https://archive.org/stream/WealthOfNationsAdamSmith/Wealth%20of%20Nations_Adam%20Smith_djvu.txt>

 

The code will work on any text in this digital archive if you find the URL for
the djvu.txt.

 

 

### Python Code explained:

 

Each time we start working with Python we need to import the packages we will
use. Here we import urllib2 or urllib.request so Python can read websites,
Beautifulsoup to download and convert the webpage to raw text and nltk to
process the raw text.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python2: >>>import urllib2
Python3: >>>import urllib.request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>from bs4 import BeautifulSoup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>import nltk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>from nltk.corpus import stopwords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Next we can establish any code that we'll use a number of times below. When we
use an equal sign the Python interpreter assigns the data or code to that value.

 

First we need to create our list of stopwords. We’ll use the English list
provided by the NLTK data you downloaded above.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>stopword = stopwords.words('english')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can add punctuation to the list of stopwords:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>punk = [".", ",", ";", "\"", "\'", "?", "(", ")", ":", "-", "_", "`","''","``","—","...","&"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>stopword.extend(punk)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can now start by downloading an English translation of Karl Marx’s Capital.

 

There are a number of way to import the contents of an Internet Archive text
page. We will use Beautiful Soup and urllib to open and reads the website, and
return the HTML code (not the small change between Python 2 and 3):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python 2:
>>>soup = BeautifulSoup(urllib2.urlopen("http://archive.org/stream/capitalcritiqueo00marx/capitalcritiqueo00marx_djvu.txt").read())

Python3:
>>>soup = BeautifulSoup(urllib.request.urlopen("http://archive.org/stream/capitalcritiqueo00marx/capitalcritiqueo00marx_djvu.txt").read())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   *You can cut and past the address to a different Internet Archive text here
    and explore the results.*

We can check the source HTML code and find that the \<pre\> tag comes after all
of the website preamble that we don't want to include. This command searches
through the string of HTML data and finds the location of the \<pre\> tag and
returns the [text
string](<http://en.wikipedia.org/wiki/String_%28computer_science%29>) from that
point forward. We now have the long raw text of Marx's Capital.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>raw = soup.pre.string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can measure the number of characters in the book:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>len(raw)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This tokenizer breaks the text in too a list of word tokens.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>tokens = nltk.word_tokenize(raw)
>>>tokens[500:600]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can measure the number of tokens in the book:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>len(tokens)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This next steps creates a NLTK "Text" from the tokens, which is a more
complicated data structure than the simple list of tokens and allows us to
preform a range of other NLTK functions below. You will not see the results and
when you ask it to display the contents of text between 500 and 600 it looks
identical to the list of tokens.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text = nltk.Text(tokens)
>>>text[500:600]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can also it normalizes all the words to lowercase, which makes it possible to
count word frequencies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>words = [w.lower() for w in text]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>words[100:200]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can list the most frequent words to see it they provide any useful
information.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>fdist0 = nltk.FreqDist(words)
>>>fdist0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our word list, however, just lists a range of common English worlds "the", "of",
"a", "to" and punctuation. The results from this book will be very similar to
most other books on found on the Internet Archive. The next step uses our
stopword list created above to strip out common words and punctuation from our
list of words. We will also only return words larger than 1 characters as this
reduces some of the noise showing up in the word frequencies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>filtered_words = [w for w in words if not w in stopword or len(w) > 1]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>filtered_words[500:600]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can now uses the Frequency Distribution function again to determine the most
frequent words in the filtered list:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>fdist1 = nltk.FreqDist(filtered_words)
>>>fdist1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Next we can produce a vocabulary of words used in the text by discarding all
duplicates and sorting the results. This makes it possible to compare the
vocabulary used by different authors. Note down the number of words used by Marx
and we can compare this result with Adam Smith below.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>vocab = sorted(set(filtered_words))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>len(vocab)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The [Collocations](<https://en.wikipedia.org/wiki/Collocation>) command is
really helpful, as it finds the most common word pairs in the text, which can
provide some insight into the topics covered in the book. You'll notice,
however, we still have some issues with end of line hyphenations from the OCR
process as a few split words show up in the collocations results:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.collocations()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

[Concordance](<https://en.wikipedia.org/wiki/Key_Word_in_Context>) is another
really powerful function that displays keywords in context (i.e. with the words
that come before and after the key term). It give us a quick way to check the
context of key terms like freedom or nature. Feel free to add a third or fourth
concordance:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.concordance('freedom')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.concordance('nature')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.concordance('**add your own word here**')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The pos\_tag function adds part of speech tags to word tokens (i.e. is the word
a noun, verb, adjective etc). This is a slow, computationally intensive, task,
so we can limited to a small sample. This is an important step in an NLP
pipeline, as more complicated tasks reply on part of speech tags. For example,
we can add Named Entity tags to the part of speech tags.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>tagged= nltk.pos_tag(tokens[8000:10000])
>>>namedentities = nltk.ne_chunk(tagged)
>>>namedentities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skim through the results and try to find some Orangizations, People and Places.
The NLTK book provides a method for extracting relationships out of this tagged
data, so you can identify organizations linked to places in the text. Marx’s
*Capital* is not the best test material for this tool.

This regular expression provide a wide range of methods to search through the
text. This example finds all the words found before the word man in the text:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.findall(r" (<.*>) <man>")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This final function creates a text dispersion graph that shows us where
different words appear in the text. This tool is particularly useful if you have
a historical corpus and you can explore changing uses of key words over time. It
can still be interesting to see where certain words show up in high
concentration throughout a long book such as *Capital*:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.dispersion_plot(["labour", "democracy", "freedom", "capital", "nature"])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   *Try changing the search terms, but make sure you keep the syntax the same
    with quotation marks and commas.*

 

### Same again for Adam Smith:

You can now explore a second classic economic text and decide whether the
results are notably different from Marx’s *Capital*.

 

Download the book using BeautifulSoup:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python 2:
>>>soup = BeautifulSoup(urllib2.urlopen("https://archive.org/stream/WealthOfNationsAdamSmith/Wealth%20of%20Nations_Adam%20Smith_djvu.txt").read())


Python 3:
>>>soup = BeautifulSoup(urllib.request.urlopen("https://archive.org/stream/WealthOfNationsAdamSmith/Wealth%20of%20Nations_Adam%20Smith_djvu.txt").read())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Identify the raw text:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>raw = soup.pre.string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Raw text length:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>len(raw)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Tokenize:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>tokens = nltk.word_tokenize(raw)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Number of tokens:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>len(tokens)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Create a NLTK Text:

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text = nltk.Text(tokens)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Lower case words:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>words = [w.lower() for w in text]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Filtered words:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>filtered_words = [w for w in words if not w in stopword or len(w) > 1]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>filtered_words[500:600]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Frequency Distribution (filtered):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>fdist1 = nltk.FreqDist(filtered_words)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python2: >>>print fdist1
Python3: >>>print(fdist1.most_common(20))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Vocabulary:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>vocab = sorted(set(filtered_words))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>len(vocab)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Which author used more non-stopwords?

 

Collocations:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.collocations()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Concordances::

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.concordance('freedom')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.concordance('nature')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.concordance('**add your own word here**')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Words before man:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.findall(r" (<.*>) <man>")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Disperson Plot:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>text.dispersion_plot(["labour", "democracy", "freedom", "capital", "nature"])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   *Try changing the search terms, but make sure you keep the syntax the same
    with quotation marks and commas.*

 

### **Challenges:​**

1.  Can you write the code above into a short program in a text editor that will
    work on any Internet Archive plain text URL?

    -   Tips: you’ll need to add print commands and you might want to add
        "input("Press Enter to continue…”)” between the steps so the program
        pauses and allows you to read the results.

2.  Can you use the Word Frequency, Collocations and/or Concordance tools from
    this lesson with the bulk downloading lessons
    ([Wget](<http://programminghistorian.org/lessons/automated-downloading-with-wget>)
    or [Internet
    Archive](<http://programminghistorian.org/lessons/data-mining-the-internet-archive>))
    to quickly explore more than a thousand Internet Archive texts?

 

### **The NLTK Book:**

Once again, this lesson only touched the surface of the power of the NLTK
package and did not introduce you to the field of computational linguistics**​**.
The NLTK book is available for [free online](<http://www.nltk.org/book/>) or
through major online books stores (wait until the revised second edition comes
out in early 2016 if you’d like to buy a paper copy). It provides a great crash
course in natural language processing and provides an opportunity to further
develop your Python skills.

-   Steven Bird, Ewan Klein, and Edward Loper, *Natural Language Processing with
    Python*, <http://www.nltk.org/book>
