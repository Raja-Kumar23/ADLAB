# 10. Extend DBSCAN to automatically label clusters in sorted order based on cluster size.

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
model = DBSCAN(eps=0.5, min_samples=5)
labels = model.fit_predict(X)
unique = [l for l in set(labels) if l != -1]
sizes = [(l, list(labels).count(l)) for l in unique]
sizes.sort(key=lambda x: x[1], reverse=True)
new_labels = labels.copy()
for new_id, (old_id, _) in enumerate(sizes):
    new_labels[labels == old_id] = new_id
plt.scatter(X[:,0], X[:,1], c=new_labels)
plt.title("Clusters Sorted by Size")
plt.show()
print("Raja Kumar Sah, 23053769")