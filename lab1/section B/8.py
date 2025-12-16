
#Generate Fibonacci series of N numbers
n = int(input("Enter N: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print("\nRoll: 23053769")