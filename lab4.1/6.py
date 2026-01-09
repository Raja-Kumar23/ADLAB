# Q6 Sensitivity to outliers leverage
import numpy as np
X=np.linspace(1,10,10)
y=2*X+np.random.randn(10)
y[-1]+=30
Xb=np.c_[np.ones(len(X)),X]
H=Xb@np.linalg.inv(Xb.T@Xb)@Xb.T
print(np.diag(H))
print("Name: Raja Kumar")
print("Roll: 23053769")