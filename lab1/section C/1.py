#Count number of vowels in a string.
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print("Number of vowels in the string:", count)
print("Roll: 23053769")