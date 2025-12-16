#Check if a list is sorted or not.
numbers = [1,2,4,6,8,10]
is_sorted = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break
print("Is the list sorted?", is_sorted)
print("Name: Raja Kumar")
print("Roll: 23053769")