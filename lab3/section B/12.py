# Q12. Detect outliers using IQR
import pandas as pd
df = pd.DataFrame({     
    "Name": ["A", "B", "C", "D", "E", "F", "G"],
    "Scores": [50, 55, 60, 65, 70,
                300, 75]  # 300 is an outlier
})      
Q1 = df["Scores"].quantile(0.25)
Q3 = df["Scores"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df["Scores"] < lower_bound) | (df["Scores"] > upper_bound)]
print("Outliers detected:")
print(outliers)
print("Name: Raja Kumar")
print("Roll: 23053769")