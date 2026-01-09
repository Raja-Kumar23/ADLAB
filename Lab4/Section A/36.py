# 36. Show how increasing λ in LASSO affects bias, variance, and sparsity.
from sklearn.linear_model import Lasso
import numpy as np
X = np.random.rand(30,5)
y = X[:,0] + np.random.randn(30)
for lam in [0.01, 0.1, 1]:
    model = Lasso(alpha=lam)
    model.fit(X,y)
    print("Lambda:", lam, "Non-zero:", np.sum(model.coef_!=0))
print("Raja Kumar Sah, 23053769")