# 2_most_successful_teams.py

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/Neel/Desktop/DAP LAb/IPL_Matches_DataAnalysis_Report/IPL_Matches_2022.csv')

# Count of matches won by each team
team_wins = df['WinningTeam'].value_counts()

print('Most successful teams (by number of wins):')
print(team_wins)

# Bar plot
team_wins.plot(kind='barh', figsize=(10,6), color='skyblue')
plt.title('Most Successful Teams (Number of Wins)')
plt.xlabel('Number of Wins')
plt.ylabel('Teams')
plt.gca().invert_yaxis()
plt.show()
