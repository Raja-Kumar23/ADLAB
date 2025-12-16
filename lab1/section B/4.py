#Calculate factorial of a number.
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is: {factorial}")
print("Roll: 23053769")