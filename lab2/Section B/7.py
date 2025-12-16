#Write a function to check if a number is perfect.
def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n
print(is_perfect(28))
print("Name: Raja Kumar")
print("Roll: 23053769")
