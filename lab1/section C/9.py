#Extract digits from a string.
s = input("Enter a string: ")
digits = ''.join(char for char in s if char.isdigit())
print("Digits extracted from the string:", digits)
print("Roll: 23053769")