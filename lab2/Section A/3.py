#Remove duplicates from a list.
numbers = [3, 5, 1, 2, 4, 8, 3, 5, 2]
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print("Unique numbers:", unique_numbers)
print("Name: Raja Kumar")
print("Roll: 23053769")