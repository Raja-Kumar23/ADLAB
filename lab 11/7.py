# 7. Write a program to compare the performance of
# McCulloch–Pitts neuron vs Perceptron on the same binary
# classification dataset.
from sklearn.linear_model import Perceptron
import numpy as np
X = np.array([
[0,0],
[0,1],
[1,0],
[1,1]
])
y = np.array([0,0,0,1]) # AND
model = Perceptron()
model.fit(X,y)
print("Perceptron Predictions")
print(model.predict(X))
print("Weights:",model.coef_)
print("Raja Kumar Sah, 23053769")