# 5. Train a Decision Tree using Gini criterion and observe the depth of the
# tree.
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier(criterion="gini")
model.fit(X, y)
print("Tree Depth:", model.get_depth())
print("Raja Kumar Sah, 23053769")
