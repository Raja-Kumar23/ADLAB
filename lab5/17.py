#17. Perfect Separation Case
#Create a perfectly separable dataset and observe what happens to coefficients during training
from sklearn.linear_model import LogisticRegression
import numpy as np
X=np.array([[1],[2],[3],[10],[11],[12]])
y=np.array([0,0,0,1,1,1])
m=LogisticRegression().fit(X,y)
print(m.coef_,m.intercept_)
print("Raja Kumar Sah, 23053769")