# 1. Implement a generalized McCulloch–Pitts neuron where the
# number of inputs, weights, and threshold are user-defined, and
# experimentally study how threshold variation affects neuron
# activation.
import numpy as np
n = int(input("Enter number of inputs: "))
weights = []
inputs = []
for i in range(n):
    w = float(input(f"Enter weight {i+1}: "))
    x = float(input(f"Enter input {i+1}: "))
    weights.append(w)
    inputs.append(x)
threshold = float(input("Enter threshold: "))
net = sum(np.array(weights) * np.array(inputs))
print("Net input =", net)
if net >= threshold:
    print("Neuron Activated (Output = 1)")
else:
    print("Neuron Not Activated (Output = 0)")
print("Raja Kumar Sah, 23053769")