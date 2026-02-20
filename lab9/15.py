# 15. Measure runtime scalability of K-Means, K-Median, and Mean Shift on increasing dataset sizes.
import numpy as np
import time
from sklearn.cluster import KMeans,MeanShift
from sklearn.datasets import make_blobs
from scipy.spatial.distance import cdist
def simple_kmedian(X,k,iterations=5):
    centers=X[np.random.choice(len(X),k,replace=False)]
    for _ in range(iterations):
        distances=cdist(X,centers,metric='cityblock')
        labels=np.argmin(distances,axis=1)
        for i in range(k):
            centers[i]=np.median(X[labels==i],axis=0)
    return labels
sizes=[500,1000,2000]
for n in sizes:
    X,_=make_blobs(n_samples=n,centers=3,random_state=42)
    start=time.time()
    KMeans(n_clusters=3,random_state=0).fit(X)
    print("KMeans size",n,"time",time.time()-start)
    start=time.time()
    simple_kmedian(X,3)
    print("KMedian size",n,"time",time.time()-start)
    start=time.time()
    MeanShift().fit(X)
    print("MeanShift size",n,"time",time.time()-start)
print("KMeans scales efficiently, KMedian slower due to median computation, MeanShift slowest due to density estimation.")
print("Raja Kumar Sah, 23053769")