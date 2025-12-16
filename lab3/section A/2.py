# 2. Write a program to create a 1D NumPy array and normalize it (scale between 0 and 1).

import numpy as np
a =np.array([5,20,15,25,30,35,40,45,50,60] , dtype=float)
normalized_a = (a - a.min()) / (a.max() - a.min())
print("Original array:")    
print(a)
print("Normalized array:")
print(normalized_a)     
print("Name: Raja Kumar")
print("Roll: 23053769")