# 6. Implement a simulation that randomly initializes weights and
# finds weight combinations that correctly implement logical gates.
import numpy as np
import random
inputs = [[0,0],[0,1],[1,0],[1,1]]
target = [0,0,0,1]   # AND
for _ in range(10000):
    w1 = random.uniform(-2,2)
    w2 = random.uniform(-2,2)
    t = random.uniform(-1,2)
    outputs=[]
    for x in inputs:
        net = w1*x[0] + w2*x[1]
        y = 1 if net >= t else 0
        outputs.append(y)
    if outputs == target:
        print("Found weights:",w1,w2,"Threshold:",t)
        break
print("Raja Kumar Sah, 23053769")