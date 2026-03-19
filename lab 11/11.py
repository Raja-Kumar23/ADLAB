# 11. Implement the Hebbian learning rule and study how weights
# evolve when training data contains conflicting patterns.
import numpy as np
inputs = np.array([
[1,1],
[1,-1],
[-1,1]
])
weights = np.zeros(2)
for x in inputs:
    y = np.sign(np.sum(x))
    weights = weights + x*y
print("Weights after Hebbian learning:",weights)
print("Raja Kumar Sah, 23053769")