# 17. Show that Ridge regression can handle p > n (high-dimensional) datasets.
import numpy as np
n = 5
p = 10  
np.random.seed(0)
X = np.random.rand(n, p)
Y = np.random.rand(n)
# Add bias term
Xb = np.c_[np.ones(n), X]
try:
    beta_ols = np.linalg.inv(Xb.T @ Xb) @ Xb.T @ Y
    print("OLS coefficients:", beta_ols)
except:
    print("OLS FAILED: X^T X is singular")
lam = 1.0
I = np.eye(Xb.shape[1])
beta_ridge = np.linalg.inv(Xb.T @ Xb + lam * I) @ Xb.T @ Y
print("Ridge coefficients:", beta_ridge)
print("Raja Kumar Sah, 23053769")
