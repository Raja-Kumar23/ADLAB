#Write code to experimentally determine the optimal ε using a k-distance graph (k = MinPts − 1).
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import NearestNeighbors
iris = load_iris()
data = iris.data
MinPts = 5
k = MinPts - 1
neighbors = NearestNeighbors(n_neighbors=k)
neighbors_fit = neighbors.fit(data)
distances, indices = neighbors_fit.kneighbors(data)
k_distances = distances[:, k-1]
k_distances = np.sort(k_distances)
plt.plot(k_distances)
plt.xlabel("Points sorted by distance")
plt.ylabel("k-distance")
plt.title("K-Distance Graph")
plt.show()
print("Raja Kumar Sah, 23053769")