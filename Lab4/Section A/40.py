import numpy as np
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import mean_squared_error
np.random.seed(0)
true_coef=3
ols_coefs=[]
ridge_coefs=[]
lasso_coefs=[]
for i in range(10):
    X=np.random.rand(20,1)
    y=true_coef*X.squeeze()+np.random.randn(20)
    ols=LinearRegression().fit(X,y)
    ridge=Ridge(alpha=1).fit(X,y)
    lasso=Lasso(alpha=0.5).fit(X,y)
    ols_coefs.append(ols.coef_[0])
    ridge_coefs.append(ridge.coef_[0])
    lasso_coefs.append(lasso.coef_[0])
print("True coefficient:",true_coef)
print("OLS mean:",np.mean(ols_coefs),"variance:",np.var(ols_coefs))
print("Ridge mean:",np.mean(ridge_coefs),"variance:",np.var(ridge_coefs))
print("LASSO mean:",np.mean(lasso_coefs),"variance:",np.var(lasso_coefs))
print("Raja Kumar Sah, 23053769")
