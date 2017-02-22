# https://pythonprogramming.net/more-stock-data-manipulation-python-programming-for-finance/?completed=/stock-data-manipulation-python-programming-for-finance/

import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



style.use('ggplot')


start = dt.date(2015,1,1)
end = dt.date(2017,2,22)
df = web.DataReader('MOMO','yahoo',start,end)

#print(df.head())

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_vol = df['Volume'].resample('10D').sum()

print(df_ohlc.head())
print(df_vol.head())

#print(type(df_ohlc.index))  #<class 'pandas.tseries.index.DatetimeIndex'>

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

#print(type(df_ohlc.index)) #<class 'pandas.indexes.range.RangeIndex'>

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)

ax1.xaxis_date()

candlestick_ohlc(ax1,df_ohlc.values,width=5, colorup='g', colordown='r')
ax2.fill_between(df_vol.index.map(mdates.date2num), df_vol.values,0)
plt.show() 
