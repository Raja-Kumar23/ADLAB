# 9. Load a CSV using numpy and print shape.

import numpy as np
filename = "data.csv"
data = np.genfromtxt(filename, delimiter=',', skip_header=1, encoding="utf-8")
print("Shape:", data.shape)
print("Name: Raja Kumar")
print("Roll: 23053769")
