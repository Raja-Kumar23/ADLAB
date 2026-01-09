#5. Log-Loss Calculation
#Given predicted probabilities and true labels, compute log-loss manually and verify with sklearn.
import numpy as np
from sklearn.metrics import log_loss
y = np.array([1, 0, 1, 1])
p = np.array([0.9, 0.2, 0.7, 0.6])
manual = -np.mean(y*np.log(p) + (1-y)*np.log(1-p))
print("Manual Log Loss:", manual)
print("Sklearn Log Loss:", log_loss(y, p))
print("Raja Kumar Sah, 23053769")