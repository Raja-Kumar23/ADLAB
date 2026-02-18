# 23. Compare SVM performance before and after standardization.
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
X, y = load_iris(return_X_y=True)
model = SVC()
print("Before scaling:", model.fit(X, y).score(X, y))
X = StandardScaler().fit_transform(X)
print("After scaling:", model.fit(X, y).score(X, y))
print("Raja Kumar Sah, 23053769")