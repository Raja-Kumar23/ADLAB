# 25. Cluster medical patient data into risk groups, normalize features, and discuss ethical implications.
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
np.random.seed(42)
age=np.random.randint(20,80,300)
bp=np.random.randint(80,180,300)
cholesterol=np.random.randint(150,300,300)
X=np.column_stack((age,bp,cholesterol))
X_scaled=StandardScaler().fit_transform(X)
kmeans=KMeans(n_clusters=3,random_state=0)
labels=kmeans.fit_predict(X_scaled)
print("Risk group centers:",kmeans.cluster_centers_)
print("Normalization prevents one medical feature from dominating.")
print("Ethical concern: clustering may lead to biased healthcare decisions if misused.")
print("Raja Kumar Sah, 23053769")