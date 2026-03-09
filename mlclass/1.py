import numpy as np
import matplotlib.pyplot as plt

x = range(-10, 11)
alpha = [0.2, 0.8, 1.5, 3]

for a in alpha:
    y = []
    for i in x:
        val = 1/(1 + np.exp(-a*i))
        y.append(val)
    plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.legend(["alpha=0.2","alpha=0.8","alpha=1.5","alpha=3"])

plt.text(5, 0.1, "Raja Kumar Sah\n23053769")

plt.show()