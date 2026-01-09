# Question 6. K-Means clustering with K=3
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
print("Cluster Centers:")
print(kmeans.cluster_centers_)
print("Name: Raja Kumar")
print("Roll: 23053769")
