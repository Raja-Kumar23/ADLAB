# 11. Train a Decision Tree on a dataset containing categorical features
# using encoding.
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np
X = np.array(["Red", "Blue", "Green", "Blue"]).reshape(-1,1)
y = np.array([1, 0, 1, 0])
le = LabelEncoder()
X_encoded = le.fit_transform(X.ravel()).reshape(-1,1)
model = DecisionTreeClassifier()
model.fit(X_encoded, y)
print("Model trained with categorical data")
print("Raja Kumar Sah, 23053769")
