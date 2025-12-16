#Count even and odd numbers in a list.
numbers = [3, 5, 1, 2, 4, 8,9,12,14,16,17]
even_count = 0
odd_count = 0
for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Name: Raja Kumar")
print("Roll: 23053769")