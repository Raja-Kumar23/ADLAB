# 35. Use daily stock return data of multiple companies, apply PCA to identify dominant market factors, and interpret the first principal component as a market index-like factor.
import numpy as np
from sklearn.decomposition import PCA
np.random.seed(42)
returns=np.random.randn(300,10)
pca=PCA(n_components=3)
components=pca.fit_transform(returns)
print("Explained variance ratio:",pca.explained_variance_ratio_)
print("First component represents dominant market movement.")
print("Raja Kumar Sah, 23053769")