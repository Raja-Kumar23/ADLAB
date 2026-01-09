import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

X,y=load_diabetes(return_X_y=True)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.3)

model=Ridge(alpha=1)
model.fit(Xtr,ytr)

print("Test error:",np.mean((model.predict(Xte)-yte)**2))
print("Raja Kumar Sah, 23053769")
