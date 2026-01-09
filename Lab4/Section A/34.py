# 34. Plot training error and validation error vs model complexity.
import numpy as np
from sklearn.linear_model import LinearRegression
X = np.random.rand(50,1)
y = 2*X.squeeze() + np.random.randn(50)
model = LinearRegression()
model.fit(X[:30], y[:30])
train_err = np.mean((model.predict(X[:30]) - y[:30])**2)
val_err = np.mean((model.predict(X[30:]) - y[30:])**2)
print("Training error:", train_err)
print("Validation error:", val_err)
print("Raja Kumar Sah, 23053769")