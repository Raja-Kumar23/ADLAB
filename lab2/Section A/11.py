#Count word frequency using dictionary.
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word Frequency:", frequency)
print("Name: Raja Kumar")
print("Roll: 23053769") 