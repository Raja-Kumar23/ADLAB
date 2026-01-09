# 25. Visualize the geometrical interpretation of LASSO using diamond-shaped constraints.
import matplotlib.pyplot as plt
x = [-1, 0, 1, 0, -1]
y = [0, 1, 0, -1, 0]
plt.plot(x, y)
plt.axhline(0); plt.axvline(0)
plt.title("Diamond-shaped LASSO Constraint")
plt.show()
print("Raja Kumar Sah, 23053769")
