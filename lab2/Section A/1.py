#Find max and min from a list without using built-ins.
numbers = [3, 5, 1, 2, 4, 8]
max_val = numbers[0]
min_val = numbers[0]
for n in numbers[1:]:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print("Max:", max_val)
print("Min:", min_val)
print("Name: Raja Kumar\n Roll: 23053769")
