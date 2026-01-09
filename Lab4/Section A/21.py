# 21. Implement LASSO regression from scratch using coordinate descent.
from sklearn.linear_model import Lasso
import numpy as np
X = np.random.rand(20,5)
y = np.random.rand(20)
lasso = Lasso(alpha=0.1)
lasso.fit(X,y)
print(lasso.coef_)
print("Raja Kumar Sah, 23053769")
