# Q11. Create a pivot table
import pandas as pd
df = pd.DataFrame({
    "Department": ["CS", "CS", "IT"],
    "Semester": [1, 2, 1],
    "Marks": [80, 90, 85]
})

pivot = pd.pivot_table(df, values="Marks", index="Department", columns="Semester")
print(pivot)

print("Name: Raja Kumar")
print("Roll: 23053769")
