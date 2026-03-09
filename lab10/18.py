# Q18: Compare Hierarchical clustering with DBSCAN using silhouette score.

from sklearn.datasets import make_moons
from sklearn.cluster import AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score
import numpy as np
X, _ = make_moons(n_samples=200, noise=0.1, random_state=42)
agg = AgglomerativeClustering(n_clusters=2)
agg_labels = agg.fit_predict(X)
agg_score = silhouette_score(X, agg_labels)
print("Agglomerative Silhouette:", agg_score)
db = DBSCAN(eps=0.2, min_samples=5)   
db_labels = db.fit_predict(X)
mask = db_labels != -1
unique_clusters = np.unique(db_labels[mask])
if len(unique_clusters) > 1:
    db_score = silhouette_score(X[mask], db_labels[mask])
    print("DBSCAN Silhouette:", db_score)
else:
    print("DBSCAN did not form enough clusters for silhouette calculation.")
print("Raja Kumar Sah, 23053769")