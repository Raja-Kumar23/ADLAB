# Q7 OLS using gradient descent
import numpy as np
X=np.random.rand(100,1)
y=4*X.squeeze()+3+np.random.randn(100)
Xb=np.c_[np.ones(100),X]
theta=np.zeros(2)
lr=0.1
for _ in range(1000):
    theta-=2/100*Xb.T@(Xb@theta-y)
print(theta)
print("Name: Raja Kumar")
print("Roll: 23053769")