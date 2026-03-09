# Q16: Cut dendrogram at different heights and analyze cluster count.

from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
X, _ = make_blobs(n_samples=50, centers=3, random_state=42)
Z = linkage(X, method="complete")
plt.figure()
dendrogram(Z)
plt.show()
for h in [5,10,15]:
    clusters = fcluster(Z, h, criterion="distance")
    print("Height", h, "Clusters:", len(np.unique(clusters)))
print("Raja Kumar Sah, 23053769")