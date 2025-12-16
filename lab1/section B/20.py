#Find sum of squares of first N natural numbers.
n = int(input("Enter a natural number: "))
sum_of_squares = sum(i**2 for i in range(1, n+1))
print("Sum of squares of first", n, "natural numbers is:", sum_of_squares)
print("Roll: 23053769")