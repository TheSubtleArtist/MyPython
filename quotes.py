import csv
from collections import namedtuple
from random import choice
import sys

def get_all_quotes(filename):
    """Read quotes from a CSV file and return as named tuples."""
    Quote = namedtuple('Quote', 'author text')
    quotes = []
    with open(filename) as quotes_file:
        for author, quote in csv.reader(quotes_file):
            quotes.append(Quote(author, quote))
    return quotes

def main(filename):
    """Print a random quote from the quotes file."""
    quote = choice(get_all_quotes(filename))
    print('"{q.text}" -- {q.author}'.format(q=quote))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quotes.py <quotes_file>")
        sys.exit(1)
    main(sys.argv[1])
