# 12. Implement a Decision Tree for a regression problem and evaluate
# using MSE.
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,4,6,8,10])
model = DecisionTreeRegressor()
model.fit(X, y)
pred = model.predict(X)
print("MSE:", mean_squared_error(y, pred))
print("Raja Kumar Sah, 23053769")

