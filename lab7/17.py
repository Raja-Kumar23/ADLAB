# 17. Train an SVM and study the effect of changing the regularization
# parameter (C).
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)
for c in [0.1, 1, 10]:
    model = SVC(C=c)
    model.fit(X, y)
    print("C =", c, "Accuracy:", model.score(X, y))
print("Raja Kumar Sah, 23053769")