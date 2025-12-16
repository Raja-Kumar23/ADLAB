# 10. Replace missing values in a file with the mean value.

import pandas as pd
filename = "data_with_missing.csv"
df = pd.read_csv(filename)
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)
print(df.head())
print("Name: Raja Kumar")
print("Roll: 23053769")
