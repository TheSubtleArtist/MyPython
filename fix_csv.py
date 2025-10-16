import csv
import sys


def convert_csv(old_filename, new_filename):
    """Convert a pipe-delimited CSV file to comma-delimited."""
    with open(old_filename, newline='') as old_file:
        reader = csv.reader(old_file, delimiter='|')
        with open(new_filename, mode='wt', newline='') as new_file:
            csv.writer(new_file).writerows(reader)


def main():
    if len(sys.argv) != 3:
        print("Usage: python fix_csv.py <input_file> <output_file>")
        sys.exit(1)

    old_filename, new_filename = sys.argv[1:]
    convert_csv(old_filename, new_filename)


if __name__ == "__main__":
    main()