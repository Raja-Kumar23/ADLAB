# 15. Credit Risk Classification
#Train a logistic regression model to classify loan defaulters. Evaluate using precision-recall curve. 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
import numpy as np
X=np.array([[50],[60],[70],[80],[90]])
y=np.array([0,0,1,1,1])
m=LogisticRegression().fit(X,y)
p=m.predict_proba(X)[:,1]
pr,re,_=precision_recall_curve(y,p)
plt.plot(re,pr);plt.show()
print("Raja Kumar Sah, 23053769")