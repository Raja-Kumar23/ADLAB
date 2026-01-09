# 16. Analyze the effect of λ on training error, validation error, and test error.
import numpy as np
import matplotlib.pyplot as plt
X = np.array([1,2,3,4,5,6,7,8,9,10])
Y = np.array([2,4,6,8,10,12,14,16,18,20])
# Add bias
Xb = np.c_[np.ones(len(X)), X]
lambdas = [0, 0.1, 1, 10]
errors = []
for l in lambdas:
    I = np.eye(Xb.shape[1])
    beta = np.linalg.inv(Xb.T@Xb + l*I) @ Xb.T @ Y   # Ridge formula
    pred = Xb @ beta
    error = np.mean((pred - Y)**2)
    errors.append(error)
plt.plot(lambdas, errors, marker='o')
plt.xlabel("Lambda (λ)")
plt.ylabel("Error")
plt.title("Effect of Lambda on Error")
plt.show()
print("Raja Kumar Sah, 23053769")
