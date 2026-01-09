# 32. Estimate bias and variance using bootstrap resampling.
import numpy as np
from sklearn.linear_model import LinearRegression
X = np.random.rand(20,1)
y = 3*X.squeeze() + np.random.randn(20)
coefs = []
for i in range(30):
    idx = np.random.choice(len(X), len(X))
    model = LinearRegression()
    model.fit(X[idx], y[idx])
    coefs.append(model.coef_[0])
print("Variance of coefficient:", np.var(coefs))
print("Raja Kumar Sah, 23053769")