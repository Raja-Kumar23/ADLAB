# 27. Cluster user embeddings in social networks and evaluate why graph clustering may outperform K-Means.
import numpy as np
from sklearn.cluster import KMeans,SpectralClustering
np.random.seed(42)
embeddings=np.random.rand(300,16)
kmeans=KMeans(n_clusters=3,random_state=0)
k_labels=kmeans.fit_predict(embeddings)
spectral=SpectralClustering(n_clusters=3,affinity='nearest_neighbors',random_state=0)
s_labels=spectral.fit_predict(embeddings)
print("KMeans clusters:",len(np.unique(k_labels)))
print("Spectral clusters:",len(np.unique(s_labels)))
print("Graph clustering captures connectivity structure beyond Euclidean distance.")
print("Raja Kumar Sah, 23053769")