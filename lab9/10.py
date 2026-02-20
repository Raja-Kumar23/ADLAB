# 10. Compare cluster detection of Mean Shift (automatic K) vs fixed K-Means on unknown-cluster dataset.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans,MeanShift
from sklearn.datasets import make_blobs
X,_=make_blobs(n_samples=500,centers=4,cluster_std=1.0,random_state=42)
kmeans=KMeans(n_clusters=4,random_state=0)
k_labels=kmeans.fit_predict(X)
meanshift=MeanShift()
m_labels=meanshift.fit_predict(X)
plt.figure()
plt.scatter(X[:,0],X[:,1],c=k_labels)
plt.title("KMeans Clusters")
plt.show()
plt.figure()
plt.scatter(X[:,0],X[:,1],c=m_labels)
plt.title("MeanShift Clusters")
plt.show()
print("KMeans clusters:",len(np.unique(k_labels)))
print("MeanShift clusters:",len(np.unique(m_labels)))
print("Mean Shift automatically determines number of clusters based on density.")
print("KMeans requires predefined K.")
print("Raja Kumar Sah, 23053769")