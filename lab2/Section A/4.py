#Find the second largest element in a list.
numbers = [3, 5, 1, 2, 4, 8]

first = max(numbers)
second = None

for n in numbers:
    if n != first:
        if second is None or n > second:
            second = n

print("Second largest:", second)
print("Name: Raja Kumar")
print("Roll: 23053769")

