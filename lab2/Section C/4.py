# 4. Write to a file and then read from it.

def write_and_read(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
filename = "output.txt"
text = "Hello KIITHub!\nThis is a sample file."
print(write_and_read(filename, text))
print("Name: Raja Kumar")
print("Roll: 23053769")
