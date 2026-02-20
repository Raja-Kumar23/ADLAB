# 9. Run Mean Shift with multiple bandwidth values and explain how bandwidth controls cluster resolution.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift
from sklearn.datasets import make_blobs
X,_=make_blobs(n_samples=400,centers=3,cluster_std=1.2,random_state=42)
bandwidth_values=[0.5,1,2]
for bw in bandwidth_values:
    ms=MeanShift(bandwidth=bw)
    labels=ms.fit_predict(X)
    plt.figure()
    plt.scatter(X[:,0],X[:,1],c=labels)
    plt.title("MeanShift Bandwidth="+str(bw))
    plt.show()
    print("Bandwidth:",bw,"Clusters:",len(np.unique(labels)))
print("Smaller bandwidth gives more clusters with fine resolution.")
print("Larger bandwidth merges clusters and reduces resolution.")
print("Raja Kumar Sah, 23053769")