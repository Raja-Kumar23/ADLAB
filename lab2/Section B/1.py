#Write a function to calculate factorial.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
n = 5
ans = factorial(n)
print(ans)
print("Name: Raja Kumar")
print("Roll: 23053769")
