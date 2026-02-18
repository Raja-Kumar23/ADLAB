# 19. Implement SVM with polynomial kernel and observe decision
# boundaries.
from sklearn.svm import SVC
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
model = SVC(kernel="poly", degree=3)
model.fit(X, y)
print("Polynomial SVM trained")
print("Raja Kumar Sah, 23053769")
