# 14. PCA Using Singular Value Decomposition
# Implement PCA using SVD instead of eigen decomposition.
# Compare results conceptually.
import numpy as np
X = np.random.rand(100,5)
X = X - np.mean(X,axis=0)
U,S,Vt = np.linalg.svd(X, full_matrices=False)
components = Vt
X_pca = np.dot(X, components.T)
print("Singular Values:", S)
print("Raja Kumar Sah, 23053769")