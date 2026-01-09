# 29. Compare model interpretability between OLS, Ridge, and LASSO.
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
X = np.array([[1,2,3],
              [2,3,4],
              [3,4,5],
              [4,5,6],
              [5,6,7]])
y = np.array([5, 7, 9, 11, 13])
ols = LinearRegression()
ols.fit(X, y)
ridge = Ridge(alpha=1)
ridge.fit(X, y)
lasso = Lasso(alpha=0.5)
lasso.fit(X, y)
print("OLS Coefficients:   ", ols.coef_)
print("Ridge Coefficients: ", ridge.coef_)
print("LASSO Coefficients: ", lasso.coef_)
print("Raja Kumar Sah, 23053769")
