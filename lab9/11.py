# 11. Apply all three algorithms to a two-moons dataset and analyze why non-convex clusters cause failure.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans,MeanShift
from scipy.spatial.distance import cdist
X,_=make_moons(n_samples=400,noise=0.05,random_state=42)
kmeans=KMeans(n_clusters=2,random_state=0)
k_labels=kmeans.fit_predict(X)
def simple_kmedian(X,k,iterations=10):
    centers=X[np.random.choice(len(X),k,replace=False)]
    for _ in range(iterations):
        distances=cdist(X,centers,metric='cityblock')
        labels=np.argmin(distances,axis=1)
        for i in range(k):
            centers[i]=np.median(X[labels==i],axis=0)
    return labels
km_labels=simple_kmedian(X,2)
meanshift=MeanShift()
m_labels=meanshift.fit_predict(X)
plt.figure()
plt.scatter(X[:,0],X[:,1],c=k_labels)
plt.title("KMeans on Two Moons")
plt.show()
plt.figure()
plt.scatter(X[:,0],X[:,1],c=km_labels)
plt.title("KMedian on Two Moons")
plt.show()
plt.figure()
plt.scatter(X[:,0],X[:,1],c=m_labels)
plt.title("MeanShift on Two Moons")
plt.show()
print("KMeans and KMedian assume convex spherical clusters, so they fail on non convex shapes.")
print("Mean Shift performs better because it detects density based regions.")
print("Raja Kumar Sah, 23053769")