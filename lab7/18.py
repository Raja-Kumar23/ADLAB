# 18. Write a program to demonstrate margin maximization in SVM.
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)
model = SVC(kernel="linear")
model.fit(X, y)
print("Support Vectors:", model.support_vectors_)
print("Raja Kumar Sah, 23053769")
