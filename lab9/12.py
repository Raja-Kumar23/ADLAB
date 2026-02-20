# 12. Generate clusters with varying density and test whether Mean Shift detects both equally.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift
X,_=make_blobs(n_samples=500,centers=[[-5,-5],[5,5]],cluster_std=[0.5,3],random_state=42)
ms=MeanShift()
labels=ms.fit_predict(X)
plt.scatter(X[:,0],X[:,1],c=labels)
plt.title("Mean Shift on Varying Density Data")
plt.show()
print("Detected clusters:",len(np.unique(labels)))
print("Mean Shift may merge sparse clusters or split dense clusters depending on bandwidth.")
print("Clusters with different densities are not always detected equally.")
print("Raja Kumar Sah, 23053769")