# 4. Implement DBSCAN and compare clustering results by varying eps while keeping MinPts constant; plot cluster changes.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
MinPts = 5
eps_values = [0.3, 0.5, 0.8]
plt.figure(figsize=(12,4))
for i, eps in enumerate(eps_values):
    model = DBSCAN(eps=eps, min_samples=MinPts)
    labels = model.fit_predict(X)
    plt.subplot(1,3,i+1)
    plt.scatter(X[:,0], X[:,1], c=labels)
    plt.title("eps = " + str(eps))
plt.show()
print("Raja Kumar Sah, 23053769")