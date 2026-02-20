import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=300, centers=3, random_state=42)


plt.scatter(X[:, 0], X[:, 1])
plt.title("Original Dataset (3 Blobs)")
plt.show()

for i in range(20):
    km = KMeans(n_clusters=3, init='random', n_init=1, random_state=i)
    km.fit(X)
    print("Run", i, "Inertia:", km.inertia_)

km = KMeans(n_clusters=3, init='random', n_init=1, random_state=0)
km.fit(X)


plt.scatter(X[:, 0], X[:, 1], c=km.labels_)
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], marker='X', s=200)
plt.title("K-Means Clustering Result")
plt.show()

print("Results differ because random initialization can lead to different local minima.")
print("Raja Kumar Sah, 23053769")