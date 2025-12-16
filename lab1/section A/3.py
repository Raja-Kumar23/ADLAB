# Swap two variables without using a third variable.
x = int(input("Enter first number x :"))
y = int(input("Enter second number y :"))

x = x + y
y = x - y
x = x - y

print("After swapping:")
print("x =", x)
print("y =", y)