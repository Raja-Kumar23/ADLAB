# 14. Compare OLS and Ridge on a dataset with highly correlated features.
from sklearn.linear_model import Ridge, LinearRegression
import numpy as np
x1 = np.random.rand(50)
x2 = x1 + 0.001*np.random.rand(50)
X = np.column_stack((x1,x2))
y = x1 + np.random.randn(50)
print("OLS:", LinearRegression().fit(X,y).coef_)
print("Ridge:", Ridge(alpha=1).fit(X,y).coef_)
print("Raja Kumar Sah, 23053769")