# 27. Apply LASSO to a high-dimensional sparse dataset and analyze selected features
import numpy as np
from sklearn.linear_model import Lasso
X = np.random.randn(20, 100)
y = X[:, 0] * 4 + np.random.randn(20)
model = Lasso(alpha=0.1)
model.fit(X, y)
print("Non-zero features:", np.sum(model.coef_ != 0))
print("Raja Kumar Sah, 23053769")