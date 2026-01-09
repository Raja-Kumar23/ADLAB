# 12. Plot Ridge coefficient paths as λ varies and interpret shrinkage behavior.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
X = np.random.rand(20,2)
y = np.random.rand(20)
alphas = np.logspace(-3,2,50)
coefs = []
for a in alphas:
    r = Ridge(alpha=a)
    r.fit(X,y)
    coefs.append(r.coef_)
plt.plot(alphas, coefs)
plt.xscale("log")
plt.show()
print("Raja Kumar Sah, 23053769")
