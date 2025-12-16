#Display sum of odd and even digits separately in a number.
n = int(input("Enter a number: "))
sum_odd = 0
sum_even = 0
for digit in str(n):
    if int(digit) % 2 == 0:
        sum_even += int(digit)
    else:
        sum_odd += int(digit)
print("Sum of odd digits:", sum_odd)
print("Sum of even digits:", sum_even)
print("Roll: 23053769")