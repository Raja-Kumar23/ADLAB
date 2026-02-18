# 18. Bias-Variance Tradeoff
#Train models with different regularization strengths and analyze bias and variance.
from sklearn.linear_model import LogisticRegression
import numpy as np
X=np.array([[1],[2],[3],[4],[5]])
y=np.array([0,0,1,1,1])
for c in [0.01,1,100]:
    m=LogisticRegression(C=c).fit(X,y)
    print("C:",c,"Coef:",m.coef_)
print("Raja Kumar Sah, 23053769")