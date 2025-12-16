# 12. Normalize a list of numbers (ML preprocessing concept).

def normalize(lst):
    lo = min(lst)
    hi = max(lst)
    return [(x - lo) / (hi - lo) for x in lst]
nums = [10, 20, 30, 40]
print("Normalized:", normalize(nums))
print("Name: Raja Kumar")
print("Roll: 23053769")
