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
# Create temp column for difference between the last two periods for ESI
esi_diff = esi.iloc[1]-esi.iloc[0]
esi_diff = esi_diff.sort_values(ascending=False)
esi_diff = esi_diff.dropna()
esi_diff;

# Create temp column for difference between the last two periods for ESI industrial sector
esi_indu = df.iloc[-2:,[0,6,12,18,24,30,36,42,49,55,61,67,73,79,85,91,97,101,107,113,119,125,131,137,143,149,155,161,167]]
esi_indu.transpose();
esi_indu_diff = esi_indu.iloc[1]-esi_indu.iloc[0]
esi_indu_diff = esi_indu_diff.sort_values(ascending=False)
esi_indu_diff = esi_indu_diff.dropna()
esi_indu_diff;

# Create temp column for difference between the last two periods for ESI service sector
esi_serv = df.iloc[-2:,[1,7,13,19,25,31,37,43,50,56,62,68,74,80,86,92,102,108,114,120,126,132,138,144,150,156,162,168]]
esi_serv.transpose();
esi_serv_diff = esi_serv.iloc[1]-esi_serv.iloc[0]
esi_serv_diff = esi_serv_diff.sort_values(ascending=False)
esi_serv_diff = esi_serv_diff.dropna()
esi_serv_diff;

# Create temp column for difference between the last two periods for ESI construction sector
esi_cons = df.iloc[-2:,[2,8,14,20,26,32,38,44,51,57,63,69,75,81,87,93,103,109,115,121,127,133,139,145,151,157,163,169]]
esi_cons.transpose();
esi_cons_diff = esi_cons.iloc[1]-esi_cons.iloc[0]
esi_cons_diff = esi_cons_diff.sort_values(ascending=False)
esi_cons_diff = esi_cons_diff.dropna()
esi_cons_diff;

# Create temp column for difference between the last two periods for ESI retail sector
esi_reta = df.iloc[-2:,[3,9,15,21,27,33,39,45,52,58,64,70,76,82,88,94,104,110,116,122,128,134,140,146,152,158,164,170]]
esi_cons.transpose();
esi_reta_diff = esi_reta.iloc[1]-esi_reta.iloc[0]
esi_reta_diff = esi_reta_diff.sort_values(ascending=False)
esi_reta_diff = esi_reta_diff.dropna()
esi_reta_diff;

# Create temp column for difference between the last two periods for ESI building sector
esi_buil = df.iloc[-2:,[4,10,16,22,28,34,40,46,53,59,65,71,77,83,89,95,105,111,117,123,129,135,141,147,153,159,165,171]]
esi_buil.transpose();
esi_buil_diff = esi_buil.iloc[1]-esi_buil.iloc[0]
esi_buil_diff = esi_buil_diff.sort_values(ascending=False)
esi_buil_diff = esi_buil_diff.dropna()
esi_buil_diff;

# Create new df with movers for each sector based on temp diff created above
esi_diff = esi.iloc[1]-esi.iloc[0]
movers = pd.DataFrame(esi_diff)
movers.reset_index(inplace=True)
movers.rename(columns={0: 'ESI'}, inplace=True)
movers['country'] = ['Europe','Euro Area','Belgium','Bulgaria','Czech Republic','Denmark','Germany','Estonia',
                           'Greece','Spain','France','Croatia','Italy','Cyprus','Latvia','Lithuania','Luxembourg',
                           'Hungary','Malta','Netherlands','Austria','Poland','Portugal','Romania',
                           'Slovenia','Slovak Republic','Finland','Sweden','United Kingdom']
movers.set_index('country', inplace=True)
movers.drop('index', axis=1, inplace=True)

esi_indu_diff = esi_indu.iloc[1]-esi_indu.iloc[0]
test = pd.DataFrame(esi_indu_diff)
test.reset_index(inplace=True)
test.rename(columns={0: 'INDU'}, inplace=True)
test['country'] = ['Europe','Euro Area','Belgium','Bulgaria','Czech Republic','Denmark','Germany','Estonia',
                           'Greece','Spain','France','Croatia','Italy','Cyprus','Latvia','Lithuania','Luxembourg',
                           'Hungary','Malta','Netherlands','Austria','Poland','Portugal','Romania',
                           'Slovenia','Slovak Republic','Finland','Sweden','United Kingdom']
test.set_index('country', inplace=True)
movers['INDU'] = test['INDU']

esi_serv_diff = esi_serv.iloc[1]-esi_serv.iloc[0]
test = pd.DataFrame(esi_serv_diff)
test.reset_index(inplace=True)
test.rename(columns={0: 'SERV'}, inplace=True)
test['country'] = ['Europe','Euro Area','Belgium','Bulgaria','Czech Republic','Denmark','Germany','Estonia',
                           'Greece','Spain','France','Croatia','Italy','Cyprus','Latvia','Lithuania',
                           'Hungary','Malta','Netherlands','Austria','Poland','Portugal','Romania',
                           'Slovenia','Slovak Republic','Finland','Sweden','United Kingdom']
test.set_index('country', inplace=True)
movers['SERV'] = test['SERV']

esi_cons_diff = esi_cons.iloc[1]-esi_cons.iloc[0]
test = pd.DataFrame(esi_cons_diff)
test.reset_index(inplace=True)
test.rename(columns={0: 'CONS'}, inplace=True)
test['country'] = ['Europe','Euro Area','Belgium','Bulgaria','Czech Republic','Denmark','Germany','Estonia',
                           'Greece','Spain','France','Croatia','Italy','Cyprus','Latvia','Lithuania',
                           'Hungary','Malta','Netherlands','Austria','Poland','Portugal','Romania',
                           'Slovenia','Slovak Republic','Finland','Sweden','United Kingdom']
test.set_index('country', inplace=True)
movers['CONS'] = test['CONS']

esi_reta_diff = esi_reta.iloc[1]-esi_reta.iloc[0]
test = pd.DataFrame(esi_reta_diff)
test.reset_index(inplace=True)
test.rename(columns={0: 'RETA'}, inplace=True)
test['country'] = ['Europe','Euro Area','Belgium','Bulgaria','Czech Republic','Denmark','Germany','Estonia',
                           'Greece','Spain','France','Croatia','Italy','Cyprus','Latvia','Lithuania',
                           'Hungary','Malta','Netherlands','Austria','Poland','Portugal','Romania',
                           'Slovenia','Slovak Republic','Finland','Sweden','United Kingdom']
test.set_index('country', inplace=True)
movers['RETA'] = test['RETA']

esi_buil_diff = esi_buil.iloc[1]-esi_buil.iloc[0]
test = pd.DataFrame(esi_buil_diff)
test.reset_index(inplace=True)
test.rename(columns={0: 'BUIL'}, inplace=True)
test['country'] = ['Europe','Euro Area','Belgium','Bulgaria','Czech Republic','Denmark','Germany','Estonia',
                           'Greece','Spain','France','Croatia','Italy','Cyprus','Latvia','Lithuania',
                           'Hungary','Malta','Netherlands','Austria','Poland','Portugal','Romania',
                           'Slovenia','Slovak Republic','Finland','Sweden','United Kingdom']
test.set_index('country', inplace=True)
movers['BUIL'] = test['BUIL']

# movers df final adjustments
movers.drop('Luxembourg',inplace=True)
movers.sort_values(by='ESI',ascending=False,inplace=True)
movers;
