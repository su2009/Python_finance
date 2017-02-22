import pandas as pd
import pandas_datareader.data as web
import numpy as np
import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt 

style.use('ggplot')

start = dt.date(2015,1,1)
end =dt.date(2017,2,22)
df = web.DataReader('MOMO','yahoo',start,end)

# print(df.head())

#df['Close'].plot()
#plt.show()

#print(df[['High','Low']])
#df[['High','Low']].plot()
#plt.show()


df['100ma'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
df['20ma'] = df['Adj Close'].rolling(window=20,min_periods=0).mean()
print(df.head())

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax1.plot(df.index, df['20ma'])
ax2.bar(df.index, df['Volume'])

plt.show()
