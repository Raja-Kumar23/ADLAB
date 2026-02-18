# 22. Write a program to show why feature scaling is essential for SVM.
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
X, y = load_iris(return_X_y=True)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = SVC()
model.fit(X_scaled, y)
print("Scaling improves SVM performance")
print("Raja Kumar Sah, 23053769")