#12. ROC Curve & AUC
#Plot ROC curve and compute AUC for logistic regression. Explain why AUC is preferred over accuracy.
from sklearn.metrics import roc_curve, auc
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([0,0,0,1,1])
model = LogisticRegression()
model.fit(X, y)
y_prob = model.predict_proba(X)[:,1]
fpr, tpr, _ = roc_curve(y, y_prob)
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr)
plt.xlabel("FPR")
plt.ylabel("TPR")
plt.title("ROC Curve")
plt.show()
print("AUC:", roc_auc)
print("Raja Kumar Sah, 23053769")