# 4. Reshape a 1D array of size 16 into a 4×4 matrix without using reshape() manually.

import numpy as np
a = np.arange(16)
matrix_4x4 = a.reshape(4, 4)
print("Original 1D array:")
print(a)
print("Reshaped 4x4 matrix:")
print(matrix_4x4)
print("Name: Raja Kumar")
print("Roll: 23053769")
