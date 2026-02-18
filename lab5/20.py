# 20. Explainability of Logistic Regression
#Compute odds ratio and interpret feature importance in real-world terms
from sklearn.linear_model import LogisticRegression
import numpy as np
X=np.array([[1],[2],[3],[4],[5]])
y=np.array([0,0,0,1,1])
m=LogisticRegression().fit(X,y)
print("Odds Ratio:",np.exp(m.coef_))
print("Raja Kumar Sah, 23053769")