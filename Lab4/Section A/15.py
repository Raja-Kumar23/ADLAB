# 15. Perform k-fold cross-validation to find the optimal λ for Ridge regression.
from sklearn.model_selection import KFold
from sklearn.linear_model import Ridge
import numpy as np
X = np.random.rand(30,2)
y = np.random.rand(30)
kf = KFold(5)
for lam in [0.1,1,10]:
    err = []
    for tr,te in kf.split(X):
        r = Ridge(alpha=lam)
        r.fit(X[tr],y[tr])
        err.append(np.mean((y[te]-r.predict(X[te]))**2))
    print(lam, np.mean(err))
print("Raja Kumar Sah, 23053769")
