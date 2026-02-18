from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier()
model.fit(X, y)
print("Without split:", model.score(X, y))
Xtr, Xte, ytr, yte = train_test_split(X, y)
model.fit(Xtr, ytr)
print("With split:", model.score(Xte, yte))
print("Shomya Sarraf , 23053668")