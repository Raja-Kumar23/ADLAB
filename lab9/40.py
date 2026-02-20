# 40. Given a dataset with highly correlated features, apply PCA, examine loading vectors, and interpret which original features contribute most to the first few principal components.
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
np.random.seed(42)
base=np.random.rand(300,1)
X=np.hstack((base,base*0.9+np.random.rand(300,1)*0.05,base*1.1+np.random.rand(300,1)*0.05))
X_scaled=StandardScaler().fit_transform(X)
pca=PCA(n_components=3)
X_pca=pca.fit_transform(X_scaled)
print("Explained variance ratio:",pca.explained_variance_ratio_)
print("Principal component loadings:")
print(pca.components_)
for i,comp in enumerate(pca.components_):
    print("PC",i+1,"largest contributing feature index:",np.argmax(np.abs(comp)))
print("First principal component captures common variance among correlated features.")
print("Features with higher absolute loading values contribute more to that component.")
print("Raja Kumar Sah, 23053769")