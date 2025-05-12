import pandas as pd

# Load dataset
df = pd.read_csv('C:/Users/Neel/Desktop/DAP LAb/IPL_Matches_DataAnalysis_Report/IPL_Matches_2022.csv')

# Count appearances of each team in Team1 and Team2 columns
team1_counts = df['Team1'].value_counts()
team2_counts = df['Team2'].value_counts()

# Combine counts
total_matches_played = team1_counts.add(team2_counts, fill_value=0).sort_values(ascending=False)

print('Matches played by each team:')
print(total_matches_played)
