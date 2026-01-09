# 20. Compare Ridge regression with OLS under data perturbation (noise injection).
from sklearn.linear_model import LinearRegression, Ridge
import numpy as np
X = np.random.rand(50,2)
y = np.random.rand(50)
print("OLS:", LinearRegression().fit(X,y).coef_)
print("Ridge:", Ridge(alpha=1).fit(X,y).coef_)
print("Raja Kumar Sah, 23053769")