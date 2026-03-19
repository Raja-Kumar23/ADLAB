# 2. Design a program to test the linear separability limitation of
# McCulloch–Pitts neurons by attempting to implement XOR and
# analyzing why it fails.
import numpy as np
inputs = np.array([
[0,0],
[0,1],
[1,0],
[1,1]
])
xor = [0,1,1,0]
w = [1,1]
threshold = 1.5
print("Testing XOR with McCulloch Pitts neuron")
for i in range(4):
    net = np.dot(inputs[i], w)
    output = 1 if net >= threshold else 0
    print(inputs[i], "Output:", output, "Expected:", xor[i])
print("Raja Kumar Sah, 23053769")