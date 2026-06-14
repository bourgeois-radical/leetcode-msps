""" 
Users By Average Session Time

Medium

Calculate each user's average session time, where a session is defined as the time difference between a page_load and a page_exit. Assume each user has only one session per day. If there are multiple page_load or page_exit events on the same day, use only the latest page_load and the earliest page_exit.
Only consider sessions where the page_load occurs before the page_exit on the same day. Output the user_id and their average session time.

https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=2

"""

# Import your libraries
import pandas as pd

# Start writing code
facebook_web_log.head()

"""
GOAL

get avrg session time per user

OUTPUT

user_id, avg_session

ANCHOR

facebook_web_log

JOIN

none 

FILTER/DROP

for each day and each user: take the LATEST page_load and EARLIEST page_exit 

filter for sessions where page_load occurs before the page_exit ON THE SAME DAY
OPERATIONS

1. new col: sesseion = page_load - page_exit 

ASSUMPTIONS 

each user has only one session a day

EDGE CASES

dupes
nons

multiple page_loads and exits:

take the LATEST page_load and earliest page_exit 

"""

# check for nons

print(facebook_web_log.isna().sum())

# dupes

print(facebook_web_log.duplicated().sum())

# for each day and each user take the earliest page_load and page_exit

# add date column
facebook_web_log["date"] = facebook_web_log["timestamp"].dt.date
print(facebook_web_log.head())

# groupby user_id and date and take the max timestamp to get the latest load
loads = (
    facebook_web_log[facebook_web_log["action"] == "page_load"]
    .groupby(["user_id", "date"])["timestamp"]
    .max()
    .rename("page_load_time")
    .reset_index()
    )

# groupby user id and dat and take the min timestapm to get the earliest exit 
exits = (
    facebook_web_log[facebook_web_log["action"] == "page_exit"]
    .groupby(["user_id", "date"])["timestamp"]
    .min()
    .rename("page_exit_time")
    .reset_index()
    )

# merge page loads and page exits to get one df

merged = loads.merge(right=exits, on=["user_id", "date"], how="inner")

# filter ou the sessions where page_load < page_exit

filtered = merged.query("page_load_time < page_exit_time")

# calculate session time

filtered["session"] = filtered["page_exit_time"] - filtered["page_load_time"]

print("negative sessions: \n", len(filtered[filtered["session"] < pd.Timedelta(0)]))

filtered = filtered[filtered["session"] >= pd.Timedelta(0)]

# calculate avg session pro user

avg = filtered.groupby("user_id")["session"].mean().rename("mean_session").reset_index()