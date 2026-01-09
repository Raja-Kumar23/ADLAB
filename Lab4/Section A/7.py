# 7. Implement OLS using batch gradient descent and study convergence behavior.
import numpy as np
X = np.array([[1,1],[1,2],[1,3],[1,4]])
y = np.array([2,4,6,8])
w = np.zeros(2)
lr = 0.01
for i in range(1000):
    w = w - lr * (2/len(y)) * X.T @ (X@w - y)
print("Weights:", w)
print("Raja Kumar Sah, 23053769")