# 5. Filter rows using multiple conditions (AND / OR operations).

import pandas as pd
df = pd.read_csv("data.csv")
cond_and = (df["age"] > 20) & (df["score"] >= 50)
cond_or = (df["city"] == "Delhi") | (df["city"] == "Mumbai")
filtered_and = df[cond_and]
filtered_or = df[cond_or]
print("Filtered (AND):")
print(filtered_and.head())
print("Filtered (OR):")
print(filtered_or.head())
print("Name: Raja Kumar")
print("Roll: 23053769")
