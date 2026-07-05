"""
https://platform.stratascratch.com/coding/9992-find-artists-that-have-been-on-spotify-the-most-number-of-times?code_type=2

Artist Appearance Count


Last Updated: June 2026

Easy


Find how many times each artist appeared on the Spotify ranking list.
Output the artist name along with the corresponding number of occurrences.
Order records by the number of occurrences in descending order.
"""

# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.head()

'''
Goal

N times each artist on the ranking list 

Output 

Artist name + number of occurances in desc

Anchor -

Filter/Sort

in desc by occurances

Merge -

Operations

groupby, sum, sort

Assumptions -

Edge Cases

dupes
nones 
'''

print("dupes: \n", spotify_worldwide_daily_song_ranking.duplicated().sum())  # noqa: F821

print("isna: \n", spotify_worldwide_daily_song_ranking.isna().sum())  # noqa: F821

# 1st way
result = spotify_worldwide_daily_song_ranking["artist"].value_counts().reset_index()  # noqa: F821

result = result.rename(columns={"index": "artist", "count": "occurences"}).sort_values(by="occurences", ascending=False)

# result

# 2nd way
result = (
    spotify_worldwide_daily_song_ranking.groupby("artist")  # noqa: F821
    .size()
    .reset_index(name="occurances")
    .sort_values(by="occurances", ascending=False)
    )
    
result