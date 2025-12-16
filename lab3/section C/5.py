# Q5. Heatmap for correlation matrix
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

data = pd.DataFrame(np.random.rand(5, 5))
sns.heatmap(data.corr(), annot=True)
plt.show()

print("Name: Raja Kumar")
print("Roll: 23053769")
