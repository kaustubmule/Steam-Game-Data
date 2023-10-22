import pandas as pd
import random

games = pd.read_csv('games-features.csv')

# print(games.head())

# print(games.columns)

#print(games.info())

##Data cleaning
null_columns = games.columns[games.isnull().any()]
print(null_columns)

games.dropna(subset=[
    'QueryName', 'SupportEmail', 'SupportURL', 'LegalNotice', 'Website',
    'DetailedDescrip'
],
             inplace=True)

#print(games)
#null_columns = games.columns[games.isnull().any()]
#print(null_columns)
#print(num_nas)

##Data Reduction
#print('Before Data Reduction: \n', games)
'''
#Convert Generic/Categoric/Boolean to Numeric:
games['IsFree'] = games['IsFree'].astype(int)
for x in games.index:
  print(games['IsFree'][x])

#print('After Data Reduction: \n', games)
games.drop(games.columns[games.dtypes == 'bool'], axis=1, inplace=True)
print(games.columns)

#Deleting the duplicates
#games.sort_values('QueryName', inplace=True)
games.drop_duplicates(subset='QueryName', keep=False, inplace=True)
print(games)

#Printing the updated list
for x in games.index:
  print(games['QueryName'][x])

#transforming 0's in Req age
'''
cnt=0
mean=0

for i in games.index:
  a=random.choice([0,15,18,22,25])
  cnt+=1
  mean+=a  

mean=mean//cnt

games['RequiredAge'] = games['RequiredAge'].replace(0,mean)
#for x in games.index:
#  print(games['RequiredAge'][x])
'''
games['PCRecReqsText'].fillna('Ryzen 5', inplace=True)
for x in games.index:
  print(games['PCRecReqsText'][x])

#games.to_csv('output.csv', index=False)
'''