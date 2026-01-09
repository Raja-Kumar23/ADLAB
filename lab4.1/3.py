# Q3 RSS contour plot
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,50)
y=2*x+np.random.randn(50)
t0=np.linspace(-5,5,50)
t1=np.linspace(-1,4,50)
RSS=np.zeros((50,50))
for i in range(50):
    for j in range(50):
        RSS[i,j]=np.sum((y-(t0[i]+t1[j]*x))**2)
plt.contour(t0,t1,RSS)
plt.show()
print("Name: Raja Kumar")
print("Roll: 23053769")