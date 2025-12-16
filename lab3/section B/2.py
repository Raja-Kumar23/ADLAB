# 2. Read a CSV and check for missing values column-wise.
import pandas as pd
df = pd.read_csv('data.csv')
missing_values = df.isnull().sum()
print("Missing values column-wise:")
print(missing_values)
print("Name: Raja Kumar")
    
