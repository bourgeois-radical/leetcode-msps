# pyrefly: ignore-errors
# ruff: noqa

# https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=2

# Import your libraries

# Start writing code
facebook_reactions.head()

"""
# Goal

Find all posts with a heart 

# Output

All columns from facebook_posts for the posts reacted with a heart

# Anchor

Facebook_posts table since it is the output

# Filter/Remove

Remove the unnecessary cols

# Join

Join facebook_reactions with facebook_posts

# Operations

1. Join by post id

2. filter by reaction == like

# Assumptions 

all posts have a reaction


# Edge Cases

Missing values after join (missaligned tables)
Nulls, dupes
"""
print(facebook_reactions["reaction"].unique())  # like and heart are not the same!!

output_col = list(facebook_posts.columns) + ["reaction"]
joined_df = facebook_posts.merge(
    right=facebook_reactions, on=["post_id"], how="left", suffixes=("", "_right")
)[output_col]

no_nulls_joined_df = joined_df.dropna(subset="reaction")
print("N reaction nulls: ", len(joined_df) - len(no_nulls_joined_df))

output = (
    no_nulls_joined_df[no_nulls_joined_df["reaction"] == "heart"]
    .drop(columns=["reaction"])
    .drop_duplicates(subset=["post_id"])
)
output
