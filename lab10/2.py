# 2. Load a real dataset (Iris without labels) and apply DBSCAN, then identify core, border, and noise points separately.
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN
iris = load_iris()
data = iris.data
model = DBSCAN(eps=0.5, min_samples=5)
labels = model.fit_predict(data)
core_indices = set(model.core_sample_indices_)
core_points = []
border_points = []
noise_points = []
for i in range(len(data)):
    if labels[i] == -1:
        noise_points.append(data[i])
    elif i in core_indices:
        core_points.append(data[i])
    else:
        border_points.append(data[i])
print("Core Points:")
for p in core_points:
    print(p)
print("Border Points:")
for p in border_points:
    print(p)
print("Noise Points:")
for p in noise_points:
    print(p)
    print("Raja Kumar Sah, 23053769")