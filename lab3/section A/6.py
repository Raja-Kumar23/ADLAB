# 6. Find unique elements and their counts in a NumPy array.

import numpy as np
array = np.array([1, 2, 2, 3, 4, 4, 4, 5])
unique_elements, counts = np.unique(array, return_counts=True)
print("Original array:")
print(array)
print("Unique elements:")
print(unique_elements)
print("Counts of unique elements:")
print(counts)
print("Name: Raja Kumar")
print("Roll: 23053769")
