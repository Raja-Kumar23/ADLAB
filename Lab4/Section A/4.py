# 4. Show how OLS coefficients become unstable when the number of features approaches the number of samples.
import numpy as np
X = np.random.rand(10,10)
y = np.random.rand(10)
print("Condition number:", np.linalg.cond(X.T @ X))
print("Raja Kumar Sah, 23053769")