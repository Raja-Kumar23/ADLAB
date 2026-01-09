#6. Gradient Descent for Logistic Regression
#Implement logistic regression using gradient descent and:
#A. Plot loss vs iterations
#B. Analyze convergence
import numpy as np
import matplotlib.pyplot as plt
X = np.array([1, 2, 3, 4])
y = np.array([0, 0, 1, 1])
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
w = 0
b = 0
lr = 0.1
loss = []
for i in range(200):
    y_pred = sigmoid(w*X + b)
    loss.append(-np.mean(y*np.log(y_pred)+(1-y)*np.log(1-y_pred)))
    w -= lr * np.mean((y_pred - y) * X)
    b -= lr * np.mean(y_pred - y)
plt.plot(loss)
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.show()
print("The loss decreases over iterations, indicating convergence of the gradient descent algorithm for logistic regression.")
print("Raja Kumar Sah, 23053769")