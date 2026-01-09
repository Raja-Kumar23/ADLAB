#14. Student Pass/Fail Prediction
#Build a logistic regression model to predict pass/fail using attendance and marks. Explain decision boundary.
from sklearn.linear_model import LogisticRegression
import numpy as np
X=np.array([[60,40],[65,45],[70,55],[75,60]])
y=np.array([0,0,1,1])
m=LogisticRegression().fit(X,y)
print("Decision Boundary:",m.coef_,m.intercept_)
print("Raja Kumar Sah, 23053769")