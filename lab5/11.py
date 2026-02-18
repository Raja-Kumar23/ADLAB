#11. Threshold Tuning
#Change classification threshold from 0.5 to other values and analyze:
#A. Precision
#B. Recall
#C. Confusion matrix
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, confusion_matrix
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    random_state=1
)
model = LogisticRegression()
model.fit(X, y)
probs = model.predict_proba(X)[:,1]
for t in [0.3, 0.5, 0.7]:
    preds = (probs >= t).astype(int)
    print("\nThreshold:", t)
    print("Precision:", precision_score(y, preds))
    print("Recall:", recall_score(y, preds))
    print("Confusion Matrix:\n", confusion_matrix(y, preds))
print("Raja Kumar Sah, 23053769")