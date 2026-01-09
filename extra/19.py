# 19. Compare Logistic vs Linear Regression
#Use linear regression and logistic regression on a binary dataset and compare predictions.from sklearn.linear_model import LinearRegression,LogisticRegression
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
X=np.array([[1],[2],[3],[4],[5]])
y=np.array([0,0,0,1,1])
lr=LinearRegression().fit(X,y)
log=LogisticRegression().fit(X,y)
print("Linear:",lr.predict(X))
print("Logistic:",log.predict(X))
