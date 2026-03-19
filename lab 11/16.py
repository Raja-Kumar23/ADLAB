# 16. Design a program that trains a neuron using Hebbian learning
# and visualize weight trajectory over training iterations.
import numpy as np
import matplotlib.pyplot as plt
w = np.zeros(2)
x = np.array([1,1])
trajectory=[]
for i in range(20):
    y = np.dot(w,x)
    w = w + x*y
    trajectory.append(w.copy())
trajectory = np.array(trajectory)
plt.plot(trajectory[:,0],trajectory[:,1])
plt.xlabel("w1")
plt.ylabel("w2")
plt.title("Weight Trajectory")
plt.show()
print("Raja Kumar Sah, 23053769")