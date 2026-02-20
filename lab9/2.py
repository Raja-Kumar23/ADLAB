# 2. Create two clusters with extreme outliers, compare K-Means and K-Median centroids, and analyze robustness using L2 vs L1 norms.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
np.random.seed(42)
cluster1=np.random.randn(100,2)
cluster2=np.random.randn(100,2)+5
outliers=np.array([[30,30],[35,35],[40,40]])
X=np.vstack((cluster1,cluster2,outliers))
kmeans=KMeans(n_clusters=2,random_state=0)
labels_kmeans=kmeans.fit_predict(X)
centroids=X[np.random.choice(len(X),2,replace=False)]
for _ in range(15):
    distances=np.array([[np.sum(np.abs(x-c)) for c in centroids] for x in X])
    labels_kmedian=np.argmin(distances,axis=1)
    new_centroids=np.array([np.median(X[labels_kmedian==k],axis=0) for k in range(2)])
    if np.allclose(centroids,new_centroids):
        break
    centroids=new_centroids
plt.figure()
plt.subplot(1,2,1)
plt.scatter(X[:,0],X[:,1],c=labels_kmeans)
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=200)
plt.title("KMeans")
plt.subplot(1,2,2)
plt.scatter(X[:,0],X[:,1],c=labels_kmedian)
plt.scatter(centroids[:,0],centroids[:,1],s=200)
plt.title("KMedian")
plt.show()
print("KMeans centroid shifts toward extreme outliers because it minimizes squared L2 distance.")
print("KMedian remains stable because L1 distance reduces influence of extreme values.")
print("Raja Kumar Sah, 23053769")