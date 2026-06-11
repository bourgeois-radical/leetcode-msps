# Import your libraries

# https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=2

# Start writing code
ms_employee_salary.head()  # pyrefly: ignore # noqa: F821

# GOAL

# We need a relevant employs' salary
# No timestamps
# Take the largest

# OUTPUT

# Sorted by ID in ascnd order
# Schema: id, first name, last name, department id, current salary

# ANCHOR TABLE

# ms_employee_salary

# REMOVE / FILTER

# JOIN/ADD - None

# OPERATIONS

# 1. Groupby id, sort by salary

# ASSUMED -
# there might be duplicates and that the salary is non-decreasing

# EDGE CASES

# dupes
# Nones in salries - return nones

ms_employee_salary.sort_values(  # pyrefly: ignore # noqa: F821
    "salary", ascending=False
).drop_duplicates(subset="id").sort_values("id")

"""
1. First we sorted by salaries to keep the top salaries in the head of the df

2. Then we dropped all the dupes by id -> we kept only the highest salary for each employee

3. Then we sorted by id in asc oreder as required by the task
"""
