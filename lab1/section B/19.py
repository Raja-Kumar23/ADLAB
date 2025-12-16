#Print the number of digits that are divisible by 3 in a given number.
n = input("Enter a number: ")
count = sum(1 for digit in n if int(digit) % 3 == 0)
print("Number of digits divisible by 3:", count)
print("Roll: 23053769")