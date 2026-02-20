# 7. Determine optimal K using Elbow and Silhouette methods on ambiguous data and compare reliability.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
X,_=make_blobs(n_samples=400,centers=4,cluster_std=2.5,random_state=42)
inertias=[]
sil_scores=[]
K_range=range(2,8)
for k in K_range:
    km=KMeans(n_clusters=k,random_state=0).fit(X)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X,km.labels_))
plt.figure()
plt.subplot(1,2,1)
plt.plot(K_range,inertias)
plt.title("Elbow")
plt.subplot(1,2,2)
plt.plot(K_range,sil_scores)
plt.title("Silhouette")
plt.show()
print("Elbow may be unclear on ambiguous data, silhouette often more reliable.")
print("Raja Kumar Sah, 23053769")