#Sort a list manually (bubble sort logic).
numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)
for i in range(n):
    for j in range(0, n-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print("Sorted list:", numbers)
print("Name: Raja Kumar")
print("Roll: 23053769")