#10. Class Imbalance Handling
#Train logistic regression on an imbalanced dataset and:
#A. Observe bias in prediction
#B. Apply class weighting
#C. Compare ROC-AUC scores

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
# imbalanced dataset
X, y = make_classification(
    n_samples=300,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    weights=[0.9, 0.1],
    random_state=1
)
# without class weight
m1 = LogisticRegression()
m1.fit(X, y)
auc1 = roc_auc_score(y, m1.predict_proba(X)[:,1])
# with class weight
m2 = LogisticRegression(class_weight="balanced")
m2.fit(X, y)
auc2 = roc_auc_score(y, m2.predict_proba(X)[:,1])
print("ROC-AUC without class weight:", auc1)
print("ROC-AUC with class weight:", auc2)
print("Raja Kumar Sah, 23053769")