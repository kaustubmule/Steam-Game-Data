import pandas as pd
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

games = pd.read_csv('games-features.csv')

# Data cleaning
null_columns = games.columns[games.isnull().any()]
print(null_columns)

# transforming 0's in Req age

cnt = 0
mean = 0

for i in games.index:
    a = random.choice([0, 15, 18, 22, 25])
    cnt += 1
    mean += a

mean = mean//cnt

games['RequiredAge'] = games['RequiredAge'].replace(0, mean)
# for x in games.index:
#  print(games['RequiredAge'][x])


# Convert Generic/Categoric/Boolean to Numeric:
games['IsFree'] = games['IsFree'].astype(int)
for x in games.index:
    print(games['IsFree'][x])


# Data Reduction:

# print('Before Data Reduction: \n', games)

games.dropna(subset=[
    'QueryName', 'SupportEmail', 'SupportURL', 'LegalNotice', 'Website',
    'DetailedDescrip'], inplace=True)

# print('After Data Reduction: \n', games)


games.drop(games.columns[games.dtypes == 'bool'], axis=1, inplace=True)
print(games.columns)


# Deleting the duplicates
# games.sort_values('QueryName', inplace=True)
games.drop_duplicates(subset='QueryName', keep=False, inplace=True)
print(games)


# Data Visualization

IQ_Range = games['RecommendationCount'].mean() * 80

# games.sort_values('RecommendationCount', inplace=True)
MostRecommended = []
cnt = []
for i in games.index:
    if (games['RecommendationCount'][i] >= IQ_Range):
        MostRecommended.append(games['QueryName'][i])
        cnt.append(games['RecommendationCount'][i])
games.loc[:, 'MostRecommended'] = pd.Series(MostRecommended)

x = np.array(MostRecommended)
y = np.array(cnt)

plt.figure(figsize=(22, 9))
plt.bar(x, y)

plt.show()


# Supported languages pie chart
language_counts = games['SupportedLanguages'].value_counts()

threshold = 100

filtered_languages = language_counts[language_counts >= threshold]

plt.figure(figsize=(8, 8))
explode = [0.1] * len(filtered_languages)

plt.pie(filtered_languages, labels=filtered_languages.index,
        autopct='%1.1f%%', startangle=140, explode=explode)

plt.axis('equal')
plt.title('Supported Languages Pie Chart'.format(threshold))

plt.tight_layout()
plt.show()


# Conversion to csv:
games.to_csv('output.csv', index=False)
