# Q5. Heatmap for correlation matrix
from matplotlib import pyplot as plt
import numpy as np
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()
print("Name: Raja Kumar")
print("Roll: 23053769")
