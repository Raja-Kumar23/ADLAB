# 8. Feature Scaling Impact
#Train logistic regression:
#A. With unscaled features
#B. With standardized features
#C. Compare convergence speed and accuracy.
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=1
)
# without scaling
m1 = LogisticRegression(max_iter=100)
m1.fit(X, y)
a1 = accuracy_score(y, m1.predict(X))
# with scaling
X_s = StandardScaler().fit_transform(X)
m2 = LogisticRegression(max_iter=100)
m2.fit(X_s, y)
a2 = accuracy_score(y, m2.predict(X_s))
print("Accuracy without scaling:", a1)
print("Accuracy with scaling:", a2)
print("Raja Kumar Sah, 23053769")