#Print sum of all numbers from 1 to N.
N = int(input("Enter a number N: "))
sum = 0
for i in range(1, N+1):
    sum += i
print(f"The sum of all numbers from 1 to {N} is: {sum}")
print("Roll: 23053769")