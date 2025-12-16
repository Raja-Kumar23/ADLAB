# Q8. MAE, MSE, RMSE
from sklearn.metrics import mean_absolute_error, mean_squared_error
import math

pred = model.predict(X_poly)

print("MAE:", mean_absolute_error(y, pred))
print("MSE:", mean_squared_error(y, pred))
print("RMSE:", math.sqrt(mean_squared_error(y, pred)))

print("Name: Raja Kumar")
print("Roll: 23053769")
