# 10. Write a program to show the effect of feature scaling on Decision
# Tree performance.
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
X, y = load_iris(return_X_y=True)
X_scaled = StandardScaler().fit_transform(X)
model = DecisionTreeClassifier()
model.fit(X, y)
model.fit(X_scaled, y)
print("Decision Trees are not affected by scaling")
print("Raja Kumar Sah, 23053769")
