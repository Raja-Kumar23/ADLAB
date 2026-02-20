# 31. Take a grayscale image and apply SVD to reconstruct it using rank-k approximation for k = 5, 20, 50; compare reconstruction error, storage reduction, and visual quality, and analyze how singular value decay controls compression efficiency.
import numpy as np
import matplotlib.pyplot as plt
img=np.random.rand(100,100)
U,S,Vt=np.linalg.svd(img,full_matrices=False)
for k in [5,20,50]:
    S_k=np.diag(S[:k])
    reconstructed=U[:,:k]@S_k@Vt[:k,:]
    error=np.linalg.norm(img-reconstructed)
    storage=k*(1+100+100)
    plt.figure()
    plt.imshow(reconstructed,cmap='gray')
    plt.title("Rank "+str(k))
    plt.axis("off")
    plt.show()
    print("k",k,"Reconstruction error:",error,"Approx storage:",storage)
print("Rapid singular value decay improves compression efficiency.")
print("Raja Kumar Sah, 23053769")