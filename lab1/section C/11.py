#Convert string to title case manually.
s = input("Enter a string: ")
title_case_string = ''
capitalize_next = True
for char in s:
    if char.isspace():
        capitalize_next = True
        title_case_string += char
    elif capitalize_next:
        title_case_string += char.upper()
        capitalize_next = False
    else:
        title_case_string += char.lower()
print("Title case string:", title_case_string)
print("Roll: 23053769")