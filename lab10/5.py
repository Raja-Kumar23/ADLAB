# 5. Modify DBSCAN to use Manhattan distance instead of Euclidean distance and compare clustering results.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
model1 = DBSCAN(eps=0.5, min_samples=5, metric='euclidean')
labels1 = model1.fit_predict(X)
model2 = DBSCAN(eps=0.5, min_samples=5, metric='manhattan')
labels2 = model2.fit_predict(X)
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.scatter(X[:,0], X[:,1], c=labels1)
plt.title("Euclidean")
plt.subplot(1,2,2)
plt.scatter(X[:,0], X[:,1], c=labels2)
plt.title("Manhattan")
plt.show()
print("Raja Kumar Sah, 23053769")