# 23. Detect crime hotspots using Mean Shift on GPS data and compare performance with K-Means.
import numpy as np
from sklearn.cluster import MeanShift,KMeans
np.random.seed(42)
hotspot1=np.random.randn(200,2)+[20,20]
hotspot2=np.random.randn(200,2)+[50,50]
X=np.vstack((hotspot1,hotspot2))
ms=MeanShift()
ms_labels=ms.fit_predict(X)
km=KMeans(n_clusters=2,random_state=0)
km_labels=km.fit_predict(X)
print("MeanShift clusters:",len(np.unique(ms_labels)))
print("KMeans clusters:",len(np.unique(km_labels)))
print("Mean Shift detects density-based hotspots automatically.")
print("Raja Kumar Sah, 23053769")