# 6. Generate a non-convex dataset (moons dataset) and show why DBSCAN performs better than K-means.

from sklearn.datasets import make_moons
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)
db = DBSCAN(eps=0.2, min_samples=5)
db_labels = db.fit_predict(X)
km = KMeans(n_clusters=2, random_state=42)
km_labels = km.fit_predict(X)
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.scatter(X[:,0], X[:,1], c=db_labels)
plt.title("DBSCAN")
plt.subplot(1,2,2)
plt.scatter(X[:,0], X[:,1], c=km_labels)
plt.title("K-Means")
plt.show()
print("Raja Kumar Sah, 23053769")