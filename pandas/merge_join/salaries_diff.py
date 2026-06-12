# https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
db_employee.head()

db_employee.info()
db_employee.isna().sum()

joined = db_employee.merge(right=db_dept, left_on="department_id", right_on="id", how="inner")

market = joined[joined["department"] == "marketing"]
engineer = joined[joined["department"] == "engineering"]

# verbose solution
diff = abs(float(market.sort_values(by="salary", ascending=False).iloc[0]["salary"]) - float(engineer.sort_values(by="salary", ascending=False).iloc[0]["salary"]))

print(joined["department"].unique())
print(diff)

# cleaner solution
diff = abs(market["salary"].max() - engineer["salary"].max())
print("clean solution", diff)

# production solution (asked claude)
def calculate_salary_difference(
    employees: pd.DataFrame,
    departments: pd.DataFrame,
    dept_a: str,
    dept_b: str,
) -> pd.DataFrame:
    """
    Calculate the absolute salary difference between the highest-paid
    employees in two departments.
    """
    joined = employees.merge(
        right=departments,
        left_on="department_id",
        right_on="id",
        suffixes=("_emp", "_dept"),
    )

    max_salary_by_dept = joined.groupby("department")["salary"].max()

    return pd.DataFrame({
        "salary_difference": [abs(max_salary_by_dept[dept_a] - max_salary_by_dept[dept_b])]
    })


# --- Run ---
result = calculate_salary_difference(
    employees=db_employee,
    departments=db_dept,
    dept_a="Marketing",
    dept_b="Engineering",
)

