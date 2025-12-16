#Count number of prime numbers in a range.
lower = int(input("Enter lower bound of range: "))
upper = int(input("Enter upper bound of range: "))
count = 0
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1
print("Number of prime numbers in the range:", count)
print("Roll: 23053769")