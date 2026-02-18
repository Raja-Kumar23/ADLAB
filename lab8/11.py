# 11. PCA and Correlated Features
# Generate correlated features.
# A. Apply PCA
# B. Observe dimensionality reduction
# C. Exlain eigenvalue distribution

import numpy as np
from sklearn.decomposition import PCA
x = np.random.rand(200)
y = x + np.random.normal(0,0.01,200)
X = np.column_stack((x,y))
pca = PCA()
pca.fit(X)
print("Eigenvalues:", pca.explained_variance_)
print("Raja Kumar Sah, 23053769")