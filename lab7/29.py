# 29. Implement cross-validation for hyperparameter tuning of SVM.
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
X, y = load_iris(return_X_y=True)
scores = cross_val_score(SVC(), X, y, cv=5)
print("Cross Validation Accuracy:", scores.mean())
print("Raja Kumar Sah, 23053769")