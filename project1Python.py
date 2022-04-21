# %%
import pandas as pd

# %% [markdown]
# # 1.Load the csv file and show top 5 records from it.

# %%
players_df = pd.read_csv("players_20.csv")
print(players_df.head())

# %% [markdown]
# # 2.How you would be able to see each column's name.

# %%
for col in players_df.columns:
    print(col)

# %% [markdown]
# # 3.Need to show number of rows and columns of this dataset.

# %%
len(players_df)

# %%
len(players_df.columns)

# %%
players_df.shape

# %% [markdown]
# # 4.Show number of players and their countries.

# %%
by_nationality = players_df.groupby('nationality')['long_name'].count()

# %% [markdown]
# # 5.If you find many records in point 4 then show only top 10 countries and their number of players.

# %%
top_10_Nations = by_nationality.nlargest(10)

# %% [markdown]
# # 6.Now you have to create a bar plot of top 5 countries and their number of players, try to fill green color in bars.

# %%
top_5_Nations = by_nationality.nlargest(5)

# %%
barplot = top_5_Nations.plot.bar(x = 'Nationality', y = 'Players', color = 'green', fontsize = '9')

# %% [markdown]
# # 7.Show top 5 players short name and wages.
# 

# %%
df_top_5 = players_df[['short_name', 'wage_eur']].head(5)

# %% [markdown]
# # 8.Show top 5 players short name and wages that are getting highest salaries.

# %%
df_top_5_salary = players_df[['short_name', 'wage_eur']].nlargest(5, 'wage_eur')

# %% [markdown]
# # 9.Create a bar plot of point number 8.

# %%
New_Colors = ['green', 'red', 'blue', 'yellow', 'black']
barplot_wages = df_top_5_salary.plot.bar(x = 'short_name', y = 'wage_eur', color = New_Colors, fontsize = '9')

# %% [markdown]
# # 10.Show top 10 records of Germany.

# %%
german_players = players_df.loc[players_df['nationality'] == 'Germany'].head(10)

# %% [markdown]
# # 11.Now show top 5 records of Germany players who have maximum height, weight and wages.

# %%
top_5_german_height = german_players.nlargest(5, 'height_cm')
top_5_german_weight = german_players.nlargest(5, 'weight_kg')
top_5_german_wages = german_players.nlargest(5, 'wage_eur')

# %% [markdown]
# # 12.Show short name and wages of top 5 Germany players.

# %%
german_top_5_salary = german_players[['short_name', 'wage_eur']].nlargest(5, 'wage_eur')

# %% [markdown]
# # 13.Show top 5 players who have great shooting skills among all with short name.

# %%
df_shooting = players_df[['short_name', 'shooting']].nlargest(5, 'shooting')

# %% [markdown]
# # 14.Show top 5 players records (short name, defending, nationality, and club) that have awesome defending skills.

# %%
df_defense = players_df[['short_name', 'defending', 'nationality', 'club']].nlargest(5, 'defending')

# %% [markdown]
# # 15.Show wages records of top 5 players of 'Real Madrid' team.

# %%
df_real_madrid_wages = players_df.loc[players_df['club'] == 'Real Madrid'].nlargest(5, 'wage_eur')

# %% [markdown]
# # 16.Show shooting records of top 5 players of 'Real Madrid' team.

# %%
df_real_madrid_shooting = players_df.loc[players_df['club'] == 'Real Madrid'].nlargest(5, 'shooting')
print(df_real_madrid_shooting['short_name'])

# %% [markdown]
# # 17.Show defending records of top 5 players of 'Real Madrid' team.

# %%
df_real_madrid_defending = players_df.loc[players_df['club'] == 'Real Madrid'].nlargest(5, 'defending')
print(df_real_madrid_defending['short_name'])

# %% [markdown]
# # 18.Show nationality records of top 5 players of 'Real Madrid' team.

# %%
df_real_madrid = players_df.loc[players_df['club'] == 'Real Madrid']
print(df_real_madrid[['short_name', 'nationality']].head())


