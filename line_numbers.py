from argparse import ArgumentParser, FileType


def print_with_line_numbers(file):
    """Print file contents with line numbers."""
    for n, line in enumerate(file, start=1):
        print(n, line.rstrip("\n"))


def main():
    parser = ArgumentParser()
    parser.add_argument("file", type=FileType("rt"))
    args = parser.parse_args()
    print_with_line_numbers(args.file)


if __name__ == "__main__":
    main()