""" 
Number of Comments Per User in 30 days before 2020-02-10

Return the total number of comments received for each user in the 30-day period up to and including 2020-02-10.
Don't output users who haven't received any comment in the defined time period.

DataFrames:
fb_comments_count

Expected Output Type:
pandas.DataFrame

https://platform.stratascratch.com/coding/2004-number-of-comments-per-user-in-past-30-days?code_type=2
"""

# Import your libraries
import pandas as pd

"""
# GOAL

total number of comments per user 2020-02-10 - 30 days 

drop the 0 commetns useres

# OUTPUT 

user_id, created_at + the number of comments

# ANCHOR TABLE

fb_comments_count

# FILTER/DROP

filter the time 2020-02-10 - 30 days

users with 0 commments

# JOIN 

none

# OPEARATIONS

groupby user + sum the comments

# ASSUMPTIONS 

the format is YYYY-MM-DD

# EDGE CASES

dupes which counted as relevant
"""

fb_comments_count.head()

# define the timespan
end_date = pd.Timestamp("2020-02-10")
start_date = end_date - pd.Timedelta(days=30)

# filter by timespan

relevant = fb_comments_count.query("@start_date <= created_at <= @end_date")

# assuming an edge case that we have only one statistics per day we wanna drop the following dupes:

relevant = relevant.drop_duplicates(subset=["user_id", "created_at"])

# group by user and sum
n_comments = relevant.groupby("user_id")["number_of_comments"].sum().reset_index() # do not to forget to reset since you turned the df into series with user_id as an index. the output however required a df
n_comments
