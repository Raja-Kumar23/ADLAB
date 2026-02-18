# 13. PCA with Explained Variance Threshold
# Automatically select number of components based on variance threshold
from sklearn.decomposition import PCA
import numpy as np
def select_pca(X, threshold=0.9):
    pca = PCA()
    X_fit = pca.fit_transform(X)
    cum = np.cumsum(pca.explained_variance_ratio_)
    k = np.argmax(cum >= threshold) + 1
    return X_fit[:, :k], k
X = np.random.rand(100,5)
X_pca, n_components = select_pca(X)
print("Selected Components:", n_components)
print("Transformed Shape:", X_pca.shape)
print("Raja Kumar Sah, 23053769")
