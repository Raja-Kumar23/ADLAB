#Write a function to return unique elements from a list.
numbers = [3, 5, 1, 2, 4, 8, 3, 5, 2]
def get_unique(numbers):
    unique = []
    for n in numbers:
        if n not in unique:
            unique.append(n)
    return unique
result = get_unique(numbers)
print("Unique Numbers:", result)
print("Name: Raja Kumar")
print("Roll: 23053769")
