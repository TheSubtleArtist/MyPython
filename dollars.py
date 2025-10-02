from argparse import ArgumentParser

def format_dollars(amount):
    """Format a number as US currency."""
    return f"${amount:.2f}"

def main():
    parser = ArgumentParser()
    parser.add_argument("amount", type=float)
    args = parser.parse_args()
    print(format_dollars(args.amount))

if __name__ == "__main__":
    main()