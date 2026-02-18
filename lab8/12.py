# 12. PCA Before KNN
# Train KNN:
# A. Without PCA
# B. With PCA
# Analyze:
# C. Curse of dimensionality effect
# D. Accuracy difference
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
X,y = load_iris(return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
knn1 = KNeighborsClassifier().fit(X_train,y_train)
acc1 = accuracy_score(y_test,knn1.predict(X_test))
pca = PCA(n_components=2)
X_train_p = pca.fit_transform(X_train)
X_test_p = pca.transform(X_test)
knn2 = KNeighborsClassifier().fit(X_train_p,y_train)
acc2 = accuracy_score(y_test,knn2.predict(X_test_p))
print("Without PCA Accuracy:", acc1)
print("With PCA Accuracy:", acc2)
print("Raja Kumar Sah, 23053769")