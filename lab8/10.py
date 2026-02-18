# 10. Compare PCA and Random Projection
# Reduce dimensionality using:
# A. PCA
# B. Random Projection
# Compare:
# A. Classification accuracy
# B. Variance retained
from sklearn.random_projection import GaussianRandomProjection
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
X, y = load_iris(return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
pca = PCA(n_components=2)
X_p_train = pca.fit_transform(X_train)
X_p_test = pca.transform(X_test)
rp = GaussianRandomProjection(n_components=2)
X_r_train = rp.fit_transform(X_train)
X_r_test = rp.transform(X_test)
m1 = SVC().fit(X_p_train,y_train)
m2 = SVC().fit(X_r_train,y_train)
print("PCA Accuracy:", accuracy_score(y_test,m1.predict(X_p_test)))
print("Random Projection Accuracy:", accuracy_score(y_test,m2.predict(X_r_test)))
print("Raja Kumar Sah, 23053769")