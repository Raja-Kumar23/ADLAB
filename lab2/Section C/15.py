# 15. Implement a simple kNN step: find nearest value from a list.

def nearest_value(target, lst):
    best = None
    best_dist = None
    for val in lst:
        d = abs(val - target)
        if best_dist is None or d < best_dist:
            best = val
            best_dist = d
    return best
lst = [2.5, 7.0, 3.1, 10.2]
print("Nearest:", nearest_value(4.0, lst))

print("Name: Raja Kumar")
print("Roll: 23053769")
