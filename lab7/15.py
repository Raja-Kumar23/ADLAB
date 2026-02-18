# 15. Demonstrate how Decision Trees handle non-linear decision
# boundaries.
from sklearn.datasets import make_moons
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
X, y = make_moons(noise=0.2)
model = DecisionTreeClassifier()
model.fit(X, y)
plt.scatter(X[:,0], X[:,1], c=y)
plt.show()
print("Raja Kumar Sah, 23053769")
