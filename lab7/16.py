# 16. Implement a linear SVM classifier using scikit-learn.
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)
model = SVC(kernel="linear")
model.fit(X, y)
print("Linear SVM trained")
print("Raja Kumar Sah, 23053769")
