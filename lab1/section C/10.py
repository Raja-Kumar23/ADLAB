# Find the longest word from a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)
print("Roll: 23053769")