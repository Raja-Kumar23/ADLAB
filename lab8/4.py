# 4. Effect of Feature Scaling
# A. Without scaling
# B. After StandardScaler
# Compare eigenvalues and explained variance
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
X = load_iris().data
p1 = PCA()
p1.fit(X)
sc = StandardScaler()
X_s = sc.fit_transform(X)
p2 = PCA()
p2.fit(X_s)
print(p1.explained_variance_)
print(p2.explained_variance_)
print(p1.explained_variance_ratio_)
print(p2.explained_variance_ratio_)
print("Effect of feature scaling completed")
print("Raja Kumar Sah, 23053769")