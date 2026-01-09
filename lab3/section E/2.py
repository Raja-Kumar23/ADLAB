# Question 2. Multiple Linear Regression and R2 score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [100, 150, 200, 250]
model = LinearRegression()
model.fit(X, y)
pred = model.predict(X)
print("R2 Score:", r2_score(y, pred))
print("Name: Raja Kumar")
print("Roll: 23053769")
