#Count frequency of each character in a string.
s = input("Enter a string: ")
frequency = {}
for char in s:
    frequency[char] = frequency.get(char, 0) + 1
print("Frequency of each character:")
for char, count in frequency.items():
    print(f"{char}: {count}")
print("Roll: 23053769")