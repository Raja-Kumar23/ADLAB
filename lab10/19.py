# Q19: Compute and display the full proximity matrix before merge.

import numpy as np
from scipy.spatial.distance import pdist, squareform
X = np.array([[1,1],[2,2],[8,8],[9,9]])
dist_matrix = squareform(pdist(X))
print("Proximity Matrix:\n", dist_matrix)
print("Raja Kumar Sah, 23053769")