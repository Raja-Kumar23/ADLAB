# 5. PCA vs No PCA in Classification
# A. Train SVM without PCA
# B. Train SVM with PCA
# Compare accuracy and training time
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import time
iris = load_iris()
X = iris.data
y = iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
t1 = time.time()
m1 = SVC()
m1.fit(X_train,y_train)
pred1 = m1.predict(X_test)
time1 = time.time()-t1
pca = PCA(n_components=2)
X_train_p = pca.fit_transform(X_train)
X_test_p = pca.transform(X_test)
t2 = time.time()
m2 = SVC()
m2.fit(X_train_p,y_train)
pred2 = m2.predict(X_test_p)
time2 = time.time()-t2
print(accuracy_score(y_test,pred1))
print(accuracy_score(y_test,pred2))
print(time1)
print(time2)
print("PCA vs No PCA in classification completed")
print("Raja Kumar Sah, 23053769")