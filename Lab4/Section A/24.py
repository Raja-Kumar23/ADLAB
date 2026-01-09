# 24. Compare Ridge and LASSO when predictors are strongly correlated.
import numpy as np
from sklearn.linear_model import Ridge, Lasso
x1 = np.random.rand(50)
x2 = x1 + 0.001*np.random.rand(50)   
X = np.column_stack((x1, x2))
y = x1 + np.random.randn(50)
print("Ridge:", Ridge(alpha=1).fit(X,y).coef_)
print("LASSO:", Lasso(alpha=0.1).fit(X,y).coef_)
print("Raja Kumar Sah, 23053769")
