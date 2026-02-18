# 28. Compare Decision Tree vs SVM on the same dataset using accuracy
# and confusion matrix.
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)
dt = DecisionTreeClassifier().fit(X, y)
svm = SVC().fit(X, y)
print("DT Accuracy:", dt.score(X, y))
print("SVM Accuracy:", svm.score(X, y))
print("Raja Kumar Sah, 23053769")