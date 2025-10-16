from argparse import ArgumentParser
from pathlib import Path
import os


def fix_newlines(path):
    """Ensure the given file ends with a newline character."""
    with open(path, mode="rb+") as file:
        file_size = file.seek(0, os.SEEK_END)
        if file_size == 0:
            file.write(b"\n")
        else:
            file.seek(-1, os.SEEK_END)
            last_char = file.read(1)
            if last_char != b"\n":
                file.write(b"\n")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    fix_newlines(args.file)