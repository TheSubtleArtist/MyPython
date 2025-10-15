import csv
from pathlib import Path
import sys

[csv_filename] = sys.argv[1:]


total = 0
with open(csv_filename) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if row["Category"] == "Air Travel":
            cost = float(row["Cost"].removeprefix("$"))
            total += cost
print(f"Total air travel expenses: ${total:.02f}")