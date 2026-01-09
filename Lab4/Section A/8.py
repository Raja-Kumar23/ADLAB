# 8. Compare OLS using normal equation vs gradient descent in terms of time and numerical stability.
import numpy as np
import matplotlib.pyplot as plt
def ne(X,y): return np.linalg.inv(X.T@X)@X.T@y
def gd(X,y):
    w=np.zeros(X.shape[1]); L=[]
    for _ in range(300):
        e=X@w-y; L.append((e**2).mean())
        w=w-0.01*(2/len(y))*X.T@e
    return w,L
X=np.c_[np.ones(10),np.random.rand(10,1)]
y=3*X[:,1]+np.random.randn(10)
b1=ne(X,y)
b2,L=gd(X,y)
print(b1,b2)
plt.plot(L); plt.show()
print("Raja Kumar Sah, 23053769")