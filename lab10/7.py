# 7. Write a program to visualize DBSCAN clusters and highlight noise points in a different color.

from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
model = DBSCAN(eps=0.5, min_samples=5)
labels = model.fit_predict(X)
plt.scatter(X[:,0], X[:,1], c=labels)
noise = labels == -1
plt.scatter(X[noise,0], X[noise,1], color='red')
plt.title("DBSCAN with Noise Highlighted")
plt.show()
print("Raja Kumar Sah, 23053769")