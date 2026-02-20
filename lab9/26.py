# 26. Cluster retail transaction feature vectors and compare clustering with association rule mining.
import numpy as np
from sklearn.cluster import KMeans
np.random.seed(42)
transactions=np.random.randint(0,2,(300,10))
kmeans=KMeans(n_clusters=3,random_state=0)
labels=kmeans.fit_predict(transactions)
print("Cluster centers:",kmeans.cluster_centers_)
print("Clustering groups similar customers.")
print("Association rule mining finds product co-occurrence patterns instead of customer groups.")
print("Raja Kumar Sah, 23053769")