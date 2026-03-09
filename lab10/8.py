#8. Implement DBSCAN on high-dimensional synthetic data and analyze the effect of dimensionality on clustering performance.
# 8. Implement DBSCAN on high-dimensional synthetic data and analyze effect of dimensionality.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
X, _ = make_blobs(n_samples=500, centers=4, n_features=10, random_state=42)
model = DBSCAN(eps=3, min_samples=5)
labels = model.fit_predict(X)
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X)
plt.scatter(X_2d[:,0], X_2d[:,1], c=labels)
plt.title("DBSCAN on High Dimensional Data (PCA view)")
plt.show()
print("Raja Kumar Sah, 23053769")