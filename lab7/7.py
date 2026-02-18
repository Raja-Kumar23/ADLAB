# 7. Write a program to visualize a Decision Tree using graphviz.
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier()
model.fit(X, y)
plt.figure(figsize=(10,6))
plot_tree(model, filled=True)
plt.show()
print("Raja Kumar Sah, 23053769")