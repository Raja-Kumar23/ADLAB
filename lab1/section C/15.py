#Find the most frequent character in a string.
s = input("Enter a string: ")
frequency = {}
for char in s:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1 
most_frequent_char = max(frequency, key=frequency.get)
print(f"The most frequent character is: '{most_frequent_char}' with frequency {frequency[
most_frequent_char]}")
print("Roll: 23053769") 
    