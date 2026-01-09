# 22. Plot LASSO regularization paths and explain coefficient sparsity.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
X = np.random.rand(20,5)
y = np.random.rand(20)
alphas = np.logspace(-3,1,50)
coefs = []
for a in alphas:
    l = Lasso(alpha=a)
    l.fit(X,y)
    coefs.append(l.coef_)
plt.plot(alphas, coefs)
plt.xscale("log")
plt.show()
print("Raja Kumar Sah, 23053769")
