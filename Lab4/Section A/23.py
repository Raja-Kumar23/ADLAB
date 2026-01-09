# 23. Demonstrate how LASSO performs automatic feature selection.
import numpy as np
from sklearn.linear_model import Lasso
X = np.random.rand(30, 5)
y = X[:, 0] * 5 + np.random.randn(30)
model = Lasso(alpha=0.5)
model.fit(X, y)
print("LASSO coefficients:", model.coef_)
print("Zero coefficients = removed features")
print("Raja Kumar Sah, 23053769")
