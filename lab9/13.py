# 13. Plot the K-Means objective function landscape in 1D and identify local minima.
import numpy as np
import matplotlib.pyplot as plt
X=np.array([1,2,3,10,11,12])
candidates=np.linspace(0,15,200)
loss=[]
for c in candidates:
    loss.append(np.sum((X-c)**2))
loss=np.array(loss)
plt.plot(candidates,loss)
plt.title("KMeans 1D Objective Landscape")
plt.xlabel("Centroid value")
plt.ylabel("Sum of Squared Errors")
plt.show()
min_index=np.argmin(loss)
print("Global minimum at centroid =",candidates[min_index])
print("Objective is convex in 1D so only one minimum exists.")
print("Raja Kumar Sah, 23053769")