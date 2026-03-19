# 14. Conduct an experiment showing weight divergence in Hebbian
# learning and propose a normalization technique to control it.
import numpy as np
x = np.array([1,1])
w = np.zeros(2)
for i in range(10):
    y = np.dot(w,x)
    w = w + x*y
    print("Iteration",i,"Weights",w)
print("Raja Kumar Sah, 23053769")