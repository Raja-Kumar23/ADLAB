# 7. Effect of Learning Rate
#Train logistic regression with different learning rates and compare:
#A. Speed of convergence
#B. Stability of loss
import numpy as np
import matplotlib.pyplot as plt
X = np.array([1, 2, 3, 4])
y = np.array([0, 0, 1, 1])
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
lrs = [0.01, 0.1, 1]
iters = 100
for lr in lrs:
    w, b = 0, 0
    loss = []
    for i in range(iters):
        y_pred = sigmoid(w*X + b)
        loss.append(-np.mean(y*np.log(y_pred)+(1-y)*np.log(1-y_pred)))
        w -= lr * np.mean((y_pred - y) * X)
        b -= lr * np.mean(y_pred - y)
    plt.plot(loss, label=f"lr={lr}")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.legend()
plt.show()
print("Raja Kumar Sah, 23053769")