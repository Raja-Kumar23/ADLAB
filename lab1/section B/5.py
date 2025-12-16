#Count digits in a number.
n = int(input("Enter a number: "))
count = 0
while n != 0:
    n //= 10
    count += 1
print(f"The number of digits is: {count}")
print("Roll: 23053769")