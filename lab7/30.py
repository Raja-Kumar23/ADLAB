# 30. Write a program to demonstrate underfitting and overfitting in SVM
# using kernel and C values.
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)
underfit = SVC(kernel="linear", C=0.01)
overfit = SVC(kernel="rbf", C=100, gamma=10)
underfit.fit(X, y)
overfit.fit(X, y)
print("Underfitting & Overfitting demonstrated")
print("Raja Kumar Sah, 23053769")