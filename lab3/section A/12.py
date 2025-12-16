#12 . Create a matrix and remove duplicate rows using NumPy.
import numpy as np
matrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                        [1, 2, 3],
                            [7, 8, 9]])
unique_rows = np.unique(matrix, axis=0)
print("Original Matrix:")
print(matrix)
print("Matrix after removing duplicate rows:")
print(unique_rows)
print("Name: Raja Kumar")
print("Roll: 23053769")