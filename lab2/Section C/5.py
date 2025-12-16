# 5. Read a CSV file and print column names.

import csv

def csv_columns(filename):
    with open(filename, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        return next(reader, [])
filename = "data.csv"
print("Columns:", csv_columns(filename))
print("Name: Raja Kumar")
print("Roll: 23053769")
