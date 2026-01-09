# 37. Design an experiment demonstrating underfitting, overfitting, and optimal fitting.
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
X = np.linspace(0, 10, 20)
y = 3*X + np.random.randn(20)*5   
degrees = [1, 2, 10] 
plt.scatter(X, y, color="black", label="Data")
for d in degrees:
    coef = np.polyfit(X, y, d)
    y_pred = np.polyval(coef, X)
    plt.plot(X, y_pred, label=f"Degree {d}")
plt.legend()
plt.xlabel("X")
plt.ylabel("y")
plt.title("Underfitting vs Optimal vs Overfitting")
plt.show()
print("Degree 1 → Underfitting")
print("Degree 2 → Optimal fitting")
print("Degree 10 → Overfitting")
print("Raja Kumar Sah, 23053769")
