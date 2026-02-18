# 6. Train a Decision Tree using Entropy criterion and compare
# performance with Gini.
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
X, y = load_iris(return_X_y=True)
gini = DecisionTreeClassifier(criterion="gini")
entropy = DecisionTreeClassifier(criterion="entropy")
gini.fit(X, y)
entropy.fit(X, y)
print("Gini Accuracy:", accuracy_score(y, gini.predict(X)))
print("Entropy Accuracy:", accuracy_score(y, entropy.predict(X)))
print("Raja Kumar Sah, 23053769")
