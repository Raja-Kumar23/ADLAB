# 6. Add a new column “BMI” using height & weight data (BMI = weight / height²).

import pandas as pd
df = pd.read_csv("data.csv")
df["BMI"] = df["weight_kg"] / (df["height_m"] ** 2)
print("Added BMI column:")
print(df[["weight_kg", "height_m", "BMI"]].head())
print("Name: Raja Kumar")
print("Roll: 23053769")
