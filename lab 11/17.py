# 17. Implement Hebbian learning on a small image dataset to detect
# common features.
import numpy as np
image = np.array([
[1,1,0],
[1,0,0],
[1,1,1]
])
weights = np.zeros_like(image)
weights = weights + image
print("Learned features")
print(weights)
print("Raja Kumar Sah, 23053769")