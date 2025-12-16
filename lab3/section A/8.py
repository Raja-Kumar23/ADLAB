# 8. Generate two random arrays and compute cosine similarity.

import numpy as np
a = np.random.rand(5)
b = np.random.rand(5)
cosine_similarity = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print("Array A:")
print(a)
print("Array B:")
print(b)
print("Cosine Similarity between A and B:")
print(cosine_similarity)
print("Name: Raja Kumar")
print("Roll: 23053769")