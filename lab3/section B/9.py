# Q9. Sort a DataFrame on two columns
import pandas as pd
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [22, 21, 22],
    "Marks": [80, 90, 85]
})

sorted_df = df.sort_values(by=["Age", "Marks"], ascending=[True, False])
print(sorted_df)

print("Name: Raja Kumar")
print("Roll: 23053769")
