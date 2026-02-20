# 1. Generate a 2D dataset with 3 clusters, run K-Means 20 times with random initialization, compare inertia values, and explain why results differ.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
np.random.seed(42)
X,_=make_blobs(n_samples=300,centers=3,random_state=42)
plt.scatter(X[:,0],X[:,1])
plt.title("Original Dataset (3 Blobs)")
plt.show()
inertias=[]
models=[]
for i in range(20):
    km=KMeans(n_clusters=3,init='random',n_init=1,random_state=i)
    km.fit(X)
    inertias.append(km.inertia_)
    models.append(km)
    print("Run",i,"Inertia:",km.inertia_)
best_index=np.argmin(inertias)
best_model=models[best_index]
plt.scatter(X[:,0],X[:,1],c=best_model.labels_)
plt.scatter(best_model.cluster_centers_[:,0],best_model.cluster_centers_[:,1],marker='X',s=200)
plt.title("Best K-Means Result (Lowest Inertia)")
plt.show()
print("Minimum Inertia:",min(inertias))
print("Maximum Inertia:",max(inertias))
print("Different random initial centroids lead to convergence at different local minima of the objective function.")
print("Hence inertia values vary across runs.")
print("Raja Kumar Sah, 23053769")