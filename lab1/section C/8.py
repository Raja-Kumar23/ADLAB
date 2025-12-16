#Replace all vowels with ‘*’.
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ''.join('*' if char in vowels else char for char in s)
print("String after replacing vowels with '*':", result)
print("Roll: 23053769")