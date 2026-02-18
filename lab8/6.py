# 6. PCA for Noise Reduction
# Add Gaussian noise to a dataset.
# A. Apply PCA
# B. Reconstruct dataset using top k components
# C. Compute reconstruction Mean Squared Error
import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
np.random.seed(0)
X = np.random.rand(200, 5)
noise = np.random.normal(0, 0.2, X.shape)
X_noisy = X + noise
pca = PCA(n_components=2)
X_p = pca.fit_transform(X_noisy)
X_rec = pca.inverse_transform(X_p)
print("Reconstruction MSE:", mean_squared_error(X, X_rec))
print("Raja Kumar Sah, 23053769")