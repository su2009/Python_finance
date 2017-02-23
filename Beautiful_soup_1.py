#https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/

import bs4 as bs
import urllib.request 

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(source,'lxml')

#print(soup.title)

#print(soup.title.name)

#print(soup.title.string)

#print(soup.title.parent.name)

#print(soup.p)

#print(soup.find_all('p'))

#print(soup.find_all('title'))


#for paragraph in soup.find_all('p'):
#    print(paragraph.string)  # if there are child tags in the paragraph item 
                             #that we're attempting to use .string on, we will get None returned.
#    print(str(paragraph.text))  


for url in soup.find_all('a'):
    print(url.get('href'))
