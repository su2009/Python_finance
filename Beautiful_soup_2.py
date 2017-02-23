https://pythonprogramming.net/navigating-pages-scraping-parsing-beautiful-soup-tutorial/?completed=/introduction-scraping-parsing-beautiful-soup-tutorial/

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

#nav = soup.nav
#print(nav)

for url in nav.find_all('a'):
    print(url.get('href'))
    

for div in soup.find_all('div', class_='body'):
    print(div.text)
