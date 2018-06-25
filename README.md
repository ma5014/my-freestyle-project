The aim of this project is to Download historical 2 years close price data of S&P 500 ,to plot Simple Moving Averages , Instantaneous Rate of Return (Log Change) , Volatility and RSI .
I used googlefinance_clientpackage to download the S&P 500 close price data 
get_closing_data() was used to retrieve the data 

Following packages were used in the project 
Numpy
Pandas
Matplotlib
Googlefinance_client

Simple moving average

I have calculated 3 simple averages , i.e10 days , 50 days and 200 days 
Rolling mean function of pandas was used to calculate.

Instantaneous rate of return

Instantaneous rate of return (Log Change) is the log of (todays price/ previous day price) 
For previous day price I used shift() function.

Historical Volatility

As general trend I have calculated volatility of 21 days period. 
I used rolling std function of pandas 

RSI

The Relative Strength Index (RSI), developed by J. Welles Wilder, is a momentum oscillator that measures the speed and change of price movements. The RSI oscillates between zero and 100. Traditionally the RSI is considered overbought when above 70 and oversold when below 30.

References 
https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/RSI
https://www.investopedia.com/terms/v/volatility.asp
https://quantivity.wordpress.com/2011/02/21/why-log-returns/
https://pypi.org/project/googlefinance.client/
