import pandas as pd

# Load dataset
df = pd.read_csv('C:/Users/Neel/Desktop/DAP LAb/IPL_Matches_DataAnalysis_Report/IPL_Matches_2022.csv')

# Find the final match (last match chronologically)
final_match = df.iloc[-1]

print('Final Match Summary:')
print(f'Date: {final_match["Date"]}')
print(f'City: {final_match["City"]}')
print(f'Venue: {final_match["Venue"]}')
print(f'{final_match["Team1"]} vs {final_match["Team2"]}')
print(f'Toss Winner: {final_match["TossWinner"]} (Decided to {final_match["TossDecision"]})')
print(f'Match Winner: {final_match["WinningTeam"]}')
print(f'Player of the Match: {final_match["Player_of_Match"]}')
