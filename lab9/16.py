# 16. Add small Gaussian noise repeatedly and measure clustering stability across runs.
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
X,_=make_blobs(n_samples=400,centers=3,cluster_std=1.0,random_state=42)
base_labels=KMeans(n_clusters=3,random_state=0).fit_predict(X)
for i in range(5):
    noisy_X=X+np.random.normal(0,0.1,X.shape)
    new_labels=KMeans(n_clusters=3,random_state=0).fit_predict(noisy_X)
    ari=adjusted_rand_score(base_labels,new_labels)
    print("Run",i,"Adjusted Rand Index:",ari)
print("ARI close to 1 indicates high stability under small Gaussian noise.")
print("Raja Kumar Sah, 23053769")