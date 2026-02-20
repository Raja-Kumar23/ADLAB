# 18. Apply PCA before clustering and compare performance before and after dimensionality reduction.
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
X,_=make_blobs(n_samples=500,centers=4,n_features=10,random_state=42)
kmeans_before=KMeans(n_clusters=4,random_state=0)
labels_before=kmeans_before.fit_predict(X)
inertia_before=kmeans_before.inertia_
sil_before=silhouette_score(X,labels_before)
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X)
kmeans_after=KMeans(n_clusters=4,random_state=0)
labels_after=kmeans_after.fit_predict(X_pca)
inertia_after=kmeans_after.inertia_
sil_after=silhouette_score(X_pca,labels_after)
print("Before PCA Inertia:",inertia_before,"Silhouette:",sil_before)
print("After PCA Inertia:",inertia_after,"Silhouette:",sil_after)
print("PCA may reduce noise and improve clustering if important structure is preserved.")
print("Raja Kumar Sah, 23053769")