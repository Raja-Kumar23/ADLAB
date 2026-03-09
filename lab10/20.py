# Q20: Visualize how different linkage methods affect cluster shape.

from sklearn.datasets import make_moons
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
X, _ = make_moons(n_samples=200, noise=0.1, random_state=42)
methods = ["single", "complete", "average"]
plt.figure(figsize=(15,4))
for i, method in enumerate(methods):
    model = AgglomerativeClustering(n_clusters=2, linkage=method)
    labels = model.fit_predict(X)
    plt.subplot(1,3,i+1)
    plt.scatter(X[:,0], X[:,1], c=labels)
    plt.title(method)
plt.show()
print("Raja Kumar Sah, 23053769")