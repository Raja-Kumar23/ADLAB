# 17. Apply all three algorithms to uniformly random data and explain why artificial clusters still form.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans,MeanShift
from scipy.spatial.distance import cdist
def simple_kmedian(X,k,iterations=5):
    centers=X[np.random.choice(len(X),k,replace=False)]
    for _ in range(iterations):
        distances=cdist(X,centers,metric='cityblock')
        labels=np.argmin(distances,axis=1)
        for i in range(k):
            centers[i]=np.median(X[labels==i],axis=0)
    return labels
X=np.random.rand(500,2)
kmeans=KMeans(n_clusters=3,random_state=0)
k_labels=kmeans.fit_predict(X)
km_labels=simple_kmedian(X,3)
meanshift=MeanShift()
m_labels=meanshift.fit_predict(X)
plt.figure()
plt.scatter(X[:,0],X[:,1],c=k_labels)
plt.title("KMeans on Uniform Data")
plt.show()
plt.figure()
plt.scatter(X[:,0],X[:,1],c=km_labels)
plt.title("KMedian on Uniform Data")
plt.show()
plt.figure()
plt.scatter(X[:,0],X[:,1],c=m_labels)
plt.title("MeanShift on Uniform Data")
plt.show()
print("Artificial clusters form because algorithms force structure even when no true clusters exist.")
print("KMeans and KMedian partition space by distance, MeanShift finds density fluctuations in random data.")
print("Raja Kumar Sah, 23053769")