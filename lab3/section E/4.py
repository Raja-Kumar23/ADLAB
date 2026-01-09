# Question 4. KNN classifier on Iris dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print("KNN Classifier Accuracy:", accuracy)
print("Name: Raja Kumar")
print("Roll: 23053769")
