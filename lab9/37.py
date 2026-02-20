# 37. Given patient clinical features, apply PCA to reduce correlated medical variables, interpret principal components, and analyze whether clustering in PCA space improves risk grouping.
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
np.random.seed(42)
patients=np.random.rand(400,10)
pca=PCA(n_components=3)
reduced=pca.fit_transform(patients)
labels=KMeans(n_clusters=3,random_state=0).fit_predict(reduced)
print("Explained variance:",pca.explained_variance_ratio_)
print("Cluster centers in PCA space:",labels[:10])
print("Raja Kumar Sah, 23053769")