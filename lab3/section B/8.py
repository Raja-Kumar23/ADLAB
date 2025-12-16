# 8. Group rows by a categorical variable and compute aggregate statistics.

import pandas as pd
df = pd.read_csv("data.csv")
grouped = df.groupby("city").agg({  
    "age": "mean",
    "score": "sum"
})
print("Grouped statistics by city:")
print(grouped)
print("Name: Raja Kumar")
print("Roll: 23053769")
        

