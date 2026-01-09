import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error

# Load dataset
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
ols = LinearRegression()
ols.fit(X_train, y_train)
ols_pred = ols.predict(X_test)
ols_rmse = np.sqrt(mean_squared_error(y_test, ols_pred))
print("OLS RMSE:", ols_rmse)

# -------- Correlation (Multicollinearity) --------
print("\nCorrelation Matrix:")
print(X.corr())

# -------- Ridge --------
ridge = Ridge(alpha=1)
ridge.fit(X_train, y_train)
ridge_pred = ridge.predict(X_test)
ridge_rmse = np.sqrt(mean_squared_error(y_test, ridge_pred))
print("\nRidge RMSE:", ridge_rmse)

# -------- Best Lambda using CV --------
params = {"alpha": [0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(Ridge(), params, cv=5)
grid.fit(X_train, y_train)
print("Best Ridge lambda:", grid.best_params_)

# -------- LASSO --------
lasso = Lasso(alpha=0.05)
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)
lasso_rmse = np.sqrt(mean_squared_error(y_test, lasso_pred))
print("\nLASSO RMSE:", lasso_rmse)

print("\nLASSO Selected Features:")
for f, c in zip(X.columns, lasso.coef_):
    if c != 0:
        print(f, c)

# -------- Final Comparison --------
print("\nRMSE Comparison")
print("OLS   :", ols_rmse)
print("Ridge :", ridge_rmse)
print("LASSO :", lasso_rmse)

print("Raja Kumar Sah, 23053769")
