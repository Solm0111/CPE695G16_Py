import pandas as pd
from prmethod import Reader

df = Reader.get_from_data('charts.csv')

df_with_trend = df.groupby(['artist', 'song'])['rank'].apply(list)
df_with_trend = df_with_trend.reset_index()
df_with_trend.rename(columns={'rank': 'trend'}, inplace=True)

df_with_trend.insert(3, 'total_weeks', 0)
df_with_trend.insert(4, '>20', 0)
df_with_trend.insert(5, '>50', 0)

temp = list()
above20 = 0
above50 = 0
for index, row in df_with_trend.iterrows():
    temp = row['trend']
    for i in temp:
        if i <= 50:
            above50 = above50 + 1
            above20 = above20 + 1
        elif i <= 20:
            above20 = above20 + 1
    df_with_trend.at[index, 'total_weeks'] = len(temp)
    df_with_trend.at[index, '>20'] = above20
    df_with_trend.at[index, '>50'] = above50
    above20 = 0
    above50 = 0

df_with_trend.to_csv("Data/songs_with_trends.csv")


