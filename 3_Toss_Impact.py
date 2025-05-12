# 3_toss_impact.py

import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Users/Neel/Desktop/DAP LAb/IPL_Matches_DataAnalysis_Report/IPL_Matches_2022.csv')

# Total matches
total_matches = len(df)

# Count how many times toss winner also won the match
toss_and_match_winner = df[df['TossWinner'] == df['WinningTeam']].shape[0]

toss_winner_pct = (toss_and_match_winner / total_matches) * 100

print(f"Toss winner also won the match in {toss_and_match_winner} out of {total_matches} matches ({toss_winner_pct:.2f}%)")
