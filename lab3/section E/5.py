# Question 5. Decision Tree classifier and confusion matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix

iris = load_iris()
X = iris.data
y = iris.target

dt = DecisionTreeClassifier()
dt.fit(X, y)

pred = dt.predict(X)
print("Confusion Matrix:")
print(confusion_matrix(y, pred))

print("Name: Raja Kumar")
print("Roll: 23053769")
