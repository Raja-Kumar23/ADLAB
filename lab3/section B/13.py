# Q13. Drop duplicate rows
import pandas as pd
df = pd.DataFrame({"A": [1, 1, 2, 3]})
before = len(df)
df = df.drop_duplicates()
after = len(df)

print("Removed rows:", before - after)
print(df)

print("Name: Raja Kumar")
print("Roll: 23053769")
