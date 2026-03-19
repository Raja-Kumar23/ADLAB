# 12. Design a program to demonstrate Hebbian associative learning
# where one input pattern triggers the recall of another stored pattern.
import numpy as np
x = np.array([1,0,1])
y = np.array([0,1])
W = np.outer(x,y)
print("Weight matrix")
print(W)
recall = np.dot(x,W)
print("Recalled pattern:",recall)
print("Raja Kumar Sah, 23053769")