from datetime import date
from pathlib import Path

def main():
    text = input("jot: ")
    jot_path = Path.home() / "jot.txt"

    with open(jot_path, mode="at") as jot_file:
        print(date.today(), text, file=jot_file)

if __name__ == "__main__":
    main()