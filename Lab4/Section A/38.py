import numpy as np
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.metrics import mean_squared_error
np.random.seed(0)
X=np.random.rand(50,1)
y=3*X.squeeze()+np.random.randn(50)*2
X_train,X_test=X[:30],X[30:]
y_train,y_test=y[:30],y[30:]
ols=LinearRegression()
ols.fit(X_train,y_train)
train_error_ols=mean_squared_error(y_train,ols.predict(X_train))
test_error_ols=mean_squared_error(y_test,ols.predict(X_test))
ridge=Ridge(alpha=1)
ridge.fit(X_train,y_train)
train_error_ridge=mean_squared_error(y_train,ridge.predict(X_train))
test_error_ridge=mean_squared_error(y_test,ridge.predict(X_test))
print("OLS Train Error:",train_error_ols)
print("OLS Test Error:",test_error_ols)
print("Ridge Train Error:",train_error_ridge)
print("Ridge Test Error:",test_error_ridge)
print("Raja Kumar Sah, 23053769")
