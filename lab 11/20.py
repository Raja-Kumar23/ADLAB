# 20. Develop a hybrid system combining McCulloch–Pitts neuron
# for inference and Hebbian learning for weight adaptation, and
# analyze its effectiveness.
import numpy as np
weights = np.zeros(2)
inputs = [[1,0],[0,1],[1,1]]
for x in inputs: 
    y = 1 if sum(x)>=1 else 0 
    weights = weights + np.array(x)*y
print("Learned weights:",weights)
test = [1,1]
output = 1 if np.dot(test,weights)>=1 else 0
print("Prediction:",output)
print("Raja Kumar Sah, 23053769")