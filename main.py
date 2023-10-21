import pandas as pd

games_df = pd.read_csv("games-features.csv")

na_nulls = games_df.isna().sum().sum()
print('There are', na_nulls, 'missing values in the Na column')
