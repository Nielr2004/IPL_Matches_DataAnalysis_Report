import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('C:/Users/Neel/Desktop/DAP LAb/IPL_Matches_DataAnalysis_Report/IPL_Matches_2022.csv')

# Count matches by venue
venue_counts = df['Venue'].value_counts()

print('Matches played at each venue:')
print(venue_counts)

# Bar plot
venue_counts.plot(kind='barh', figsize=(10,6), color='purple')
plt.title('Matches per Venue')
plt.xlabel('Number of Matches')
plt.ylabel('Venue')
plt.gca().invert_yaxis()
plt.show()
