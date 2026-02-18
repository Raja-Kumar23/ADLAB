# 1. Manual PCA from Scratch
# A. Standardize dataset
# B. Compute covariance matrix
# C. Calculate eigenvalues and eigenvectors
# D. Sort eigenvalues in descending order
# E. Project data onto first two principal components
import numpy as np
X = np.array([[2.5,2.4,1.2],
              [0.5,0.7,0.3],
              [2.2,2.9,1.5],
              [1.9,2.2,1.1],
              [3.1,3.0,1.8]])
X_std = (X - np.mean(X,axis=0)) / np.std(X,axis=0)
cov = np.cov(X_std.T)
eig_val, eig_vec = np.linalg.eig(cov)
idx = np.argsort(eig_val)[::-1]
eig_val = eig_val[idx]
eig_vec = eig_vec[:,idx]
X_pca = np.dot(X_std, eig_vec[:,:2])
print(eig_val)
print(X_pca)
print("PCA from scratch completed")
print("Raja Kumar Sah, 23053769")