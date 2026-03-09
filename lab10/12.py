# 12. Implement Complete-Link clustering manually by updating the distance matrix after each merge.

import numpy as np
from scipy.spatial.distance import pdist, squareform
X = np.array([[1,2],[2,2],[5,5],[6,5]])
dist_matrix = squareform(pdist(X))
clusters = [[i] for i in range(len(X))]
while len(clusters) > 1:
    min_dist = float('inf')
    merge_pair = (0,1)
    for i in range(len(clusters)):
        for j in range(i+1,len(clusters)):
            max_dist = max([dist_matrix[p][q] for p in clusters[i] for q in clusters[j]])
            if max_dist < min_dist:
                min_dist = max_dist
                merge_pair = (i,j)
    clusters[merge_pair[0]] += clusters[merge_pair[1]]
    clusters.pop(merge_pair[1])
    print("Clusters:", clusters)
    print("Raja Kumar Sah, 23053769")