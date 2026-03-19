# 5. Create a visualization showing the decision boundary of a
# McCulloch–Pitts neuron in 2D space and analyze how weight
# changes shift the boundary.
import numpy as np
import matplotlib.pyplot as plt
w1 = 1
w2 = -1
threshold = 0
x = np.linspace(-5,5,100)
y = (threshold - w1*x)/w2
plt.plot(x,y,label="Decision Boundary")
plt.scatter([0,1,1,0],[0,0,1,1])
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Decision Boundary of MP Neuron")
plt.legend()
plt.show()
print("Raja Kumar Sah, 23053769")