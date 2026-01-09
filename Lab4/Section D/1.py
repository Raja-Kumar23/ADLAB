import numpy as np
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
np.random.seed(0)
# Create synthetic finance data
# Features: income, loan_amount, credit_score
# Target: risk_score
X = np.random.rand(100,3)
X[:,1] = X[:,0]*0.9 + np.random.rand(100)*0.1   # correlated features
y = 5*X[:,0] + 3*X[:,1] + 2*X[:,2] + np.random.randn(100)
# Train-test split
Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=0.3,random_state=1)
# 1. OLS Regression
ols = LinearRegression()
ols.fit(Xtr,ytr)
pred_ols = ols.predict(Xte)
rmse_ols = np.sqrt(mean_squared_error(yte,pred_ols))
print("OLS RMSE:",rmse_ols)
# 2. Effect of noisy features
X_noisy = Xtr.copy()
X_noisy[:,0] = X_noisy[:,0] + np.random.randn(len(X_noisy))*2
ols_noisy = LinearRegression()
ols_noisy.fit(X_noisy,ytr)
print("OLS Coefficients with noise:",ols_noisy.coef_)
# 3. Ridge Regression
ridge = Ridge(alpha=1)
ridge.fit(Xtr,ytr)
pred_ridge = ridge.predict(Xte)
rmse_ridge = np.sqrt(mean_squared_error(yte,pred_ridge))
print("Ridge RMSE:",rmse_ridge)
print("Ridge Coefficients:",ridge.coef_)
# 4. LASSO Feature Selection
lasso = Lasso(alpha=0.1)
lasso.fit(Xtr,ytr)
pred_lasso = lasso.predict(Xte)
rmse_lasso = np.sqrt(mean_squared_error(yte,pred_lasso))
print("LASSO RMSE:",rmse_lasso)
print("LASSO Selected Features:")
for i,c in enumerate(lasso.coef_):
    if c!=0:
        print("Feature",i,"=",c)
# 5. Stability under perturbation
X_perturb = Xtr + np.random.randn(*Xtr.shape)*0.05
ols_p = LinearRegression().fit(X_perturb,ytr)
ridge_p = Ridge(alpha=1).fit(X_perturb,ytr)
print("OLS coef change:",ols_p.coef_-ols.coef_)
print("Ridge coef change:",ridge_p.coef_-ridge.coef_)
# 6–7. Bias–Variance & Generalization
print("\nRMSE Comparison")
print("OLS  :",rmse_ols)
print("Ridge:",rmse_ridge)
print("LASSO:",rmse_lasso)
# 8. Final Recommendation
print("\nPreferred Model for Banking: Ridge (stable & accurate)")
print("Raja Kumar Sah, 23053769")
