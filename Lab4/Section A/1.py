# 1. Implement OLS regression from scratch using the normal equation and validate results with sklearn.
import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1,1],[1,2],[1,3],[1,4]])
y = np.array([2,4,6,8])
w = np.linalg.inv(X.T @ X) @ X.T @ y
print("OLS (scratch):", w)
model = LinearRegression(fit_intercept=False)
model.fit(X, y)
print("OLS (sklearn):", model.coef_)
print("Raja Kumar Sah, 23053769")
