# Question 1. Train a Linear Regression model to predict house prices using one feature
from sklearn.linear_model import LinearRegression
X = [[1], [2], [3], [4]]
y = [100, 200, 300, 400]
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[5]])
print("Predicted Price:", prediction)
print("Name: Raja Kumar")
print("Roll: 23053769")
