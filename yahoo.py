#importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

CAD = ['MSFT', 'AAPL', '%5EGSPC', 'NQ%3DF']
displayStocks = []

def real_time_value(stock_symbol):
    url = ('https://ca.finance.yahoo.com/quote/') + stock_symbol + ('?p=') + stock_symbol + ('&.tsrc=fin-srch')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    stock_content = BeautifulSoup(r.text, 'html.parser')
    stock_content = stock_content.find('div', {'class' : 'D(ib) Mend(20px)'})
    stock_content = stock_content.find('fin-streamer').text

    #incase there are values that aren't updated, use default MSFT
    if stock_content == []:
        stock_content = 'MSFT'

    return stock_content


#for loop from 1 - 100 
for step in range(1,101):
    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime('%Y-%m-%d %H: %M: %S')
    for stock_symbol in CAD:
        price.append(real_time_value(stock_symbol))
    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('stock data.csv', mode = 'a', header = False)
    print(col)


