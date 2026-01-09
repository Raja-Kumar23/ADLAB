# 18. Visualize the geometrical interpretation of Ridge using constraint regions and RSS contours.
import numpy as np
import matplotlib.pyplot as plt
# Create coefficient grid
b1 = np.linspace(-4, 4, 200)
b2 = np.linspace(-4, 4, 200)
B1, B2 = np.meshgrid(b1, b2)
# RSS contours (ellipses)
RSS = B1**2 + 2*(B2**2)
# Ridge constraint (circle)
ridge_constraint = B1**2 + B2**2
# Plot RSS contours
plt.contour(B1, B2, RSS, levels=8)
# Plot ridge constraint
plt.contour(B1, B2, ridge_constraint, levels=[4], colors='red')
plt.xlabel("β1")
plt.ylabel("β2")
plt.title("Geometrical Interpretation of Ridge Regression")
plt.show()
print("Raja Kumar Sah, 23053769")
