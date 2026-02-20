# 34. Given a customer dataset with 15–20 features, apply PCA to reduce dimensions, then perform K-Means clustering before and after PCA, and compare clustering stability and interpretability.
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
np.random.seed(42)
X=np.random.rand(500,18)
labels_before=KMeans(n_clusters=3,random_state=0).fit_predict(X)
pca=PCA(n_components=5)
X_pca=pca.fit_transform(X)
labels_after=KMeans(n_clusters=3,random_state=0).fit_predict(X_pca)
ari=adjusted_rand_score(labels_before,labels_after)
print("ARI between before and after PCA:",ari)
print("Raja Kumar Sah, 23053769")