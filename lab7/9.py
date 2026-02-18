# 9. Control overfitting using pruning parameters such as max_depth,
# min_samples_split, and min_samples_leaf.
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier(
    max_depth=3,
    min_samples_split=5,
    min_samples_leaf=3
)
model.fit(X, y)
print("Pruned Tree Accuracy:", model.score(X, y))
print("Raja Kumar Sah, 23053769")
