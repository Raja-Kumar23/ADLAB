# 13. Demonstrate how Ridge regression reduces variance at the cost of increased bias.
import numpy as np
# Ridge regression using gradient descent
def ridge_gd(X, y, lam):
    Xb = np.c_[np.ones(len(X)), X]
    w = np.zeros(Xb.shape[1])
    for _ in range(300):
        w = w - 0.01 * ((2/len(y)) * Xb.T @ (Xb @ w - y) + 2 * lam * w)
    return w
def mse_vs_lambda(lam):
    X = np.random.randn(30, 5)
    y = X @ np.ones(5) + np.random.randn(30)
    beta = ridge_gd(X, y, lam)
    return np.mean((y - np.c_[np.ones(len(X)), X] @ beta)**2)
for l in [0, 0.1, 1, 10]:
    print(l, mse_vs_lambda(l))

print("Raja Kumar Sah, 23053769")

