# 3. Generate a 3×3 identity matrix and multiply it with a 3×3 matrix of your choice.

import numpy as np
identity_matrix = np.eye(3)
custom_matrix = np.array([[2, 4, 6],
                          [1, 3, 5],
                            [7, 8, 9]])     
result = np.dot(identity_matrix, custom_matrix)
print("Identity Matrix:")
print(identity_matrix)
print("Custom Matrix:")
print(custom_matrix)
print("Result of Multiplication:")
print(result)
print("Name: Raja Kumar")
print("Roll: 23053769")
