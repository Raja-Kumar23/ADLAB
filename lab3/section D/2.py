# Question 2. Standardize a numeric column using Z-score
import numpy as np
data = np.array([10, 20, 30, 40, 50])
z_score = (data - np.mean(data)) / np.std(data)
print(z_score)
print("Name: Raja Kumar")
print("Roll: 23053769")
