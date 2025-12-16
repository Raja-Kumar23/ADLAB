# 11. Write a program to check whether two NumPy arrays are equal.

import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 2, 3, 4, 5])
are_equal = np.array_equal(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Are the two arrays equal?", are_equal)
print("Name: Raja Kumar")
print("Roll: 23053769")