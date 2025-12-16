# 6. Write a program to find average of numbers stored in a file.

with open("numbers.txt", "r") as f:
    nums = [float(x) for x in f.read().split()]

avg = sum(nums) / len(nums)
print("Average:", avg)

print("Name: Raja Kumar")
print("Roll: 23053769")
