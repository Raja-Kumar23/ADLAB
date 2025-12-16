# 8. Load a CSV using pandas and print first 5 rows.

import pandas as pd
filename = "data.csv"
df = pd.read_csv(filename)
print(df.head())
print("Name: Raja Kumar")
print("Roll: 23053769")
