# 19. Implement a Hebbian associative memory model that stores
# multiple patterns and retrieves them when partial inputs are
# provided.
import numpy as np
patterns = [
np.array([1,-1,1]),
np.array([-1,1,-1])
]
W = np.zeros((3,3))
for p in patterns:
    W += np.outer(p,p)
test = np.array([1,-1,0])
recall = np.sign(np.dot(W,test))
print("Recalled:",recall)
print("Raja Kumar Sah, 23053769")