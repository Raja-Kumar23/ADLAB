# 3. Write a program to calculate Gini Index for a dataset and compare it
# with entropy.
import numpy as np
def entropy(y):
    values, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    return -np.sum(p * np.log2(p))
def gini(y):
    values, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    return 1 - np.sum(p ** 2)
y = np.array([1, 1, 0, 0, 1])
print("Entropy:", entropy(y))
print("Gini Index:", gini(y))
print("Raja Kumar Sah, 23053769")
