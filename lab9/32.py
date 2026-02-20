# 32. Use a small face image dataset, compute PCA to obtain eigenfaces, reduce dimensionality, project new test images into PCA space, and evaluate how classification accuracy changes as the number of principal components increases.
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
np.random.seed(42)
faces=np.random.rand(200,64)
labels=np.random.randint(0,5,200)
X_train,X_test,y_train,y_test=train_test_split(faces,labels,test_size=0.3,random_state=0)
for k in [5,15,30]:
    pca=PCA(n_components=k)
    X_train_pca=pca.fit_transform(X_train)
    X_test_pca=pca.transform(X_test)
    clf=KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_train_pca,y_train)
    preds=clf.predict(X_test_pca)
    print("Components:",k,"Accuracy:",accuracy_score(y_test,preds))
print("Raja Kumar Sah, 23053769")