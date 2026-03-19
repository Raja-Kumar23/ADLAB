# 13. Implement Hebbian learning with normalization and compare
# its stability with the basic Hebbian rule.
import numpy as np
x = np.array([1,1])
w = np.zeros(2)
for _ in range(5):
    y = np.dot(w, x)
    w = w + x * y
    norm = np.linalg.norm(w)
    if norm != 0:
        w = w / norm
print("Normalized weights:", w)
print("Raja Kumar Sah, 23053769")