# 1. Load a CSV file and display only the rows where a given column has values above its column mean.

import pandas as pd
df = pd.read_csv('data.csv')
column_name = 'age'
mean_value = df[column_name].mean()
filtered_rows = df[df[column_name] > mean_value]
print("Rows where", column_name, "is above its mean (", mean_value, "):")
print(filtered_rows)
print("Name: Raja Kumar")
print("Roll: 23053769")
