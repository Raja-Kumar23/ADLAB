#Check whether a number is a palindrome.

n = int(input("Enter number: "))
rev = 0
temp = n
while temp != 0:
    r = temp % 10
    rev = rev * 10 + r
    temp //= 10
if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")
print("Roll: 23053769")