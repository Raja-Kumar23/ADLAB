#Write a program to print all factors of a number.
n = int(input("Enter a number: "))
factors = [i for i in range(1, n+1) if n % i == 0]
print("Factors of", n, "are:", factors)
print("Roll: 23053769")