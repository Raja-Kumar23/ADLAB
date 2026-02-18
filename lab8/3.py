# 3. Cumulative Variance Plot
# A. Compute cumulative explained variance
# B. Plot variance vs number of components
# C. Determine minimum components to retain 95% variance
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
X = load_iris().data
pca = PCA()
pca.fit(X)
cum = np.cumsum(pca.explained_variance_ratio_)
plt.plot(range(1,len(cum)+1), cum)
plt.xlabel("Components")
plt.ylabel("Cumulative Variance")
plt.show()
print(np.argmax(cum>=0.95)+1)
print("Cumulative variance plot completed")
print("Raja Kumar Sah, 23053769")