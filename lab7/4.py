# 4. Implement Information Gain calculation for a single feature split.
import numpy as np
def entropy(y):
    _, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    return -np.sum(p * np.log2(p))
def information_gain(parent, left, right):
    return entropy(parent) - (
        len(left)/len(parent)*entropy(left) +
        len(right)/len(parent)*entropy(right)
    )
parent = np.array([1,1,0,0])
left = np.array([1,1])
right = np.array([0,0])
print("Information Gain:", information_gain(parent, left, right))
print("Raja Kumar Sah, 23053769")