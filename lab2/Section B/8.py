#Write a function to compute square root without using math library.
def square_root(n):
    x = n
    for _ in range(20):
        x = (x + n / x) / 2
    return x
print(square_root(25))
print("Name: Raja Kumar")
print("Roll: 23053769")
