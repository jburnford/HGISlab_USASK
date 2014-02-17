__author__ = 'jimclifford'

from bs4 import BeautifulSoup
import urllib2, csv
import pandas as pd

soup = BeautifulSoup(urllib2.urlopen("http://www.hgis.usask.ca/bibliography/").read())

tagP = soup.find_all("p")[5:]


data = pd.DataFrame()

for tag in tagP:
    cont = tag.contents
    l = list()
    for line in cont:
        st = line.string
        l.append(st)
    #print l
    data = data.append(l)


print data

data.to_csv('HGISBIB.csv', encoding='utf-8')