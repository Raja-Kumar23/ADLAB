# 28. Study the impact of λ on number of selected features in LASSO.
import numpy as np
from sklearn.linear_model import Lasso
X = np.random.randn(30, 10)
y = X[:,0] + np.random.randn(30)
for lam in [0.01, 0.1, 1]:
    model = Lasso(alpha=lam)
    model.fit(X,y)
    print("Lambda:", lam, "Non-zero:", np.sum(model.coef_ != 0))
print("Raja Kumar Sah, 23053769")