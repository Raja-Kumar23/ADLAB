# 14. Write a program to calculate Euclidean distance between two points.

import math
def euclidean(p1, p2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))
print("Distance:", euclidean([1, 2, 3], [4, 0, -1]))
print("Name: Raja Kumar")
print("Roll: 23053769")
