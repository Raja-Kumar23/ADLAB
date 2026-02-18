# 27. Train an SVM on an imbalanced dataset and analyze its performance.
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
X, y = make_classification(weights=[0.9, 0.1])
model = SVC()
model.fit(X, y)
print(confusion_matrix(y, model.predict(X)))
print("Raja Kumar Sah, 23053769")