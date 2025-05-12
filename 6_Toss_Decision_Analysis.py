import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('C:/Users/Neel/Desktop/DAP LAb/IPL_Matches_DataAnalysis_Report/IPL_Matches_2022.csv')

# Count toss decisions
toss_decisions = df['TossDecision'].value_counts()

print('Toss decision counts:')
print(toss_decisions)

# Pie chart
plt.figure(figsize=(6,6))
plt.pie(toss_decisions, labels=toss_decisions.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
plt.title('Toss Decisions: Bat vs Field')
plt.show()
