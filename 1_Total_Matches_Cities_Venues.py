# 1_total_matches_cities_venues.py

import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Users/Neel/Desktop/DAP LAb/IPL_Matches_DataAnalysis_Report/IPL_Matches_2022.csv')

# Total number of matches
total_matches = len(df)

# Unique cities and venues
unique_cities = df['City'].nunique()
unique_venues = df['Venue'].nunique()

print(f'Total matches played: {total_matches}')
print(f'Number of cities: {unique_cities}')
print(f'Number of venues: {unique_venues}')

# List of cities and venues
print("\nCities:")
print(df['City'].unique())

print("\nVenues:")
print(df['Venue'].unique())
