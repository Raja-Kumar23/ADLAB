# 8. Group rows by a categorical variable and compute aggregate statistics.
import pandas as pd
data = {
    "Category": ["A", "B", "A", "B", "A"],
    "Values": [10, 20, 15, 25, 10]
}
df = pd.DataFrame(data)
grouped = df.groupby("Category").agg({"Values": ["mean", "sum", "max"]})
print(grouped)
print("Name: Raja Kumar")
print("Roll: 23053769")

        

