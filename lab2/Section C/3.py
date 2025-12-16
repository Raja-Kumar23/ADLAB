# 3. Count characters in a file.

def count_characters(filename):
    chars = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            chars += len(line)
    return chars
filename = "sample.txt"
print("Character count:", count_characters(filename))
print("Name: Raja Kumar")
print("Roll: 23053769")
