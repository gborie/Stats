# Commands to use in Jupyter Notebook

# Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LinReg
%matplotlib inline

# read excel file
df = pd.read_excel('esi_nace2.xlsx',sheet_name='ESI MONTHLY')

# Data wrangling
# reset index to only keep dates
index = df.index.levels[0].unique()
df.reset_index(inplace=True)
df['Dates'] = pd.to_datetime(index)
df.set_index('Dates',inplace=True)
# clean df by dropping empty columns
df.drop('level_0', axis=1, inplace=True)
df = df.dropna(axis=1,how='all')


# Check last two periods for all stats - Can be ignored
esi_last = df.sort_index(ascending=False)
esi_last = esi_last.iloc[0:2]
esi_last

# Check ESI stats for last two periods of each country
esi = df.iloc[-2:,[5,11,17,23,29,35,41,48,54,60,66,72,78,84,90,96,100,106,112,118,124,130,136,142,148,154,160,166,172]]
esi.transpose()
