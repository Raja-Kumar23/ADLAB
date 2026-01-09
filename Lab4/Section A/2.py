# 2. Demonstrate the effect of multicollinearity on OLS coefficients using synthetic correlated features.
import numpy as np
x1 = np.random.rand(50)
x2 = x1 + 0.001*np.random.rand(50)
X = np.column_stack((np.ones(50), x1, x2))
y = 3*x1 + np.random.randn(50)
w = np.linalg.inv(X.T @ X) @ X.T @ y
print("Coefficients:", w)
print("Raja Kumar Sah, 23053769")