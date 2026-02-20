#image segmentation using k-means clustering

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
path = os.path.join(os.path.dirname(__file__), "input.png")

image = Image.open(path).convert("RGB")
image = np.array(image, dtype=np.float64)
rows, cols, ch = image.shape
pixels = image.reshape((-1, 3))
k = 4
np.random.seed(0)
centroids = pixels[np.random.choice(pixels.shape[0], k, replace=False)]
for _ in range(15):
    distances = np.linalg.norm(pixels[:, None] - centroids, axis=2)
    labels = np.argmin(distances, axis=1)

    new_centroids = []
    for i in range(k):
        points = pixels[labels == i]
        if len(points) > 0:
            new_centroids.append(points.mean(axis=0))
        else:
            new_centroids.append(centroids[i])
    centroids = np.array(new_centroids)
segmented_pixels = centroids[labels]
segmented_image = segmented_pixels.reshape(rows, cols, 3)
segmented_image = np.clip(segmented_image, 0, 255).astype(np.uint8)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(image.astype(np.uint8))
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(segmented_image)
plt.axis("off")
plt.show()


