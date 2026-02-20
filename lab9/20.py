# 20. Construct a dataset where K-Means fails, K-Median partially works, and Mean Shift succeeds, and justify mathematically.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans,MeanShift
from scipy.spatial.distance import cdist
def simple_kmedian(X,k,iterations=5):
    centers=X[np.random.choice(len(X),k,replace=False)]
    for _ in range(iterations):
        distances=cdist(X,centers,metric='cityblock')
        labels=np.argmin(distances,axis=1)
        for i in range(k):
            if np.any(labels==i):
                centers[i]=np.median(X[labels==i],axis=0)
    return labels
X,_=make_moons(n_samples=400,noise=0.05,random_state=42)
outliers=np.array([[3,3],[4,4]])
X=np.vstack((X,outliers))
kmeans=KMeans(n_clusters=2,random_state=0)
k_labels=kmeans.fit_predict(X)
km_labels=simple_kmedian(X,2)
meanshift=MeanShift()
m_labels=meanshift.fit_predict(X)
plt.figure()
plt.scatter(X[:,0],X[:,1],c=k_labels)
plt.title("KMeans Result")
plt.show()
plt.figure()
plt.scatter(X[:,0],X[:,1],c=km_labels)
plt.title("KMedian Result")
plt.show()
plt.figure()
plt.scatter(X[:,0],X[:,1],c=m_labels)
plt.title("MeanShift Result")
plt.show()
print("KMeans fails due to squared distance sensitivity to outliers and convex assumption.")
print("KMedian partially works since L1 norm reduces outlier influence but still assumes convex clusters.")
print("Mean Shift succeeds by detecting density based non convex regions.")
print("Mathematically L2 exaggerates large deviations while L1 is more robust, density estimation captures true structure.")
print("Raja Kumar Sah, 23053769")