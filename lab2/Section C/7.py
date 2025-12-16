# 7. Read a CSV (dataset) and print number of rows.

import csv
def csv_row_count(filename):
    with open(filename, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        return sum(1 for _ in reader)
filename = "data.csv"
print("Number of rows:", csv_row_count(filename))
print("Name: Raja Kumar")
print("Roll: 23053769")
