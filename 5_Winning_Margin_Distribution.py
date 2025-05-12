import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/Neel/Desktop/DAP LAb/IPL_Matches_DataAnalysis_Report/IPL_Matches_2022.csv')

# Plot distribution of margin using Matplotlib only
plt.figure(figsize=(10,6))
plt.hist(df['Margin'], bins=20, color='green', edgecolor='black')
plt.title('Distribution of Winning Margins')
plt.xlabel('Margin (Runs or Wickets)')
plt.ylabel('Number of Matches')
plt.show()

# Basic stats
print('Winning margin statistics:')
print(df['Margin'].describe())
