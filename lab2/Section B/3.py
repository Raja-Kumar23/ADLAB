#Write a function to return reverse of a number.
num = 12345
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed Number:", rev)
print("Name: Raja Kumar")
print("Roll: 23053769")