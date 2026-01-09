#1. Binary Classification Using Logistic Regression
#Write a Python program to implement Logistic Regression from scratch (without using sklearn) for a binary classification dataset with one feature. Plot the sigmoid curve.

import numpy as np
import matplotlib.pyplot as plt
X = np.array([1, 2, 3, 4])
y = np.array([0, 0, 1, 1])
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
w = 0
b = 0
lr = 0.1
for i in range(500):
    y_pred = sigmoid(w*X + b)
    w = w - lr * np.mean((y_pred - y) * X)
    b = b - lr * np.mean(y_pred - y)
x = np.linspace(0, 5, 100)
plt.plot(x, sigmoid(w*x + b))
plt.scatter(X, y)
plt.show()
print("Raja Kumar Sah, 23053769")