#6. Multicollinearity Effect
#Create correlated features and observe how logistic regression coefficients behave.
from sklearn.linear_model import LogisticRegression
import numpy as np
x1=np.array([1,2,3,4,5])
x2=x1+0.01
X=np.c_[x1,x2]
y=np.array([0,0,1,1,1])
m=LogisticRegression().fit(X,y)
print(m.coef_)
print("Raja Kumar Sah, 23053769")
