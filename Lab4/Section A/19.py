# 19. Study the effect of Ridge regression on noisy features.
from sklearn.linear_model import Ridge
import numpy as np
X = np.random.randn(100,5)
y = X[:,0] + np.random.randn(100)
print(Ridge(alpha=10).fit(X,y).coef_)
print("Raja Kumar Sah, 23053769")
