# Q14: Implement Centroid-Linkage clustering and demonstrate centroid updates numerically.

import numpy as np
X = np.array([[1,1],[2,2],[8,8],[9,9]])
clusters = [[i] for i in range(len(X))]
def centroid(cluster):
    points = X[cluster]
    return np.mean(points, axis=0)
while len(clusters) > 1:
    min_dist = float("inf")
    merge_pair = None
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            c1 = centroid(clusters[i])
            c2 = centroid(clusters[j])
            dist = np.linalg.norm(c1-c2)
            if dist < min_dist:
                min_dist = dist
                merge_pair = (i, j)
    print("\nClusters:", clusters)
    print("Centroids:", [centroid(c) for c in clusters])
    print("Merging:", clusters[merge_pair[0]], clusters[merge_pair[1]])
    new_cluster = clusters[merge_pair[0]] + clusters[merge_pair[1]]
    clusters.pop(merge_pair[1])
    clusters.pop(merge_pair[0])
    clusters.append(new_cluster)
print("Raja Kumar Sah, 23053769")