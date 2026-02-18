# 2. PCA Using scikit-learn
# A. Load Iris dataset
# B. Apply PCA (2 components)
# C. Display explained variance ratio
# D. Visualize transformed data
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
iris = load_iris()
X = iris.data
y = iris.target
pca = PCA(n_components=2)
X_new = pca.fit_transform(X)
print(pca.explained_variance_ratio_)
plt.scatter(X_new[:,0], X_new[:,1], c=y)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
print("PCA using scikit-learn completed")
print("Raja Kumar Sah, 23053769")