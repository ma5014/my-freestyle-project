# Problem Statement

# Primary User:

Any user who wants to download historical 2 years close price data of S&P 500, to plot Simple Moving Averages , Instantaneous Rate of Return (Log Change) , Volatility and Relative Strength Index(RSI). (The relative strength index is a momentum indicator developed by technical analyst Welles Wilder, that compare the magnitude of recent gains and losses over a specified time period to measure speed and change or price movements of a security. It is primarily used to identify overbought or oversold conditions in the trading of an asset). 


# User Needs Statement:

To download close price and historical data and to calculate simple averages i.e 10 days, 50 days and 200 days. To help user with the instantaneous rate of return todays price/previous day price will be shown in the form of graphs and charts. The historical volatility will show the volatility of 21 days period. 


# Technology requirements:

Description:

Calculate 3 simple averages i.e 10 days,50 days, and 200 days. Function of pandas will be used to calculate these. 
Instantaneous rate of return will log the todays price and previous price for previous price shift () function is used.
To Calculate the volatility of 21 days period std function of pandas is used.
Technology Requirements
Python Package Requirements
I used googlefinance_client package to download the S&P 500 close price data 
get_closing_data() was used to retrieve the data 

# Packages 
 Following packages were used in the project 
Numpy
Pandas
Matplotlib
Googlefinance_client

# Hardware Requirements
The application will be running on my local machine. I have no plans to deploy it to a public server.
