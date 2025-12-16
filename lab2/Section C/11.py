# 11. Compute correlation between two lists.

import math
def pearson_correlation(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    num = sum((a - mean_x) * (b - mean_y) for a, b in zip(x, y))
    den1 = math.sqrt(sum((a - mean_x)**2 for a in x))
    den2 = math.sqrt(sum((b - mean_y)**2 for b in y))
    return num / (den1 * den2)
x = [1, 2, 3, 4]
y = [2, 4, 5, 4]
print("Correlation:", pearson_correlation(x, y))
print("Name: Raja Kumar")
print("Roll: 23053769")
