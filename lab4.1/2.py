# Q2 Effect of multicollinearity
import numpy as np
np.random.seed(0)
x1=np.random.rand(100)
x2=x1+np.random.normal(0,0.01,100)
X=np.c_[np.ones(100),x1,x2]
y=3*x1+np.random.randn(100)
theta=np.linalg.inv(X.T@X)@X.T@y
print(theta)
print("Name: Raja Kumar")
print("Roll: 23053769")