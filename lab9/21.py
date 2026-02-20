# 21. Perform customer segmentation using K-Means, interpret clusters, and justify choice of K-Median for income-heavy features.
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
np.random.seed(42)
age=np.random.randint(18,60,300)
income=np.random.randint(20000,200000,300)
spending=np.random.randint(1,100,300)
X=np.column_stack((age,income,spending))
X_scaled=StandardScaler().fit_transform(X)
kmeans=KMeans(n_clusters=3,random_state=0)
labels=kmeans.fit_predict(X_scaled)
print("Cluster centers:",kmeans.cluster_centers_)
print("High income values can skew KMeans due to L2 norm sensitivity.")
print("KMedian preferred for income-heavy data because L1 norm reduces extreme value impact.")
print("Raja Kumar Sah, 23053769")