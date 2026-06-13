General rule: place the task in the folder of whatever concept would have blocked you if you didn't know it.

- `filtering` — boolean indexing, query
- `sorting` — sort_values, nlargest
- `groupby_agg` — groupby, agg, transform
- `merge_join` — merge, suffixes, join keys
- `window_functions` — rolling, rank, shift
- `reshaping` — pivot, melt, stack/unstack
- `string_ops` — str.contains, str.extract, regex on text columns
- `datetime` — resample, date arithmetic, dt accessor
- `missing_data` — fillna, dropna, interpolate strategies


A blueprint for each pandas task:
```python
"""
# GOAL
What the task is asking for in plain language.

# OUTPUT
Expected columns and shape of the result.

# ANCHOR TABLE
The primary table the output is built from.

# FILTER/DROP
Rows or columns to exclude before any operations.

# JOIN
Tables to join, join keys, and join type (left/inner/etc).

# OPERATIONS
Transformations in order: groupby, agg, sort, window functions, etc.

# ASSUMPTIONS
Things assumed about the data (format, completeness, uniqueness).

# EDGE CASES
Known data quality risks: nulls, duplicates, mismatched keys, empty groups.
"""
```
