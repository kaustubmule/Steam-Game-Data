# %%
import pandas as pd

games = pd.read_csv('games-features.csv')

# print(games.head())

# print(games.columns)

# print(games.info())

print(games.isnull().sum())

num_nas = games.isna().sum().sum()
print(num_nas)

# print(games.describe())
