# 5. Track and plot centroid movement per iteration in K-Means and analyze convergence behavior.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
X,_=make_blobs(n_samples=300,centers=3,random_state=42)
kmeans=KMeans(n_clusters=3,init="random",n_init=1,max_iter=1,random_state=0)
centroids_history=[]
for i in range(10):
    kmeans.max_iter=i+1
    kmeans.fit(X)
    centroids_history.append(kmeans.cluster_centers_)
plt.figure()
plt.scatter(X[:,0],X[:,1],alpha=0.3)
for i in range(len(centroids_history)-1):
    for j in range(3):
        plt.plot([centroids_history[i][j][0],centroids_history[i+1][j][0]],[centroids_history[i][j][1],centroids_history[i+1][j][1]])
plt.title("Centroid Movement")
plt.show()
print("Centroids move significantly in early iterations and stabilize at convergence.")
print("Raja Kumar Sah, 23053769")