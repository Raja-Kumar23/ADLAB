# 18. Compare Hebbian learning vs gradient-based learning for
# simple pattern classification tasks.
from sklearn.linear_model import Perceptron
import numpy as np
X = [[0,0],[0,1],[1,0],[1,1]]
y = [0,0,0,1]
model = Perceptron()
model.fit(X,y)
print("Perceptron accuracy:",model.score(X,y))
print("Raja Kumar Sah, 23053769")