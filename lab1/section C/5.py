#Convert string to uppercase without using built-in function.
s = input("Enter a string: ")
uppercase_string = ''
for char in s:
    if 'a' <= char <= 'z':
        uppercase_string += chr(ord(char) - 32)
    else:
        uppercase_string += char
print("String in uppercase:", uppercase_string)
print("Roll: 23053769")