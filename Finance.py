import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import googlefinance.client as gf

# getting S&P 500 closing data for last 2 years
param=[{'q': ".INX",
        'x': "INDEXSP",}]
period="2Y"
df=gf.get_closing_data(param,period)
df.columns=['Close_Price']
print(df)


# Calculating Simple Moving averages 10days , 50 Days and 200 days
df['SMA_10']=df.Close_Price.rolling(10).mean()

df['SMA_50']=df.Close_Price.rolling(50).mean()

df['SMA_200']=df.Close_Price.rolling(200).mean()

print(df)

# Ploting Close price and SMA using matplotlib
plt.figure(figsize=(15,10))
plt.grid(True)
plt.title('Plot of Closing Prices and SMA for S&P 500 for last 2 years')
plt.plot(df['Close_Price'],label='S&P 500 Close Price')
plt.plot(df['SMA_10'],label='SMA 10 Days')
plt.plot(df['SMA_50'],label='SMA 50 Days')
plt.plot(df['SMA_200'],label='SMA 200 Days')
plt.legend(loc=2)
plt.show()

#Calculating Instantaneous rate of return (log Change)
df['Log_change']=np.log(df['Close_Price']/df['Close_Price'].shift())
plt.figure(figsize=(15,10))
plt.title('Log Change(Instantaneous rate of return')
plt.plot(df.Log_change)
plt.show()

#Computing Historical Volatility
df['Volatility']=df.Close_Price.rolling(21).std().shift()
plt.figure(figsize=(15,10))
plt.title('Volatility')
plt.plot(df.Volatility)
plt.show()
import pandas as pd
import numpy as np

def RSI(series, period):
    delta = series.diff().dropna()
    u = delta * 0
    d = u.copy()
    u[delta > 0] = delta[delta > 0]
    d[delta < 0] = -delta[delta < 0]
    u[u.index[period-1]] = np.mean( u[:period] ) #first value is sum of avg gains
    u = u.drop(u.index[:(period-1)])
    d[d.index[period-1]] = np.mean( d[:period] ) #first value is sum of avg losses
    d = d.drop(d.index[:(period-1)])
    rs = pd.stats.moments.ewma(u, com=period-1, adjust=False)/ pd.stats.moments.ewma(d, com=period-1, adjust=False)
    return 100 - 100 / (1 + rs)

df['RSI']=RSI(df['Close_Price'],14)
plt.figure(figsize=(15,10))
plt.grid(True)
plt.title('RSI')
plt.plot(df.RSI)
plt.legend(loc=2)
plt.show()
