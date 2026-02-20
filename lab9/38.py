# 38. Apply PCA to a dataset, reconstruct the data using first k components, compute reconstruction error for each sample, and use high error points as anomaly candidates.
import numpy as np
from sklearn.decomposition import PCA
np.random.seed(42)
X=np.random.rand(300,8)
pca=PCA(n_components=3)
X_reduced=pca.fit_transform(X)
X_reconstructed=pca.inverse_transform(X_reduced)
errors=np.linalg.norm(X-X_reconstructed,axis=1)
threshold=np.percentile(errors,95)
anomalies=np.where(errors>threshold)[0]
print("Anomaly indices:",anomalies)
print("Raja Kumar Sah, 23053769")