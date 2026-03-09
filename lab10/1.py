#Write a program to implement DBSCAN from scratch (without using sklearn DBSCAN) and cluster a 2D dataset given ε and MinPts as input.
import math
def dbscan(data, eps, MinPts):
    labels = [0]*len(data)  #o means unvisted 
    cluster = 0
    for i in range(len(data)):
        if labels[i] != 0:    
            continue
        neighbors = []
        for j in range(len(data)):
            d = math.sqrt((data[i][0]-data[j][0])**2 + (data[i][1]-data[j][1])**2)
            if d <= eps:
                neighbors.append(j)
        if len(neighbors) < MinPts:
            labels[i] = -1
        else:
            cluster += 1
            for n in neighbors:
                labels[n] = cluster
    return labels
data = [(1,2),(2,2),(2,3),(8,7),(8,8),(25,80),(24,79),(25,82)]
labels = dbscan(data, 3, 2)
for i in range(len(data)):
    if labels[i] == -1:
        print("Point", data[i], "is Noise")
    else:
        print("Point", data[i], "- cluster", labels[i])
        print("Raja Kumar Sah, 23053769")