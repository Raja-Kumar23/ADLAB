# 35. Show how increasing λ in Ridge increases bias and decreases variance.
from sklearn.linear_model import Ridge
import numpy as np
X = np.random.rand(30,2)
y = X[:,0] + np.random.randn(30)
for lam in [0.1, 1, 10]:
    print("Lambda:", lam, Ridge(alpha=lam).fit(X,y).coef_)
print("Raja Kumar Sah, 23053769")