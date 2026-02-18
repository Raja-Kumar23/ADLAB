# 7. PCA on High-Dimensional Data
# Generate synthetic dataset with 100 features.
# A. Apply PCA
# B. Plot eigenvalue spectrum
# C. Identify intrinsic dimensionality
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
X = np.random.rand(300, 100)
pca = PCA()
pca.fit(X)
plt.plot(pca.explained_variance_)
plt.xlabel("Component Number")
plt.ylabel("Eigenvalue")
plt.show()
cum = np.cumsum(pca.explained_variance_ratio_)
print("Intrinsic Dimensionality:", np.argmax(cum >= 0.95) + 1)
print("PCA on high-dimensional data completed")
print("Raja Kumar Sah, 23053769")