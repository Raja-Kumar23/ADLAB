# 24. Implement SVM for a non-linearly separable dataset.
from sklearn.datasets import make_moons
from sklearn.svm import SVC
X, y = make_moons(noise=0.3)
model = SVC(kernel="rbf")
model.fit(X, y)
print("Non-linear SVM trained")
print("Raja Kumar Sah, 23053769")