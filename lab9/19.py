# 19. Design an incremental version of K-Means for streaming data and explain why Mean Shift struggles in streaming scenarios.
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_blobs
X,_=make_blobs(n_samples=1000,centers=3,random_state=42)
mbk=MiniBatchKMeans(n_clusters=3,batch_size=100,random_state=0)
for i in range(0,len(X),100):
    batch=X[i:i+100]
    mbk.partial_fit(batch)
print("Final cluster centers:",mbk.cluster_centers_)
print("MiniBatchKMeans supports streaming using partial_fit updates.")
print("Mean Shift struggles in streaming because it requires full dataset density estimation each time.")
print("Raja Kumar Sah, 23053769")