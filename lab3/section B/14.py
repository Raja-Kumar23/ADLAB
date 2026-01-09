# Q14. Save cleaned data to CSV
import pandas as pd
df = pd.read_csv("data.csv")
df.to_csv("cleaned_data.csv", index=False)
print("Saved cleaned_data.csv")
print("Name: Raja Kumar")
print("Roll: 23053769")
