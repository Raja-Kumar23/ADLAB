# 31. Illustrate the bias–variance trade-off using polynomial regression of increasing degree.
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
X = np.linspace(0,1,20).reshape(-1,1)
y = np.sin(2*np.pi*X).ravel() + np.random.randn(20)*0.1
for d in [1,3,10]:
    poly = PolynomialFeatures(d)
    Xp = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(Xp,y)
    print("Degree", d, "Training error:", np.mean((model.predict(Xp)-y)**2))
print("Shomya Sarraf, 23053668")