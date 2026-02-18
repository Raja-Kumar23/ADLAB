# 8. Visualization of Principal Directions
# For a 2D synthetic dataset:
# A. Plot original data
# B. Plot principal component vectors
# C. Show projection onto first principal component
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
np.random.seed(0)
X = np.dot(np.random.rand(200,2), [[3,1],[1,2]])
pca = PCA(n_components=2)
pca.fit(X)
plt.scatter(X[:,0], X[:,1])
for v in pca.components_:
    plt.arrow(0, 0, v[0]*3, v[1]*3, width=0.1)
plt.show()
X_proj = pca.transform(X)[:,0]
print("Raja Kumar Sah, 23053769")