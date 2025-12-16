# 10. Create a 5×5 matrix and calculate row-wise and column-wise sums.

import numpy as np
matrix = np.random.randint(1, 5, (5, 5))       
row_sums = matrix.sum(axis=1)
col_sums = matrix.sum(axis=0)
print("5x5 Matrix:")
print(matrix)
print("Row-wise sums:")
print(row_sums)
print("Column-wise sums:")
print(col_sums)
print("Name: Raja Kumar")
print("Roll: 23053769")
