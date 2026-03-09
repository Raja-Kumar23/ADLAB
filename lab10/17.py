# Q17: Implement Divisive Hierarchical Clustering using recursive splitting.

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=100, centers=1, random_state=42)
def divisive(data, k):
    clusters = [data]
    while len(clusters) < k:
        cluster = clusters.pop(0)
        km = KMeans(n_clusters=2, random_state=42)
        labels = km.fit_predict(cluster)
        clusters.append(cluster[labels==0])
        clusters.append(cluster[labels==1])
    return clusters
result = divisive(X, 3)
print("Total clusters formed:", len(result))
print("Raja Kumar Sah, 23053769")