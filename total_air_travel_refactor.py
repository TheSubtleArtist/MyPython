# Refactored by the LLM to improve testability in the total_air_Travel_test.py
# expense_calculator.py
import csv
from pathlib import Path
import sys

def calculate_air_travel_expenses(csv_filename):
    """Calculate total air travel expenses from a CSV file."""
    total = 0
    with open(csv_filename) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row["Category"] == "Air Travel":
                cost = float(row["Cost"].removeprefix("$"))
                total += cost
    return total

def main():
    """Main function - original script logic."""
    [csv_filename] = sys.argv[1:]
    total = calculate_air_travel_expenses(csv_filename)
    print(f"Total air travel expenses: ${total:.02f}")

if __name__ == "__main__":
    main()