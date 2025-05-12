# 4_player_of_the_match_distribution.py

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/Neel/Desktop/DAP LAb/IPL_Matches_DataAnalysis_Report/IPL_Matches_2022.csv')

# Count of Player of the Match awards
top_players = df['Player_of_Match'].value_counts().head(5)

print('Top 5 Player of the Match award winners:')
print(top_players)

# Bar plot
top_players.plot(kind='bar', figsize=(8,6), color='orange')
plt.title('Top 5 Player of the Match Winners')
plt.ylabel('Number of Awards')
plt.xlabel('Players')
plt.show()
