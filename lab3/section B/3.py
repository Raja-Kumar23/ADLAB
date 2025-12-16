# 3. Replace missing values using mean for numeric columns and mode for categorical ones.
import pandas as pd
data = pd.DataFrame({
    "age": [20, None, 30, None],
    "city": ["Delhi", "Mumbai", None, "Delhi"]
})
data["age"] = data["age"].fillna(data["age"].mean())
data["city"] = data["city"].fillna(data["city"].mode()[0])
print(data)
print("Name: Raja Kumar")
print("Roll: 23053769")


