# 10. Verify that OLS fails when XᵀX is singular and explain why.
import numpy as np
X = np.array([[1,2],[2,4]])
print("Determinant:", np.linalg.det(X.T@X))
print("Raja Kumar Sah, 23053769")