import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error

# Load dataset
X, y = load_diabetes(return_X_y=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# -------- OLS --------
ols = LinearRegression()
ols.fit(X_train, y_train)
ols_pred = ols.predict(X_test)
print("OLS RMSE:", np.sqrt(mean_squared_error(y_test, ols_pred)))

# -------- Outlier Sensitivity --------
y_out = y_train.copy()
y_out[0] = y_out[0] * 5

ols_out = LinearRegression()
ols_out.fit(X_train, y_out)
print("\nOLS Coefficients with outlier:")
print(ols_out.coef_)

# -------- Ridge --------
ridge = Ridge(alpha=10)
ridge.fit(X_train, y_out)
print("\nRidge Coefficients with outlier:")
print(ridge.coef_)

# -------- LASSO --------
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

print("\nSelected Biomarkers (LASSO):")
for i, c in enumerate(lasso.coef_):
    if c != 0:
        print("Feature", i, "=", c)

# -------- Lambda vs Sparsity --------
print("\nEffect of lambda on sparsity:")
for a in [0.01, 0.1, 1, 10]:
    l = Lasso(alpha=a)
    l.fit(X_train, y_train)
    print("lambda:", a, "non-zero features:", np.sum(l.coef_ != 0))

print("\nRecommended Model: LASSO (better explainability in medical diagnosis)")
print("Raja Kumar Sah, 23053769")
