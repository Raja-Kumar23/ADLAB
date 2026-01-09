# Question 7. Polynomial Regression (degree 2)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([1, 4, 9, 16])
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)
plt.scatter(X, y)
plt.plot(X, model.predict(X_poly))
plt.show()
print("Name: Raja Kumar")
print("Roll: 23053769")
