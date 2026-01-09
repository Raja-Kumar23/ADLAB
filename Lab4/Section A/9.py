# 9. Show experimentally that OLS achieves low bias but high variance on small datasets.
import numpy as np
from sklearn.linear_model import LinearRegression
for i in range(3):
    X = np.random.rand(10,1)
    y = 3*X.squeeze() + np.random.randn(10)
    model = LinearRegression()
    model.fit(X,y)
    print("Run", i+1, "coef:", model.coef_)
print("Raja Kumar Sah, 23053769")