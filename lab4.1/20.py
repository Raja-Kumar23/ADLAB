# Write a program to calculate compound interest.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
compound_interest = principal * (1 + rate / 100) ** time - principal
print(f"The compound interest is: {compound_interest}")
print("Roll: 23053769")