# Question 8. Model evaluation using MAE, MSE, RMSE
from sklearn.metrics import mean_absolute_error, mean_squared_error
import math
y_true = [10, 20, 30]
y_pred = [12, 18, 33]
print("MAE:", mean_absolute_error(y_true, y_pred))
print("MSE:", mean_squared_error(y_true, y_pred))
print("RMSE:", math.sqrt(mean_squared_error(y_true, y_pred)))
print("Name: Raja Kumar")
print("Roll: 23053769")
