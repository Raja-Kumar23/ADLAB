#13. Medical Diagnosis Prediction
#Use logistic regression to predict disease presence based on medical features. Interpret coefficients in terms of odds ratio.
from sklearn.linear_model import LogisticRegression
import numpy as np
X=np.array([[120,80],[140,90],[130,85],[160,100]])
y=np.array([0,0,1,1])
m=LogisticRegression().fit(X,y)
odds=np.exp(m.coef_)
print("Coefficients:",m.coef_)
print("Odds Ratio:",odds)
print("Raja Kumar Sah, 23053769")