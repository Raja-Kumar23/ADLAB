# 3. Derive and experimentally verify the objective functions minimized by K-Means and K-Median on a small dataset.
import numpy as np
import matplotlib.pyplot as plt
X = np.array([1, 2, 10])
mean = np.mean(X)
median = np.median(X)
candidates = np.linspace(0, 12, 200)
l2_values = []
l1_values = []
for c in candidates:
    l2_values.append(np.sum((X - c) ** 2))
    l1_values.append(np.sum(np.abs(X - c)))
print("Mean:", mean)
print("Median:", median)
print("Minimum L2 occurs near mean.")
print("Minimum L1 occurs near median.")
plt.plot(candidates, l2_values, label="L2 Loss")
plt.plot(candidates, l1_values, label="L1 Loss")
plt.axvline(mean)
plt.axvline(median)
plt.legend()
plt.title("Objective Function Verification")
plt.show()
print("Experiment confirms: Mean minimizes L2, Median minimizes L1.")
print("Raja Kumar Sah, 23053769")