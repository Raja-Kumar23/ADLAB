# 5. Compare OLS performance with and without feature standardization.
import numpy as np
from sklearn.preprocessing import StandardScaler
X = np.random.rand(20,2)
y = np.random.rand(20)
w1 = np.linalg.inv(X.T@X) @ X.T@y
print("Without scaling:", w1)
scaler = StandardScaler()
Xs = scaler.fit_transform(X)
w2 = np.linalg.inv(Xs.T@Xs) @ Xs.T@y
print("With scaling:", w2)
print("Raja Kumar Sah, 23053769")
