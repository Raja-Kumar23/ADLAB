# 9. PCA for Image Compression
# Load a grayscale image.
# A. Apply PCA
# B. Reconstruct image using different k values
# C. Compare reconstruction quality

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
img = load_digits().images[0]
pca = PCA(n_components=5)
X_p = pca.fit_transform(img)
X_rec = pca.inverse_transform(X_p)
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.subplot(1,2,2)
plt.title("Reconstructed")
plt.imshow(X_rec, cmap='gray')
plt.show()
print("Raja Kumar Sah, 23053769")
