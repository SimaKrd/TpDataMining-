# -*- coding: utf-8 -*-
"""DataExploration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lyVWmMY-nGFmSl5wUvUOGdSXfpVwxAdV

#Loading The Data
"""

import pandas as pd
data = pd.read_csv('/content/cars_synthetic.csv')

data.head(225)

"""#Data Cleaning"""

data.info()

data['weight'] = pd.to_numeric(data['weight'], errors='coerce')

data.head(225)

data.isnull().sum()

data.dropna(subset = ['color'], inplace=True)

data.isnull().sum()

"""#Data Exploration"""

'''import matplotlib.pyplot as plt
plt.plot(data['width'], )
plt.show()'''

data['length'].plot.hist()

data = data[(data['length']<8) & (data['length']>0)]

data['length'].plot.hist(bins=4)

data['length'].plot.kde()

pip install Plotly

pd.options.plotting.backend = "plotly"

data['length'].plot.hist(bins=4)

import plotly.express as px

data.info()

meanWeight = data['weight'].mean()
data['weight'].fillna(value=meanWeight, inplace=True)

fig = px.scatter(data, x='year', y='price', color='color',size='weight', symbol='type', title='plot exploration')

fig.show()

"""# Distributions

"""

# this plot represent the distribution of the length
import matplotlib.pyplot as plt
plt.hist(data['length'], bins=6,edgecolor='k')
plt.xlabel('value')
plt.ylabel('Frequency')
plt.title('Distribution Plot')
plt.grid(True)

# Distribution plot by each type of car
carType = data['type'].unique()
for Type in carType :
  filtred_data = data[data['type']==Type]
  plt.hist(filtred_data['length'], bins=8,edgecolor='k')
  plt.xlabel('values of '+Type+ ' cars')
  plt.ylabel('Frequency')
  plt.title('Distribution of length based on car\'s type')
  plt.grid(True)
  plt.show()

"""SUV(sports utility cars) have muche higher length than standard cars

## Test of Shapiro-Wilk
"""

from scipy import stats
res = stats.shapiro(data['length'])
res.statistic

res.pvalue

alpha = 0.01
if( res.pvalue < alpha) :
  print(res.pvalue)
  print('Data doesnt follow a normal distribution')
else :
  print(res.pvalue)
  print('follows a Normal Distribution')

"""#Dispersion, Correlation"""

#creating a new dataframe with numerical variables only

data_numerical = data[['length','year','width','weight','price']]

data_numerical.head(5)

data_numerical.isnull().sum()

"""## Variance and standard deviation"""

# variance of  Variables
print('variance of length  ' + str(data_numerical['length'].var()))
print('variance of year   ' + str(data_numerical['year'].var()))
print('variance of width  ' + str(data_numerical['width'].var()))
print('variance of weight  ' + str(data_numerical['weight'].var()))
print('variance of price  ' +str(data_numerical['price'].var()))

# Standard deviation
print('Standard deviation of length: ' + str(data_numerical['length'].std()))
print('Standard deviation of year: ' + str(data_numerical['year'].std()))
print('Standard deviation of width: ' + str(data_numerical['width'].std()))
print('Standard deviation of weight: ' + str(data_numerical['weight'].std()))
print('Standard deviation of the price: ' + str(data_numerical['price'].std()))

# Covariance Matrix

data_numerical.cov()

#correlation coefficents
data_numerical.corr()

pd.plotting.scatter_matrix(data_numerical, figsize=(12,12))

data_numerical.corr(method="spearman")

data_numerical.corr()