# 30. Cluster transformed traffic time-series feature vectors and analyze how seasonality affects Euclidean-based clustering.
import numpy as np
from sklearn.cluster import KMeans
np.random.seed(42)
time=np.linspace(0,24,300)
traffic=np.sin(time)+np.random.normal(0,0.2,300)
features=np.column_stack((time,traffic))
kmeans=KMeans(n_clusters=3,random_state=0)
labels=kmeans.fit_predict(features)
print("Cluster centers:",kmeans.cluster_centers_)
print("Seasonality affects Euclidean clustering since phase shifts increase distance.")
print("Raja Kumar Sah, 23053769")