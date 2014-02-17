__author__ = 'jimclifford'

#this script needs beautifulsoup$ (i.e. bs4), urllib2 and pandas

from bs4 import BeautifulSoup
import urllib2
import pandas as pd

#this opens our bibiography webpage and turns the HTML code into a BeautifulSoup object
soup = BeautifulSoup(urllib2.urlopen("http://www.hgis.usask.ca/bibliography/").read())

#this finds all of the <p> tags on the page and removes the first 4 which do not contain bibiographic information
tagP = soup.find_all("p")[5:]

#this creates an empty pandas dataframe
data = pd.DataFrame()

#this goes through each of the <p> tags and breaks it into a list of the constituent parts. 
#it then converts each part to a string, stripping out HTML code and forms a list from these strings
#finally it appends the list to the pandas dataframe created above. 
#this is repeated for all of the tags, creating a very simple dataframe with all of the content from the page
#the next step is to add structure to the dataframe with columns for "author", "article_title", "journal_title", "book_title", "journal_vol" etc
#it will be a little complicated because the data for books, chapters and journal articles are all different

for tag in tagP:
    cont = tag.contents
    l = list()
    for line in cont:
        st = line.string
        l.append(st)
    data = data.append(l)

#this prints the data and confirms the script worked
print data

#this exports the data to a CSV file
data.to_csv('HGISBIB.csv', encoding='utf-8')
