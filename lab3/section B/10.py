# Q10. Merge DataFrames using all joins
import pandas as pd
df1 = pd.DataFrame({"ID": [1, 2], "Name": ["A", "B"]})
df2 = pd.DataFrame({"ID": [2, 3], "Marks": [85, 90]})
print(pd.merge(df1, df2, how="inner"))
print(pd.merge(df1, df2, how="outer"))
print(pd.merge(df1, df2, how="left"))
print(pd.merge(df1, df2, how="right"))
print("Name: Raja Kumar")
print("Roll: 23053769")
