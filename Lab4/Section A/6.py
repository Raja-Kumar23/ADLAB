# 6. Analyze the sensitivity of OLS to outliers using leverage and Cook’s distance.
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import OLSInfluence
import matplotlib.pyplot as plt
# data with an outlier
np.random.seed(0)
x = np.linspace(0, 10, 20)
y = 2*x + np.random.normal(0, 1, 20)
x = np.append(x, 12)
y = np.append(y, 50)
X = sm.add_constant(x)
# fit OLS
model = sm.OLS(y, X).fit()
# influence measures
influence = OLSInfluence(model)
leverage = influence.hat_matrix_diag
cooks_d = influence.cooks_distance[0]
# plots
plt.stem(leverage)
plt.title("Leverage")
plt.show()
plt.stem(cooks_d)
plt.title("Cook's Distance")
plt.show()
print("Raja Kumar Sah, 23053769")