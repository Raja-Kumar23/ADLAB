# Q13: Perform Average-Link clustering and show cluster formation step-by-step.

import numpy as np
X = np.array([[1,1],[2,2],[8,8],[9,9]])
clusters = [[i] for i in range(len(X))]
def average_distance(c1, c2):
    total = 0
    count = 0
    for i in c1:
        for j in c2:
            total += np.linalg.norm(X[i]-X[j])
            count += 1
    return total/count
while len(clusters) > 1:
    min_dist = float("inf")
    merge_pair = None
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            dist = average_distance(clusters[i], clusters[j])
            if dist < min_dist:
                min_dist = dist
                merge_pair = (i, j)
    print("\nClusters:", clusters)
    print("Merging:", clusters[merge_pair[0]], clusters[merge_pair[1]])
    new_cluster = clusters[merge_pair[0]] + clusters[merge_pair[1]]
    clusters.pop(merge_pair[1])
    clusters.pop(merge_pair[0])
    clusters.append(new_cluster)
print("Raja Kumar Sah, 23053769")