# 3. Build a two-layer McCulloch–Pitts network to implement XOR
# and compare its architecture with a single neuron.
import numpy as np
def neuron(x, w, t):
    net = np.dot(x, w)
    return 1 if net >= t else 0
inputs = [[0,0],[0,1],[1,0],[1,1]]
print("XOR using 2 layer MP network")
for x in inputs:
    h1 = neuron(x,[1,-1],1)
    h2 = neuron(x,[-1,1],1)
    out = neuron([h1,h2],[1,1],1)
    print(x,"->",out)
print("Raja Kumar Sah, 23053769")