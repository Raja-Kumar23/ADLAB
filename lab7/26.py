# 26. Implement SVM for multi-class classification using one-vs-rest
# strategy.
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)
model = SVC(decision_function_shape='ovr')
model.fit(X, y)
print("Multi-class SVM trained")
print("Raja Kumar Sah, 23053769")