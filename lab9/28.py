# 28. Use K-Means for anomaly detection by distance from centroids and evaluate robustness vs K-Median.
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
np.random.seed(42)
X=np.vstack((np.random.randn(200,2),[[10,10],[12,12]]))
kmeans=KMeans(n_clusters=2,random_state=0)
labels=kmeans.fit_predict(X)
distances=np.min(cdist(X,kmeans.cluster_centers_),axis=1)
threshold=np.percentile(distances,95)
anomalies=X[distances>threshold]
print("Detected anomalies:",anomalies)
print("KMeans sensitive to outliers due to squared distance.")
print("KMedian more robust since L1 norm reduces extreme influence.")
print("Raja Kumar Sah, 23053769")