# 8. Design an experiment to analyze noise sensitivity of a
# McCulloch–Pitts neuron by adding random perturbations to inputs.
import numpy as np
import random
w = [1,1]
t = 1.5
for _ in range(10):
    x1 = random.random()
    x2 = random.random()
    net = x1*w[0] + x2*w[1]
    y = 1 if net>=t else 0
    print(round(x1,2),round(x2,2),"->",y)
print("Raja Kumar Sah, 23053769")