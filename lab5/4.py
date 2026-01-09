#4. Decision Boundary Visualization
#Train a logistic regression model on a 2-feature dataset and:
#A. Plot the decision boundary
#B. Mark misclassified points

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
# create 2-feature dataset
X, y = make_classification(
    n_samples=100,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    random_state=1
)
# train logistic regression
model = LogisticRegression()
model.fit(X, y)
# predictions
y_pred = model.predict(X)
# plot data points
plt.scatter(X[:,0], X[:,1], c=y, cmap="bwr")
# mark misclassified points
mis = y != y_pred
plt.scatter(X[mis,0], X[mis,1], edgecolors="black", facecolors="none", s=100)
# decision boundary
x1 = np.linspace(X[:,0].min(), X[:,0].max(), 100)
x2 = -(model.coef_[0][0]*x1 + model.intercept_[0]) / model.coef_[0][1]
plt.plot(x1, x2, color="black")
plt.show()
print("Raja Kumar Sah, 23053769")




