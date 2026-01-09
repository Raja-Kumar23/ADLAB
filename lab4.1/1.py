# Q1 OLS from scratch using Normal Equation and validation
import numpy as np
from sklearn.linear_model import LinearRegression
X=np.array([[1],[2],[3],[4],[5]])
y=np.array([2,4,6,8,10])
Xb=np.c_[np.ones(len(X)),X]
theta=np.linalg.inv(Xb.T@Xb)@Xb.T@y
model=LinearRegression().fit(X,y)
print(theta)
print(model.intercept_,model.coef_)
print("Name: Raja Kumar")
print("Roll: 23053769")