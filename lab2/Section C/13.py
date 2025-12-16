# 13. Standardize a list of numbers manually.

import math
def standardize(lst):
    mean = sum(lst) / len(lst)
    var = sum((x - mean)**2 for x in lst) / len(lst)
    std = math.sqrt(var)
    return [(x - mean) / std for x in lst]
nums = [10, 20, 30, 40]
print("Standardized:", standardize(nums))

print("Name: Raja Kumar")
print("Roll: 23053769")
