# 9. Compare DBSCAN with Hierarchical Single-Link clustering on same dataset.

from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
db = DBSCAN(eps=0.5, min_samples=5)
db_labels = db.fit_predict(X)
hc = AgglomerativeClustering(n_clusters=3, linkage='single')
hc_labels = hc.fit_predict(X)
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.scatter(X[:,0], X[:,1], c=db_labels)
plt.title("DBSCAN")
plt.subplot(1,2,2)
plt.scatter(X[:,0], X[:,1], c=hc_labels)
plt.title("Single-Link")
plt.show()
print("Raja Kumar Sah, 23053769")