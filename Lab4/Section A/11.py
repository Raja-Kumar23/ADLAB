# 11. Implement Ridge regression from scratch using gradient descent.
import numpy as np
X = np.array([[1,1],[1,2],[1,3],[1,4]])
y = np.array([2,4,6,8])
lam = 1
w = np.zeros(2)
for i in range(1000):
    w = w - 0.01*((2/len(y))*X.T@(X@w-y) + 2*lam*w)
print("Ridge weights:", w)
print("Raja Kumar Sah, 23053769")
