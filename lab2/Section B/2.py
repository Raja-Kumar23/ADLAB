#Write a function to check prime number.
def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
num = 6
if check_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
print("Name: Raja Kumar")
print("Roll: 23053769")
