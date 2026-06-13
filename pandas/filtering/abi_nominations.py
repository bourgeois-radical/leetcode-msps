# Import your libraries
import pandas as pd

# Start writing code
print(oscar_nominees.head())

print("nones:\n", oscar_nominees.isna().sum(), "\n")
print("summary:\n", oscar_nominees.info(), "\n")
print("duplicates:\n", oscar_nominees.duplicated().sum(), "\n")
print("describe:\n", oscar_nominees["year"].describe(), "\n") # just for fun

print(oscar_nominees[oscar_nominees["nominee"] == "Abigail Breslin"])
print(oscar_nominees["nominee"].unique())

abi_wins = oscar_nominees[oscar_nominees["nominee"] == "Abigail Breslin"]["winner"].sum() # you do not need the wins

you need the number of times Abi was nominated

abi_n = oscar_nominees[oscar_nominees["nominee"] == "Abigail Breslin"]["nominee"].count()

# or simpler

abi_n = len(oscar_nominees[oscar_nominees["nominee"] == "Abigail Breslin"])


