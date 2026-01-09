# Q4 Instability when features approach samples
import numpy as np
X=np.random.randn(10,9)
y=np.random.randn(10)
theta=np.linalg.pinv(X)@y
print(theta)
print("Name: Raja Kumar")
print("Roll: 23053769")