# 29. Perform land segmentation on satellite image pixel data using K-Means and compare with Mean Shift for irregular terrain.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans,MeanShift
img=np.random.randint(0,255,(100,100,3))
pixels=img.reshape(-1,3)
kmeans=KMeans(n_clusters=4,random_state=0)
k_labels=kmeans.fit_predict(pixels)
meanshift=MeanShift()
m_labels=meanshift.fit_predict(pixels)
plt.imshow(k_labels.reshape(100,100))
plt.title("KMeans Segmentation")
plt.show()
plt.imshow(m_labels.reshape(100,100))
plt.title("MeanShift Segmentation")
plt.show()
print("KMeans assumes compact color regions.")
print("Mean Shift better handles irregular terrain patterns.")
print("Raja Kumar Sah, 23053769")