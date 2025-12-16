# 1. Write a program to count number of lines in a text file.

def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

name = input("Enter file name: ")
filename = fr"C:\Users\KIIT0001\OneDrive\Desktop\AD LAB\lab2\Section C\{name}"

print("Line count:", count_lines(filename))
print("Name: Raja Kumar")
print("Roll: 23053769")
