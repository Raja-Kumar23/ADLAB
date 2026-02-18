# 15. PCA Reconstruction Error Analysis
# For different values of k:
# A. Project data
# B. Reconstruct data
# C. Plot reconstruction error versus k
# D. Interpret bias variance tradeoff
import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
X = np.random.rand(200,10)
errors = []
for k in range(1,11):
    pca = PCA(n_components=k)
    X_p = pca.fit_transform(X)
    X_rec = pca.inverse_transform(X_p)
    errors.append(mean_squared_error(X,X_rec))
plt.plot(range(1,11), errors)
plt.xlabel("Number of Components")
plt.ylabel("Reconstruction Error")
plt.show()
print("Raja Kumar Sah, 23053769")