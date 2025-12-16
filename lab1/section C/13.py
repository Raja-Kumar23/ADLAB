#Remove special characters from a string.
s = input("Enter a string: ")
special_characters = "!@#$%^&*()-+"
cleaned_string = ''.join(char for char in s if char not in special_characters)
print("String after removing special characters:", cleaned_string)
print("Roll: 23053769")
