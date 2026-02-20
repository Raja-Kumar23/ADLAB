# 8. Apply K-Means to 100-dimensional Gaussian data and analyze distance concentration effects.
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist
np.random.seed(0)
X=np.random.randn(500,100)
pairwise_distances=pdist(X)
print("Minimum distance:",np.min(pairwise_distances))
print("Maximum distance:",np.max(pairwise_distances))
print("Mean distance:",np.mean(pairwise_distances))
print("Std of distances:",np.std(pairwise_distances))
print("Ratio (max/min):",np.max(pairwise_distances)/np.min(pairwise_distances))
km=KMeans(n_clusters=3,random_state=0).fit(X)
print("KMeans inertia:",km.inertia_)
print("In high dimensions, distances become similar so separation weakens.")
print("Raja Kumar Sah, 23053769")