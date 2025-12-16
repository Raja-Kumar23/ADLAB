#Write a function to count uppercase and lowercase letters in a string.
def count_case(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower
print(count_case("Hello World"))
print("Name: Raja Kumar")
print("Roll: 23053769")
