#Write a program to compute the remainder without using % operator.
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))     
quotient = dividend // divisor

remainder = dividend - (quotient * divisor)
print("Remainder is:", remainder)
print("Roll: 23053769")