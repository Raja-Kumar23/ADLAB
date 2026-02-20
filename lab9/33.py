# 33. Add Gaussian noise to an image, apply truncated SVD to reconstruct the image, and experimentally verify how low-rank approximation removes noise while preserving structure.
import numpy as np
import matplotlib.pyplot as plt
img=np.random.rand(100,100)
noisy=img+np.random.normal(0,0.2,img.shape)
U,S,Vt=np.linalg.svd(noisy,full_matrices=False)
k=20
reconstructed=U[:,:k]@np.diag(S[:k])@Vt[:k,:]
plt.imshow(reconstructed,cmap='gray')
plt.title("Denoised Image")
plt.axis("off")
plt.show()
print("Low rank approximation removes noise while preserving major structure.")
print("Raja Kumar Sah, 23053769")