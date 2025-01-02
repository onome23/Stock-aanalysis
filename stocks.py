# import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the csv file
df = pd.read_csv('stocks.csv')

#     1
# carry out exploratory analysis 
# of the dataframe.

#print(df.head()) #summary of the dataframe

# Check the features
#print(df.columns)

# Check the basic statistical properties
#print(df.describe())

# Check  for the general information of the dataframe
#print(df.info())

# check the size of the dataset

# check for null values
#print(df.isna().sum())

# check for duplicate values
#print(df.duplicated().sum())

#       2
# clean the data

# convert the 'Date' feauture from 
# object to datetime
#df['Date'] = pd.to_datetime(df['Date'])
#print(df['Date'].dtypes)

#       3
#. Carry Out Technical Analysis on 
# The Data

# compare the prices of the different
# stocks over time

#plt.figure(figsize=(12, 6))

#plt.plot(df['MSFT'], color='blue', label='MSFT') #MSFT
#plt.plot(df['KLM'], color='red', label='KLM') #KLM
#plt.plot(df['MOS'], color='yellow', label='MOS') #MOS
#plt.plot(df['ING'], color='black', label='ING')  #ING

#plt.title('Relationship between MSFT, KLM, MOS, and ING prices')
#plt.xlabel('year')
#plt. ylabel('price')
#plt.legend(title='')
#plt.show()

# Calculate and plot the simple moving average for each column
#window_size = 20
#df.set_index('Date', inplace=True)

# iterate over each column/feature
#for column in df.columns:
    # create a new column for the 
    # moving average
    #df[f'{column}_MA'] = df[column].rolling(window=window_size).mean()

# plot original data & moving averages
#plt.figure(figsize=(10, 6)) 

#(a) plot the original data
#df[['MSFT', 'KLM', 'ING', 'MOS']].plot(marker='o', linestyle='-', alpha=0.7, label='Original data')

#(b) plot the simple moving average
#df[['MSFT', 'KLM', 'ING', 'MOS']].plot(linestyle='--', alpha=0.7, label=f'Moving average(window={window_size})')

#plt.title('Original data & Simple moving average for the 4 stocks')
#plt.xlabel('Date')
#plt.ylabel('Value')
#plt.legend()
#plt.show()

# Calculate the daily return of the various stock's on average

#plt.figure(figsize=(12, 9))
#daily_returns = df[['MSFT', 'KLM', 'ING', 'MOS']].pct_change(axis=1)
#sns.pairplot(daily_returns)
#plt.title('The dsily return various stocks')
#plt.show()

# calculate the correlation between different stocks daily returns
#plt.figure(figsize=(12, 9))
#corr = daily_returns.corr(numeric_only=True)
#sns.heatmap(data=corr, linewidth=0.5)
#plt.show()
