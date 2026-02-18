# 25. Write a program to visualize support vectors in a trained SVM model.
from sklearn.datasets import make_moons
from sklearn.svm import SVC
import matplotlib.pyplot as plt
X, y = make_moons(noise=0.3)
model = SVC(kernel="rbf")
model.fit(X, y)
plt.scatter(X[:,0], X[:,1], c=y)
plt.scatter(model.support_vectors_[:,0],
            model.support_vectors_[:,1],
            s=100, edgecolors='k', facecolors='none')
plt.show()
print("Raja Kumar Sah, 23053769")