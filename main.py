# %%
import pandas as pd
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
games = pd.read_csv('games-features.csv')

# Data cleaning

# transforming 0's in Req age
print("Before transforming 0's in Req age:\n")
print(games['RequiredAge'])
cnt = 0
mean = 0

for i in games.index:
    a = random.choice([0, 15, 18, 22, 25])
    cnt += 1
    mean += a

mean = mean//cnt

games['RequiredAge'] = games['RequiredAge'].replace(0, mean)
print("After transforming 0's in Req age\n")
print(games['RequiredAge'])


# Convert Generic/Categoric/Boolean to Numeric:
print("Before converting Boolean to Numeric:\n")
print(games['IsFree'])

games['IsFree'] = games['IsFree'].astype(int)

print("After converting Boolean to Numeric:\n")
print(games['IsFree'])
# for x in games.index:
# print(games['IsFree'][x])


# Data Reduction:
null_columns = games.columns[games.isnull().any()]
print(null_columns)
print('Before Data Reduction: \n', games)

games.dropna(subset=[
    'QueryName', 'SupportEmail', 'SupportURL', 'LegalNotice', 'Website',
    'DetailedDescrip'], inplace=True)

print('After Data Reduction: \n', games)

# feature selection - removing irrelevant information from the dataset.
print("before:", games.columns)
games.drop(games.columns[games.dtypes == 'bool'], axis=1, inplace=True)
print("after", games.columns)


# Deleting the duplicates
print('Before dropping duplicates: \n', games)
games.drop_duplicates(subset='QueryName', keep=False, inplace=True)
print('After dropping duplicates: \n', games)


# Data Visualization

IQ_Range = games['RecommendationCount'].mean() * 80

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

plt.xlabel('Game Name')
plt.ylabel('Recommendation Count')


def format_func(value, tick_number):
    return f'{int(value):,}'  # Format as whole numbers


plt.xticks(rotation=90)
plt.gca().get_yaxis().set_major_formatter(FuncFormatter(format_func))
plt.title('Most Recommended Games by Recommendation Count')
plt.tight_layout()
plt.show()


# Supported languages pie chart

language_counts = games['SupportedLanguages'].value_counts()

threshold = 100

filtered_languages = language_counts[language_counts >= threshold]
other_count = language_counts[language_counts < threshold].sum()
filtered_languages['Other'] = other_count

colors = plt.cm.Paired(range(len(filtered_languages)))

plt.figure(figsize=(10, 10))
explode = [0.1] * len(filtered_languages)

plt.pie(filtered_languages, labels=filtered_languages.index,
        autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)

plt.legend(filtered_languages.index, title="Languages",
           loc="upper right", bbox_to_anchor=(1.2, 1))

plt.axis('equal')
plt.title('Supported Languages'.format(threshold))

plt.tight_layout()
plt.show()


'''
# Conversion to csv:
games.to_csv('output.csv', index=False)
'''
