# 15. Implement competitive Hebbian learning where multiple
# neurons compete to represent input patterns.
import numpy as np
w = np.random.rand(2,2)
inputs = [[1,0],[0,1]]
for x in inputs:
    scores = np.dot(w,x)
    winner = np.argmax(scores)
    w[winner] = w[winner] + x
print(w)
print("Raja Kumar Sah, 23053769")