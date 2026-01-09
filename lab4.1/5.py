# Q5 OLS with and without standardization
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
X=np.array([[1,100],[2,200],[3,300]])
y=np.array([1,2,3])
ols1=LinearRegression().fit(X,y)
Xs=StandardScaler().fit_transform(X)
ols2=LinearRegression().fit(Xs,y)
print(ols1.coef_)
print(ols2.coef_)
print("Name: Raja Kumar")
print("Roll: 23053769")