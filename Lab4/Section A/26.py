import numpy as np
from sklearn.linear_model import Lasso
x1 = np.random.rand(50)
x2 = x1 + 0.0001*np.random.rand(50)
X = np.column_stack((x1, x2))
y = x1 + np.random.randn(50)
for i in range(3):
    model = Lasso(alpha=0.1)
    model.fit(X, y + np.random.randn(50)*0.01)
    print("Run", i+1, model.coef_)
print("Raja Kumar Sah, 23053769")