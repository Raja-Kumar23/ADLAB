# 8. Demonstrate overfitting in Decision Trees by increasing max_depth.
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
X, y = load_iris(return_X_y=True)
for d in [1, 3, 10]:
    model = DecisionTreeClassifier(max_depth=d)
    model.fit(X, y)
    print(f"Depth {d}, Accuracy:", model.score(X, y))
print("Raja Kumar Sah, 23053769")