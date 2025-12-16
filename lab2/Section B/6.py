#Write a function to compute nCr (Combination).
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f
def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
print(nCr(5, 2))
print("Name: Raja Kumar")
print("Roll: 23053769")
