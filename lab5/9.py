#9. Regularization Study
#Train logistic regression with:
#A. No regularization
#B. L1 regularization
#C. L2 regularization
#Compare coefficients and sparsity.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
X, y = make_classification(n_samples=100, n_features=5, random_state=1)
# No regularization
m0 = LogisticRegression(penalty=None)
m0.fit(X, y)
# L1 regularization
m1 = LogisticRegression(penalty="l1", solver="liblinear")
m1.fit(X, y)
# L2 regularization
m2 = LogisticRegression(penalty="l2")
m2.fit(X, y)
print("No reg coef:", m0.coef_)
print("L1 coef:", m1.coef_)
print("L2 coef:", m2.coef_)
print("Raja Kumar Sah, 23053769")