# 4. Generate elongated clusters, apply K-Means and K-Median, and explain why spherical assumptions cause failure.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
X,_=make_blobs(n_samples=400,centers=2,cluster_std=[1,4],random_state=42)
X[:,1]=X[:,1]*5
kmeans=KMeans(n_clusters=2,random_state=0)
labels_kmeans=kmeans.fit_predict(X)
centroids=X[np.random.choice(len(X),2,replace=False)]
for _ in range(10):
    distances=np.array([[np.sum(np.abs(x-c)) for c in centroids] for x in X])
    labels_kmedian=np.argmin(distances,axis=1)
    new_centroids=np.array([np.median(X[labels_kmedian==k],axis=0) for k in range(2)])
    if np.allclose(centroids,new_centroids):
        break
    centroids=new_centroids
plt.figure()
plt.subplot(1,2,1)
plt.scatter(X[:,0],X[:,1],c=labels_kmeans)
plt.title("KMeans")
plt.subplot(1,2,2)
plt.scatter(X[:,0],X[:,1],c=labels_kmedian)
plt.title("KMedian")
plt.show()
print("KMeans minimizes squared Euclidean distance and assumes spherical clusters.")
print("KMedian minimizes Manhattan distance and is less sensitive to elongation.")
print("Raja Kumar Sah, 23053769")