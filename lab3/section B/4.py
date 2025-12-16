# Rename columns of a DataFrame and drop specified columns.
import pandas as pd
df = pd.read_csv("data.csv")
df = df.rename(columns={
    "name": "full_name",
    "score": "test_score"
})
df = df.drop(columns=["color", "height_m"])
print(list(df.columns))
print("Name: Raja Kumar")
print("Roll: 23053769")


