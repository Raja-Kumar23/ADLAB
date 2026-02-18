# 21. Demonstrate the effect of gamma on SVM with RBF kernel.
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)
for g in [0.1, 1, 10]:
    model = SVC(kernel="rbf", gamma=g)
    model.fit(X, y)
    print("Gamma:", g, "Accuracy:", model.score(X, y))
print("Raja Kumar Sah, 23053769")