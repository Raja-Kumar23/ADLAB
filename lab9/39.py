# 39. Extract frames from a short video, stack them as columns in a matrix, apply SVD, and show how low-rank approximation separates static background from moving objects.
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
height,width,frames_count=80,80,20
background=np.ones((height,width))*0.5
frames=[]
for t in range(frames_count):
    frame=background.copy()
    frame[20:30,10+t:20+t]=1
    frames.append(frame)
frames=np.array(frames)
matrix=frames.reshape(frames_count,height*width).T
U,S,Vt=np.linalg.svd(matrix,full_matrices=False)
rank=1
low_rank=U[:,:rank]@np.diag(S[:rank])@Vt[:rank,:]
background_est=low_rank.T.reshape(frames_count,height,width)
foreground=frames-background_est
plt.figure()
plt.imshow(background_est[0],cmap='gray')
plt.title("Estimated Background")
plt.axis("off")
plt.show()
plt.figure()
plt.imshow(foreground[10],cmap='gray')
plt.title("Extracted Moving Object")
plt.axis("off")
plt.show()
print("Rank 1 approximation captures static background.")
print("Subtracting low rank component reveals moving foreground object.")
print("Raja Kumar Sah, 23053769")