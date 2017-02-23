"""
Spyder Editor

https://pythonprogramming.net/sp500-company-list-python-programming-for-finance/?completed=/more-stock-data-manipulation-python-programming-for-finance/
"""

import bs4 as bs
import requests
import pickle 

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class':'wikitable sortable'})
    # 'class'='wikitable sortable'  SyntaxError: keyword can't be an expression  why?
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    
    with open('sp500ticker.pickle','wb') as f:
        pickle.dump(tickers,f)
    
    return tickers

list = save_sp500_tickers()
print(list[0:5])
