# 11. Perform Agglomerative Hierarchical Clustering using Single-Link and plot dendrogram.

from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
X, _ = make_blobs(n_samples=100, centers=3, random_state=42)
Z = linkage(X, method='single')
plt.figure(figsize=(8,4))
dendrogram(Z)
plt.title("Single-Link Dendrogram")
plt.show()
print("Raja Kumar Sah, 23053769")