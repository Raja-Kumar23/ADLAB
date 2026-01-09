# 3. Visualize RSS contour plots for OLS in a 2D feature space.
import numpy as np
import matplotlib.pyplot as plt
w1 = np.linspace(-5,5,100)
w2 = np.linspace(-5,5,100)
W1, W2 = np.meshgrid(w1,w2)
RSS = (W1-2)**2 + (W2-3)**2
plt.contour(W1, W2, RSS)
plt.xlabel("w1")
plt.ylabel("w2")
plt.show()
print("Raja Kumar Sah, 23053769")
