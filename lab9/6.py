# 6. Run K-Means before and after feature scaling on unevenly scaled data and explain geometric impact.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
np.random.seed(42)
X=np.random.rand(300,2)
X[:,1]=X[:,1]*1000
kmeans1=KMeans(n_clusters=3,random_state=0)
labels1=kmeans1.fit_predict(X)
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
kmeans2=KMeans(n_clusters=3,random_state=0)
labels2=kmeans2.fit_predict(X_scaled)
plt.figure()
plt.subplot(1,2,1)
plt.scatter(X[:,0],X[:,1],c=labels1)
plt.title("Without Scaling")
plt.subplot(1,2,2)
plt.scatter(X_scaled[:,0],X_scaled[:,1],c=labels2)
plt.title("With Scaling")
plt.show()
print("Without scaling, large feature dominates distance.")
print("With scaling, both dimensions contribute equally.")
print("Raja Kumar Sah, 23053769")