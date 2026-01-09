# 33. Compare bias and variance for OLS, Ridge, and LASSO models.
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
true_coef = 3
print("Model Estimated Coefficient")
for i in range(5): 
    X = np.random.rand(20, 1)
    y = 3*X.squeeze() + np.random.randn(20)  
    ols = LinearRegression()
    ridge = Ridge(alpha=1)
    lasso = Lasso(alpha=0.5)
    ols.fit(X, y)
    ridge.fit(X, y)
    lasso.fit(X, y)
    print("OLS   :", round(ols.coef_[0], 2))
    print("Ridge :", round(ridge.coef_[0], 2))
    print("LASSO :", round(lasso.coef_[0], 2))
    print("-"*30)
print("True coefficient =", true_coef)
print("Raja Kumar Sah, 23053769")

