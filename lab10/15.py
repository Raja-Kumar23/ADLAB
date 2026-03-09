# Q15: Compare Single, Complete, and Average linkage methods.

from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Generate dataset
X, _ = make_blobs(n_samples=100, centers=3, random_state=42)

methods = ["single", "complete", "average"]

for method in methods:
    model = AgglomerativeClustering(n_clusters=3, linkage=method)
    labels = model.fit_predict(X)
    score = silhouette_score(X, labels)
    print(method, "Silhouette Score:", score)

print("Raja Kumar Sah, 23053769")