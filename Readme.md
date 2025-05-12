# IPL 2022 Data Analysis Report

This repository contains Python scripts that analyze the IPL 2022 matches dataset (`IPL_Matches_2022.csv`). The goal is to extract insights, visualize patterns, and provide statistical summaries of key aspects of the tournament.

## Dataset

* **File**: `IPL_Matches_2022.csv`
* **Source**: IPL 2022 season matches data
* **Contents**: Match-level information such as teams, venue, winner, toss, margin, and Player of the Match

## Repository Structure

```
IPL_2022_Data_Analysis/
│
├── IPL_Matches_2022.csv
│
├── 1_total_matches_cities_venues.py
├── 2_most_successful_teams.py
├── 3_toss_impact.py
├── 4_player_of_the_match_distribution.py
├── 5_winning_margin_distribution.py
├── 6_toss_decision_analysis.py
├── 7_most_frequent_matchups.py
├── 8_most_matches_played.py
├── 9_venue_wise_match_count.py
├── 10_final_match_summary.py
│
└── README.md
```

## Analyses Overview

1. **Total Matches, Cities, Venues**
   Script: `1_total_matches_cities_venues.py`
   Summarizes total matches played, unique cities, and venues used.

2. **Most Successful Teams (Wins)**
   Script: `2_most_successful_teams.py`
   Lists teams ranked by number of matches won.

3. **Toss Impact**
   Script: `3_toss_impact.py`
   Analyzes how often toss winners also won the match.

4. **Player of the Match Distribution**
   Script: `4_player_of_the_match_distribution.py`
   Shows top players with most Player of the Match awards.

5. **Winning Margin Distribution**
   Script: `5_winning_margin_distribution.py`
   Visualizes distribution of victory margins (tight vs dominant wins).

6. **Toss Decision Analysis**
   Script: `6_toss_decision_analysis.py`
   Shows whether teams chose to bat or field after winning toss.

7. **Most Frequent Matchups**
   Script: `7_most_frequent_matchups.py`
   Highlights teams that played each other most frequently.

8. **Most Matches Played by a Team**
   Script: `8_most_matches_played.py`
   Ranks teams by total matches played (including playoffs).

9. **Venue-wise Match Count**
   Script: `9_venue_wise_match_count.py`
   Displays number of matches hosted by each venue.

10. **Final Match Summary**
    Script: `10_final_match_summary.py`
    Provides details of the final match of IPL 2022.

## Requirements

Install necessary libraries using pip:

```
pip install pandas matplotlib seaborn
```

## How to Run

Run each script individually:

```
python 1_total_matches_cities_venues.py
```

Ensure `IPL_Matches_2022.csv` is present in the same folder as the scripts or adjust the file path accordingly `(e.g., C:/Users/Neel/Desktop/DAP LAb/IPL_Matches_DataAnalysis_Report/IPL_Matches_2022.csv)`.

## Author

*Snehashis Roy*
CSE Student — Data Analysis Project Report

## License

This project is for academic and educational purposes only.
